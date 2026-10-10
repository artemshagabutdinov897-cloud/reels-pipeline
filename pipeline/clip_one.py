"""Немой клип через Братуху (Seedance 2.5).
python pipeline/clip_one.py <name> <seconds> <mode> "<image prompt|url>" "<motion prompt>"
mode: 0 — картинка nano-banana по описанию, потом оживление; 1 — сразу видео по эталону бабы Зои (references);
      url — оживление готовой картинки по ссылке."""
import math, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M

name, secs, mode, img_p, mot_p = sys.argv[1:6]
cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
br = M.Bratuha(cfg, M.ROOT / "output" / "bratuha_spend.json", M.log)
out = M.ROOT / "previews"; out.mkdir(exist_ok=True)
tail = "Realistic subtle natural motion, slow gentle camera push-in, nobody speaks, no text, no subtitles."
style = ("Photorealistic, natural light, shot on 35mm, vertical 9:16, documentary style, realistic textures. "
         "No text, letters or labels anywhere in the picture.")
if mode == "1":
    ref = (M.ROOT / "assets" / "reference" / "baba-zoya.url").read_text().strip()
    prompt = (f"@image1 — this exact elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, "
              f"blue floral dress, white apron. {img_p}. {mot_p}. {style} {tail}")
    payload = {"seedance_2_5_generation_type": "references", "prompt": prompt, "reference_image_urls": [ref],
               "size": "9:16", "resolution": cfg["bratuha"]["video_resolution"], "duration": min(30, max(4, math.ceil(float(secs)))),
               "generate_audio": False, "watermark": False, "output_format": "mp4"}
    vid = br.run(cfg["bratuha"]["video_tool"], payload, f"{name} видео")
else:
    img = img_p if mode == "url" else br.image(f"{img_p}. {style}", f"{name} кадр")
    vid = br.video(f"{mot_p}. {tail}", img, float(secs), f"{name} видео")
M.download(vid, out / f"{name}.mp4")
(out / f"{name}.url").write_text(vid + "\n")
M.log(f"готово {vid}")
