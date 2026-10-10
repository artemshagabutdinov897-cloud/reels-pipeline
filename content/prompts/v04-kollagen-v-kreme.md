# v04-kollagen-v-kreme — Коллаген в креме — куда он девается

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
She holds a plain unbranded cream jar and reads the tiny blurred print on the back at the kitchen table. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
She spreads a little cream on the back of her hand in daylight by the window. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
She sits relaxed at the kitchen table with a cup of tea, looking at the camera and explaining something with her hands. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
She raises her eyebrows and points at the camera with a playful smile. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
She reads, then looks up at the camera with a skeptical half-smile. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She rubs the cream into her hand and looks at it, unimpressed. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She gestures with one hand as if showing something big, then something small. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She points at the camera and nods, as if saying "next time". Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Sulafat**. Если его нет — любой похожий:

```
Молодая девушка 27 лет, живой тёплый голос с улыбкой и лёгкой иронией, говорит как подруге, не спеша, но бодро.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Крем «с коллагеном» за три тысячи. Слушай, молекула коллагена огромная — в глубокие слои кожи она почти не проходит. В креме коллаген работает как увлажнитель на поверхности: приятно, но не больше. Так что платить за него как за чудо — странно. А вот с коллагеном, который пьют, всё сложнее — об этом в следующем ролике. Интересно? Пиши «КОЛЛАГЕН».
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/v04-kollagen-v-kreme/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Крем «с коллагеном» — за что платим? 🤔

Молекула коллагена очень большая. В глубокие слои кожи из крема она практически не проходит — это общее мнение дерматологов. На поверхности коллаген работает как увлажнитель: удерживает воду, кожа приятнее на ощупь.

Это неплохо! Но это умеют и глицерин, и гиалуронка — только дешевле.

Как смотрю я:
1. Где в составе Collagen — в начале или в хвосте списка?
2. Что стоит в первых пяти строчках — там и есть основа крема.
3. Сравниваю цену с таким же увлажняющим кремом без модного слова.

А с коллагеном, который пьют, история другая и сложнее. Разберу честно, с документами — в следующем ролике. Напиши «КОЛЛАГЕН», если интересно 👇

Я ИИ-персонаж: читаю составы без рекламной шелухи. Я не врач и не косметолог.

#коллаген #составкосметики #уходзакожей #разборсостава #косметика #бьюти
```
