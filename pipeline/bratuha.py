"""Бэкенд Братуха.ру: картинки, видео и голос через Public API (оплата в рублях).

Ключ берётся из переменной окружения BRATUHA_API_KEY (создаётся в кабинете
bratuha.ru → Аккаунт → API). Все операции асинхронные: создаём, опрашиваем,
забираем ссылку на файл. Каждая оплата пишется в output/bratuha_spend.json,
и при превышении bratuha.budget_rub конвейер останавливается сам.

Братуха принимает файлы только по публичным ссылкам, поэтому для эталона и
стартовых кадров рядом с картинкой хранится .url — ссылка на неё в хранилище
Братухи. По ней следующая нейросеть и получает картинку.
"""

import json
import math
import os
import sys
import time

import requests

API = "https://bratuha.ru/api/v1"


def all_urls(obj):
    """Все http-ссылки из поля result (формат у нейросетей разный)."""
    found = []
    if isinstance(obj, str):
        if obj.startswith(("http://", "https://")):
            found.append(obj)
    elif isinstance(obj, dict):
        for value in obj.values():
            found += all_urls(value)
    elif isinstance(obj, list):
        for value in obj:
            found += all_urls(value)
    return list(dict.fromkeys(found))


class Bratuha:
    def __init__(self, cfg, spend_path, log):
        self.key = os.environ.get("BRATUHA_API_KEY")
        if not self.key:
            sys.exit("Нет BRATUHA_API_KEY в переменных окружения (кабинет bratuha.ru → API).")
        self.cfg = cfg["bratuha"]
        self.log = log
        self.spend_path = spend_path
        if spend_path.exists():
            self.spend = json.loads(spend_path.read_text(encoding="utf-8"))
        else:
            self.spend = {"total_rub": 0, "operations": []}

    @property
    def headers(self):
        return {"Authorization": f"Bearer {self.key}", "Content-Type": "application/json"}

    def _record(self, op_id, tool, label, cost):
        self.spend["total_rub"] = round(self.spend["total_rub"] + cost, 2)
        self.spend["operations"].append({"id": op_id, "tool": tool, "label": label, "cost_rub": cost,
                                         "at": time.strftime("%Y-%m-%d %H:%M:%S")})
        self.spend_path.parent.mkdir(parents=True, exist_ok=True)
        self.spend_path.write_text(json.dumps(self.spend, ensure_ascii=False, indent=1), encoding="utf-8")

    def run(self, tool, payload, label, pending=None):
        """Запускает нейросеть, ждёт результат, возвращает первую ссылку на файл.

        pending — файл, куда записывается id операции, пока она идёт. Если запуск
        оборвался (сеть, перезагрузка), следующий запуск найдёт этот файл и дождётся
        уже оплаченной операции, а не закажет её заново.
        """
        if pending and pending.exists():
            op_id = pending.read_text(encoding="utf-8").strip()
            self.log(f"    {label}: жду уже оплаченную операцию {op_id}")
            url = self._wait(tool, op_id)
            pending.unlink()
            return url
        budget = self.cfg.get("budget_rub")
        if budget and self.spend["total_rub"] >= budget:
            sys.exit(f"Бюджет {budget} ₽ исчерпан (потрачено {self.spend['total_rub']} ₽). "
                     f"Поднимите bratuha.budget_rub в config.yaml или обнулите output/bratuha_spend.json.")
        for _ in range(6):
            r = requests.post(f"{API}/operations", headers=self.headers,
                              json={"tool": tool, "input": payload}, timeout=60)
            if r.status_code != 503:  # 503 — операция не создана и не оплачена, можно повторить
                break
            time.sleep(int(r.headers.get("Retry-After", 5)))
        try:
            data = r.json()
        except ValueError:
            data = {}
        if r.status_code >= 400:
            err = data.get("error", {})
            sys.exit(f"Братуха, {tool}: {r.status_code} {err.get('code')} — {err.get('message')} "
                     f"(request_id {err.get('request_id') or r.headers.get('X-Request-Id')})")
        op_id, cost = data["id"], float(data.get("cost") or 0)
        if pending:
            pending.parent.mkdir(parents=True, exist_ok=True)
            pending.write_text(op_id + "\n", encoding="utf-8")
        self._record(op_id, tool, label, cost)
        self.log(f"    {label}: {tool}, {cost:g} ₽ (всего {self.spend['total_rub']:g} ₽, "
                 f"на балансе {data.get('balance_after')} ₽)")
        url = self._wait(tool, op_id)
        if pending:
            pending.unlink(missing_ok=True)
        return url

    def _wait(self, tool, op_id):
        started = time.time()
        while True:
            time.sleep(4)
            try:
                s = requests.get(f"{API}/operations/{op_id}", headers=self.headers, timeout=60)
            except requests.RequestException:  # сеть моргнула — операция идёт дальше, просто спросим ещё раз
                if time.time() - started > 1800:
                    raise
                time.sleep(10)
                continue
            if s.status_code == 429 or s.status_code >= 500:
                continue
            s.raise_for_status()
            status = s.json()
            if status["status"] == "completed":
                break
            if status["status"] == "failed":
                sys.exit(f"Братуха, {tool}: ошибка генерации — {status.get('error_message')} (операция {op_id})")
            if time.time() - started > 1800:
                sys.exit(f"Братуха, {tool}: нет результата за 30 минут (операция {op_id})")
        urls = all_urls(status.get("result"))
        if not urls:
            sys.exit(f"Братуха, {tool}: в ответе нет ссылки на файл: {json.dumps(status)[:500]}")
        return urls[0]

    # --- конкретные нейросети; slug и параметры — в pipeline/config.yaml → bratuha

    def image(self, prompt, label, image_urls=None, pending=None):
        c = self.cfg
        payload = {"mode": c["image_mode"], "prompt": prompt, "aspect_ratio": "9:16", "image_size": c["image_size"]}
        if image_urls:
            payload["image_urls"] = image_urls
        return self.run(c["image_tool"], payload, label, pending)

    def video(self, prompt, image_url, seconds, label, pending=None):
        """Оживление стартового кадра в Seedance 2.5 (режим image).

        Длительность — от 4 до 30 с с шагом в секунду, поэтому заказываем ровно под
        слот сцены: не переплачиваем за лишние секунды и не замедляем клип при монтаже.
        """
        c = self.cfg
        duration = min(30, max(4, int(seconds + 0.3)))  # 6.2 с → 6 с; недостающее добираем лёгким замедлением при монтаже
        payload = {"seedance_2_5_generation_type": "image", "prompt": prompt, "image_urls": [image_url],
                   "size": "9:16", "resolution": c["video_resolution"], "duration": duration,
                   "generate_audio": False, "watermark": False, "output_format": "mp4"}
        return self.run(c["video_tool"], payload, label, pending)

    def voice(self, text, label, sample=None):
        """Озвучка. Gemini — готовый голос из config (tts_voice).

        Qwen3 TTS — первый раз голос по описанию, дальше клон этого голоса (sample).
        """
        c = self.cfg
        if c["tts_tool"].startswith("gemini"):
            payload = {"text": text, "language": "Russian (Russia)", "voice": c["tts_voice"]}
            return self.run(c["tts_tool"], payload, label)
        payload = {"text": text, "language": "Russian"}
        if sample:
            payload.update(generation_type="clone", audio=sample["url"], reference_text=sample["text"][:1000])
        else:
            payload.update(generation_type="design", voice_description=c["voice_description"])
        return self.run(c["tts_tool"], payload, label)
