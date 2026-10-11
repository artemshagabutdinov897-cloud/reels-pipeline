"""Видео Grok через Братуху: python pipeline/grok_one.py <name> "<prompt>" "<url1,url2>" <seconds> <resolution> [tool]
Результат — previews/<name>.url (ссылка на mp4)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, prompt, images, seconds, res = sys.argv[1:6]
tool = sys.argv[6] if len(sys.argv) > 6 else "grok-video-1-5"
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
payload = {"prompt": prompt, "image_urls": [u.strip() for u in images.split(",") if u.strip()],
           "aspect_ratio": "9:16", "duration": int(seconds), "resolution": res}
url = br.run(tool, payload, name, None)
out = M.ROOT / "previews"
out.mkdir(exist_ok=True)
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
