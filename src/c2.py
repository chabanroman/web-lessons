from helpers import *
from svgs import *

# ───────────── БЛОК 2: CSS ─────────────
lesson(6, "css", "Знайомство з CSS: селектори й кольори",
 "Вдягаємо сторінку: підключаємо стилі, вчимося «цілитися» в елементи й працювати з кольорами.",
 ["підключати окремий файл style.css", "використовувати селектори: тег, .клас, #id", "задавати кольори в hex, rgb, hsl", "розуміти каскад: яке правило перемагає"],
 [
  H("Анатомія CSS-правила"),
  FIG(RULE, "Кожне правило: КОГО (селектор) → ЩО (властивість) → ЯК (значення)."),
  H("Три способи підключити CSS"),
  CODE("html", r'''
<!-- 1. Окремий файл — ✅ найкраще, так роблять професіонали -->
<head>
  <link rel="stylesheet" href="css/style.css">
</head>

<!-- 2. Всередині сторінки — ок для експериментів -->
<style>
  h1 { color: tomato; }
</style>

<!-- 3. Прямо в тезі — ❌ уникай, важко підтримувати -->
<h1 style="color: tomato;">Заголовок</h1>'''),
  H("Селектори: як «прицілитися»"),
  CODE("html", r'''
<style>
  /* за тегом — усі абзаци */
  p { color: #444; }

  /* за класом — усі елементи з class="card" */
  .card { background: #fff3cc; padding: 10px; }

  /* за id — один унікальний елемент */
  #main-title { color: #f0622e; }

  /* нащадок — посилання всередині nav */
  nav a { color: #2f6feb; }

  /* групування — кілька селекторів одразу */
  h1, h2 { font-family: sans-serif; }
</style>

<h1 id="main-title">Моя полиця</h1>
<nav><a href="#">Головна</a> <a href="#">Про мене</a></nav>
<p>Звичайний абзац.</p>
<p class="card">Абзац-картка</p>
<div class="card">І div теж може бути карткою</div>''', run=True),
  TIP("Клас можна давати скільки завгодно елементам, а id — лише одному. Можна кілька класів одразу: <code>class=\"card big\"</code>."),
  H("Кольори"),
  TABLE(["Формат", "Приклад", "Коли зручно"], [
    ["Назва", "<code>tomato</code>, <code>white</code>", "Швидкі експерименти"],
    ["HEX", "<code>#F0622E</code>", "Найпоширеніший, копіюєш з дизайну"],
    ["RGB", "<code>rgb(240, 98, 46)</code>", "Червоний, зелений, синій від 0 до 255"],
    ["HSL", "<code>hsl(16, 87%, 56%)</code>", "Відтінок, насиченість, світлість: легко робити світліше/темніше"]]),
  TRY(r'''<style>
  body { background: #fbf8f3; }
  h1 { color: hsl(16, 87%, 56%); }
  .box { background: rgb(47, 111, 235); color: white; padding: 20px; }
</style>
<h1>Змінюй кольори!</h1>
<div class="box">Спробуй hsl(200, 80%, 40%)</div>'''),
  H("Каскад: хто перемагає?"),
  P("Якщо два правила сперечаються, перемагає: <b>1)</b> точніший селектор (#id &gt; .клас &gt; тег); <b>2)</b> якщо однакові — те, що написано <b>нижче</b>. Звідси й назва: Cascading Style Sheets — «каскадні таблиці стилів»."),
  TIP("Палітри для натхнення: <a href='https://coolors.co' target='_blank'>coolors.co</a>. Натискай пробіл, поки не знайдеш свою."),
 ],
 "Створи <code>css/style.css</code> і підключи до <code>index.html</code>. Обери палітру з 3–4 кольорів (coolors.co). Розфарбуй фон сторінки, шапку, футер, заголовки. Дай статтям класу <code>card</code>.",
 ["F12 → Elements → клікни по h1 → справа у Styles видно твої правила і файл <code>style.css</code>", "Якщо стилі не застосувались — F12 → Network: чи є style.css (а не 404)?", "Спробуй змінити колір прямо в Styles, а потім перенеси вдале значення у файл"],
 [("Базовий", "Розфарбуй сторінку «Про мене»: окремий style.css, мінімум 6 правил, усі три типи селекторів."),
  ("Середній", "Зроби дві версії одного стилю: світлу й темну (два CSS-файли). Перемикай, міняючи href у link."),
  ("Зірочка ⭐", "Пограй у <a href='https://flukeout.github.io' target='_blank'>CSS Diner</a> і пройди мінімум 15 рівнів селекторів.")],
 [("Як вибрати всі елементи з class=\"card\"?", ["card", "#card", ".card", "*card"], 2, "Крапка = клас."),
  ("Що переможе: #title { color: red } чи h1 { color: blue }?", ["blue, бо нижче", "red, бо #id точніший", "Змішається у фіолетовий", "Жоден"], 1, "Специфічність: id > клас > тег."),
  ("Найкращий спосіб підключити CSS?", ["Атрибут style", "Окремий файл через &lt;link&gt;", "Тег &lt;css&gt;", "Не підключати"], 1, "Окремий файл легко підтримувати.")])

