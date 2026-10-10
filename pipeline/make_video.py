#!/usr/bin/env python3
"""Собирает вертикальный ролик бабы Зои из сценария в content/scripts.yaml.

Шаги:
  1. эталонное фото бабушки (один раз);
  2. для каждой сцены: стартовый кадр (правка эталона) -> видеоклип;
  3. озвучка и тайминг каждого слова;
  4. субтитры с подсветкой текущего слова + надпись-крючок;
  5. монтаж 1080x1920: клипы, голос, фоновая музыка, субтитры.

Всё, что уже сгенерировано, кешируется в output/<id>/ и повторно не оплачивается.

Где генерировать — pipeline/config.yaml → provider:
  bratuha — Братуха.ру (рубли, один ключ BRATUHA_API_KEY): Nano Banana Pro, Hailuo, Qwen3 TTS;
  fal     — fal.ai (Flux, Seedance) + ElevenLabs (ключи FAL_KEY и ELEVENLABS_API_KEY).

Примеры:
  python pipeline/make_video.py 01-kapusta            # полный прогон через API
  python pipeline/make_video.py --all                 # все ролики
  python pipeline/make_video.py 01-kapusta --demo     # без API: цветные заглушки и тишина
  python pipeline/make_video.py 01-kapusta --dry-run  # показать, что будет сгенерировано

Свои клипы (например, сделанные вручную в Seedance/Dreamina) кладите в
output/<id>/clips/scene_1.mp4, scene_2.mp4 ... — они будут взяты вместо генерации.
Свою озвучку — в output/<id>/voice.mp3 (тогда субтитры распределятся по времени
равномерно, без точной привязки к словам).
"""

import argparse
import base64
import json
import mimetypes
import os
import re
import subprocess
import sys
import time
from pathlib import Path

import imageio_ffmpeg
import requests
import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from bratuha import Bratuha  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()


WHO = "баба Зоя"  # имя персонажа в логе; меняется при сборке роликов другого персонажа


def log(msg):
    print(f"[{WHO}] {msg}", flush=True)


def load_yaml(path):
    with open(path, encoding="utf-8") as f:
        return yaml.safe_load(f)


def run_ffmpeg(args, cwd=None):
    cmd = [FFMPEG, "-hide_banner", "-loglevel", "error", "-y", *args]
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        sys.exit(f"ffmpeg завершился с ошибкой:\n{result.stderr}")


def media_duration(path):
    """Длительность файла в секундах (через ffmpeg, ffprobe не нужен)."""
    result = subprocess.run([FFMPEG, "-hide_banner", "-i", str(path)], capture_output=True, text=True)
    match = re.search(r"Duration: (\d+):(\d+):(\d+\.\d+)", result.stderr)
    if not match:
        sys.exit(f"Не удалось определить длительность {path}")
    h, m, s = match.groups()
    return int(h) * 3600 + int(m) * 60 + float(s)


def download(url, path):
    with requests.get(url, stream=True, timeout=300) as r:
        r.raise_for_status()
        with open(path, "wb") as f:
            for chunk in r.iter_content(1 << 20):
                f.write(chunk)


def data_uri(path):
    mime = mimetypes.guess_type(str(path))[0] or "image/png"
    return f"data:{mime};base64," + base64.b64encode(Path(path).read_bytes()).decode()


def first_url(obj):
    """Находит первую ссылку на файл в ответе fal.ai (формат у моделей разный)."""
    if isinstance(obj, dict):
        if isinstance(obj.get("url"), str):
            return obj["url"]
        for value in obj.values():
            found = first_url(value)
            if found:
                return found
    elif isinstance(obj, list):
        for value in obj:
            found = first_url(value)
            if found:
                return found
    return None


# ---------------------------------------------------------------- fal.ai

