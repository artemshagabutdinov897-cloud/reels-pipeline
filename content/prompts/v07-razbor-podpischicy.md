# v07-razbor-podpischicy — Разбираю крем подписчицы

Рубрика: Вопрос от подписчицы.

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (Вера) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `vera.jpg`.

```
Candid smartphone front-camera photo of a 27-year-old Russian woman with a friendly, slightly ironic expression: one eyebrow a little raised and a half-smile. Long dark chestnut hair loosely pinned up with a tortoiseshell claw clip, a few loose strands, warm brown eyes, light freckles across the nose, natural skin with visible texture and almost no makeup, small gold hoop earrings, oversized cream knit sweater. Sitting at a sunlit kitchen table by a window with green plants and a few plain unbranded skincare jars. Natural daylight, slight phone-camera grain, vertical 9:16. No text or logos.
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
She sits at the kitchen table looking at her smartphone screen with curiosity, a plain cream tube next to her. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
Close-up of her fingertip sliding down tiny blurred unreadable print on the back of a plain white tube. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
She holds the plain tube up to the camera and gives a thumbs up by the window. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
She points at the camera with a friendly grin, sitting at the kitchen table. Keep exactly the same young woman: same face and freckles, dark chestnut hair in a tortoiseshell claw clip, small gold hoop earrings, oversized cream knit sweater. Photorealistic candid smartphone footage, natural daylight, cozy apartment, vertical 9:16. Product packaging plain and unbranded. No text, letters, logos or brand names anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
She reads a message on the phone, raises her eyebrows and smiles. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
Her finger moves down the list line by line and pauses in the middle. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She shows a thumbs up and nods approvingly. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She points at the camera and winks. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Sulafat**. Если его нет — любой похожий:

```
Молодая девушка 27 лет, живой тёплый голос с улыбкой и лёгкой иронией, говорит как подруге, не спеша, но бодро.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Мне прислали крем: «Это нормальный состав или меня развели?» Окей, проверяем. Первые пять строк — вода, глицерин, масло ши, эмульгатор, пантенол. Это основа, и она хорошая. Ниацинамид в середине — отлично. Отдушка в конце — если кожа спокойная, не страшно. Вердикт: не развели. Хочешь, разберу твой? Напиши «СОСТАВ».
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/v07-razbor-podpischicy/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Подписчица прислала крем: «Нормальный состав или меня развели?» Разбираю 🔍

Первые пять строк — основа крема:
вода, глицерин, масло ши, эмульгатор, пантенол. Увлажнение и питание — хорошая база.

В середине — ниацинамид. Отлично, это рабочий компонент, и стоит он не в самом хвосте.

В конце — отдушка. Если кожа спокойная — не страшно. Если реактивная — я бы искала без неё.

Вердикт: не развели 👌

Хочешь, разберу твой? Напиши «СОСТАВ» в комментариях — пришлю в директ, как прислать фото. Самые интересные разберу в роликах 💬

Я ИИ-персонаж: читаю составы без рекламной шелухи. Я не врач и не косметолог.

#разборсостава #составкосметики #уходзакожей #ниацинамид #косметика #бьюти
```