lesson(7, "css", "Текст і шрифти",
 "Типографіка — 90% дизайну. Підбираємо шрифти з кирилицею, розміри, інтервали й стилі посилань.",
 ["підключати Google Fonts з підтримкою кирилиці", "задавати розміри в px і rem", "налаштовувати міжрядковий інтервал і вирівнювання", "стилізувати посилання та стан :hover"],
 [
  H("Основні властивості тексту"),
  CODE("html", r'''
<style>
  body {
    font-family: Arial, sans-serif;   /* шрифт + запасний */
    font-size: 18px;
    line-height: 1.6;                 /* міжрядковий інтервал */
    color: #1d1b26;
  }
  h1 {
    font-size: 2.5rem;                /* 2.5 × базовий розмір */
    font-weight: 800;                 /* товщина: 100..900 */
    letter-spacing: -1px;
    text-align: center;
  }
  .muted { color: #6b6878; font-style: italic; }
  .caps  { text-transform: uppercase; letter-spacing: 3px; font-size: 12px; }
</style>
<p class="caps">Колекція 2026</p>
<h1>Моя полиця</h1>
<p>Звичайний текст сторінки читається легко, бо має інтервал 1.6.</p>
<p class="muted">Другорядний текст — сірий і курсивний.</p>''', run=True),
  H("Google Fonts: красиві шрифти безкоштовно"),
  STEPS(["Відкрий <a href='https://fonts.google.com' target='_blank'>fonts.google.com</a>.",
         "Увімкни фільтр <b>Language → Cyrillic</b>. Без цього українські літери будуть стандартним шрифтом!",
         "Обери шрифт (наприклад, <i>Montserrat</i>, <i>Unbounded</i>, <i>Nunito</i>, <i>Rubik</i>) → <b>Get font → Get embed code</b>.",
         "Скопіюй <code>&lt;link&gt;</code> у <code>&lt;head&gt;</code>, а <code>font-family</code> — у CSS."]),
  CODE("html", r'''
<head>
  <link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@700&family=Nunito:wght@400;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/style.css">
</head>''', title="index.html"),
  CODE("css", r'''
body   { font-family: 'Nunito', sans-serif; }
h1, h2 { font-family: 'Unbounded', sans-serif; }''', title="css/style.css"),
  TIP("Правило двох шрифтів: один для заголовків (з характером), другий для тексту (простий і читабельний). Більше — це вже хаос."),
  H("Одиниці виміру"),
  TABLE(["Одиниця", "Що це"], [
    ["<code>px</code>", "Пікселі: точно й просто"],
    ["<code>rem</code>", "Відносно базового шрифту (зазвичай 1rem = 16px). Масштабується, якщо людина збільшила шрифт у налаштуваннях"],
    ["<code>%</code>", "Відсоток від батьківського елемента"],
    ["<code>vw / vh</code>", "Відсоток ширини / висоти екрана"]]),
  H("Посилання та :hover"),
  TRY(r'''<style>
  a { color: #2f6feb; text-decoration: none; font-weight: bold; }
  a:hover { color: #f0622e; text-decoration: underline; }
  a:visited { color: #8b5cf6; }
</style>
<p>Наведи мишку: <a href="#">це посилання</a> змінить колір.</p>''', "Стани посилань"),
  P("<code>:hover</code> — це <b>псевдоклас</b>, стан «на мене навели мишку». Ще є <code>:focus</code> (поле, в якому курсор), <code>:active</code> (натискання), <code>:first-child</code> і багато інших."),
 ],
 "Підключи 2 шрифти з кирилицею. Налаштуй <code>body</code> (шрифт, розмір, line-height, колір), заголовки і стилі посилань у меню з <code>:hover</code>.",
 ["F12 → Elements → вкладка <b>Computed</b> → <code>font-family</code>: видно, який шрифт реально застосувався", "Перевір, що й літери «ї», «є», «ґ» гарні (не стандартний шрифт)", "Ctrl + «+» у браузері: текст масштабується?"],
 [("Базовий", "Оформи текст сторінки «Про мене»: 2 шрифти з Google Fonts, різні розміри заголовків, стилізовані посилання."),
  ("Середній", "Зроби «постер» події (шкільна дискотека/хакатон) лише текстом і CSS: великий заголовок, дата, деталі."),
  ("Зірочка ⭐", "Дізнайся про <code>text-shadow</code> і зроби заголовок з «неоновим» світінням.")],
 [("Що треба увімкнути на Google Fonts для українських літер?", ["Bold", "Cyrillic", "Latin", "Serif"], 1, "Фільтр Cyrillic."),
  ("Що робить line-height: 1.6?", ["Товщина шрифту", "Міжрядковий інтервал у 1.6 раза більший за розмір шрифту", "Висота сторінки", "Відступ зліва"], 1, "Більший інтервал — легше читати."),
  ("Що таке :hover?", ["Новий тег", "Стан елемента, коли на нього навели мишку", "Анімація", "Колір"], 1, "Псевдоклас стану.")])