def fal_run(model, payload):
    key = os.environ.get("FAL_KEY")
    if not key:
        sys.exit("Нет FAL_KEY в переменных окружения.")
    headers = {"Authorization": f"Key {key}", "Content-Type": "application/json"}
    r = requests.post(f"https://queue.fal.run/{model}", headers=headers, json=payload, timeout=120)
    r.raise_for_status()
    job = r.json()
    status_url, response_url = job["status_url"], job["response_url"]
    started = time.time()
    while True:
        status = requests.get(status_url, headers=headers, timeout=60).json().get("status")
        if status == "COMPLETED":
            break
        if status not in ("IN_QUEUE", "IN_PROGRESS"):
            sys.exit(f"fal.ai: неожиданный статус {status} для {model}")
        if time.time() - started > 1200:
            sys.exit(f"fal.ai: {model} не ответил за 20 минут")
        time.sleep(5)
    result = requests.get(response_url, headers=headers, timeout=120)
    result.raise_for_status()
    url = first_url(result.json())
    if not url:
        sys.exit(f"fal.ai: в ответе {model} нет ссылки на файл: {result.text[:500]}")
    return url


def ensure_reference(cfg, br=None):
    """Эталонное фото. Для Братухи рядом лежит .url — публичная ссылка на тот же файл."""
    path = ROOT / cfg["reference_image"]
    url_file = path.with_suffix(".url")
    if path.exists() and (br is None or url_file.exists()):
        return path
    if path.exists():
        sys.exit(f"Братуха берёт картинки только по ссылке. Положите публичную ссылку на эталон в "
                 f"{url_file.relative_to(ROOT)} или удалите {path.name}, чтобы сгенерировать новый.")
    log("Эталонного фото нет — генерирую по промпту персонажа…")
    path.parent.mkdir(parents=True, exist_ok=True)
    if br:
        url = br.image(cfg["reference_prompt"], "эталон")
        url_file.write_text(url + "\n", encoding="utf-8")
    else:
        url = fal_run(cfg["image_model"], {"prompt": cfg["reference_prompt"], "aspect_ratio": "9:16"})
    download(url, path)
    log(f"Эталон сохранён: {path.relative_to(ROOT)} — проверьте его, все ролики строятся от него.")
    return path


# ---------------------------------------------------------------- media/<id>.json
# Ссылки на всё, что сгенерировала Братуха для ролика (кадры, клипы, голос). Файл лежит в
# репозитории, а сами файлы — в хранилище Братухи, поэтому ролик можно пересобрать на любом
# компьютере без повторной оплаты: недостающее скачается по ссылкам.

def media_path(vid):
    return ROOT / "media" / f"{vid}.json"


def load_media(vid):
    p = media_path(vid)
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def remember(vid, key, **urls):
    m = load_media(vid)
    m.setdefault(key, {}).update(urls)
    p = media_path(vid)
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def restore_media(cfg, vid, out, n_scenes):
    """Скачивает по ссылкам из media/<id>.json то, чего нет в output/ (бесплатно)."""
    m = load_media(vid)
    clips = out / "clips"
    for i in range(1, n_scenes + 1):
        s = m.get(f"scene_{i}", {})
        clip = clips / f"scene_{i}.mp4"
        if s.get("frame") and not clip.with_suffix(".url").exists():
            clips.mkdir(parents=True, exist_ok=True)
            download(s["frame"], clip.with_suffix(".png"))
            clip.with_suffix(".url").write_text(s["frame"] + "\n", encoding="utf-8")
        if s.get("video") and not clip.exists():
            log(f"  сцена {i}: скачиваю готовый клип по ссылке из media/{vid}.json")
            download(s["video"], clip)
    v = m.get("voice", {})
    if v.get("url") and not (out / "voice.mp3").exists():
        log(f"  озвучка: скачиваю по ссылке из media/{vid}.json")
        finish_voice(cfg, v["url"], out / "voice.mp3")


def finish_voice(cfg, url, audio_path):
    speed = float(cfg["bratuha"].get("voice_speed", 1))
    if speed != 1:
        # ускоряем без изменения тембра: у TTS бабушка говорит медленнее, чем нужно для рилса
        raw = audio_path.with_name("voice_raw.mp3")
        download(url, raw)
        run_ffmpeg(["-i", str(raw), "-filter:a", f"atempo={speed}", "-c:a", "libmp3lame", "-q:a", "2", str(audio_path)])
    else:
        download(url, audio_path)


