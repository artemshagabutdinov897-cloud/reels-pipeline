#!/usr/bin/env python3
"""Пишет шпаргалки для ручной генерации в Братухе: content/prompts/<id>.md.

На каждый ролик — одна страница с готовыми промптами по шагам: кадры сцен
(Nano Banana), видео (Seedance), озвучка, подпись к посту. Каждый промпт —
в отдельном блоке, чтобы копировать одним нажатием.

  python pipeline/make_prompts.py
"""

import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_video import load_videos, scene_prompts  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent

VOICE = ("Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, "
         "говорит спокойно, по-доброму, чуть с хитринкой.")


def block(text):
    return f"```\n{text.strip()}\n```\n"


def page(video, cfg):
    vid = video["id"]
    lines = [
        f"# {vid} — {video['title']}\n",
        f"Рубрика: {video['rubric']}."
        + (f" Надпись-крючок (её добавлю сам при монтаже): «{video['hook']}»" if video.get("hook") else "") + "\n",
        "## Шаг 0. Эталонное фото (один раз на весь проект)\n",
        f"Если эталон ({cfg.get('name', 'баба Зоя')}) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, "
        f"3–4 варианта, выберите лучший и сохраните как `{Path(cfg['reference_image']).name}`.\n",
        block(cfg["reference_prompt"]),
        "## Шаг 1. Кадры сцен — Nano Banana\n",
        "Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. "
        "Сохраните как `scene_N.png`.\n",
    ]
    for i, scene in enumerate(video["scenes"], 1):
        note = " — флешбэк: **без** эталона, просто по тексту" if scene.get("flashback") else ""
        lines += [f"**Сцена {i}**{note} → `scene_{i}.png`\n", block(scene_prompts(cfg, scene)[0])]
    lines += [
        "## Шаг 2. Видео — Seedance\n",
        "Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, "
        "вставьте промпт. Сохраните как `scene_N.mp4`.\n",
    ]
    for i, scene in enumerate(video["scenes"], 1):
        lines += [f"**Сцена {i}**: кадр `scene_{i}.png` → `scene_{i}.mp4`\n",
                  block(scene_prompts(cfg, scene)[1])]
    lines += [
        "## Шаг 3. Озвучка\n",
        f"Озвучка в Братухе: Gemini TTS, голос **{cfg['bratuha'].get('tts_voice', '—')}**. Если его нет — любой похожий:\n",
        block(cfg.get("voice_hint") or VOICE),
        "Текст целиком, как есть (сохраните как `voice.mp3`):\n",
        block(video["voiceover"]),
        "## Шаг 4. Отдать мне на монтаж\n",
        f"Загрузите `scene_1.mp4`…`scene_{len(video['scenes'])}.mp4` и `voice.mp3` в папку "
        f"`inbox/{vid}/` на GitHub (ветка `main` → "
        "Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.\n",
        "Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.\n",
        "## Подпись к посту\n",
        block(video["caption"]),
    ]
    return "\n".join(lines)


def main():
    base = yaml.safe_load((ROOT / "pipeline" / "config.yaml").read_text(encoding="utf-8"))
    videos = load_videos(base)
    out = ROOT / "content" / "prompts"
    out.mkdir(parents=True, exist_ok=True)
    for video, cfg in videos.values():
        (out / f"{video['id']}.md").write_text(page(video, cfg), encoding="utf-8")
    print(f"Шпаргалки: {len(videos)} файлов в {out.relative_to(ROOT)}/")


if __name__ == "__main__":
    main()
