# 18-superfud — Внук назвал это суперфудом

Рубрика: Пасека.

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (баба Зоя) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `baba-zoya.jpg`.

```
Photorealistic portrait of a 74-year-old Russian village grandmother, round kind face, deep laugh lines around light-blue eyes, rosy cheeks, gentle closed-mouth smile, grey hair almost fully covered by a red headscarf with small white polka dots tied at the back, burgundy hand-knitted cardigan over a blue floral cotton dress, white apron with red embroidered hem, standing in a rustic wooden kitchen with a whitewashed Russian stove, checkered oilcloth on the table, geranium on the window sill, warm morning window light, shot on 35mm, shallow depth of field, natural skin texture, documentary style
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
Extreme close-up of honeycomb cells packed with multicoloured bee bread granules, yellow, orange and brown. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
The grandmother at a blue wooden beehive in a flowering meadow holding a honeycomb frame, wearing her headscarf. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
The grandmother and her teenage grandson at a wooden table outside the house, a small bowl of bee bread granules between them. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
Close-up of the grandmother holding half a teaspoon of bee bread granules. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
Slow sideways camera pan across the colourful cells. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She lifts the frame and looks at it, a few bees fly around calmly. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
The boy looks at the granules with suspicion, she laughs and pushes the bowl towards him. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She shows the spoon to the camera, then puts the granules in her mouth. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Внук приехал, говорит: бабуль, это ж суперфуд, в Москве втридорога продают. А мы это семьдесят лет едим. Перга — пыльца, которую пчёлки в сотах сами законсервировали. Кисленькая, как хлебушек. Утром половинку чайной ложки — и хватит. Если на мёд аллергия — не трогай. Про пасеку — в моей книжке. Напиши в комментариях «книга» — пришлю.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/18-superfud/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Внук приехал из Москвы и говорит: бабуль, это же суперфуд, у нас за баночку втридорога берут. А мы с дедом Колей её семьдесят лет едим и слова такого не знали 🐝

Перга — это пыльца, которую пчёлы сложили в соты и сами же законсервировали мёдом. Пасечники её берегут для себя, на продажу идёт мало.

Какая на вкус: кисленькая, чуть сладкая, похожа на ржаной хлебушек. Держишь во рту, пока не растает.

Как ем я:
— утром натощак, половинку чайной ложки;
— не запиваю, не глотаю сразу — рассасываю;
— больше не надо, это не варенье.

Как выбрать: гранулы плотные, шестигранные, разного цвета — от жёлтого до коричневого. Если слиплись в ком и пахнут кисло-плесенью — не бери.

Сохрани, чтобы в следующий раз знать, что это за «суперфуд». Пробовал пергу? Напиши, на что похожа 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Нельзя при аллергии на мёд и продукты пчеловодства, детям — только после врача.
Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#перга #пасека #мёд #пчеловодство #суперфуд #бабушкинырецепты #деревня #продуктыпчеловодства #бабазоя
```