def scene_prompts(cfg, scene):
    """Промпты кадра и движения. Флешбэк (flashback: true) — старая плёнка 70-х:
    без эталона бабы Зои и без её нынешней одежды, свой стиль видео."""
    if scene.get("flashback"):
        return f"{scene['image']}. {cfg['flashback_style']}", f"{scene['motion']}. {cfg['flashback_video_style']}"
    return f"{scene['image']}. {cfg['character_lock']}", f"{scene['motion']}. {cfg['video_style']}"


def make_scene_clip_bratuha(cfg, br, reference, scene, index, slot, clip_path):
    frame_path = clip_path.with_suffix(".png")
    url_file = clip_path.with_suffix(".url")
    if not (frame_path.exists() and url_file.exists()):
        log(f"  сцена {index}: стартовый кадр")
        ref_url = reference.with_suffix(".url").read_text(encoding="utf-8").strip()
        prompt = scene_prompts(cfg, scene)[0]
        refs = None if scene.get("flashback") else [ref_url]
        url = br.image(prompt, f"сцена {index}, кадр", image_urls=refs, pending=clip_path.with_suffix(".img-op"))
        download(url, frame_path)
        url_file.write_text(url + "\n", encoding="utf-8")
        remember(clip_path.parent.parent.name, f"scene_{index}", frame=url)
    log(f"  сцена {index}: видео")
    frame_url = url_file.read_text(encoding="utf-8").strip()
    url = br.video(scene_prompts(cfg, scene)[1], frame_url, slot, f"сцена {index}, видео",
                   pending=clip_path.with_suffix(".vid-op"))
    remember(clip_path.parent.parent.name, f"scene_{index}", video=url, prompt=scene["motion"])
    download(url, clip_path)


def make_scene_clip(cfg, reference, scene, index, slot, clip_path):
    frame_path = clip_path.with_suffix(".png")
    if not frame_path.exists():
        log(f"  сцена {index}: стартовый кадр")
        prompt = scene_prompts(cfg, scene)[0]
        if scene.get("flashback"):
            url = fal_run(cfg["image_model"], {"prompt": prompt, "aspect_ratio": "9:16"})
        else:
            url = fal_run(cfg["edit_model"], {"prompt": prompt, "image_url": data_uri(reference), "aspect_ratio": "9:16"})
        download(url, frame_path)
    log(f"  сцена {index}: видео")
    payload = {
        "prompt": scene_prompts(cfg, scene)[1],
        "image_url": data_uri(frame_path),
        "duration": "10" if slot > 6 else "5",
        "resolution": cfg["video_resolution"],
    }
    download(fal_run(cfg["video_model"], payload), clip_path)


# ---------------------------------------------------------------- голос

def make_voice(cfg, text, audio_path, align_path):
    key = os.environ.get("ELEVENLABS_API_KEY")
    if not key:
        sys.exit("Нет ELEVENLABS_API_KEY в переменных окружения.")
    if cfg["voice_id"].startswith("REPLACE"):
        sys.exit("Укажите voice_id в pipeline/config.yaml.")
    log("Озвучка…")
    r = requests.post(
        f"https://api.elevenlabs.io/v1/text-to-speech/{cfg['voice_id']}/with-timestamps",
        headers={"xi-api-key": key, "Content-Type": "application/json"},
        json={"text": text, "model_id": cfg["tts_model"], "voice_settings": cfg["voice_settings"]},
        timeout=300,
    )
    r.raise_for_status()
    data = r.json()
    audio_path.write_bytes(base64.b64decode(data["audio_base64"]))
    align = data.get("alignment") or data["normalized_alignment"]
    align_path.write_text(json.dumps(words_from_alignment(align), ensure_ascii=False, indent=1), encoding="utf-8")


