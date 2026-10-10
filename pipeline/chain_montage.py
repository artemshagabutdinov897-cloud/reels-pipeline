#!/usr/bin/env python3
"""Склейка ролика-цепочки (content/chain.yaml) в готовый вертикальный ролик с музыкой.

chain.py делает только кадры и клипы и записывает ссылки в media/<id>.json.
Этот скрипт скачивает клипы по порядку, приводит к 1080x1920, склеивает и
подкладывает фоновую музыку. Ничего не генерирует и не тратит.

  python pipeline/chain_montage.py l05-whisky                 # музыка №1
  python pipeline/chain_montage.py l06-kedrovka --music 2     # previews/gradus-music-2.url
  python pipeline/chain_montage.py l07-medovuha --music none  # без музыки

Результат: output/<id>/<id>.mp4. Клипы кешируются в output/<id>/clips/.
"""

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import make_video as M  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description="Склейка ролика-цепочки с музыкой")
    parser.add_argument("id", help="id из content/chain.yaml, например l05-whisky")
    parser.add_argument("--music", default="1", help="номер трека previews/gradus-music-N.url, путь к файлу или none")
    parser.add_argument("--volume", type=float, default=0.7, help="громкость музыки (0..1)")
    args = parser.parse_args()

    cfg = M.load_yaml(M.ROOT / "pipeline" / "config.yaml")
    M.WHO = "склейка"
    clips = M.load_media(args.id).get("clips", {})
    order = sorted(clips, key=lambda k: int(k.split("_")[1]))
    if not order:
        sys.exit(f"В media/{args.id}.json нет клипов — сначала python pipeline/chain.py {args.id}")
    expected = [v for v in M.load_yaml(M.ROOT / "content" / "chain.yaml")["chains"] if v["id"] == args.id]
    if expected and len(expected[0].get("clips", [])) != len(order):
        M.log(f"клипов {len(order)} из {len(expected[0]['clips'])} по сценарию — склеиваю те, что есть")

    out = M.ROOT / "output" / args.id
    (out / "clips").mkdir(parents=True, exist_ok=True)
    normalized = []
    for key in order:
        src = out / "clips" / f"{key}.mp4"
        if not src.exists():
            M.log(f"скачиваю {key}")
            M.download(clips[key], src)
        norm = out / f"norm_{key}.mp4"
        M.normalize_clip(cfg, src, norm, M.media_duration(src))
        normalized.append(norm)

    (out / "concat.txt").write_text("".join(f"file '{p.name}'\n" for p in normalized), encoding="utf-8")
    M.run_ffmpeg(["-f", "concat", "-safe", "0", "-i", "concat.txt", "-c", "copy", "video.mp4"], cwd=out)
    total = M.media_duration(out / "video.mp4")

    music = None
    if args.music != "none":
        url_file = M.ROOT / "previews" / f"gradus-music-{args.music}.url"
        if url_file.exists():
            music = out / f"music-{args.music}.m4a"
            if not music.exists():
                M.download(url_file.read_text(encoding="utf-8").strip(), music)
        elif Path(args.music).exists():
            music = Path(args.music).resolve()
        else:
            sys.exit(f"Нет музыки {args.music}: ни {url_file.relative_to(M.ROOT)}, ни такого файла")

    final = out / f"{args.id}.mp4"
    if music:
        fade = max(total - 1.5, 0)
        M.run_ffmpeg(["-i", "video.mp4", "-stream_loop", "-1", "-i", str(music),
                      "-filter_complex", f"[1:a]volume={args.volume},afade=t=out:st={fade:.2f}:d=1.5[a]",
                      "-map", "0:v", "-map", "[a]", "-t", f"{total:.3f}", "-c:v", "copy",
                      "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", final.name], cwd=out)
    else:
        M.run_ffmpeg(["-i", "video.mp4", "-c", "copy", "-movflags", "+faststart", final.name], cwd=out)

    for tmp in normalized + [out / "concat.txt", out / "video.mp4"]:
        tmp.unlink(missing_ok=True)
    M.log(f"Готово: {final.relative_to(M.ROOT)} ({total:.1f} с, клипов {len(order)})")


if __name__ == "__main__":
    main()
