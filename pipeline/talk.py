"""Ролик «говорящая голова»: баба Зоя говорит в камеру (липсинк) + вставки готовки под закадровый голос.

python pipeline/talk.py <id>        — сценарий в content/talk.yaml (ключ talks)

Структура: talk_in (в камеру) → broll (сцены под закадр) → talk_out (в камеру).
Говорящие куски — Seedance 2.5 references (кадр + голос → губы в такт), вставки — Seedance 2.5.
Всё кешируется в output/<id>/, оплаченное повторно не заказывается.
"""
import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import requests

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M  # noqa: E402

API = "https://bratuha.ru/api/v1"
LOCK = threading.Lock()
SPEED = 1.15

vid = sys.argv[1]
base = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
talks = {t["id"]: t for t in M.load_yaml(M.ROOT / "content" / "talk.yaml")["talks"]}
video = talks[vid]
cfg = {**base, **video.get("cfg", {})}  # свои настройки ролика (например, субтитры по слову)
out = M.ROOT / "output" / vid
out.mkdir(parents=True, exist_ok=True)
state_path = out / "state.json"
prev = M.ROOT / "previews" / f"{vid}-state.json"
state = {}
for _p in (prev, state_path):  # объединяем: в кеше может лежать старый неполный state, в previews — полный
    if _p.exists():
        state.update(json.loads(_p.read_text()))


def save():
    with LOCK:
        state_path.write_text(json.dumps(state, ensure_ascii=False, indent=1))


_remember = M.remember
def _locked_remember(*a, **k):
    with LOCK:
        return _remember(*a, **k)
M.remember = _locked_remember
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
_rec = br._record
br._record = lambda *a, **k: (LOCK.acquire(), _rec(*a, **k), LOCK.release())
ref_url = (M.ROOT / "assets" / "reference" / "baba-zoya.url").read_text().strip()

