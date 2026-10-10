# s02-pirog-na-tancah — Тетрадь деда Коли. Часть 2: Он украл мой пирог на танцах

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
A 1970s Soviet village club dance hall in the evening, young people dancing, a table with a round apple pie on a plate, young Zoya in a red polka-dot headscarf standing by the table. 1970s Soviet village, faded amateur color photograph look, warm washed-out colors, soft film grain, slightly blurred edges, natural light, vertical 9:16. Young Kolya: tall man in his twenties, dark wavy hair, short moustache, rolled-up sleeves of a checked shirt. Young Zoya: slim woman about twenty, long light-brown braid, red headscarf with small white polka dots. No text, letters or labels anywhere in the picture.
```

**Сцена 2** — флешбэк: **без** эталона, просто по тексту → `scene_2.png`

```
Young Kolya with his mouth full, holding a big piece of apple pie, grinning shyly at young Zoya in the village club. 1970s Soviet village, faded amateur color photograph look, warm washed-out colors, soft film grain, slightly blurred edges, natural light, vertical 9:16. Young Kolya: tall man in his twenties, dark wavy hair, short moustache, rolled-up sleeves of a checked shirt. Young Zoya: slim woman about twenty, long light-brown braid, red headscarf with small white polka dots. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
The grandmother in her kitchen taking a golden apple pie out of the oven, the old notebook lying open on the table. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
Close-up of the grandmother's fingers pulling a small folded yellowed piece of paper from between the notebook pages. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
Couples dance in the background, young Zoya turns away from the table to talk to a friend. Old 1970s amateur 8mm home movie footage: faded warm colors, film grain, gentle frame flicker, slightly uneven speed, soft focus. Subtle natural motion only. No text, no subtitles.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
He chews, grins and says something, she puts her hands on her hips and laughs. Old 1970s amateur 8mm home movie footage: faded warm colors, film grain, gentle frame flicker, slightly uneven speed, soft focus. Subtle natural motion only. No text, no subtitles.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
She sets the pie on the table and smiles, shaking her head at a memory. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She unfolds the paper slowly and her face becomes serious. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Семьдесят второй год, клуб, танцы. Я принесла пирог с антоновкой, на всех. Отвернулась — половины нет. Стоит парень, щёки набиты, и говорит: «Выйдешь за меня — буду каждый день такой есть». Сорок лет я рассказывала, что это он ко мне пристал. А в тетради Коля пишет: «Пирог я не крал. Мне его Зоина подружка отдала — чтоб я наконец подошёл». А между страницами — бумажка. Адрес. В соседней деревне.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/s02-pirog-na-tancah/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Тетрадь деда Коли. Часть 2 🥧

1972 год, танцы в клубе. Я принесла пирог с антоновкой — на всех. Отвернулась на минутку, а половины уже нет. Стоит парень, щёки набиты, и говорит: «Выйдешь за меня — буду каждый день такой есть».

Сорок лет я всем рассказывала, что это Коля ко мне пристал. А в тетради у него совсем другая история:
«Пирог я не крал. Мне его Галька, Зоина подружка, сама отдала — чтоб я наконец подошёл. Сам бы год не решился».

Галька, ну ты и хитрая! Пятьдесят лет молчала.

Тот самый пирог с антоновкой:
1. 3 яйца взбей с полстаканом сахара.
2. Стакан кефира, щепотка соли, пол-ложки соды.
3. Мука — примерно полтора стакана, до густой сметаны.
4. 3–4 антоновки дольками на дно формы, сверху тесто.
5. 180 градусов, 40 минут. Проверь лучинкой.

А между страницами лежала бумажка. Адрес. В соседней деревне. Коля туда никогда при мне не ездил.

Как вы со своими познакомились? Пишите, я всё читаю 👇

📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#тетрадьдедаколи #бабазоя #пирогсяблоками #антоновка #любовь #семидесятые #бабушкинырецепты #сериал
```
