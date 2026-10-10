"""Ролик-цепочка: опорные кадры (каждый — правка предыдущего) и клипы между ними.

python pipeline/chain.py <id>   — сценарий в content/chain.yaml
frames-клип: Seedance 2.5 плавно ведёт от кадра A к кадру B (камера стоит, меняется только содержимое).
image-клип: обычное оживление одного кадра. Всё, что уже сделано, берётся из media/<id>.json (повтор бесплатный).
"""
import sys, json, threading
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M
from bratuha import Bratuha

vid = sys.argv[1]
spec = next(v for v in M.load_yaml(M.ROOT / "content" / "chain.yaml")["chains"] if v["id"] == vid)
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
cfg["bratuha"]["video_resolution"] = spec.get("resolution", cfg["bratuha"]["video_resolution"])
br = Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
mp = M.ROOT / "media" / f"{vid}.json"
media = json.loads(mp.read_text(encoding="utf-8")) if mp.exists() else {"keyframes": {}, "clips": {}}
LOCK = threading.Lock()
def save():
    with LOCK:
        mp.parent.mkdir(parents=True, exist_ok=True)
        mp.write_text(json.dumps(media, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

img_style = spec.get("image_style", "")
for name, k in spec["keyframes"].items():
    if media["keyframes"].get(name):
        continue
    if k.get("url"):  # готовый кадр (например, та же банка из прошлого ролика)
        media["keyframes"][name] = k["url"]
        save()
        continue
    refs = [media["keyframes"][r] for r in (k.get("refs") or [])]
    prompt = f"{k['prompt']} {img_style}".strip()
    M.log(f"кадр {name}")
    media["keyframes"][name] = br.image(prompt, f"{vid} кадр {name}", image_urls=refs or None)
    save()

vstyle = spec.get("video_style", "")
def clip(i, c):
    key = f"clip_{i}"
    if media["clips"].get(key):
        return key
    prompt = f"{c['prompt']} {vstyle}".strip()
    dur = int(c.get("seconds", 4))
    base = {"prompt": prompt, "resolution": br.cfg["video_resolution"], "duration": dur,
            "generate_audio": False, "watermark": False, "output_format": "mp4"}
    if c["type"] == "frames":
        payload = dict(base, seedance_2_5_generation_type="frames", size="adaptive",
                       first_frame_url=media["keyframes"][c["first"]], last_frame_url=media["keyframes"][c["last"]])
    else:
        payload = dict(base, seedance_2_5_generation_type="image", size="9:16",
                       image_urls=[media["keyframes"][c["image"]]])
    url = br.run(br.cfg["video_tool"], payload, f"{vid} клип {i}")
    with LOCK:
        media["clips"][key] = url
    save()
    return key

with ThreadPoolExecutor(4) as ex:
    futs = [ex.submit(clip, i, c) for i, c in enumerate(spec["clips"], 1)]
    for f in futs:
        try:
            M.log(f"готов {f.result()}")
        except BaseException as e:
            M.log(f"клип упал: {e!r}")
missing = [i for i in range(1, len(spec["clips"]) + 1) if not media["clips"].get(f"clip_{i}")]
M.log(f"Братуха: потрачено {br.spend['total_rub']} ₽")
if missing:
    sys.exit(f"не готовы клипы {missing} — перезапуск доделает только их")