if len(sys.argv) > 2 and sys.argv[2] == "ops":
    # статус и ссылки на результат по id операций (id берём из имён скачанных с сайта файлов)
    res = {}
    for op in sys.argv[3:]:
        r = requests.get(f"{API}/operations/{op}", headers=br.headers, timeout=60)
        try:
            res[op] = {"status": r.status_code, "body": r.json()}
        except ValueError:
            res[op] = {"status": r.status_code, "body": r.text[:2000]}
    (M.ROOT / "previews").mkdir(exist_ok=True)
    (M.ROOT / "previews" / f"{vid}-ops.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    sys.exit(0)

if len(sys.argv) > 2 and sys.argv[2] == "dump":
    # выгрузка последних операций Братухи — чтобы восстановить уже оплаченное, если state потерялся
    res = {}
    for q in ("?limit=100", "?per_page=100", "?page=1&per_page=100", ""):
        try:
            r = requests.get(f"{API}/operations{q}", headers=br.headers, timeout=60)
            res[q or "plain"] = {"status": r.status_code, "body": r.json() if r.headers.get("content-type", "").startswith("application/json") else r.text[:3000]}
            if r.status_code == 200:
                break
        except Exception as e:  # noqa: BLE001
            res[q or "plain"] = {"error": repr(e)}
    (M.ROOT / "previews").mkdir(exist_ok=True)
    (M.ROOT / "previews" / f"{vid}-ops.json").write_text(json.dumps(res, ensure_ascii=False, indent=1))
    sys.exit(0)


def avatar(image_url, audio_url, seconds, text, motion, label, pending):
    """Говорящий кусок через Seedance 2.5 в режиме references: кадр (@image1) + голос (@audio1),
    модель двигает губы под голос. Аватар-нейросети Братухи (Kling Avatar, OmniHuman, InfiniteTalk)
    в публичном API недоступны."""
    prompt = (
        "@image1 — this exact elderly woman in this exact kitchen, same face, same clothes, same headscarf, same props. "
        "Vertical smartphone selfie-style video, she looks straight into the camera and speaks in Russian; "
        "her lips, jaw and facial expressions move precisely in sync with the voice from @audio1 from the very first frame. "
        f"She says: «{text.strip()}». {motion}. "
        "Natural skin, no music, no subtitles, no captions, no text on screen, the camera stays on her face and upper body."
    )
    payload = {
        "seedance_2_5_generation_type": "references",
        "prompt": prompt,
        "reference_image_urls": [image_url],
        "audio_urls": [audio_url],
        "size": "9:16",
        "resolution": "480p",
        "duration": max(4, int(seconds) + 1),
        "generate_audio": True,
        "watermark": False,
        "output_format": "mp4",
    }
    return br.run("seedance-2-5", payload, label, pending=pending)


def _env(path):
    """Громкость звука по 10 мс — для поиска сдвига между двумя дорожками."""
    import subprocess
    import numpy as np
    pcm = subprocess.run([M.FFMPEG, "-hide_banner", "-loglevel", "error", "-i", str(path), "-vn", "-ac", "1",
                          "-ar", "8000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.abs(np.frombuffer(pcm, dtype=np.int16).astype(np.float32))
    n = len(a) // 80
    e = a[: n * 80].reshape(n, 80).mean(1)
    return (e - e.mean()) / (e.std() + 1e-6)


def align(model_video, our_audio):
    """Сдвиг (с) голоса в ролике модели относительно нашего и сила совпадения 0..1."""
    import numpy as np
    m, o = _env(model_video), _env(our_audio)
    best = (0, -1.0)
    for lag in range(-100, 301):  # от -1 до +3 с
        a, b = (m[lag:], o) if lag >= 0 else (m, o[-lag:])
        n = min(len(a), len(b))
        if n < 200:
            continue
        c = float(np.dot(a[:n], b[:n]) / n)
        if c > best[1]:
            best = (lag, c)
    return best[0] / 100, best[1]


# ---------- 1. голос: три куска
def tts(key, text):
    if key + "_url" not in state:
        state[key + "_url"] = br.voice(text, f"голос {key}")
        save()
    return state[key + "_url"]


STILL = len(sys.argv) > 2 and sys.argv[2] == "still"
ONLY_IN = "broll" not in video  # короткое обращение в камеру (например, кружочек для бота)
PARTS = ("talk_in",) if ONLY_IN else ("talk_in", "broll", "talk_out")
with ThreadPoolExecutor(3) as ex:
    fut = {k: ex.submit(tts, k, video[k]["text"]) for k in PARTS}
    urls = {k: f.result() for k, f in fut.items()}

raw = {}
for k in [x for x in PARTS if x != "broll"]:
    p = out / f"{k}_raw.mp3"
    if not p.exists():
        M.download(urls[k], p)
    raw[k] = p
if not ONLY_IN:
    # закадр ускоряем как обычно; говорящие куски — ускорим вместе с видео (губы останутся в такт)
    vo = out / "vo.mp3"
    if not vo.exists():
        M.finish_voice(cfg, urls["broll"], vo)
    vo_len = M.media_duration(vo)
    scenes = video["broll"]["scenes"]
    slot = vo_len / len(scenes)
    M.log(f"закадр {vo_len:.1f} с на {len(scenes)} сцен по {slot:.1f} с; "
          f"в камеру {M.media_duration(raw['talk_in']):.1f} + {M.media_duration(raw['talk_out']):.1f} с (до ускорения)")


# ---------- 2. кадры и видео параллельно
def talk_job(k):
    clip = out / f"{k}_a.mp4"  # _a — с выравниванием голоса
    if clip.exists():
        return k
    src = out / f"{k}_src.mp4"
    loc = M.ROOT / "previews" / f"{vid}-{k}_src.mp4"
    if not src.exists() and loc.exists() and k + "_video" not in state:
        import shutil as _sh; _sh.copy(loc, src); state[k + "_video"] = "local"
    if k + "_frame" not in state and not src.exists():
        prompt = f"{video[k]['image']}. {cfg['character_lock']}"
        state[k + "_frame"] = br.image(prompt, f"кадр {k}", image_urls=[ref_url])
        save()
        M.download(state[k + "_frame"], out / f"{k}.png")
    if STILL and k + "_video" not in state:
        # без аватара: кадр + голос (губы потом делает Wan в Higgsfield) — не платим за Seedance
        M.run_ffmpeg(["-loop", "1", "-i", str(out / f"{k}.png"), "-i", str(raw[k]), "-vf", "scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,fps=30",
                      "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest", str(src)])
        state[k + "_video"] = "still"; save()
    if k + "_video" not in state:
        secs = M.media_duration(raw[k])
        state[k + "_video"] = avatar(state[k + "_frame"], urls[k], secs, video[k]["text"], video[k]["motion"],
                                     f"{k} в камеру", out / f"{k}.pending")
        save()
    if not src.exists() and state[k + "_video"] != "still":
        M.download(state[k + "_video"], src)
    (M.ROOT / "previews").mkdir(exist_ok=True)
    import shutil; shutil.copy(src, M.ROOT / "previews" / f"{vid}-{k}_src.mp4")
    # модель озвучивает сама и обычно с небольшой задержкой: находим сдвиг её звука относительно нашего,
    # срезаем тишину в начале и кладём наш голос точно туда, где двигаются губы
    lag, corr = align(src, raw[k])
    t0 = max(0.0, lag - 0.08)
    M.log(f"    {k}: сдвиг голоса модели {lag:+.2f} с (совпадение {corr:.2f}), срезаю начало {t0:.2f} с")
    # голос всегда наш: у модели своя озвучка, она коверкает слова («батул», «плесения»)
    a_in = str(raw[k])
    if lag - t0 > 0:
        a_chain = f"adelay={int((lag - t0) * 1000)}:all=1,"
    elif lag < 0:
        a_chain = f"atrim=start={-lag},asetpts=PTS-STARTPTS,"
    else:
        a_chain = ""
    M.run_ffmpeg(["-i", str(src), "-i", a_in, "-filter_complex",
                  f"[0:v]trim=start={t0},setpts=(PTS-STARTPTS)/{SPEED},scale=1080:1920:force_original_aspect_ratio=increase,"
                  f"crop=1080:1920,fps=30,setsar=1,tpad=stop_mode=clone:stop_duration=3[v];"
                  f"[1:a]{a_chain}atempo={SPEED},aresample=44100[a]",
                  "-map", "[v]", "-map", "[a]", "-shortest", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                  "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k", "-ac", "2", str(clip)])
    return k


def broll_job(i):
    clip = out / "clips" / f"scene_{i}.mp4"
    clip.parent.mkdir(exist_ok=True)
    loc = M.ROOT / "previews" / f"{vid}-scene_{i}.mp4"
    if not clip.exists() and loc.exists():
        import shutil as _sh; _sh.copy(loc, clip)
    got = state.get(f"scene_{i}_video")
    if got == "placeholder" and not clip.exists():  # сцену подставлю при финальном монтаже вручную
        M.run_ffmpeg(["-f", "lavfi", "-i", "color=c=black:s=480x854:r=24:d=6", "-c:v", "libx264",
                      "-pix_fmt", "yuv420p", str(clip)])
    if got and got != "placeholder" and not clip.exists():
        M.download(got, clip)
    if not clip.exists():
        M.make_scene_clip_bratuha(cfg, br, M.ROOT / "assets" / "reference" / "baba-zoya.jpg", scenes[i - 1], i, slot, clip)
    m = M.load_media(vid).get(f"scene_{i}", {})
    if m.get("video"):
        state[f"scene_{i}_video"] = m["video"]; save()
    return i


# сначала один говорящий кусок — проверяем, что аватар принят, прежде чем платить за вставки
talk_job("talk_in")
if ONLY_IN:
    # кружочек для Telegram: квадрат 640x640 вокруг лица
    note = M.ROOT / "previews" / f"{vid}-note.mp4"
    M.run_ffmpeg(["-i", str(out / "talk_in_a.mp4"), "-vf", "crop=1080:1080:0:260,scale=640:640,setsar=1",
                  "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-pix_fmt", "yuv420p",
                  "-c:a", "aac", "-b:a", "96k", "-movflags", "+faststart", str(note)])
    M.log(f"Готово: {note} ({M.media_duration(note):.1f} с)")
    sys.exit(0)
if len(sys.argv) > 2 and sys.argv[2] == "check":
    sys.exit(0)
with ThreadPoolExecutor(8) as ex:
    futs = [ex.submit(talk_job, "talk_out")] + [ex.submit(broll_job, i) for i in range(1, len(scenes) + 1)]
    errors = []
    for f in futs:
        try:
            M.log(f"готово: {f.result()}")
        except BaseException as e:
            errors.append(repr(e))
            M.log(f"ошибка: {e!r}")
if errors:
    sys.exit("есть ошибки — перезапуск доделает только недостающее")

# ---------- 3. монтаж: talk_in → вставки + закадр → talk_out
norm = []
for i in range(1, len(scenes) + 1):
    n = out / f"norm_{i}.mp4"
    M.normalize_clip(cfg, out / "clips" / f"scene_{i}.mp4", n, slot)
    norm.append(n)
(out / "concat.txt").write_text("".join(f"file '{p.name}'\n" for p in norm))
M.run_ffmpeg(["-f", "concat", "-safe", "0", "-i", "concat.txt", "-c", "copy", "broll_v.mp4"], cwd=out)
bl = M.media_duration(out / "broll_v.mp4")  # -shortest + apad + копия видео у ffmpeg зависает навсегда
M.run_ffmpeg(["-i", "broll_v.mp4", "-i", "vo.mp3", "-map", "0:v", "-map", "1:a", "-c:v", "copy",
              "-af", f"aresample=44100,apad=whole_dur={bl:.3f}", "-t", f"{bl:.3f}", "-c:a", "aac", "-b:a", "192k", "-ac", "2",
              "broll.mp4"], cwd=out)
M.run_ffmpeg(["-i", "talk_in_a.mp4", "-i", "broll.mp4", "-i", "talk_out_a.mp4", "-filter_complex",
              "[0:v][0:a][1:v][1:a][2:v][2:a]concat=n=3:v=1:a=1[v][a]", "-map", "[v]", "-map", "[a]",
              "-c:v", "libx264", "-preset", "veryfast", "-crf", "18", "-pix_fmt", "yuv420p",
              "-c:a", "aac", "-b:a", "192k", "joined.mp4"], cwd=out)
run_audio = out / "joined.wav"
M.run_ffmpeg(["-i", str(out / "joined.mp4"), "-vn", "-ac", "1", "-ar", "16000", str(run_audio)])
total = M.media_duration(out / "joined.mp4")
text = " ".join(video[k]["text"] for k in ("talk_in", "broll", "talk_out"))
words = M.speech_words(cfg, text, run_audio) or M.even_words(text, total)
(out / "subs.ass").write_text(M.build_subtitles(cfg, {"hook": None}, words, total), encoding="utf-8")
fonts = str((M.ROOT / "assets" / "fonts").resolve())
final = out / f"{vid}.mp4"
M.run_ffmpeg(["-i", "joined.mp4", "-vf", f"ass=subs.ass:fontsdir={fonts}", "-c:v", "libx264", "-preset", "medium",
              "-crf", "20", "-pix_fmt", "yuv420p", "-c:a", "copy", "-movflags", "+faststart", final.name], cwd=out)
(out / "caption.txt").write_text(video["caption"], encoding="utf-8")
import shutil as _sh
_sh.copy(out / "joined.mp4", M.ROOT / "previews" / f"{vid}-joined.mp4")
_sh.copy(out / "subs.ass", M.ROOT / "previews" / f"{vid}-subs.ass")
(M.ROOT / "previews" / f"{vid}-layout.json").write_text(json.dumps(
    {"talk_in": M.media_duration(out / "talk_in_a.mp4"), "slot": slot, "broll": M.media_duration(out / "broll.mp4"),
     "total": total}))
M.log(f"Готово: {final} ({total:.1f} с). Братуха всего: {br.spend['total_rub']:g} ₽")
