"""Быстрый прогон: озвучка, потом все сцены параллельно, потом обычная сборка make_video.build."""
import sys, threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

LOCK = threading.Lock()
_remember = M.remember
def remember(*a, **k):
    with LOCK:
        return _remember(*a, **k)
M.remember = remember

vid = sys.argv[1]
video, cfg = M.load_videos(M.load_yaml(M.ROOT / "pipeline" / "config.yaml"))[vid]
scenes = video["scenes"]
out = M.ROOT / "output" / vid
clips = out / "clips"
clips.mkdir(parents=True, exist_ok=True)
M.restore_media(cfg, vid, out, len(scenes))
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
_rec = br._record
def rec(*a, **k):
    with LOCK:
        return _rec(*a, **k)
br._record = rec
audio = out / "voice.mp3"
if not audio.exists():
    M.make_voice_bratuha(cfg, br, video["voiceover"], audio)
total = M.media_duration(audio) + cfg["tail_seconds"]
slot = total / len(scenes)
M.log(f"голос {total:.1f} с, на сцену {slot:.1f} с")
ref = M.ensure_reference(cfg, br)
def one(i):
    clip = clips / f"scene_{i}.mp4"
    if not clip.exists():
        M.make_scene_clip_bratuha(cfg, br, ref, scenes[i - 1], i, slot, clip)
    return i
with ThreadPoolExecutor(len(scenes)) as ex:
    for f in [ex.submit(one, i) for i in range(1, len(scenes) + 1)]:
        try:
            M.log(f"сцена {f.result()} готова")
        except BaseException as e:
            M.log(f"сцена упала: {e!r}")
missing = [i for i in range(1, len(scenes) + 1) if not (clips / f"scene_{i}.mp4").exists()]
if missing:
    sys.exit(f"не готовы сцены {missing} — перезапуск доделает только их")
M.build(video, cfg)
