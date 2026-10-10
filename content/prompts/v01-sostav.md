# v01-sostav — Крем «с гиалуронкой» — а где она?

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
Close-up of her hands holding a white unbranded cream tube in front of her, turning it to the back side with tiny unreadable blurred print. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
She sits at a wooden table with unbranded skincare jars, wearing glasses, reading the back of the tube. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
Extreme close-up of her fingertip sliding down the tiny blurred unreadable print on the back of a white tube. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
She puts the tube on the table and looks at the camera, relaxed, by the window with plants. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
She flips the tube over and brings it closer to her eyes. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She reads, then raises one eyebrow and looks at the camera with a knowing half-smile. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
Her finger slowly slides down the list and stops near the bottom. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She takes off her glasses, smiles warmly and gives a small nod to the camera. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Sulafat**. Если его нет — любой похожий:

```
Молодая девушка 27 лет, живой тёплый голос с улыбкой и лёгкой иронией, говорит как подруге, не спеша, но бодро.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Покупаешь крем «с гиалуронкой»? Переверни и прочитай состав. Ингредиенты пишут по убыванию: чего больше — то в начале. Если гиалуроновая кислота в самом конце, после отдушки, — её там капля, а платишь ты в основном за воду. Смотри на первые пять строчек — это и есть твой крем. Какой разобрать следующим? Пиши в комментариях.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/v01-sostav/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Купила крем, потому что на банке крупно «с гиалуроновой кислотой»? Переверни 👀

Состав на упаковке пишут по убыванию: чего в креме больше — то стоит в начале списка. А всё, чего меньше одного процента, можно перечислять в конце в любом порядке.

Как читаю я:
1. Смотрю первые пять строчек — обычно это и есть основа крема, большая часть того, что ты наносишь на лицо.
2. Ищу «звезду» с этикетки. Если она стоит после отдушки (Parfum / Fragrance) — её там совсем немного.
3. Сравниваю с ценой. Платить за гиалуронку в хвосте списка как за серьёзный актив — странно.

Это не значит, что крем плохой. Просто покупай его за то, что в нём правда есть, а не за надпись на банке.

Какой крем или сыворотку разобрать следующим? Пиши название в комментариях 👇

Я ИИ-персонаж: разбираю составы и уход без рекламной шелухи. Я не врач и не косметолог — если с кожей проблемы, иди к дерматологу.

#составкосметики #уходзакожей #гиалуроноваякислота #косметика #разборсостава #бьюти #уход
```
