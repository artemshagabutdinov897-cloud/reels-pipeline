# 17-posle-zastolya — После застолья

Рубрика: Каши и взвары.

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (баба Зоя) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `baba-zoya.jpg`.

```
Photorealistic portrait of a 74-year-old Russian village grandmother, round kind face, deep laugh lines around light-blue eyes, rosy cheeks, gentle closed-mouth smile, grey hair almost fully covered by a red headscarf with small white polka dots tied at the back, burgundy hand-knitted cardigan over a blue floral cotton dress, white apron with red embroidered hem, standing in a rustic wooden kitchen with a whitewashed Russian stove, checkered oilcloth on the table, geranium on the window sill, warm morning window light, shot on 35mm, shallow depth of field, natural skin texture, documentary style
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
Close-up: boiling water poured from an enamel kettle over dried apricots, prunes and dried apple slices in an enamel pot. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
The grandmother wrapping the enamel pot in a thick knitted blanket on the warm stove bench. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
Morning light, the grandmother ladling amber dried-fruit drink from the pot into a glass mug. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
The grandmother by the window with geraniums sipping the warm drink from the glass mug. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
Water pours in, the dried fruit shifts and floats up. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She tucks the blanket around the pot and pats it twice. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She ladles slowly, then lifts the mug towards the camera. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She sips, closes her eyes for a second and smiles. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Вчера все объелись? Знаю. Я на следующий день плиту не включаю. Вечером горсть сухофруктов — курага, чернослив, яблочки — кипятком в кастрюлю, полотенцем укутала и спать. Утром взвар тёплый, сладкий без сахару. Стаканчик натощак — и живот как новый. Вот так-то. Ещё рецепты — в моей книжке, ссылка в шапке профиля.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/17-posle-zastolya/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
После праздников у меня правило: на следующий день плиту не включаю. Вечером запариваю взвар — и утром живот сам говорит спасибо 🍑

Взвар — это не компот. Компот варят, а взвар запаривают, поэтому вкус мягче и глубже.

Что нужно на двухлитровую кастрюлю:
— горсть кураги
— горсть чернослива
— горсть сушёных яблок
— немного изюма
— ложка мёда (по желанию)

Как делаю:
1. Сухофрукты хорошо промываю тёплой водой.
2. Складываю в кастрюлю и заливаю крутым кипятком.
3. Крышка, сверху полотенце или старый плед — и до утра. Можно в термос.
4. Утром процеживаю. Мёд кладу, только когда взвар остынет до тёплого.

Пью стаканчик натощак, остальное — в течение дня вместо чая. Сухофрукты потом съедаю, не выбрасываю.

Сохрани до следующего праздника — пригодится. У тебя что после застолья спасает? Делись 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Мёд нельзя детям до года и при аллергии.
Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#взвар #сухофрукты #последпраздников #бабушкинырецепты #деревенскаяеда #чернослив #рецептыбабушки #простыерецепты #бабазоя
```
