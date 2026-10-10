# 19-myod-kipyatok — Мёд в кипяток — зря

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
Close-up of a wooden honey dipper with thick golden honey slowly dripping into a small bowl. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
The grandmother at the kitchen table pouring tea from an enamel kettle into a glass in a metal glass holder. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
The grandmother stirring a spoon of honey into a glass of tea. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
Early morning, the grandmother by the window drinking a glass of warm water. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
Honey drips in a slow thick stream, catching the window light. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She pours the tea, stops and wags her finger at the camera with a smile. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She stirs gently and taps the spoon on the rim of the glass. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She drinks, lowers the glass and looks out of the window contentedly. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Мёд в горячий чай кладёшь? Зря. В кипятке он весь свой вкус и аромат теряет, одна сладость остаётся. Я делаю так: чай налила, подождала, пока пить можно, — и тогда ложку мёда. А утром — стакан тёплой воды с мёдом, с этого у меня день начинается. Детям до года мёд нельзя. Остальное — в книжке, ссылка в шапке профиля.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/19-myod-kipyatok/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Мёд в горячий чай кладёшь? Я тоже раньше клала, пока дед Коля, пасечник, не отругал: «Зоя, ты его варишь» 🍯

В кипятке мёд теряет свой вкус и запах — остаётся просто сладость, как от сахара. Мёд переводишь зря.

Как делаю теперь:
1. Наливаю чай и жду пару минут, пока его можно пить, не обжигаясь.
2. Тогда кладу ложку мёда и размешиваю.
3. Или ем мёд вприкуску, а чай пью отдельно — так вкус лучше всего слышно.

А утро начинаю со стакана тёплой воды с чайной ложкой мёда. Вода — как парное молоко, не горячее. Выпила, полчасика — и завтракать.

Как проверить мёд: хороший со временем густеет и засахаривается. Если год стоит жидкий — задумайся.

Сохрани и перешли тому, кто кладёт мёд в кипяток 😉 А ты как ешь мёд — в чай или вприкуску? 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Мёд нельзя детям до года и при аллергии.
Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#мёд #чай #пасека #полезныепривычки #утро #бабушкинысоветы #деревенскаяеда #пчеловодство #бабазоя
```