lesson(8, "css", "Блокова модель: кожен елемент — коробка",
 "Відступи, рамки, розміри. Зрозумієш блокову модель, і верстка перестане бути магією.",
 ["пояснити content, padding, border, margin", "розрізняти блочні й рядкові елементи", "використовувати box-sizing: border-box", "робити картки з закругленнями й тінями"],
 [
  H("Кожен елемент — це коробка"),
  FIG(BOX, "Ззовні всередину: margin → border → padding → content."),
  CODE("html", r'''
<style>
  .box {
    width: 250px;
    padding: 20px;               /* всередині, від рамки до тексту */
    border: 4px solid #1d1b26;   /* товщина, стиль, колір */
    margin: 30px;                /* ззовні, від сусідів */
    background: #dce8ff;
  }
</style>
<div class="box">Я коробка. Відкрий F12 і наведи на мене: побачиш кольорові відступи!</div>
<div class="box">Я сусідня коробка</div>''', run=True),
  P("Відступи можна задати по сторонах: <code>padding: 10px 20px</code> (верх-низ, ліво-право) або <code>margin-top: 40px</code>. Центрувати блок: <code>margin: 0 auto</code>."),
  H("Блочні й рядкові"),
  TABLE(["Блочні (block)", "Рядкові (inline)"], [
    ["div, p, h1–h6, section, ul, form", "a, span, strong, img, input"],
    ["Займають усю ширину, нові з нового рядка", "Стоять у рядку, як слова"],
    ["Можна задати width / height", "width / height не працюють (крім img)"]]),
  P("Поміняти поведінку можна властивістю <code>display: block | inline | inline-block | none</code>. <code>none</code> взагалі ховає елемент."),
  H("box-sizing: секретна суперсила"),
  WARN("За замовчуванням <code>width: 250px</code> + <code>padding: 20px</code> + <code>border: 4px</code> = <b>298px</b>! Щоб ширина була рівно тією, що написав, додай на початок кожного CSS-файлу:"),
  CODE("css", r'''
* { box-sizing: border-box; }   /* тепер width включає padding і border */
body { margin: 0; }              /* прибираємо стандартний відступ браузера */'''),
  H("Робимо гарну картку"),
  TRY(r'''<style>
  * { box-sizing: border-box; }
  body { background: #fbf8f3; font-family: sans-serif; padding: 20px; }
  .card {
    max-width: 280px;
    padding: 16px;
    background: white;
    border-radius: 16px;
    box-shadow: 0 8px 24px rgba(0,0,0,.12);
  }
  .card img { width: 100%; border-radius: 10px; display: block; background: #ddd; height: 140px; }
  .card h3 { margin: 12px 0 4px; }
  .card p { margin: 0; color: #6b6878; }
</style>
<article class="card">
  <img alt="обкладинка">
  <h3>Stardew Valley</h3>
  <p>Ферма · ★★★★★</p>
</article>''', "Картка для полиці"),
  TIP("Тіні генеруй тут: <a href='https://shadows.brumm.af' target='_blank'>shadows.brumm.af</a>. М'які тіні з великим розмиттям виглядають сучасно."),
 ],
 "Додай <code>* { box-sizing: border-box }</code>. Перетвори кожен <code>&lt;article&gt;</code> зі своєю річчю на картку: картинка, назва, автор, оцінка. Відступи, закруглення, тінь.",
 ["F12 → Elements → вкладка <b>Computed</b>: внизу схема блокової моделі з цифрами", "Наведи на елемент в Elements: margin підсвічується помаранчевим, padding — зеленим", "Зніми галочку біля властивості в Styles — побачиш, що вона робить"],
 [("Базовий", "Зроби 3 картки «Мої друзі/улюблені персонажі» з фото, ім'ям і описом."),
  ("Середній", "Скопіюй вигляд картки товару з будь-якого інтернет-магазину (тільки HTML + CSS)."),
  ("Зірочка ⭐", "Пройди гру <a href='https://cssbattle.dev' target='_blank'>CSSBattle</a>, перші 3 рівні.")],
 [("Що таке padding?", ["Зовнішній відступ", "Внутрішній відступ від рамки до вмісту", "Рамка", "Тінь"], 1, "padding — всередині."),
  ("Що робить box-sizing: border-box?", ["Додає рамку", "Робить так, що width включає padding і border", "Ховає елемент", "Центрує"], 1, "Ширина стає передбачуваною."),
  ("Як відцентрувати блок з фіксованою шириною?", ["text-align: center", "margin: 0 auto", "padding: center", "align: middle"], 1, "Автоматичні відступи зліва й справа.")])

