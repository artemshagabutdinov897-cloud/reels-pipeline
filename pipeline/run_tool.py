"""Один вызов любой нейросети Братухи: python pipeline/run_tool.py <name> <tool_slug> '<json payload>'
Ссылку на результат пишет в previews/<name>.url (и все ссылки — в previews/<name>.json).
Payload "SCHEMA" — не запускать, а выгрузить каталог: slug содержит <tool_slug> (через запятую несколько) ->
previews/<name>.json со списком моделей и их input_schema."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M
from bratuha import Bratuha, API
import requests
name, tool, payload = sys.argv[1], sys.argv[2], sys.argv[3]
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
out = M.ROOT / "previews"; out.mkdir(exist_ok=True)
if payload == "SCHEMA":
    keys = [k.strip().lower() for k in tool.split(",") if k.strip()]
    tools = requests.get(f"{API}/tools", headers=br.headers, timeout=60).json()
    items = tools.get("data", tools) if isinstance(tools, dict) else tools
    res = []
    for t in items:
        slug = t.get("slug", "")
        if any(k in slug.lower() for k in keys):
            sch = requests.get(f"{API}/tools/{slug}/schema", headers=br.headers, timeout=60)
            try:
                s = sch.json()
            except ValueError:
                s = {"raw": sch.text[:3000]}
            res.append({"slug": slug, "name": t.get("name"), "description": t.get("description"), "pricing": t.get("pricing"),
                        "input_schema": s.get("input_schema", s)})
    (out / f"{name}.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
    M.log(f"{name}: {len(res)} моделей — " + ", ".join(r["slug"] for r in res))
    sys.exit(0)
payload = json.loads(payload)
url = br.run(tool, payload, name)
(out / f"{name}.url").write_text(url + "\n", encoding="utf-8")
M.log(f"{name}: {url}")
