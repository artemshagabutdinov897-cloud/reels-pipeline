# v02-bez-otdushki — «Без отдушки» — а это тогда что?

Рубрика: Читаю состав.

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (Вера) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `vera.jpg`.

```
Candid smartphone front-camera photo of a 27-year-old Russian woman with a friendly, slightly ironic expression: one eyebrow a little raised and a half-smile. Long dark chestnut hair loosely pinned up with a tortoiseshell claw clip, a few loose strands, warm brown eyes, light freckles across the nose, natural skin with visible texture and almost no makeup, small gold hoop earrings, oversized cream knit sweater. Sitting at a sunlit kitchen table by a window with green plants and a few plain unbranded skincare jars. Natural daylight, slight phone-camera grain, vertical 9:16. No text or logos.
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
Close-up of her hand holding a plain white unbranded cream jar towards the camera, the other hand pointing at the front of the jar. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
She sits at the sunlit kitchen table turning the plain jar to its back side, squinting at tiny blurred unreadable print. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
She sniffs an opened plain cream jar with a skeptical face at the kitchen table. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
She looks straight at the camera by the window with plants, holding the jar next to her face. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
She taps the front of the jar with a fingernail and raises one eyebrow. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She turns the jar around, brings it closer to her eyes and slowly nods. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She smells the cream, pulls back and gives the camera an ironic look. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She shrugs slightly and smiles, as if saying "that's how it is". Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Sulafat**. Если его нет — любой похожий:

```
Молодая девушка 27 лет, живой тёплый голос с улыбкой и лёгкой иронией, говорит как подруге, не спеша, но бодро.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
На банке крупно: «без отдушки». Переворачиваю — а в составе эфирное масло лаванды. Формально не врут: отдушки нет, а пахнуть есть чему. Если у тебя кожа реагирует на запахи, ищи не надпись на лицевой стороне, а слова Parfum, Fragrance и масла в конце списка. Какую надпись на банке проверим следующей? Пиши в комментариях.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/v02-bez-otdushki/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
На банке крупно «без отдушки», а пахнет лавандой. Как так? 👀

«Без отдушки» обычно значит: нет синтетического ароматизатора (Parfum / Fragrance). А эфирные масла — лаванда, цитрус, чайное дерево — отдушкой формально не считаются. Пахнуть есть чему.

Как проверяю я:
1. Ищу в составе Parfum или Fragrance.
2. Смотрю, нет ли эфирных масел: Lavandula, Citrus, Mentha…
3. Если кожа капризная — «без отдушки» на лицевой стороне ничего не гарантирует, решает только состав.

Это не значит, что эфирные масла — зло. Просто покупай, понимая, что внутри.

Какую надпись на банке проверим следующей? Пиши в комментариях 👇

Я ИИ-персонаж: читаю составы без рекламной шелухи. Я не врач и не косметолог — если с кожей проблемы, иди к дерматологу.

#составкосметики #уходзакожей #чувствительнаякожа #разборсостава #косметика #бьюти
```
