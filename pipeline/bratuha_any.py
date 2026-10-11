"""Любая нейросеть Братухи: python pipeline/bratuha_any.py <name> <tool> '<json input>'
Результат — previews/<name>.url."""
import json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, tool, payload = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
if tool == "__list__":
    import os, urllib.request
    req = urllib.request.Request("https://bratuha.ru/api/v1/tools", headers={"Authorization": "Bearer " + os.environ["BRATUHA_API_KEY"]})
    data = json.loads(urllib.request.urlopen(req, timeout=60).read())
    items = data.get("tools") or data.get("data") or data
    want = payload.get("filter", "")
    out = []
    for t in (items if isinstance(items, list) else []):
        s = json.dumps(t, ensure_ascii=False)
        if want.lower() in s.lower():
            out.append(s[:600])
    print("\n".join(out) or json.dumps(data, ensure_ascii=False)[:3000])
    sys.exit(0)
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
url = br.run(tool, payload, name, None)
out = M.ROOT / "previews"
out.mkdir(exist_ok=True)
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
