"""Одна картинка через Братуху: python pipeline/one_image.py <name> "<prompt>" [url ...]
Первым референсом идёт эталон бабы Зои, дальше — переданные ссылки. Результат — previews/<name>.png и .url"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, prompt, extra = sys.argv[1], sys.argv[2], sys.argv[3:]
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
ref = (M.ROOT / "assets" / "reference" / "baba-zoya.url").read_text().strip()
url = br.image(prompt, name, image_urls=[ref] + extra)
out = M.ROOT / "previews"
out.mkdir(exist_ok=True)
M.download(url, out / f"{name}.png")
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
