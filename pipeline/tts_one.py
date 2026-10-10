"""Голос через Братуху: клон голоса по образцу (Qwen3 TTS).
python pipeline/tts_one.py <name> "<text>" <sample_url> "<sample_text>" -> previews/<name>.url и .mp3"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, text, sample_url, sample_text = sys.argv[1:5]
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
if sample_url == "gacrux":  # голос бабы Зои: Gemini, Gacrux, как в роликах
    url = br.run("gemini-3-1-flash-tts", {"text": text, "language": "Russian (Russia)", "voice": "Gacrux"}, f"{name} голос")
elif sample_url.startswith("design:"):  # Qwen3 TTS: голос по описанию
    url = br.run("qwen3-tts", {"text": text, "language": "Russian", "generation_type": "design", "voice_description": sample_url.split(":", 1)[1]}, f"{name} голос")
elif sample_url.startswith("gemini:"):  # любой готовый голос Gemini, напр. gemini:Charon (граф)
    url = br.run("gemini-3-1-flash-tts", {"text": text, "language": "Russian (Russia)", "voice": sample_url.split(":", 1)[1]}, f"{name} голос")
else:
    payload = {"text": text, "language": "Russian", "generation_type": "clone", "audio": sample_url, "reference_text": sample_text}
    # Клон только своего голоса: Артём подтвердил 2026-10-07, что образец graf-voice-sample.mp3 — его голос.
    # Братуха требует отметку «имею право использовать этот голос» — ищем её поле в схеме инструмента.
    import json, re, requests
    sch = requests.get("https://bratuha.ru/api/v1/tools/qwen3-tts/schema", headers=br.headers, timeout=30)
    txt = sch.text
    M.log("схема qwen3-tts: " + txt[:6000])
    try:
        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(v, dict) and re.search(r"право|consent|rights", json.dumps(v, ensure_ascii=False), re.I) \
                            and v.get("type") == "boolean":
                        payload[k] = True
                        M.log(f"отметка прав: {k}")
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
        walk(sch.json())
    except Exception as ex:
        M.log(f"схему не разобрал: {ex}")
    url = br.run("qwen3-tts", payload, f"{name} голос")
out = M.ROOT / "previews"; out.mkdir(exist_ok=True)
M.download(url, out / f"{name}.mp3")
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово {url}")