def make_voice_bratuha(cfg, br, text, audio_path):
    """Голос бабы Зои через Братуху. Первый раз — по описанию, потом — клон первого голоса.

    Образец голоса хранится в assets/voice/sample.json. Не понравился голос —
    удалите этот файл и voice.mp3 ролика, запустите снова.
    """
    b = cfg["bratuha"]
    cloning = b["tts_tool"] == "qwen3-tts"
    sample_file = ROOT / "assets" / "voice" / "sample.json"
    sample = json.loads(sample_file.read_text(encoding="utf-8")) if cloning and sample_file.exists() else None
    if cloning:
        log("Озвучка…" + (" (клон сохранённого голоса)" if sample else " (голос по описанию)"))
    else:
        log(f"Озвучка… ({b['tts_tool']}, голос {b.get('tts_voice')})")
    url = br.voice(text, "озвучка", sample=sample)
    remember(audio_path.parent.name, "voice", url=url, tool=b["tts_tool"], voice=b.get("tts_voice"))
    finish_voice(cfg, url, audio_path)
    if cloning and not sample:
        sample_file.parent.mkdir(parents=True, exist_ok=True)
        sample_file.write_text(json.dumps({"url": url, "text": text}, ensure_ascii=False, indent=1), encoding="utf-8")
        log(f"Образец голоса сохранён: {sample_file.relative_to(ROOT)} — следующие ролики будут этим голосом.")


def words_from_alignment(align):
    """Склеивает посимвольные тайминги ElevenLabs в слова."""
    words, current, start, end = [], "", None, None
    for ch, s, e in zip(align["characters"], align["character_start_times_seconds"], align["character_end_times_seconds"]):
        if ch.isspace():
            if current:
                words.append({"text": current, "start": start, "end": end})
            current, start = "", None
            continue
        if start is None:
            start = s
        current += ch
        end = e
    if current:
        words.append({"text": current, "start": start, "end": end})
    return words


def even_words(text, duration):
    """Равномерная раскладка слов по времени — для демо и своей озвучки."""
    tokens = text.split()
    step = duration / max(len(tokens), 1)
    return [{"text": t, "start": i * step, "end": (i + 1) * step} for i, t in enumerate(tokens)]


def speech_words(cfg, text, audio_path):
    """Тайминги слов для готовой озвучки (например, из Братухи) через распознавание речи.

    Берём из faster-whisper только время, а текст — из сценария, чтобы в субтитрах
    не было ошибок распознавания. Слова сценария раскладываются по распознанным
    словам пропорционально, так паузы и темп голоса сохраняются.
    Если faster-whisper не установлен или модель не скачать — возвращает None.
    """
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel(cfg.get("whisper_model", "small"), device="cpu", compute_type="int8")
        segments, _ = model.transcribe(str(audio_path), language="ru", word_timestamps=True)
        heard = [w for seg in segments for w in seg.words]
    except Exception as e:  # нет пакета, нет сети до модели, битый файл
        log(f"Распознавание речи недоступно ({e.__class__.__name__}) — субтитры равномерно.")
        return None
    tokens = text.split()
    if not heard or not tokens:
        return None
    words = []
    for i, token in enumerate(tokens):
        pos = i * len(heard) / len(tokens)
        h = heard[int(pos)]
        start = h.start + (pos - int(pos)) * (h.end - h.start)
        words.append({"text": token, "start": start, "end": h.end})
    words[-1]["end"] = heard[-1].end
    return words


# ---------------------------------------------------------------- субтитры

def ass_time(t):
    t = max(t, 0)
    cs = int(round(t * 100))
    return f"{cs // 360000}:{cs // 6000 % 60:02d}:{cs // 100 % 60:02d}.{cs % 100:02d}"


def ass_color(rgb):
    return f"&H00{rgb[4:6]}{rgb[2:4]}{rgb[0:2]}&".upper()


def clean_word(word):
    word = word.strip(",.;:—–-…\"«»")
    return word.replace("{", "(").replace("}", ")")


