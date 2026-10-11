"""Любая нейросеть Братухи: python pipeline/bratuha_any.py <name> <tool> '<json input>'
Результат — previews/<name>.url."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, tool, payload = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
url = br.run(tool, payload, name, None)
out = M.ROOT / "previews"
out.mkdir(exist_ok=True)
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
