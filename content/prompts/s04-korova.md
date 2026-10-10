# s04-korova — Тетрадь деда Коли. Часть 4: Он продал ульи, чтобы…

Рубрика: Сериал.

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (баба Зоя) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `baba-zoya.jpg`.

```
Photorealistic portrait of a 74-year-old Russian village grandmother, round kind face, deep laugh lines around light-blue eyes, rosy cheeks, gentle closed-mouth smile, grey hair almost fully covered by a red headscarf with small white polka dots tied at the back, burgundy hand-knitted cardigan over a blue floral cotton dress, white apron with red embroidered hem, standing in a rustic wooden kitchen with a whitewashed Russian stove, checkered oilcloth on the table, geranium on the window sill, warm morning window light, shot on 35mm, shallow depth of field, natural skin texture, documentary style
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** — флешбэк: **без** эталона, просто по тексту → `scene_1.png`

```
A snowy 1980 Soviet village street in winter, young Kolya in a sheepskin coat leading a brown cow by a rope towards a wooden house. 1970s Soviet village, faded amateur color photograph look, warm washed-out colors, soft film grain, slightly blurred edges, natural light, vertical 9:16. Young Kolya: tall man in his twenties, dark wavy hair, short moustache, rolled-up sleeves of a checked shirt. Young Zoya: slim woman about twenty, long light-brown braid, red headscarf with small white polka dots. No text, letters or labels anywhere in the picture.
```

**Сцена 2** — флешбэк: **без** эталона, просто по тексту → `scene_2.png`

```
Young Zoya in a winter shawl at the door of a wooden house holding a small child, looking surprised at a cow in the yard. 1970s Soviet village, faded amateur color photograph look, warm washed-out colors, soft film grain, slightly blurred edges, natural light, vertical 9:16. Young Kolya: tall man in his twenties, dark wavy hair, short moustache, rolled-up sleeves of a checked shirt. Young Zoya: slim woman about twenty, long light-brown braid, red headscarf with small white polka dots. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
The grandmother in her kitchen pouring warm soured milk from a pot into a cheesecloth hanging over a bowl. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
The grandmother sitting at the table holding the old notebook to her chest, eyes wet, a bowl of fresh cottage cheese in front of her. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
He walks through the snow pulling the cow, breath steaming, and waves towards the house. Old 1970s amateur 8mm home movie footage: faded warm colors, film grain, gentle frame flicker, slightly uneven speed, soft focus. Subtle natural motion only. No text, no subtitles.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
She steps onto the porch, holds the child closer and laughs in disbelief. Old 1970s amateur 8mm home movie footage: faded warm colors, film grain, gentle frame flicker, slightly uneven speed, soft focus. Subtle natural motion only. No text, no subtitles.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
Whey drips from the cloth, she ties the cloth into a bundle. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She presses the notebook to her chest, closes her eyes and nods slowly. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Восьмидесятый год, голодная зима, дочка маленькая. И вдруг Коля приводит корову. Говорит: в карты выиграл. Я сорок лет верила. Ругала его ещё за эти карты. А он ульи продал. Последние два. Чтобы у дочки молоко было. И ни слова. Творог я с той коровы делала — до сих пор так делаю. А на последней странице… теперь я знаю, чей это почерк.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/s04-korova/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Тетрадь деда Коли. Часть 4 🐄

Зима 1980-го. Дочке два года, в магазине пусто, молока нет. И вдруг Коля приводит во двор корову. Бурёнку. Говорит: «В карты у мужиков выиграл».

Я его тогда так ругала за эти карты! Сорок лет потом вспоминала: «Картёжник ты мой».

А в тетради:
«Продал Ильичу два улья, последние. Купил корову. Зое скажу — выиграл. Она ульи любит больше меня, не простит».

Не в карты он выиграл. Он пасеку свою отдал, чтоб у дочки молоко было. И ни разу не проговорился.

Коля, ну как же так. Я бы простила. Я бы гордилась.

С той коровы я творог научилась делать. Делаю так до сих пор:
1. 2 литра деревенского молока оставь в тепле на сутки — пусть скиснет.
2. Кастрюлю с простоквашей поставь в большую кастрюлю с горячей водой (водяная баня), грей 20–30 минут, не кипяти.
3. Как сыворотка отойдёт — откинь на марлю.
4. Подвесь на 2–3 часа, пусть стечёт.
Сыворотку не выливай — на ней блины отличные.

А на последней странице… теперь я знаю, чей это почерк. Завтра расскажу.

Какой поступок ваших родных вы узнали только спустя годы? 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#тетрадьдедаколи #бабазоя #творог #домашнийтворог #любовь #семья #история #сериал
```