def build_subtitles(cfg, video, words, total):
    w, h = cfg["width"], cfg["height"]
    fs = cfg["font_size"]
    header = f"""[Script Info]
ScriptType: v4.00+
PlayResX: {w}
PlayResY: {h}
WrapStyle: 0
ScaledBorderAndShadow: yes

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Sub,{cfg['font_name']},{fs},&H00FFFFFF,&H00FFFFFF,&H00000000,&H64000000,1,0,0,0,100,100,0,0,1,7,3,2,80,80,{int(h * 0.27)},1
Style: Simple,{cfg['font_name']},{int(fs * 0.62)},&H00FFFFFF,&H00FFFFFF,&H00000000,&H80000000,0,0,0,0,100,100,0,0,1,2.5,1,2,90,90,{int(h * 0.13)},1
Style: Hook,{cfg['font_name']},{int(fs * 0.85)},&H00FFFFFF,&H00FFFFFF,&H00202020,&H28202020,1,0,0,0,100,100,0,0,3,22,0,8,90,90,{int(h * 0.12)},1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    lines = []
    hook = video.get("hook") if cfg.get("hook", True) else None
    if hook:
        lines.append(f"Dialogue: 1,{ass_time(0)},{ass_time(min(cfg['hook_seconds'], total))},Hook,,0,0,0,,{{\\fad(150,250)}}{hook}")

    mode = cfg.get("subtitles", "karaoke")
    if mode == "none":
        return header + "\n".join(lines) + "\n"
    per_line = cfg["words_per_line"] if mode == "karaoke" else cfg.get("simple_words_per_line", 6)

    # строки по N слов, но не через конец предложения
    groups, current = [], []
    for wd in words:
        text = clean_word(wd["text"])
        if not text:
            continue
        current.append(dict(wd, text=text, raw=wd["text"].replace("{", "(").replace("}", ")")))
        if len(current) >= per_line or wd["text"].rstrip("»\"").endswith((".", "!", "?", "…")):
            groups.append(current)
            current = []
    if current:
        groups.append(current)
    if mode == "simple":
        # спокойные субтитры фразами, как в обычном видео с телефона: без подсветки слов
        for gi, group in enumerate(groups):
            end = groups[gi + 1][0]["start"] if gi + 1 < len(groups) else total
            text = " ".join(x["raw"] for x in group)  # с пунктуацией, как пишут люди
            lines.append(f"Dialogue: 0,{ass_time(group[0]['start'])},{ass_time(end)},Simple,,0,0,0,,{text}")
        return header + "\n".join(lines) + "\n"
    highlight = ass_color(cfg["highlight_color"])
    for gi, group in enumerate(groups):
        group_end = groups[gi + 1][0]["start"] if gi + 1 < len(groups) else total
        for wi, word in enumerate(group):
            start = word["start"]
            end = group[wi + 1]["start"] if wi + 1 < len(group) else group_end
            text = " ".join(
                f"{{\\c{highlight}}}{x['text']}{{\\c&H00FFFFFF&}}" if xi == wi else x["text"]
                for xi, x in enumerate(group)
            )
            lines.append(f"Dialogue: 0,{ass_time(start)},{ass_time(end)},Sub,,0,0,0,,{text}")
    return header + "\n".join(lines) + "\n"


# ---------------------------------------------------------------- монтаж

def normalize_clip(cfg, src, dst, slot):
    w, h, fps = cfg["width"], cfg["height"], cfg["fps"]
    # клип чуть короче слота (6 с на слот 6.5 с) — плавно замедляем, а не замораживаем последний кадр
    stretch = slot / media_duration(src)
    slow = f"setpts={stretch:.4f}*PTS," if 1 < stretch <= 1.25 else ""
    vf = (
        f"{slow}scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={fps},setsar=1,"
        f"tpad=stop_mode=clone:stop_duration={slot + 1:.2f},trim=duration={slot:.3f},setpts=PTS-STARTPTS"
    )
    run_ffmpeg(["-i", str(src), "-an", "-vf", vf, "-c:v", "libx264", "-preset", "veryfast",
                "-crf", "18", "-pix_fmt", "yuv420p", str(dst)])


def demo_clip(cfg, dst, index, slot):
    colors = ["0x8B3A3A", "0x3A5F8B", "0x6B8E23", "0xB8860B", "0x5B3A8B"]
    run_ffmpeg(["-f", "lavfi", "-i", f"color=c={colors[(index - 1) % len(colors)]}:s={cfg['width']}x{cfg['height']}:r={cfg['fps']}:d={slot:.3f}",
                "-c:v", "libx264", "-preset", "veryfast", "-pix_fmt", "yuv420p", str(dst)])


def find_music():
    folder = ROOT / "assets" / "music"
    for ext in ("*.mp3", "*.m4a", "*.wav", "*.ogg"):
        tracks = sorted(folder.glob(ext))
        if tracks:
            return tracks[0]
    return None


AUDIO_EXTS = (".mp3", ".m4a", ".wav", ".ogg", ".aac")


def import_inbox(vid, out):
    """Забирает файлы, сгенерированные вручную (например, в Братухе), из inbox/<id>/.

    Видео берутся по порядку имён: scene_1.mp4, scene_2.mp4… (или любые имена —
    тогда по алфавиту). Озвучка — первый аудиофайл, переводится в voice.mp3.
    Уже импортированное не перезаписывается.
    """
    inbox = ROOT / "inbox" / vid
    if not inbox.is_dir():
        return
    clips_dir = out / "clips"
    clips_dir.mkdir(parents=True, exist_ok=True)

    def order(p):
        nums = re.findall(r"\d+", p.stem)
        return (int(nums[-1]) if nums else 10**6, p.name)

    videos = sorted((p for p in inbox.iterdir() if p.suffix.lower() in (".mp4", ".mov", ".webm")), key=order)
    for i, src in enumerate(videos, 1):
        dst = clips_dir / f"scene_{i}.mp4"
        if not dst.exists():
            run_ffmpeg(["-i", str(src), "-an", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                        "-pix_fmt", "yuv420p", str(dst)])
            log(f"  из inbox: {src.name} → сцена {i}")
    voice = out / "voice.mp3"
    audios = sorted(p for p in inbox.iterdir() if p.suffix.lower() in AUDIO_EXTS)
    if audios and not voice.exists():
        run_ffmpeg(["-i", str(audios[0]), "-vn", "-c:a", "libmp3lame", "-b:a", "192k", str(voice)])
        log(f"  из inbox: {audios[0].name} → озвучка")


def build(video, cfg, demo=False, dry_run=False, new_voice=False):
    vid = video["id"]
    # демо пишем в отдельную папку, чтобы заглушки не подхватились в настоящий прогон
    out = ROOT / "output" / (f"{vid}-demo" if demo else vid)
    clips_dir = out / "clips"
    scenes = video["scenes"]
    log(f"Ролик {vid}: {video['title']} ({len(scenes)} сцен)")

    # --- озвучка и тайминги слов
    audio, align = out / "voice.mp3", out / "words.json"
    if new_voice and not dry_run:
        # поменяли текст озвучки: старый голос и тайминги слов — в сторону, клипы остаются
        m = load_media(vid)
        if "voice" in m:
            m["voice_old"] = m.pop("voice")
            media_path(vid).write_text(json.dumps(m, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        for f in (audio, align):
            f.unlink(missing_ok=True)
        log("  новая озвучка: старый голос убран, клипы переиспользую")
    bratuha = cfg.get("provider") == "bratuha"
    if dry_run:
        inbox = ROOT / "inbox" / vid
        files = sorted(p.name for p in inbox.iterdir()) if inbox.is_dir() else []
        saved = load_media(vid)
        missing = [i for i in range(1, len(scenes) + 1)
                   if not (clips_dir / f"scene_{i}.mp4").exists() and not saved.get(f"scene_{i}", {}).get("video")]
        log(f"  inbox/{vid}: {', '.join(files) or 'пусто'}")
        if saved:
            log(f"  media/{vid}.json: есть ссылки на готовое — скачается бесплатно")
        if not os.environ.get("BRATUHA_API_KEY" if bratuha else "FAL_KEY"):
            log("  ключа нет — ручной режим: ничего не генерирую и не трачу, монтирую из inbox")
            return
        where = "Братуха" if bratuha else "ElevenLabs / fal.ai"
        log(f"  озвучка: {'есть' if audio.exists() else f'будет сгенерирована ({where})'}")
        log(f"  клипы к генерации ({where}): {missing or 'все на месте'}")
        if bratuha:
            b = cfg["bratuha"]
            ref = 0 if (ROOT / cfg["reference_image"]).exists() else 1
            frames = sum(1 for i in missing if not (clips_dir / f"scene_{i}.url").exists())
            voice = 0 if audio.exists() else len(video["voiceover"]) * b["price_tts_per_1000"] / 1000
            # длина ролика: по готовой озвучке или ~14 символов текста в секунду (Gemini, x1.15)
            total = media_duration(audio) if audio.exists() else len(video["voiceover"]) / 14
            clip_sec = max(4, -(-total // len(scenes)))
            est = (ref + frames) * b["price_image"] + len(missing) * clip_sec * b["price_video_per_sec"] + voice
            log(f"  примерно {est:.0f} ₽ (эталон {ref}, кадров {frames}, видео {len(missing)}; точная цена — в логе запуска)")
        return
    clips_dir.mkdir(parents=True, exist_ok=True)
    if not demo:
        restore_media(cfg, vid, out, len(scenes))
        import_inbox(vid, out)
    # без ключа выбранного сервиса ничего не генерируем: собираем из того, что загружено вручную
    key_name = "BRATUHA_API_KEY" if bratuha else "FAL_KEY"
    manual = not demo and not os.environ.get(key_name)
    br = Bratuha(cfg, ROOT / "output" / "bratuha_spend.json", log) if bratuha and not demo and not manual else None
    if manual:
        ready = sorted(clips_dir.glob("scene_*.mp4"), key=lambda p: int(re.findall(r"\d+", p.stem)[0]))
        if not ready:
            sys.exit(f"Нет клипов. Положите scene_1.mp4, scene_2.mp4… в inbox/{vid}/ (или задайте {key_name}).")
        if not audio.exists() and (bratuha or not os.environ.get("ELEVENLABS_API_KEY")):
            sys.exit(f"Нет озвучки. Положите voice.mp3 в inbox/{vid}/ (или задайте {key_name}).")
        if len(ready) != len(scenes):
            log(f"  клипов {len(ready)} из {len(scenes)} по сценарию — собираю из тех, что есть")
        scenes = scenes[:len(ready)] + [{}] * (len(ready) - len(scenes))
    if demo and not audio.exists():
        duration = max(len(video["voiceover"].split()) / 2.6, 8)
        run_ffmpeg(["-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono", "-t", f"{duration:.2f}", "-c:a", "libmp3lame", str(audio)])
        align.write_text(json.dumps(even_words(video["voiceover"], duration), ensure_ascii=False), encoding="utf-8")
    elif not audio.exists():
        if br:
            make_voice_bratuha(cfg, br, video["voiceover"], audio)
        else:
            make_voice(cfg, video["voiceover"], audio, align)
    if not align.exists():
        log("Своя озвучка — подгоняю субтитры под голос…")
        words = speech_words(cfg, video["voiceover"], audio) or even_words(video["voiceover"], media_duration(audio))
        align.write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
    words = json.loads(align.read_text(encoding="utf-8"))
    total = max(media_duration(audio), words[-1]["end"]) + cfg["tail_seconds"]

    # --- клипы сцен
    slot = total / len(scenes)
    reference = None
    normalized = []
    for i, scene in enumerate(scenes, 1):
        clip = clips_dir / f"scene_{i}.mp4"
        if not clip.exists():
            if demo:
                demo_clip(cfg, clip, i, slot)
            else:
                reference = reference or ensure_reference(cfg, br)
                if br:
                    make_scene_clip_bratuha(cfg, br, reference, scene, i, slot, clip)
                else:
                    make_scene_clip(cfg, reference, scene, i, slot, clip)
        norm = out / f"norm_{i}.mp4"
        normalize_clip(cfg, clip, norm, slot)
        normalized.append(norm)

    (out / "concat.txt").write_text("".join(f"file '{p.name}'\n" for p in normalized), encoding="utf-8")
    run_ffmpeg(["-f", "concat", "-safe", "0", "-i", "concat.txt", "-c", "copy", "video.mp4"], cwd=out)

    # --- субтитры
    (out / "subs.ass").write_text(build_subtitles(cfg, video, words, total), encoding="utf-8")

    # --- финальная сборка
    fonts = os.path.relpath(ROOT / "assets" / "fonts", out)
    inputs = ["-i", "video.mp4", "-i", "voice.mp3"]
    music = find_music()
    if music:
        inputs += ["-stream_loop", "-1", "-i", str(music)]
        audio_filter = (f"[1:a]apad[voice];[2:a]volume={cfg['music_volume']},afade=t=out:st={max(total - 1.5, 0):.2f}:d=1.5[bg];"
                        f"[voice][bg]amix=inputs=2:duration=first:normalize=0[a]")
    else:
        audio_filter = "[1:a]apad[a]"
    filters = f"[0:v]ass=subs.ass:fontsdir={fonts}[v];{audio_filter}"
    final = out / f"{vid}.mp4"
    run_ffmpeg([*inputs, "-filter_complex", filters, "-map", "[v]", "-map", "[a]", "-t", f"{total:.3f}",
                "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p",
                "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", final.name], cwd=out)

    (out / "caption.txt").write_text(video["caption"], encoding="utf-8")
    for tmp in normalized + [out / "concat.txt", out / "video.mp4"]:
        tmp.unlink(missing_ok=True)
    log(f"Готово: {final.relative_to(ROOT)} ({total:.1f} с), подпись к посту — caption.txt")
    if br:
        log(f"Братуха: всего потрачено {br.spend['total_rub']:g} ₽ (детали — output/bratuha_spend.json)")


def load_videos(base_cfg):
    """Все ролики из content/*.yaml: id → (ролик, настройки).

    Файл сценариев может начинаться с блока persona: — это настройки персонажа
    (эталон, character_lock, голос…), они накрывают pipeline/config.yaml для его роликов.
    Так у бабы Зои (content/scripts.yaml) и Веры (content/vera.yaml) свои лица и голоса.
    """
    found = {}
    for path in sorted((ROOT / "content").glob("*.yaml")):
        data = load_yaml(path) or {}
        if not isinstance(data, dict) or "videos" not in data:
            continue
        cfg = json.loads(json.dumps(base_cfg))
        for key, value in (data.get("persona") or {}).items():
            if isinstance(value, dict) and isinstance(cfg.get(key), dict):
                cfg[key].update(value)
            else:
                cfg[key] = value
        for video in data["videos"]:
            if video["id"] in found:
                sys.exit(f"Ролик {video['id']} встречается дважды (второй раз — в {path.name})")
            found[video["id"]] = (video, cfg)
    return found


def main():
    parser = argparse.ArgumentParser(description="Сборка роликов бабы Зои")
    parser.add_argument("ids", nargs="*", help="id роликов из content/*.yaml (баба Зоя, Вера…)")
    parser.add_argument("--all", action="store_true", help="собрать все ролики")
    parser.add_argument("--demo", action="store_true", help="без API: заглушки вместо видео и голоса")
    parser.add_argument("--dry-run", action="store_true", help="только показать, что будет сгенерировано")
    parser.add_argument("--new-voice", action="store_true",
                        help="переозвучить (после правки voiceover): новый голос и субтитры, клипы те же")
    args = parser.parse_args()

    by_id = load_videos(load_yaml(ROOT / "pipeline" / "config.yaml"))
    ids = list(by_id) if args.all else args.ids
    if not ids:
        parser.error("укажите id ролика или --all. Доступны: " + ", ".join(by_id))
    for vid in ids:
        if vid not in by_id:
            sys.exit(f"Нет ролика {vid}. Доступны: {', '.join(by_id)}")
        global WHO
        video, cfg = by_id[vid]
        WHO = cfg.get("name", "баба Зоя")
        build(video, cfg, demo=args.demo, dry_run=args.dry_run, new_voice=args.new_voice)


if __name__ == "__main__":
    main()
