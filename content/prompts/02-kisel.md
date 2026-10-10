# 02-kisel — Овсяный кисель

Рубрика: Каши и взвары. Надпись-крючок (её добавлю сам при монтаже): «Кисель, который варили в каждой деревне»

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (баба Зоя) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `baba-zoya.jpg`.

```
Photorealistic portrait of a 74-year-old Russian village grandmother, round kind face, deep laugh lines around light-blue eyes, rosy cheeks, gentle closed-mouth smile, grey hair almost fully covered by a red headscarf with small white polka dots tied at the back, burgundy hand-knitted cardigan over a blue floral cotton dress, white apron with red embroidered hem, standing in a rustic wooden kitchen with a whitewashed Russian stove, checkered oilcloth on the table, geranium on the window sill, warm morning window light, shot on 35mm, shallow depth of field, natural skin texture, documentary style
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
The grandmother pouring rolled oats from a paper bag into a clay jug on the kitchen table. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
Close-up of a crust of rye bread floating on oats in water in a clay jug. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
The grandmother straining the oat liquid through gauze into an enamel pot. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
Enamel pot on the Russian stove, thick pale oat kissel being stirred with a wooden spoon. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 5** → `scene_5.png`

```
The grandmother with a cup of warm oat kissel with a melting pat of butter, smiling. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
Oats pour into the jug, she adds water from a kettle. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She places the bread crust on top and covers the jug with a linen cloth. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
Milky liquid streams through gauze, she squeezes the gauze. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
Spoon stirs thick kissel, steam rises. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 5**: кадр `scene_5.png` → `scene_5.mp4`

```
She blows on the cup, sips, and nods warmly. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Милок, это не тот кисель из пакета. Овсяный, настоящий. Стакан овсянки залей тремя стаканами тёплой воды, корочку ржаного хлеба сверху — и на ночь. Утром процеди, отожми. Вари на тихом огне, мешай, пока не загустеет. Соли щепотку. Тёплый, с ложкой масла — живот обволакивает, сытно и легко. Ещё сто рецептов в моей книжке. Напиши в комментариях «книга» — пришлю.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_5.mp4` и `voice.mp3` в папку `inbox/02-kisel/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Не тот кисель из пакета, что в детском саду давали. Этот варили в каждой деревне из того, что было в доме: овсянка, вода и корка хлеба 🥣

Что нужно:
— 1 стакан овсяных хлопьев (не быстрого приготовления)
— 3 стакана тёплой кипячёной воды
— корочка ржаного хлеба
— щепотка соли, кусочек сливочного масла

Как делаю:
1. Вечером заливаю хлопья тёплой водой, сверху корочку хлеба, накрываю полотенцем — и на ночь.
2. Утром процеживаю через марлю и хорошо отжимаю. Гущу не выбрасываю — в оладьи.
3. Варю на тихом огне и всё время мешаю, пока не загустеет, как сметана. Минут 5–7.
4. Соль по вкусу, ложку масла сверху.

Пью тёплым на завтрак. Сытно, дёшево, и до обеда про еду не вспоминаешь.

Сохрани себе на утро. А ты такой кисель пробовал или только из пакета? 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#овсяныйкисель #кисель #бабушкинырецепты #деревенскаяеда #завтрак #овсянка #рецептыбабушки #простыерецепты #бабазоя
```
