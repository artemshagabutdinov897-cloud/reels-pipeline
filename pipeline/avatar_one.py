"""Говорящий кусок через Seedance 2.5 (references) на Братухе: кадр + голос -> губы в такт.
python pipeline/avatar_one.py <name> <image_url> <audio_url|-> <seconds> "<prompt>"  -> previews/<name>.mp4"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, image_url, audio_url, secs, prompt = sys.argv[1:6]
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
payload = {"seedance_2_5_generation_type": "references", "prompt": prompt,
           "reference_image_urls": [image_url], "audio_urls": [audio_url],
           "size": "9:16", "resolution": "480p", "duration": max(4, int(float(secs))),
           "generate_audio": True, "watermark": False, "output_format": "mp4"}
if audio_url in ("", "-"):  # закадровый план: без голоса, только движение
    payload.pop("audio_urls"); payload["generate_audio"] = False
url = br.run("seedance-2-5", payload, name)
out = M.ROOT / "previews"; out.mkdir(exist_ok=True)
M.download(url, out / f"{name}.mp4")
(out / f"{name}.url").write_text(url + "\n")
M.log(f"готово: {url}")