lesson(9, "css", "Flexbox: розставляємо елементи",
 "Головний інструмент сучасної верстки: меню в ряд, центрування, рівні колонки. Все це кількома рядками.",
 ["вмикати flex-контейнер", "керувати розташуванням: justify-content, align-items", "використовувати gap, flex-wrap, flex-direction", "робити шапку сайту з логотипом і меню"],
 [
  H("Ідея Flexbox"),
  P("Даєш <b>батьку</b> <code>display: flex</code>, і всі його діти стають в ряд. Далі ти керуєш, як їх розподілити."),
  FIG(FLEX, "Дві осі: головна (за замовчуванням горизонтальна) і поперечна."),
  TABLE(["Властивість (для батька)", "Значення", "Що робить"], [
    ["<code>justify-content</code>", "flex-start, center, space-between, space-around", "Розподіл уздовж головної осі"],
    ["<code>align-items</code>", "stretch, center, flex-start, flex-end", "Вирівнювання по поперечній осі"],
    ["<code>gap</code>", "16px", "Відстань між дітьми"],
    ["<code>flex-direction</code>", "row, column", "Напрям: рядок чи стовпчик"],
    ["<code>flex-wrap</code>", "wrap", "Переносити на новий рядок, якщо не вміщається"]]),
  TRY(r'''<style>
  .row {
    display: flex;
    justify-content: space-between;  /* спробуй: center, flex-end, space-around */
    align-items: center;             /* спробуй: flex-start, flex-end */
    gap: 12px;
    height: 160px;
    background: #fff; border: 2px dashed #9c98a8; padding: 10px;
  }
  .item { background: #f0622e; color: white; padding: 20px; border-radius: 10px; font: bold 20px sans-serif; }
  .item:nth-child(2) { background: #2f6feb; padding: 40px 20px; }
  .item:nth-child(3) { background: #e8a400; }
</style>
<div class="row">
  <div class="item">1</div>
  <div class="item">2</div>
  <div class="item">3</div>
</div>''', "Пісочниця Flexbox: міняй значення"),
  H("Класична шапка сайту"),
  CODE("html", r'''
<style>
  header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 16px 24px;
    background: #1d1b26;
    color: white;
    font-family: sans-serif;
  }
  nav { display: flex; gap: 20px; }
  nav a { color: white; text-decoration: none; }
  nav a:hover { color: #e8a400; }
</style>
<header>
  <strong>📚 Моя полиця</strong>
  <nav>
    <a href="#">Колекція</a>
    <a href="#">Додати</a>
    <a href="#">Про мене</a>
  </nav>
</header>''', run=True),
  H("Ідеальне центрування"),
  CODE("css", r'''
.center {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;   /* на весь екран */
}'''),
  P("Для дітей є властивість <code>flex: 1</code>: «займи все вільне місце». Якщо всім дітям дати <code>flex: 1</code>, вони стануть рівними колонками."),
  TIP("Найкращий спосіб вивчити Flexbox — гра <a href='https://flexboxfroggy.com/#uk' target='_blank'>Flexbox Froggy</a> (є українською!) 🐸"),
 ],
 "Зроби шапку полиці на Flexbox (логотип зліва, меню справа). Карткам колекції дай батька <code>.cards</code> з <code>display: flex; flex-wrap: wrap; gap: 20px</code>.",
 ["F12 → Elements: біля flex-контейнера є значок <b>flex</b>. Клацни, і побачиш лінії-напрямні", "Звузь вікно браузера: картки переносяться на новий рядок?", "Спробуй змінювати justify-content прямо в DevTools: там є візуальний редактор (іконка біля display: flex)"],
 [("Базовий", "Пройди всі 24 рівні Flexbox Froggy. Скріншот фінального екрана."),
  ("Середній", "Зверстай «картку профілю»: аватар зліва, ім'я та опис справа, внизу 3 кнопки в ряд."),
  ("Зірочка ⭐", "Зроби футер на Flexbox з трьома колонками, які на вузькому екрані стають одна під одною (підказка: flex-wrap і flex: 1 1 200px).")],
 [("Кому пишемо display: flex?", ["Кожній дитині", "Батьківському контейнеру", "Тегу body завжди", "Лише картинкам"], 1, "Flex вмикається на батьку."),
  ("Як розкидати елементи по краях з рівними проміжками?", ["justify-content: center", "justify-content: space-between", "align-items: stretch", "gap: auto"], 1, "space-between — перший і останній притиснуті до країв."),
  ("Що робить flex-wrap: wrap?", ["Ховає елементи", "Переносить елементи на новий рядок, якщо не вміщаються", "Обгортає рамкою", "Повертає на 90°"], 1, "wrap = переносити.")])

