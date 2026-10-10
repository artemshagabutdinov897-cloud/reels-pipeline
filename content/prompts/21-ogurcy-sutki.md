# 21-ogurcy-sutki — Огурцы за сутки — и без уксуса

Рубрика: Живые заготовки.

## Шаг 0. Эталонное фото (один раз на весь проект)

Если эталон (баба Зоя) уже есть — пропустите. Иначе: **Nano Banana**, формат **9:16**, 3–4 варианта, выберите лучший и сохраните как `baba-zoya.jpg`.

```
Photorealistic portrait of a 74-year-old Russian village grandmother, round kind face, deep laugh lines around light-blue eyes, rosy cheeks, gentle closed-mouth smile, grey hair almost fully covered by a red headscarf with small white polka dots tied at the back, burgundy hand-knitted cardigan over a blue floral cotton dress, white apron with red embroidered hem, standing in a rustic wooden kitchen with a whitewashed Russian stove, checkered oilcloth on the table, geranium on the window sill, warm morning window light, shot on 35mm, shallow depth of field, natural skin texture, documentary style
```

## Шаг 1. Кадры сцен — Nano Banana

Для каждой сцены: загрузите **эталонное фото** персонажа, вставьте промпт, формат **9:16**. Сохраните как `scene_N.png`.

**Сцена 1** → `scene_1.png`

```
Close-up of a crisp lightly salted cucumber being snapped in half above an open glass jar, drops of brine. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 2** → `scene_2.png`

```
The grandmother's hands trimming the ends of small green cucumbers on a wooden cutting board. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 3** → `scene_3.png`

```
A glass jar packed with cucumbers, dill umbrellas, garlic and horseradish leaves, the grandmother pouring hot brine from an enamel ladle. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

**Сцена 4** → `scene_4.png`

```
The grandmother at the kitchen table holding a lightly salted cucumber. Keep exactly the same elderly woman: same face, red headscarf with small white polka dots, burgundy knitted cardigan, blue floral dress, white apron with red embroidered hem. Photorealistic, warm natural light, rustic Russian village setting, vertical 9:16. No text, letters or labels anywhere in the picture.
```

## Шаг 2. Видео — Seedance

Режим **из изображения (image-to-video)**, **5 секунд**, **9:16**. Загрузите кадр сцены, вставьте промпт. Сохраните как `scene_N.mp4`.

**Сцена 1**: кадр `scene_1.png` → `scene_1.mp4`

```
The cucumber snaps in half with a crunch, brine drips down. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 2**: кадр `scene_2.png` → `scene_2.mp4`

```
The knife trims the ends quickly, she drops the cucumbers into a glass jar. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 3**: кадр `scene_3.png` → `scene_3.mp4`

```
The brine fills the jar, dill leaves shift and float up. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

**Сцена 4**: кадр `scene_4.png` → `scene_4.mp4`

```
She bites it with a loud crunch, chews and nods approvingly at the camera. Amateur vertical smartphone video filmed by a grandchild: slight handheld shake, natural daylight, ordinary everyday pace, subtle realistic motion only. No bubbles, no gas, no sparkles, no magic effects, no exaggerated steam, no slow motion, no text, no subtitles, no letters or labels on jars, packaging or any objects.
```

## Шаг 3. Озвучка

Озвучка в Братухе: Gemini TTS, голос **Gacrux**. Если его нет — любой похожий:

```
Пожилая женщина из русской деревни, около 75 лет, тёплый голос с лёгкой хрипотцой, говорит спокойно, по-доброму, чуть с хитринкой.
```

Текст целиком, как есть (сохраните как `voice.mp3`):

```
Малосольные за сутки, и ни капли уксуса. Огурчикам кончики срежь — и в банку. Чеснок, укроп зонтиком, лист хрена, смородины. Литр воды, две ложки соли без горки — вскипяти и горячим залей. Сутки на столе — и хрустят так, что соседи слышат. Рецепт — в описании, а сто таких — в книжке.
```

## Шаг 4. Отдать мне на монтаж

Загрузите `scene_1.mp4`…`scene_4.mp4` и `voice.mp3` в папку `inbox/21-ogurcy-sutki/` на GitHub (ветка `main` → Add file → Upload files) и напишите мне «собери». Субтитры, крючок и музыку добавлю сам.

Не хватило бюджета на все сцены — ничего страшного, соберу из тех клипов, что есть.

## Подпись к посту

```
Малосольные огурчики за сутки — и ни капли уксуса. Хрустят так, что соседи через забор слышат 🥒

Уксус огурцу не нужен. Соль, укроп да время — вот и вся хитрость.

Что нужно на 3-литровую банку:
— огурцы мелкие, крепкие — сколько влезет (около 1,5–2 кг)
— 4–5 зубчиков чеснока
— 2–3 зонтика укропа
— лист хрена, 5–6 листьев смородины или вишни
— на литр воды 2 столовые ложки соли без горки (соль крупная, без йода)

Как делаю:
1. Огурцы замочи в холодной воде на пару часов — будут крепче.
2. Кончики срежь — так рассол быстрее зайдёт.
3. На дно — половину зелени и чеснок, огурцы стоймя, плотно, сверху остальную зелень.
4. Рассол вскипяти и горячим залей. Горячий — за сутки, холодный — за двое-трое.
5. Накрой крышкой неплотно и оставь на столе. Через сутки — в холодильник.

Совет: хочешь похрустеть уже к ужину — разрежь огурцы вдоль на четвертинки.

Сохрани, пока огурцы на грядке 😉 А вы с уксусом солите или без? 👇
📖 Напиши в комментариях «КНИГА» или просто ❤️ — пришлю тебе в директ бабушкины рецепты даром и ссылку на книжку.

Баба Зоя — собирательный образ, рецепты из деревенских тетрадей. Это еда, а не лечение.

#огурцы #малосольныеогурцы #заготовки #рецепт #безуксуса #деревенскаяеда #бабушкинрецепт #бабазоя
```
