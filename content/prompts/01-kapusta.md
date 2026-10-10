# 01-kapusta — Квашеная капуста без уксуса

Рубрика: Живые заготовки. Надпись-крючок (её добавлю сам при монтаже): «Капуста, после которой живот спасибо скажет»

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (баба Зоя) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `baba-zoya.jpg`.

```
Photorealistic portrait of a 74-year-old Russian village grandmother, round kind face, deep laugh lines around light-blue eyes, rosy cheeks, gentle closed-mouth smile, grey hair almost fully covered by a red headscarf with small white polka dots tied at the back, burgundy hand-knitted cardigan over a blue floral cotton dress, white apron with red embroidered hem, standing in a rustic wooden kitchen with a whitewashed Russian stove, checkered oilcloth on the table, geranium on the window sill, warm morning window light, shot on 35mm, shallow depth of field, natural skin texture, documentary style
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
The grandmother at the wooden kitchen table shredding a large head of white cabbage with a big knife, pile of shredded cabbage in an enamel basin. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
Close-up of the grandmother's hands kneading shredded cabbage with grated carrot in an enamel basin. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
The grandmother pressing cabbage into a three-litre glass jar with her fist, brine visible on top. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
The grandmother at the windowsill with geraniums pushing a long wooden stick down into a three-litre jar of shredded cabbage. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 5** → `scene_5.png`

```
The grandmother at the table with a small bowl of sauerkraut and a slice of rye bread, smiling at the camera. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
She shreds cabbage with steady strokes, looks up at the camera and smiles. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
Hands squeeze and knead the cabbage, juice appears, slow push-in. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She presses the cabbage down, brine rises, she nods satisfied. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She pokes the cabbage with the stick a couple of times and pulls it out, ordinary movement, camera almost still. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 5**: кадр `scene_5.png` → `scene_5.mp4`

```
She takes a forkful, chews, gives a thumbs up. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Доча, магазинную капусту с уксусом выкинь. Живая капустка — только соль да время. Три кило капусты, морковка, две столовые ложки соли без горки. Мни руками, пока сок не пустит. Утрамбуй в банку, чтоб сок сверху был. Три дня в тепле, каждый день протыкай палкой, газ выпускай. Потом в холод. Ешь понемножку к обеду — и тяжести как не бывало. Ещё сто рецептов в моей книжке, ссылка в шапке профиля.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_5.mp4` и `voice.mp3` в папку `inbox/01-kapusta/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Капуста с уксусом из магазина и живая квашеная — это две разные еды. Вторую моя мать делала каждую осень, и я делаю 🥬

Что нужно на трёхлитровую банку:
— 3 кг белокочанной капусты
— 1 крупная морковь
— 2 столовые ложки соли без горки (простая, не йодированная)

Как делаю:
1. Капусту тонко шинкую, морковь тру на крупной тёрке.
2. Солю и мну руками, пока не пустит сок. Рук не жалей, минут пять.
3. Плотно утрамбовываю в банку кулаком, чтобы сок был сверху.
4. Три дня держу в тепле. Каждый день протыкаю до дна деревянной палочкой, чтобы вышел газ, иначе будет горчить.
5. Потом крышку — и в холод. Через неделю самый вкус.

Ем понемножку к обеду, пару ложек. Просто так или с чёрным хлебом.

Сохрани, чтобы в сезон не искать. А ты квасишь с морковкой или без? Напиши 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#квашенаякапуста #заготовки #деревенскаяеда #бабушкинырецепты #рецептыбабушки #капуста #домашниезаготовки #простыерецепты #бабазоя
```
