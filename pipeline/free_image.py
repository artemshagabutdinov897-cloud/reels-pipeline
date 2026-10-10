"""Картинка без эталона бабы Зои: python pipeline/free_image.py <name> "<prompt>" [aspect]
aspect — 4:5, 3:4, 2:3, 1:1, 9:16 и т. п. Результат — previews/<name>.png и .url"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, prompt = sys.argv[1], sys.argv[2]
aspect = sys.argv[3] if len(sys.argv) > 3 else "3:4"
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
c = br.cfg
payload = {"mode": c["image_mode"], "prompt": prompt, "aspect_ratio": aspect, "image_size": c["image_size"]}
url = br.run(c["image_tool"], payload, name, None)
out = M.ROOT / "previews"
out.mkdir(exist_ok=True)
M.download(url, out / f"{name}.png")
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