lesson(10, "css", "Grid, адаптивність і анімації",
 "Сітка карток, що підлаштовується під телефон і комп'ютер, плюс плавні ефекти. Сайт починає виглядати професійно.",
 ["будувати сітку на CSS Grid", "робити адаптивну верстку з media queries", "перевіряти сайт у мобільному режимі DevTools", "додавати transition, transform і CSS-змінні"],
 [
  H("CSS Grid: сітка одним рядком"),
  CODE("html", r'''
<style>
  .cards {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(160px, 1fr));
    gap: 16px;
    font-family: sans-serif;
  }
  .card { background: #dce8ff; padding: 30px 10px; border-radius: 12px; text-align: center; }
</style>
<div class="cards">
  <div class="card">1</div><div class="card">2</div><div class="card">3</div>
  <div class="card">4</div><div class="card">5</div><div class="card">6</div>
</div>''', run=True, note="«Скільки влізе колонок, але кожна мінімум 160px». Зміни ширину вікна: кількість колонок зміниться сама!"),
  TIP("Flexbox — для рядка/стовпчика (меню, шапка). Grid — для сітки у двох напрямках (галерея, картки)."),
  H("Адаптивність: сайт для телефона"),
  P("Понад половина людей відкриває сайти з телефона. Три правила:"),
  STEPS(["У <code>&lt;head&gt;</code> обов'язково <code>&lt;meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\"&gt;</code> (VS Code вставляє його в шаблон).",
         "Не задавай фіксовану ширину великим блокам: <code>max-width</code> замість <code>width</code>, картинкам <code>max-width: 100%</code>.",
         "Використовуй <b>media queries</b>: правила, що спрацьовують лише на певній ширині екрана."]),
  CODE("css", r'''
/* Спочатку стилі для телефона */
nav { display: flex; flex-direction: column; }

/* Від 768px (планшет/комп'ютер) — меню в рядок */
@media (min-width: 768px) {
  nav { flex-direction: row; }
}'''),
  H("Плавні ефекти"),
  TRY(r'''<style>
  :root { --accent: #f0622e; }          /* CSS-змінна */
  .card {
    width: 200px; padding: 24px; margin: 30px;
    background: white; border-radius: 16px; font-family: sans-serif;
    box-shadow: 0 4px 12px rgba(0,0,0,.1);
    transition: transform .25s, box-shadow .25s;   /* плавність */
  }
  .card:hover {
    transform: translateY(-8px) rotate(-2deg);
    box-shadow: 0 16px 32px rgba(0,0,0,.18);
  }
  .badge { background: var(--accent); color: white; padding: 4px 10px; border-radius: 99px; }
  @keyframes pulse { 50% { transform: scale(1.15); } }
  .heart { display: inline-block; animation: pulse 1s infinite; }
</style>
<div class="card">
  <span class="badge">NEW</span>
  <h3>Наведи на мене</h3>
  <p>Улюблене <span class="heart">❤️</span></p>
</div>''', "Hover, transform, анімація, змінні"),
  P("<b>CSS-змінні</b> (<code>--accent</code>) — зберігаєш колір один раз у <code>:root</code> і використовуєш через <code>var(--accent)</code> скрізь. Захотів іншу тему — змінив один рядок."),
  CODE("css", r'''
:root {
  --bg: #fbf8f3;
  --text: #1d1b26;
  --accent: #f0622e;
  --radius: 16px;
}
/* Темна тема для тих, у кого вона увімкнена в системі */
@media (prefers-color-scheme: dark) {
  :root { --bg: #16151c; --text: #f3f0ea; }
}
body { background: var(--bg); color: var(--text); }''', title="Тема через змінні"),
 ],
 "Перероби <code>.cards</code> на Grid з <code>auto-fill</code>. Перенеси всі кольори в CSS-змінні. Додай hover-ефект карткам і перевір сайт на телефоні. <b>Верстка полиці готова!</b> 🎉",
 ["F12 → іконка 📱 (Toggle device toolbar, <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>): перевір iPhone SE і iPad", "Немає горизонтальної прокрутки на телефоні", "F12 → Lighthouse → Analyze: подивись бали Accessibility і SEO"],
 [("Базовий", "Пройди перші 12 рівнів <a href='https://cssgridgarden.com/#uk' target='_blank'>Grid Garden</a> (українською)."),
  ("Середній", "Фотогалерея на Grid: на телефоні 1 колонка, на планшеті 2, на комп'ютері 4. Hover — збільшення фото."),
  ("Зірочка ⭐", "Додай на сайт перемикач теми лише на CSS: дізнайся про <code>:has()</code> і чекбокс.")],
 [("Що робить repeat(auto-fill, minmax(160px, 1fr))?", ["Рівно 160 колонок", "Стільки колонок, скільки влізе, кожна не менше 160px", "Одна колонка", "Анімацію"], 1, "Адаптивна сітка без media queries."),
  ("Для чого @media (min-width: 768px)?", ["Друк сторінки", "Правила для екранів від 768px завширшки", "Відео", "Мінімальний шрифт"], 1, "Media query = умова на екран."),
  ("Як використати CSS-змінну --accent?", ["color: --accent", "color: $accent", "color: var(--accent)", "color: accent()"], 2, "var(--ім'я).")])
