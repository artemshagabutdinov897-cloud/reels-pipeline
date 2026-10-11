"""Любая нейросеть Братухи: python pipeline/bratuha_any.py <name> <tool> '<json input>'
tool = "__list__" (payload {"filter": "..."}) — список инструментов; "__schema__:<slug>" — поля инструмента.
Результат генерации — previews/<name>.url."""
import json, os, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M


def api(path):
    req = urllib.request.Request("https://bratuha.ru/api/v1/" + path,
                                 headers={"Authorization": "Bearer " + os.environ["BRATUHA_API_KEY"]})
    return json.loads(urllib.request.urlopen(req, timeout=60).read())


name, tool, payload = sys.argv[1], sys.argv[2], json.loads(sys.argv[3])
if tool.startswith("__schema__:"):
    sch = api("tools/" + tool.split(":", 1)[1] + "/schema").get("input_schema", {})
    for k, v in sch.get("properties", {}).items():
        print(k, json.dumps({x: v.get(x) for x in ("type", "enum", "default", "minimum", "maximum")}))
    print("required:", sch.get("required"))
    sys.exit(0)
if tool == "__list__":
    data = api("tools")
    items = data.get("tools") or data.get("data") or []
    want = payload.get("filter", "").lower()
    for t in items:
        s = json.dumps(t, ensure_ascii=True)
        if want in s.lower():
            print(t.get("slug"), t.get("name"), json.dumps(t.get("pricing")))
    sys.exit(0)
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
url = br.run(tool, payload, name, None)
out = M.ROOT / "previews"
out.mkdir(exist_ok=True)
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
