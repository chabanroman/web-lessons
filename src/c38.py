import copy
from helpers import *
from svgs import *
import helpers, c1, c2, c3, c4

ID25 = ["web","text","img","semantic","forms","css-intro","fonts","box","flex","grid","js-intro","cond","arrays","func","objects","dom","events","shelf","sql","fetch","express","supa","ai","agents","final"]
S = {ID25[l["n"]-1]: l for l in helpers.LESSONS}
def src(i): return copy.deepcopy(S[i])
def secs(i, idx): return [copy.deepcopy(S[i]["sections"][k]) for k in idx]
def Qs(lst): return [{"q": q, "o": o, "a": a, "w": w} for q, o, a, w in lst]
def HW(lst): return [{"lvl": a, "v": b} for a, b in lst]

def new(id, block, title, sub, goals, sections, project, check, hw, quiz, mins=45):
    d = make(0, block, title, sub, goals, sections, project, check, hw, quiz, mins=mins, id=id)
    return d

L = []
def add(d, id=None):
    if id: d["id"] = id
    L.append(d)

# ───── HTML (1–7)
add(src("web"), "web")

add(new("text", "html", "Текст: заголовки, абзаци, виділення",
 "З тексту починається будь-який сайт. Вчимося правильно його розмічати.",
 ["використовувати заголовки h1–h6 за правилами", "розмічати абзаци, виділення, переноси", "вставляти спецсимволи й цитати", "залишати коментарі в коді"],
 secs("text", [0,1,2,3]) + [
  H("Спецсимволи"),
  P("Деякі символи в HTML мають особливе значення (наприклад, <code>&lt;</code> відкриває тег). Щоб показати їх як текст, використовують <b>HTML-сутності</b>:"),
  TABLE(["Пишеш", "Бачиш", "Для чого"], [
    ["<code>&amp;lt;</code> / <code>&amp;gt;</code>", "&lt; &gt;", "Кутові дужки як текст"],
    ["<code>&amp;copy;</code>", "©", "Авторське право у футері"],
    ["<code>&amp;nbsp;</code>", "нерозривний пробіл", "Щоб «10 км» не розірвались на два рядки"],
    ["<code>&amp;mdash;</code>", "—", "Довге тире"]]),
  H("Цитати й код"),
  CODE("html", r'''
<blockquote>
  Програмування — це мистецтво розбивати велику задачу на маленькі.
</blockquote>

<p>Щоб вивести текст у консоль, напиши <code>console.log()</code>.</p>

<!-- Це коментар: браузер його не показує -->
<p>&copy; 2026 Моя полиця</p>''', run=True),
  TRY(r'''<h1>Моя улюблена книга</h1>
<p>Це <strong>найкраща</strong> книга, яку я <em>коли-небудь</em> читав.</p>
<blockquote>Додай тут улюблену цитату з книги</blockquote>
<!-- Додай h2 «Чому раджу» і два абзаци -->'''),
 ],
 "На <code>index.html</code> додай під h1 абзац-опис полиці з виділенням <code>&lt;strong&gt;</code> та цитату <code>&lt;blockquote&gt;</code> про твою тему. У футер — <code>&amp;copy;</code>, рік і своє ім'я.",
 ["F12 → Elements: структура заголовків логічна (h1 → h2 → h3)", "Символ © відображається правильно", "Коментар не видно на сторінці, але видно в Elements"],
 [("Базовий", "Сторінка «Мій улюблений персонаж»: h1, два h2, 4 абзаци з виділеннями."),
  ("Середній", "Зроби «статтю для шкільної газети» про подію в класі: заголовки, цитата однокласника, підпис автора."),
  ("Зірочка ⭐", "Знайди на MDN теги &lt;mark&gt;, &lt;abbr&gt;, &lt;time&gt; і використай їх у статті.")],
 [("Скільки h1 має бути на сторінці?", ["Скільки завгодно", "Один", "Жодного", "Шість"], 1, "Один h1 — головна тема."),
  ("Як показати символ &lt; як текст?", ["&lt;&lt;", "&amp;lt;", "\\&lt;", "Ніяк"], 1, "HTML-сутність &amp;lt;."),
  ("Навіщо коментарі в коді?", ["Щоб браузер їх показав", "Щоб пояснити код людям", "Для швидкості", "Для SEO"], 1, "Браузер їх ігнорує.")]), "text")

add(new("links", "html", "Списки й посилання",
 "Нумеровані й марковані списки, посилання на сайти, на свої сторінки і навіть на місце всередині сторінки.",
 ["робити марковані й нумеровані списки, зокрема вкладені", "ставити посилання на сайти й свої сторінки", "робити якірні посилання всередині сторінки", "будувати меню з кількох сторінок"],
 secs("text", [4,5,6,7,8]) + [
  H("Якірні посилання: стрибок по сторінці"),
  CODE("html", r'''
<nav>
  <a href="#top5">Топ-5</a> |
  <a href="#all">Уся колекція</a>
</nav>

<h2 id="top5">Мій топ-5</h2>
<p>...</p>

<h2 id="all">Уся колекція</h2>
<p>...</p>''', note="<code>href=\"#all\"</code> веде до елемента з <code>id=\"all\"</code>. Так роблять меню на односторінкових сайтах."),
  secs("text", [9])[0], secs("text", [10])[0],
 ],
 "Додай на <code>index.html</code> нумерований список «Мій топ-5», меню <code>nav</code> з якірними посиланнями на розділи і посилання на сторінку <code>about.html</code>.",
 ["Клік по пункту меню прокручує до розділу", "Посилання «Про мене» відкриває твою сторінку, а з неї є посилання назад", "F12 → Elements: <code>&lt;li&gt;</code> лежать усередині <code>&lt;ol&gt;</code>"],
 [("Базовий", "Сторінка «Мій ідеальний день»: розклад нумерованим списком (7+ пунктів)."),
  ("Середній", "Рецепт улюбленої страви: інгредієнти (ul), кроки (ol), посилання на відео."),
  ("Зірочка ⭐", "Міні-сайт з 3 сторінок (головна, хобі, контакти) з однаковим меню.")],
 [("Який тег робить нумерований список?", ["&lt;ul&gt;", "&lt;li&gt;", "&lt;ol&gt;", "&lt;list&gt;"], 2, "ol = ordered list."),
  ("Куди веде href=\"#contacts\"?", ["На сайт contacts.com", "До елемента з id=\"contacts\" на цій сторінці", "На файл contacts.html", "Нікуди"], 1, "Якірне посилання."),
  ("Що робить target=\"_blank\"?", ["Ховає посилання", "Відкриває в новій вкладці", "Робить порожнім", "Фарбує"], 1, "_blank — нова вкладка.")]), "links")

add(src("img"), "img")

sem = src("semantic")
add(new("semantic", "html", "Семантика: структура сторінки",
 "Header, nav, main, footer: теги, які роблять сторінку зрозумілою людям, пошуковикам і програмам для незрячих.",
 ["будувати сторінку з header, nav, main, section, article, aside, footer", "розуміти, коли потрібен div і span", "пояснити, що таке доступність"],
 secs("semantic", [0,1,2,3,4]) + [
  H("Доступність: сайт для всіх"),
  P("Близько кожної шостої людини у світі має певну інвалідність. Хтось не бачить і слухає сайт через <b>програму екранного доступу</b>, хтось керує лише клавіатурою. Семантика — перший крок до доступності:"),
  LIST(["Один <code>&lt;h1&gt;</code> і логічні заголовки — програма читає їх як зміст.", "<code>&lt;nav&gt;</code> — людина одразу переходить до меню.", "<code>alt</code> у картинок, <code>&lt;label&gt;</code> у полів.", "Спробуй: натискай <kbd>Tab</kbd> на своїй сторінці. Чи можна дістатися до всіх посилань?"]),
  TRY(r'''<header><h1>Мій сайт</h1><nav><a href="#">Головна</a> <a href="#">Блог</a></nav></header>
<main>
  <article>
    <h2>Перша стаття</h2>
    <p>Текст статті...</p>
  </article>
  <!-- додай aside з цікавим фактом -->
</main>
<footer>&copy; 2026</footer>'''),
 ],
 "Перебудуй <code>index.html</code>: <code>header</code> (назва + <code>nav</code>), <code>main</code> з розділами <code>section</code> («Топ-5», «Вся колекція»), <code>aside</code> з фактом про твою тему, <code>footer</code>.",
 ["F12 → Elements: згорни <code>&lt;body&gt;</code>, і ти бачиш header / main / footer", "Пройдися по сторінці клавішею Tab: видно, де фокус?", "F12 → Lighthouse → Accessibility: які зауваження?"],
 [("Базовий", "Сторінка «Мій клас» із семантичною структурою: header, nav, main (2 section), aside, footer."),
  ("Середній", "Візьми будь-який сайт новин, відкрий F12 і випиши, які семантичні теги він використовує."),
  ("Зірочка ⭐", "Увімкни на телефоні VoiceOver (iPhone) або TalkBack (Android) і «послухай» свою сторінку. Що незручно?")],
 [("Який тег для головного вмісту сторінки?", ["&lt;header&gt;", "&lt;main&gt;", "&lt;div&gt;", "&lt;body&gt;"], 1, "main — унікальне головне."),
  ("Коли використовувати div?", ["Завжди", "Коли жоден семантичний тег не підходить", "Ніколи", "Лише для картинок"], 1, "div — коробка без змісту."),
  ("Що таке доступність?", ["Швидкість сайту", "Зручність сайту для всіх людей, зокрема з інвалідністю", "Безкоштовність", "Пароль"], 1, "a11y.")]), "semantic")

add(new("tables", "html", "Таблиці",
 "Таблиці показують дані рядками й стовпцями. Це перший крок до розуміння баз даних.",
 ["створювати таблиці з thead і tbody", "об'єднувати клітинки colspan і rowspan", "додавати підпис caption", "перевіряти HTML валідатором"],
 secs("semantic", [5,6,7]) + [
  H("Об'єднання клітинок"),
  CODE("html", r'''
<table border="1">
  <caption>Розклад на понеділок</caption>
  <tr><th>Час</th><th>Урок</th></tr>
  <tr><td>8:30</td><td>Математика</td></tr>
  <tr><td colspan="2" style="text-align:center">🍎 Велика перерва</td></tr>
  <tr><td rowspan="2">10:00</td><td>Інформатика (група 1)</td></tr>
  <tr><td>Англійська (група 2)</td></tr>
</table>''', run=True, note="<code>colspan=\"2\"</code> — клітинка на 2 стовпці, <code>rowspan=\"2\"</code> — на 2 рядки."),
  WARN("Таблиці — лише для <b>даних</b>. Колись ними верстали цілі сайти, але сьогодні для розташування є CSS (Flexbox і Grid)."),
  secs("semantic", [8])[0],
  H("Перевірка валідатором"),
  STEPS(["Відкрий <a href='https://validator.w3.org/#validate_by_input' target='_blank'>validator.w3.org</a> → вкладка <b>Validate by Direct Input</b>.", "Встав весь код свого index.html → <b>Check</b>.", "Виправ усі <b>Error</b>. Warning — підказки, їх теж варто прочитати."]),
 ],
 "У розділі «Вся колекція» зроби таблицю з <code>caption</code>: назва, автор/студія, рік, оцінка (мінімум 6 рядків). Перевір усю сторінку валідатором.",
 ["Таблиця має <code>thead</code> і <code>tbody</code>", "Валідатор: 0 помилок", "F12 → Elements: розгорни таблицю й знайди свій <code>colspan</code>"],
 [("Базовий", "Свій розклад уроків на тиждень у вигляді таблиці з caption."),
  ("Середній", "Таблиця «Турнір класу» (футбол / шахи): команди, ігри, перемоги, поразки, очки."),
  ("Зірочка ⭐", "Таблиця-календар на місяць з об'єднаними клітинками для свят і канікул.")],
 [("Що таке &lt;td&gt;?", ["Рядок", "Звичайна клітинка", "Заголовок", "Таблиця"], 1, "table data."),
  ("Що робить colspan=\"3\"?", ["3 рядки", "Клітинка займає 3 стовпці", "3 таблиці", "Рамка 3px"], 1, "Об'єднання по горизонталі."),
  ("Для чого НЕ варто використовувати таблиці?", ["Розклад", "Результати змагань", "Розташування блоків сторінки (верстка)", "Ціни"], 2, "Для верстки є CSS.")]), "tables")

add(src("forms"), "forms")

# ───── CSS (8–16)
add(new("css-intro", "css", "Знайомство з CSS: селектори",
 "Вдягаємо сторінку: підключаємо стилі й вчимося «цілитися» в потрібні елементи.",
 ["підключати окремий файл style.css", "використовувати селектори: тег, .клас, #id, нащадок", "розуміти каскад і специфічність", "редагувати стилі в DevTools"],
 secs("css-intro", [0,1,2,3,4,5,6,10,11]) + [
  TRY(r'''<style>
  p { color: gray; }
  .important { color: crimson; font-weight: bold; }
  #special { background: gold; }
  /* яке правило переможе для третього абзацу? */
</style>
<p>Звичайний абзац</p>
<p class="important">Важливий абзац</p>
<p class="important" id="special">Особливий абзац</p>''', "Хто переможе?"),
 ],
 "Створи <code>css/style.css</code> і підключи до <code>index.html</code>. Дай класи <code>card</code> статтям і зроби 8+ правил з різними типами селекторів (тег, клас, id, нащадок).",
 ["F12 → Elements → клік по h1 → у Styles видно твої правила і файл <code>style.css</code>", "Якщо стилі не працюють — Network: чи є style.css (а не 404)?", "Закресленні правила в Styles — це ті, що програли в каскаді"],
 [("Базовий", "Розфарбуй сторінку «Про мене»: окремий style.css, усі три типи селекторів."),
  ("Середній", "Пройди 15 рівнів <a href='https://flukeout.github.io' target='_blank'>CSS Diner</a>."),
  ("Зірочка ⭐", "Пройди всі 32 рівні CSS Diner.")],
 [("Як вибрати всі елементи з class=\"card\"?", ["card", "#card", ".card", "*card"], 2, "Крапка = клас."),
  ("Що переможе: #title { color: red } чи h1 { color: blue }?", ["blue", "red", "Змішаються", "Жоден"], 1, "id специфічніший."),
  ("Що вибирає nav a?", ["Усі nav і всі a", "Посилання всередині nav", "nav з класом a", "Нічого"], 1, "Пробіл = нащадок.")]), "css-intro")

add(new("colors", "css", "Кольори, фони й градієнти",
 "Палітра сайту: формати кольорів, фонові картинки, градієнти та прозорість.",
 ["записувати кольори в hex, rgb, hsl", "робити фон кольором, градієнтом і картинкою", "керувати прозорістю", "підбирати гармонійну палітру"],
 secs("css-intro", [7,8,9]) + [
  H("Градієнти"),
  CODE("html", r'''
<style>
  .g1 { background: linear-gradient(90deg, #f0622e, #e8a400); }
  .g2 { background: linear-gradient(135deg, #2f6feb, #8b5cf6); }
  .g3 { background: radial-gradient(circle, #fff3cc, #f0622e); }
  div { height: 70px; border-radius: 14px; margin: 8px 0; color: white;
        display: grid; place-items: center; font: bold 18px sans-serif; }
</style>
<div class="g1">linear 90deg</div>
<div class="g2">linear 135deg</div>
<div class="g3">radial</div>''', run=True),
  H("Фонова картинка"),
  CODE("css", r'''
.hero {
  background-image: url('../images/hero.jpg');
  background-size: cover;        /* заповнити весь блок */
  background-position: center;   /* центр картинки в центрі блоку */
  min-height: 300px;
}

/* текст на фото читається краще з темним шаром */
.hero {
  background: linear-gradient(rgba(0,0,0,.5), rgba(0,0,0,.5)), url('../images/hero.jpg') center / cover;
  color: white;
}'''),
  H("Прозорість"),
  P("<code>opacity: 0.5</code> робить прозорим увесь елемент разом з текстом. Щоб прозорим був лише фон, використовуй колір з альфа-каналом: <code>rgba(0, 0, 0, 0.5)</code> або <code>#00000080</code>."),
  H("Як підібрати палітру"),
  LIST(["Правило <b>60–30–10</b>: 60% — основний (фон), 30% — додатковий (картки, шапка), 10% — акцент (кнопки, посилання).", "Генератори: <a href='https://coolors.co' target='_blank'>coolors.co</a>, <a href='https://color.adobe.com' target='_blank'>color.adobe.com</a>.", "Перевір контраст тексту й фону: <a href='https://webaim.org/resources/contrastchecker/' target='_blank'>WebAIM Contrast Checker</a> (мінімум 4.5 : 1)."]),
  TRY(r'''<style>
  body { margin: 0; font-family: sans-serif; }
  .hero {
    background: linear-gradient(135deg, #1d1b26, #2f6feb);
    color: white; padding: 40px 20px; text-align: center;
  }
  .btn { background: #f0622e; color: white; padding: 10px 20px; border-radius: 99px; display: inline-block; }
</style>
<div class="hero">
  <h1>Моя полиця</h1>
  <p>Зміни градієнт і колір кнопки</p>
  <span class="btn">Дивитися колекцію</span>
</div>''', "Шапка з градієнтом"),
 ],
 "Обери палітру з 3–4 кольорів за правилом 60–30–10. Зроби шапці градієнтний фон, кнопкам — акцентний колір. Перевір контраст тексту.",
 ["F12 → Styles → клацни квадратик кольору: побачиш контраст (Contrast ratio) і чи достатній він", "Фонова картинка не «розтягнута»: background-size: cover", "Кольори схожі на палітру, яку ти обрав"],
 [("Базовий", "Зроби 5 кнопок з різними градієнтами й назви їх (Захід сонця, Океан…)."),
  ("Середній", "Шапка-банер з фоновим фото й темним напівпрозорим шаром, на ній заголовок і кнопка."),
  ("Зірочка ⭐", "Знайди палітру улюбленого бренду/гри (через піпетку DevTools на їхньому сайті) і повтори її на своїй сторінці.")],
 [("Що означає #000000?", ["Білий", "Чорний", "Червоний", "Прозорий"], 1, "Усі канали 0 — чорний."),
  ("Як зробити прозорим лише фон, а не текст?", ["opacity: 0.5", "background: rgba(0,0,0,.5)", "color: transparent", "display: none"], 1, "Альфа-канал у кольорі фону."),
  ("Що робить background-size: cover?", ["Повторює картинку", "Масштабує картинку, щоб вона заповнила блок", "Ховає картинку", "Робить її маленькою"], 1, "Заповнити повністю.")]), "colors")

add(src("fonts"), "fonts")
add(src("box"), "box")
add(src("flex"), "flex")

add(new("grid", "css", "CSS Grid: сітка сторінки",
 "Сітки для галерей, карток і цілих макетів сторінок. Grid — найпотужніший інструмент верстки.",
 ["створювати сітку з колонками й рядками", "використовувати fr, repeat, minmax, auto-fill", "розтягувати елементи на кілька клітинок", "будувати макет сторінки через grid-template-areas"],
 secs("grid", [0,1,2]) + [
  H("Колонки й одиниця fr"),
  CODE("html", r'''
<style>
  .layout {
    display: grid;
    grid-template-columns: 200px 1fr 1fr;   /* фіксована + дві рівні частки */
    gap: 10px;
    font-family: sans-serif;
  }
  .layout div { background: #fff3cc; padding: 20px; border-radius: 10px; }
  .wide { grid-column: span 2; background: #ffe3d6 !important; }  /* займає 2 колонки */
</style>
<div class="layout">
  <div>200px</div><div>1fr</div><div>1fr</div>
  <div class="wide">span 2</div><div>1</div>
</div>''', run=True, note="<b>fr</b> (fraction) — частка вільного місця. <code>1fr 2fr</code> = друга колонка вдвічі ширша."),
  H("Макет сторінки через області"),
  CODE("html", r'''
<style>
  .page {
    display: grid;
    grid-template-areas:
      "header header"
      "aside  main"
      "footer footer";
    grid-template-columns: 160px 1fr;
    gap: 8px; min-height: 260px; font: bold 15px sans-serif;
  }
  header { grid-area: header; background: #ffe3d6; }
  aside  { grid-area: aside;  background: #fff3cc; }
  main   { grid-area: main;   background: #dce8ff; }
  footer { grid-area: footer; background: #d7f5e3; }
  .page > * { padding: 14px; border-radius: 10px; }
</style>
<div class="page">
  <header>header</header><aside>aside</aside><main>main</main><footer>footer</footer>
</div>''', run=True, note="Ти буквально «малюєш» макет словами! Зміни розташування областей і запусти ще раз."),
  TRY(r'''<style>
  .gallery { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
  .gallery div { background: #2f6feb; color: #fff; height: 80px; border-radius: 10px;
                 display: grid; place-items: center; font: bold 20px sans-serif; }
  .big { grid-column: span 2; grid-row: span 2; height: auto !important; background: #f0622e !important; }
</style>
<div class="gallery">
  <div class="big">1</div><div>2</div><div>3</div><div>4</div><div>5</div><div>6</div>
</div>''', "Галерея з великим фото"),
  TIP("Тренажер: <a href='https://cssgridgarden.com/#uk' target='_blank'>Grid Garden</a> (українською) 🥕"),
 ],
 "Переведи сітку карток колекції на Grid з <code>repeat(auto-fill, minmax(220px, 1fr))</code>. Першу картку («Улюблене») зроби на 2 колонки.",
 ["F12 → Elements: біля контейнера значок <b>grid</b>. Клацни — побачиш лінії сітки з номерами", "Звузь вікно: кількість колонок змінюється сама", "Немає горизонтальної прокрутки"],
 [("Базовий", "Пройди 12 рівнів Grid Garden."),
  ("Середній", "Макет сторінки блогу через grid-template-areas: шапка, меню зліва, стаття, бічна панель, футер."),
  ("Зірочка ⭐", "Пройди всі 28 рівнів Grid Garden.")],
 [("Що означає 1fr?", ["1 піксель", "Одна частка вільного місця", "1 рядок", "Шрифт"], 1, "fraction."),
  ("Як змусити елемент зайняти 2 колонки?", ["width: 2", "grid-column: span 2", "colspan=2", "flex: 2"], 1, "span 2."),
  ("Коли краще Grid, а не Flexbox?", ["Для меню в рядок", "Для сітки в двох напрямках (рядки й колонки)", "Для тексту", "Ніколи"], 1, "Grid — двовимірний.")]), "grid")

add(new("responsive", "css", "Адаптивність: сайт для телефона",
 "Понад половина людей відкриває сайти з телефона. Вчимося робити сторінки, що гарно виглядають на будь-якому екрані.",
 ["пояснити, що таке адаптивний дизайн", "писати media queries", "використовувати підхід mobile-first", "тестувати сайт у мобільному режимі DevTools"],
 secs("grid", [3,4,5,6]) + [
  H("Mobile-first"),
  P("Професійний підхід: <b>спочатку</b> пишемо стилі для телефона (вони простіші: все в один стовпчик), а потім через <code>min-width</code> додаємо складніше для великих екранів."),
  CODE("html", r'''
<style>
  .cards { display: grid; gap: 10px; font: bold 16px sans-serif; }
  .cards div { background: #dce8ff; padding: 24px; border-radius: 10px; }

  /* планшет */
  @media (min-width: 500px) { .cards { grid-template-columns: 1fr 1fr; } }
  /* комп'ютер */
  @media (min-width: 800px) { .cards { grid-template-columns: repeat(4, 1fr); } }
</style>
<div class="cards"><div>1</div><div>2</div><div>3</div><div>4</div></div>''', run=True, note="Запусти й зміни ширину вікна браузера: 1 → 2 → 4 колонки."),
  TABLE(["Типові точки зламу", "Пристрій"], [["до 480px", "Телефон"], ["480–768px", "Великий телефон / маленький планшет"], ["768–1024px", "Планшет"], ["від 1024px", "Ноутбук, комп'ютер"]]),
  H("Гумові картинки й відео"),
  CODE("css", r'''
img, video, iframe {
  max-width: 100%;   /* ніколи не ширше за батька */
  height: auto;      /* зберегти пропорції */
}'''),
  H("Мобільний режим DevTools"),
  STEPS(["F12 → іконка 📱 (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>M</kbd>).", "Вгорі обери пристрій: iPhone SE (найвужчий), iPad, Galaxy.", "Перевір: нема горизонтальної прокрутки, текст читається без збільшення, кнопки достатньо великі для пальця (мін. 44×44px).", "Найнадійніше — відкрити сайт на справжньому телефоні."]),
 ],
 "Зроби полицю mobile-first: на телефоні меню стовпчиком і картки в 1 колонку, на планшеті 2, на комп'ютері 3–4. Картинкам — <code>max-width: 100%</code>.",
 ["📱 iPhone SE: нема горизонтальної прокрутки", "📱 iPad: 2 колонки карток", "Lighthouse → Accessibility: кнопки й посилання достатнього розміру"],
 [("Базовий", "Зроби сторінку «Про мене» адаптивною: фото зверху на телефоні, зліва — на комп'ютері."),
  ("Середній", "Меню, яке на телефоні стає стовпчиком, а на комп'ютері — рядком."),
  ("Зірочка ⭐", "Меню-«бургер» на телефоні: кнопка ☰ показує/ховає меню (лише CSS, через чекбокс і :checked).")],
 [("Що таке mobile-first?", ["Сайт лише для телефонів", "Спершу стилі для телефона, потім доповнення для великих екранів", "Додаток замість сайту", "Швидкий інтернет"], 1, "Від простого до складного."),
  ("Що робить @media (min-width: 768px)?", ["Застосовує правила від 768px ширини", "Ширина 768px", "Лише для телефонів", "Друк"], 0, "Умова на екран."),
  ("Навіщо img { max-width: 100% }?", ["Збільшити картинки", "Щоб картинка не виходила за межі батька", "Сховати", "Обрізати"], 1, "Гумові картинки.")]), "responsive")

add(new("anim", "css", "Переходи, анімації та CSS-змінні",
 "Плавні ефекти, «живі» елементи та теми оформлення. Сайт починає виглядати професійно.",
 ["робити плавні переходи transition", "трансформувати елементи: зсув, поворот, масштаб", "створювати анімації через @keyframes", "зберігати кольори в CSS-змінних і робити темну тему"],
 secs("grid", [7,8,9,10]) + [
  H("Трансформації"),
  TABLE(["transform", "Що робить"], [["<code>translate(20px, -10px)</code>", "Зсув"], ["<code>rotate(15deg)</code>", "Поворот"], ["<code>scale(1.2)</code>", "Масштаб (1 = як є)"], ["<code>skew(10deg)</code>", "Нахил"]]),
  H("Анімація з кадрами"),
  CODE("html", r'''
<style>
  @keyframes float {
    0%   { transform: translateY(0); }
    50%  { transform: translateY(-15px); }
    100% { transform: translateY(0); }
  }
  @keyframes spin { to { transform: rotate(360deg); } }
  .rocket { font-size: 50px; display: inline-block; animation: float 2s ease-in-out infinite; }
  .loader { width: 40px; height: 40px; border: 5px solid #e7e1d6; border-top-color: #f0622e;
            border-radius: 50%; animation: spin 1s linear infinite; display: inline-block; margin-left: 30px; }
</style>
<span class="rocket">🚀</span>
<span class="loader"></span>''', run=True, note="Індикатор завантаження (loader) знадобиться нам, коли будемо завантажувати дані з бази!"),
  WARN("Не перестарайся: анімація має допомагати, а не відволікати. Деякі люди погано переносять рух на екрані: для них є <code>@media (prefers-reduced-motion: reduce)</code>."),
 ],
 "Перенеси всі кольори полиці в CSS-змінні. Додай hover-ефект карткам (піднімання + тінь) і анімований loader, який поки що просто лежить у футері.",
 ["F12 → Elements → :root: видно твої змінні, змінюй їх наживо", "F12 → ⋮ → More tools → <b>Animations</b>: можна сповільнити анімацію і роздивитися", "Hover плавний, без «стрибка»"],
 [("Базовий", "Кнопка, яка при наведенні збільшується, міняє колір і злегка повертається."),
  ("Середній", "Анімований банер «Новинка!», що пульсує, і картка, що перевертається при наведенні (rotateY)."),
  ("Зірочка ⭐", "Перемикач світлої/темної теми лише на CSS-змінних + prefers-color-scheme.")],
 [("Що робить transition: transform .3s?", ["Плавна зміна transform за 0.3 с", "Поворот на 30°", "Нескінченна анімація", "Затримка"], 0, "Плавний перехід."),
  ("Як використати CSS-змінну --accent?", ["color: --accent", "color: var(--accent)", "color: $accent", "color: accent()"], 1, "var(--ім'я)."),
  ("Чим @keyframes відрізняється від transition?", ["Нічим", "keyframes може працювати сам, без дій користувача, і має кілька кадрів", "transition — лише для кольору", "keyframes — для JS"], 1, "Анімація з кадрами.")]), "anim")

add(new("landing", "css", "Практикум: верстаємо лендінг",
 "Великий практичний урок: від макета до готової сторінки. Збираємо все, що вивчили в HTML і CSS.",
 ["читати макет і розбивати його на блоки", "верстати сторінку від загального до деталей", "перевіряти результат за чеклистом якості"],
 [
  H("Що таке лендінг"),
  P("<b>Лендінг</b> (landing page) — односторінковий сайт з однією метою: зареєструватися на подію, купити товар, дізнатися про проєкт. Наш лендінг — <b>сторінка-презентація полиці</b> або шкільної події (на вибір)."),
  H("Структура"),
  CODE("text", r'''
┌──────────────────────────────────────┐
│ HEADER: логотип          меню        │
├──────────────────────────────────────┤
│ HERO: великий заголовок, опис,       │
│       кнопка «Дивитися»   [картинка] │
├──────────────────────────────────────┤
│ ПЕРЕВАГИ: 3 картки з іконками        │
├──────────────────────────────────────┤
│ ГАЛЕРЕЯ / КОЛЕКЦІЯ: сітка карток      │
├──────────────────────────────────────┤
│ ВІДГУК / ЦИТАТА                      │
├──────────────────────────────────────┤
│ ФОРМА: «Порадь мені щось»            │
├──────────────────────────────────────┤
│ FOOTER: контакти, ©                  │
└──────────────────────────────────────┘''', title="Макет лендінгу"),
  H("Порядок роботи професіонала"),
  STEPS(["<b>HTML без стилів.</b> Спочатку вся структура й текст: семантичні теги, класи. Сторінка «гола», але логічна.",
         "<b>Глобальні стилі.</b> <code>box-sizing</code>, змінні кольорів, шрифти, body, контейнер <code>max-width: 1100px; margin: 0 auto</code>.",
         "<b>Блок за блоком згори вниз.</b> Header → Hero → Переваги… Закінчив блок — перевірив у браузері.",
         "<b>Адаптивність.</b> Переглянь усе в 📱 режимі й допиши media queries.",
         "<b>Полірування.</b> Hover-ефекти, переходи, відступи. Перевір контраст, alt, валідатор, Lighthouse."]),
  H("Каркас для старту"),
  CODE("html", r'''
<header class="header container">
  <a class="logo" href="#">📚 Полиця</a>
  <nav class="nav"><a href="#features">Чому</a><a href="#collection">Колекція</a><a href="#form">Порадь</a></nav>
</header>

<section class="hero container">
  <div>
    <h1>Мої улюблені ігри в одному місці</h1>
    <p>Оцінки, відгуки й рекомендації для друзів.</p>
    <a class="btn" href="#collection">Дивитися колекцію</a>
  </div>
  <img src="images/hero.png" alt="Колаж з обкладинок ігор">
</section>

<section id="features" class="features container">
  <article class="feature"><span>⭐</span><h3>Чесні оцінки</h3><p>…</p></article>
  <article class="feature"><span>🔍</span><h3>Зручний пошук</h3><p>…</p></article>
  <article class="feature"><span>🤝</span><h3>Поради друзям</h3><p>…</p></article>
</section>''', title="index.html (початок)"),
  CODE("css", r'''
.container { max-width: 1100px; margin: 0 auto; padding: 0 20px; }
.header { display: flex; justify-content: space-between; align-items: center; padding-block: 16px; }
.hero { display: grid; gap: 30px; align-items: center; padding-block: 60px; }
@media (min-width: 800px) { .hero { grid-template-columns: 1.2fr 1fr; } }
.features { display: grid; gap: 20px; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); }
.btn { display: inline-block; background: var(--accent); color: #fff; padding: 12px 24px;
       border-radius: 99px; text-decoration: none; transition: transform .2s; }
.btn:hover { transform: translateY(-3px); }''', title="css/style.css (ключові правила)"),
  H("Чекліст якості"),
  LIST(["☐ Один h1, логічні заголовки", "☐ Усі картинки з alt, стиснуті", "☐ Палітра 60–30–10, контраст ≥ 4.5", "☐ Максимум 2 шрифти", "☐ Немає горизонтальної прокрутки на iPhone SE", "☐ Валідатор: 0 помилок", "☐ Lighthouse: Accessibility ≥ 90"]),
  TIP("Шукай натхнення на <a href='https://dribbble.com/search/landing-page' target='_blank'>Dribbble</a> чи <a href='https://www.awwwards.com' target='_blank'>Awwwards</a>. Не копіюй, а бери ідеї: розташування, кольори, шрифти."),
 ],
 "Зверстай повний лендінг своєї полиці за макетом: header, hero, 3 переваги, сітка колекції, цитата, форма, footer. Адаптивно.",
 ["Пройди чекліст якості вище", "Покажи сусіду по парті на телефоні: чи все зрозуміло без пояснень?", "Lighthouse: запиши свої бали в коментар у HTML"],
 [("Обов'язково", "Доведи лендінг до кінця за чеклистом."),
  ("Середній", "Додай секцію FAQ з тегами &lt;details&gt;&lt;summary&gt; (розкривні питання)."),
  ("Зірочка ⭐", "Зверстай другий лендінг для шкільної події (дискотека, ярмарок, хакатон) за 1 вечір.")],
 [("З чого починати верстку?", ["Зі стилів кнопок", "З HTML-структури всіх блоків", "З анімацій", "З картинок"], 1, "Спочатку скелет."),
  ("Навіщо .container { max-width: 1100px; margin: 0 auto }?", ["Щоб вміст не розтягувався на широких екранах і був по центру", "Щоб сховати", "Для анімації", "Для телефона"], 0, "Обмеження ширини + центр."),
  ("Що таке лендінг?", ["Багатосторінковий магазин", "Односторінковий сайт з однією метою", "Додаток", "База даних"], 1, "Landing page.")], mins=90), "landing")

# ───── JS (17–28)
add(src("js-intro"), "js-intro")
add(src("cond"), "cond")

add(new("arrays", "js", "Масиви: списки даних",
 "Масив — це список: друзі, ігри, оцінки. Вчимося створювати, читати й змінювати списки.",
 ["створювати масиви й отримувати елементи за індексом", "додавати, видаляти й шукати елементи", "використовувати методи push, pop, includes, indexOf, slice, join"],
 secs("arrays", [0,1,2]) + [
  H("Ще корисні методи"),
  TABLE(["Метод", "Що робить", "Приклад"], [
    ["<code>unshift(x)</code>", "Додати на початок", "<code>arr.unshift('new')</code>"],
    ["<code>shift()</code>", "Видалити перший", "<code>arr.shift()</code>"],
    ["<code>slice(a, b)</code>", "Копія частини (з a до b, не включаючи b)", "<code>arr.slice(0, 3)</code> — перші три"],
    ["<code>reverse()</code>", "Перевернути", "<code>arr.reverse()</code>"],
    ["<code>join(', ')</code>", "Склеїти в рядок", "<code>'a, b, c'</code>"],
    ["<code>Array.isArray(x)</code>", "Чи це масив?", "<code>true</code>"]]),
  CODE("javascript", r'''
const top = ['Minecraft', 'Terraria', 'Portal 2', 'Celeste', 'Hades'];

console.log(top.slice(0, 3));        // топ-3
top.unshift('Stardew Valley');       // нове на перше місце
console.log(top[0], top.length);
console.log(top.at(-1));             // останній (сучасний спосіб)
console.log(top.join(' → '));''', run=True),
  TRY(r'''<script>
  const playlist = ['Пісня 1', 'Пісня 2', 'Пісня 3'];
  // 1. Додай пісню в кінець
  // 2. Видали першу
  // 3. Виведи кількість і весь список через ' | '
  console.log(playlist);
</script>''', "Плейлист"),
 ],
 "У <code>app.js</code> створи масив <code>titles</code> з 6+ назвами з колекції. Виведи першу, останню, кількість і топ-3 через <code>slice</code>.",
 ["Console: напиши <code>titles</code> і розгорни стрілочкою — видно індекси", "Спробуй <code>titles[100]</code> — що поверне? Чому?", "Червоних помилок нема"],
 [("Базовий", "Масив з 7 днів тижня. Виведи перший, останній і середній (індекс 3)."),
  ("Середній", "Черга в їдальні: масив імен, хтось приходить (push), хтось отримує обід (shift). Покажи чергу після 5 дій."),
  ("Зірочка ⭐", "Перевір, чи є в масиві дублікати, без циклів (підказка: new Set(arr).size).")],
 [("Що виведе ['a','b','c'][1]?", ["a", "b", "c", "undefined"], 1, "Індекс 1 — другий."),
  ("Який метод додає елемент у кінець?", ["pop()", "push()", "add()", "shift()"], 1, "push."),
  ("Що поверне [1,2,3,4,5].slice(1, 3)?", ["[1,2,3]", "[2,3]", "[2,3,4]", "[1,2]"], 1, "З 1 до 3, не включаючи 3.")]), "arrays")

add(new("loops", "js", "Цикли: повторення без копіювання",
 "Комп'ютер не втомлюється повторювати. Цикли обробляють 5 чи 5 мільйонів елементів однаковим кодом.",
 ["використовувати цикли for, for...of, while", "рахувати суму, середнє, максимум", "керувати циклом через break і continue", "писати вкладені цикли"],
 secs("arrays", [3,4,5,6,7,8]) + [
  H("break і continue"),
  CODE("javascript", r'''
const ratings = [5, 4, 0, 3, 5, 2];

for (const r of ratings) {
  if (r === 0) continue;        // пропустити цей крок
  if (r < 3) {
    console.log('Знайшли погану оцінку, зупиняємось');
    break;                      // вийти з циклу повністю
  }
  console.log('Оцінка:', r);
}''', run=True),
  H("Пошук максимуму"),
  CODE("javascript", r'''
const scores = [72, 95, 88, 61, 99, 84];
let max = scores[0];

for (const s of scores) {
  if (s > max) max = s;
}
console.log('Найкращий результат:', max);''', run=True),
  H("Вкладені цикли"),
  CODE("javascript", r'''
for (let row = 1; row <= 3; row++) {
  let line = '';
  for (let col = 1; col <= 5; col++) {
    line += (row + col) % 2 === 0 ? '⬛' : '⬜';
  }
  console.log(line);
}''', run=True, note="Шахова дошка! Зовнішній цикл — рядки, внутрішній — клітинки в рядку."),
 ],
 "Виведи в консоль усі назви колекції з номерами (з 1), середню оцінку і назву річчі з найвищою оцінкою (поки що два окремі масиви titles і ratings з однаковим порядком).",
 ["Console: номери з 1, а не з 0", "Середня оцінка правильна — перевір на калькуляторі", "Якщо сторінка «зависла» — найімовірніше, нескінченний while. Закрий вкладку й перевір умову"],
 [("Базовий", "Виведи всі парні числа від 2 до 50."),
  ("Середній", "Масив оцінок за семестр. Знайди максимальну, мінімальну, середню і скільки 12-ок."),
  ("Зірочка ⭐", "Таблиця множення 1–9 у консоль (вкладені цикли), вирівняна по колонках (padStart).")],
 [("Скільки разів виконається for (let i = 0; i < 3; i++)?", ["2", "3", "4", "Безкінечно"], 1, "0, 1, 2."),
  ("Що робить break?", ["Пропускає крок", "Повністю виходить з циклу", "Перезапускає цикл", "Видаляє масив"], 1, "break = вихід."),
  ("Що робить continue?", ["Виходить з циклу", "Пропускає решту поточного кроку й переходить до наступного", "Зупиняє програму", "Нічого"], 1, "continue = пропуск кроку.")]), "loops")

add(src("func"), "func")

add(new("objects", "js", "Об'єкти: опис однієї речі",
 "Об'єкт збирає всі властивості однієї речі в одному місці. А масив об'єктів — це вже таблиця даних.",
 ["створювати об'єкти й звертатися до властивостей", "змінювати, додавати й видаляти властивості", "працювати з вкладеними об'єктами й масивами", "зберігати колекцію як масив об'єктів"],
 secs("objects", [0,1,2,3,4]) + [
  H("Вкладені дані"),
  CODE("javascript", r'''
const book = {
  title: 'Тигролови',
  author: { name: 'Іван Багряний', born: 1906 },
  genres: ['пригоди', 'роман'],
  rating: 5
};

console.log(book.author.name);     // об'єкт в об'єкті
console.log(book.genres[0]);       // масив в об'єкті
console.log(Object.keys(book));    // список усіх ключів
delete book.rating;                // видалити властивість
console.log('rating' in book);     // чи є така властивість? false''', run=True),
  TRY(r'''<script>
  const me = {
    name: 'Твоє імʼя',
    grade: 8,
    hobbies: ['ігри', 'музика']
  };
  // 1. Додай властивість city
  // 2. Додай ще одне хобі через push
  // 3. Виведи: "Я Олекса з 8 класу, люблю ігри, музика"
  console.log(me);
</script>''', "Опиши себе об'єктом"),
 ],
 "Створи <code>js/data.js</code> з масивом <code>items</code>: 6–8 об'єктів з полями <code>id, title, author, category, rating, review</code>. Підключи його <b>перед</b> app.js і виведи <code>console.table(items)</code>.",
 ["Console: <code>console.table</code> показує гарну таблицю", "Напиши в Console <code>items[0].title</code>", "Якщо <code>items is not defined</code> — перевір порядок підключення скриптів"],
 [("Базовий", "Об'єкт «Мій телефон/комп'ютер» з 6 властивостями, виведи кожну окремо."),
  ("Середній", "Масив 5 учнів <code>{name, grade, scores: [..]}</code>. Для кожного виведи середній бал."),
  ("Зірочка ⭐", "Дізнайся про <code>Object.entries</code> і виведи всі властивості об'єкта у форматі «ключ: значення» циклом.")],
 [("Як отримати title з об'єкта game?", ["game(title)", "game.title", "game->title", "title.game"], 1, "Через крапку."),
  ("Що виведе book.author.name?", ["Помилку", "Значення name з вкладеного об'єкта author", "undefined завжди", "author"], 1, "Ланцюжок крапок."),
  ("Що описує масив об'єктів?", ["Одну річ", "Колекцію схожих речей — як таблиця", "Функцію", "Рядок"], 1, "Рядки таблиці.")]), "objects")

add(new("array-methods", "js", "Методи масивів і JSON",
 "filter, map, find, sort, reduce — п'ять суперсил для роботи з даними. Плюс JSON — мова, якою говорять сервери.",
 ["відбирати дані через filter", "перетворювати через map", "знаходити через find, сортувати через sort", "рахувати через reduce", "читати й писати JSON"],
 secs("objects", [5,6,7]) + [
  H("reduce: згорнути масив в одне значення"),
  CODE("javascript", r'''
const items = [
  { title: 'Minecraft', rating: 5 },
  { title: 'Кобзар', rating: 5 },
  { title: 'Мавка', rating: 4 }
];

const sum = items.reduce((total, item) => total + item.rating, 0);
console.log('Сума:', sum, 'Середня:', (sum / items.length).toFixed(1));''', run=True, note="<code>total</code> — «накопичувач», 0 — його початкове значення."),
  H("Ланцюжки методів"),
  CODE("javascript", r'''
const items = [
  { title: 'Minecraft', category: 'гра', rating: 5 },
  { title: 'Terraria', category: 'гра', rating: 4 },
  { title: 'Portal 2', category: 'гра', rating: 3 },
  { title: 'Кобзар', category: 'книга', rating: 5 }
];

const bestGames = items
  .filter(i => i.category === 'гра')      // лише ігри
  .filter(i => i.rating >= 4)             // з оцінкою 4+
  .map(i => i.title);                     // лише назви

console.log(bestGames);''', run=True),
  secs("objects", [8,9])[0], secs("objects", [8,9])[1],
  CODE("javascript", r'''
const items = [{ title: 'Minecraft', rating: 5 }];

const text = JSON.stringify(items);   // масив → текст
console.log(typeof text, text);

const back = JSON.parse(text);        // текст → масив
console.log(back[0].title);''', run=True),
 ],
 "У app.js виведи: кількість речей кожної категорії (filter), список назв великими літерами (map), найкращу річ (sort), середню оцінку (reduce).",
 ["Console: усі 4 результати правильні", "Перевір, що sort не зіпсував оригінальний порядок (копія через [...items])", "Спробуй у Console: <code>JSON.stringify(items, null, 2)</code>"],
 [("Базовий", "Масив товарів. Знайди всі дешевші за 100 грн і виведи їх назви."),
  ("Середній", "Масив учнів з оцінками. Відсортуй за середнім балом і виведи рейтинг класу."),
  ("Зірочка ⭐", "Через reduce згрупуй речі за категоріями: <code>{ гра: [...], книга: [...] }</code>.")],
 [("Що поверне filter?", ["Один елемент", "Новий масив з тих, що пройшли перевірку", "Число", "true/false"], 1, "Завжди масив."),
  ("Що поверне [1,2,3].reduce((s, n) => s + n, 0)?", ["[1,2,3]", "6", "0", "123"], 1, "Сума."),
  ("Що робить JSON.parse?", ["Масив → текст", "Текст JSON → об'єкт/масив", "Видаляє JSON", "Відправляє на сервер"], 1, "parse = розібрати текст.")]), "array-methods")

add(src("dom"), "dom")

add(new("events", "js", "Події: сторінка реагує на людину",
 "Кліки, наведення, клавіатура. Вчимося слухати події й реагувати на них.",
 ["підписуватися на події через addEventListener", "використовувати об'єкт події event", "обробляти click, input, keydown", "перемикати класи через classList.toggle"],
 secs("events", [0,1,2,3,4]) + [
  H("Клавіатура"),
  CODE("html", r'''
<p>Натисни будь-яку клавішу (спочатку клацни сюди)</p>
<h2 id="key">—</h2>
<script>
  document.addEventListener('keydown', (e) => {
    document.querySelector('#key').textContent = `Ти натиснув: ${e.key}`;
    if (e.key === 'Enter') console.log('Enter! 🚀');
  });
</script>''', run=True),
  H("Об'єкт події"),
  P("Обробник отримує параметр <code>event</code> (часто пишуть <code>e</code>) з деталями: <code>e.target</code> — елемент, на якому сталась подія; <code>e.key</code> — клавіша; <code>e.clientX</code> — координати мишки."),
  TRY(r'''<style>
  .box { width: 120px; height: 120px; background: #2f6feb; border-radius: 16px; transition: .3s; }
  .box.active { background: #f0622e; transform: rotate(45deg) scale(.8); }
</style>
<div class="box" id="box"></div>
<script>
  document.querySelector('#box').addEventListener('click', (e) => {
    e.target.classList.toggle('active');
    // додай: console.log з кількістю кліків
  });
</script>''', "Клацни по квадрату"),
 ],
 "Додай у шапку кнопку перемикання темної теми (classList.toggle). Додай до карток ефект: клік по картці додає їй клас <code>.selected</code> з рамкою.",
 ["Elements → обери кнопку → вкладка <b>Event Listeners</b>: видно твій click", "Клас з'являється/зникає в Elements при кліку", "Console без помилок"],
 [("Базовий", "Лічильник з кнопками +1, −1, скинути. Не менше 0."),
  ("Середній", "Гра «Клікер»: кнопка-печиво, лічильник, кожні 10 кліків — нове досягнення."),
  ("Зірочка ⭐", "Керуй квадратом стрілками клавіатури (keydown + style.left/top).")],
 [("Що робить classList.toggle('dark')?", ["Завжди додає клас", "Додає клас, якщо нема, і прибирає, якщо є", "Видаляє елемент", "Міняє колір"], 1, "Перемикач."),
  ("Що таке e.target?", ["Ціль сайту", "Елемент, на якому сталася подія", "Клавіша", "Помилка"], 1, "Де сталося."),
  ("Яка подія для натискання клавіші?", ["click", "keydown", "input", "change"], 1, "keydown.")]), "events")

add(new("forms-js", "js", "Форми та перевірка даних",
 "Читаємо дані з форми, перевіряємо їх і показуємо зрозумілі помилки. Форма полиці оживає!",
 ["обробляти submit без перезавантаження", "читати значення полів і перетворювати типи", "перевіряти дані й показувати помилки", "очищати форму після відправки"],
 secs("events", [5,6,7]) + [
  H("Перевірка даних (валідація)"),
  CODE("html", r'''
<style>
  .error { color: #e5484d; font-size: 14px; min-height: 18px; }
  input.bad { border: 2px solid #e5484d; }
</style>
<form id="f">
  <input id="title" placeholder="Назва гри">
  <p class="error" id="err"></p>
  <button>Додати</button>
</form>
<script>
  document.querySelector('#f').addEventListener('submit', (e) => {
    e.preventDefault();
    const input = document.querySelector('#title');
    const err = document.querySelector('#err');
    const title = input.value.trim();          // прибрати пробіли по краях

    if (title.length < 2) {
      err.textContent = 'Назва має бути мінімум 2 символи';
      input.classList.add('bad');
      return;                                   // зупинити
    }
    err.textContent = '';
    input.classList.remove('bad');
    console.log('✅ Додано:', title);
    e.target.reset();
  });
</script>''', run=True, note="Спробуй відправити порожнє поле, пробіли або одну літеру."),
  TIP("HTML-перевірки (<code>required</code>, <code>min</code>) — для зручності. JS-перевірки — для гарних повідомлень. А справжній захист — лише на сервері (дізнаємось в уроці ⟦express⟧)."),
  secs("events", [8])[0],
 ],
 "«Оживи» форму «Додати на полицю»: при submit — <code>preventDefault</code>, зібрати об'єкт з усіх полів (rating через Number), перевірити назву й показати помилку під полем, вивести об'єкт у консоль.",
 ["Сторінка НЕ перезавантажується", "Console: rating — число (синім), а не рядок (в лапках)", "Порожня назва або пробіли — показується помилка"],
 [("Базовий", "Форма реєстрації: ім'я (мін. 2 символи), вік (10–18). Помилки під полями."),
  ("Середній", "Перевірка пароля наживо (подія input): показуй ✅/❌ для довжини, цифри, великої літери."),
  ("Зірочка ⭐", "Гра «Вгадай число»: форма з полем, комп'ютер каже «більше/менше» і рахує спроби.")],
 [("Що робить event.preventDefault() у submit?", ["Видаляє форму", "Скасовує перезавантаження сторінки", "Відправляє дані", "Очищає поля"], 1, "Стандартна дія скасована."),
  ("Що поверне input.value, якщо там 5?", ["Число 5", "Рядок '5'", "true", "undefined"], 1, "value — завжди рядок."),
  ("Навіщо .trim()?", ["Робить великі літери", "Прибирає пробіли на початку й в кінці", "Обрізає до 10 символів", "Видаляє текст"], 1, "Щоб «   » не вважалось назвою.")]), "forms-js")

add(src("shelf"), "shelf")

add(new("debug", "js", "Налагодження: як шукати й виправляти помилки",
 "Помилки бувають у всіх, навіть у професіоналів. Різниця в тому, що професіонал знає, як їх швидко знайти.",
 ["розрізняти синтаксичні, runtime- і логічні помилки", "читати повідомлення про помилки", "використовувати console.log, console.table і точки зупинки", "діяти за алгоритмом пошуку бага"],
 [
  H("Три види помилок"),
  TABLE(["Вид", "Що це", "Приклад", "Як помітити"], [
    ["<b>Синтаксична</b>", "Код написано неправильно — JS не може його прочитати", "Пропущена дужка", "Червона помилка одразу, нічого не працює"],
    ["<b>Runtime</b>", "Код правильний, але падає під час роботи", "Звернення до null", "Червона помилка, коли доходить до рядка"],
    ["<b>Логічна</b>", "Працює без помилок, але результат неправильний", "Середня рахується з помилкою", "Немає червоного! Лише неправильний результат"]]),
  H("Читаємо помилку"),
  CODE("text", r'''
Uncaught TypeError: Cannot read properties of null (reading 'addEventListener')
    at app.js:12:27
   ↑ тип     ↑ що сталося                          ↑ файл:рядок:символ''', title="Console"),
  TABLE(["Помилка", "Переклад", "Що перевірити"], [
    ["<code>X is not defined</code>", "Змінну/функцію X не знайдено", "Друкарська помилка, регістр, порядок скриптів"],
    ["<code>Cannot read properties of null</code>", "Звертаєшся до елемента, якого нема", "Селектор у querySelector, defer"],
    ["<code>Cannot read properties of undefined</code>", "Звертаєшся до властивості того, чого нема", "Індекс масиву, назва властивості"],
    ["<code>Unexpected token</code>", "Неочікуваний символ", "Дужки, лапки, коми"],
    ["<code>X is not a function</code>", "Викликаєш як функцію те, що нею не є", "Назва методу (push, не puhs)"],
    ["<code>Assignment to constant variable</code>", "Змінюєш const", "Заміни на let"]]),
  H("Знайди баг"),
  CODE("javascript", r'''
const ratings = [5, 4, 3];
let sum = 0;
for (let i = 0; i <= ratings.length; i++) {
  sum += ratings[i];
}
console.log('Середня:', sum / ratings.length);   // NaN?! чому?''', run=True, note="Підказка: скільки разів виконується цикл? Що таке ratings[3]? Додай console.log(i, ratings[i]) всередину циклу."),
  H("Точки зупинки (breakpoints)"),
  STEPS(["F12 → вкладка <b>Sources</b> → зліва відкрий <code>app.js</code>.",
         "Клацни на номер рядка — з'явиться синя мітка. Це точка зупинки.",
         "Зроби дію на сторінці (клік, оновлення). Програма зупиниться на цьому рядку!",
         "Наведи мишку на будь-яку змінну — побачиш її значення. Справа — панель <b>Scope</b> з усіма змінними.",
         "Кнопки вгорі: ▶ продовжити, ⤵ наступний рядок. Йди крок за кроком і дивись, де значення стає неправильним."]),
  TIP("Замість кліку на рядок можна написати в коді <code>debugger;</code> — з відкритими DevTools програма зупиниться там."),
  H("Алгоритм пошуку бага"),
  STEPS(["<b>Відтвори.</b> Що саме треба зробити, щоб помилка з'явилась?", "<b>Читай Console.</b> Є червоне? Клацни на рядок.", "<b>Звузь.</b> Додавай <code>console.log</code> у ключові місця: до якого моменту все правильно?", "<b>Перевір припущення.</b> Ти думаєш, що там число? Перевір <code>typeof</code>.", "<b>Поясни качці 🦆.</b> Розкажи код уголос рядок за рядком.", "<b>Виправ і перевір знову.</b> А заодно — чи не зламалось щось інше?"]),
 ],
 "Влаштуй «полювання на баги» у своїй полиці: попроси сусіда навмисно зламати 3 речі в твоєму app.js (поки ти не дивишся). Знайди й виправ усі, записуючи в коментарях, як знайшов.",
 ["Постав breakpoint у функції render() і пройди її крок за кроком", "Спробуй <code>console.table(items)</code> і <code>console.error('тест')</code>", "Після виправлень Console чиста"],
 [("Базовий", "Виправ 5 помилок у коді, який дасть учитель (або знайди баги в прикладі «Знайди баг» вище)."),
  ("Середній", "Опиши в README.md три найчастіші свої помилки за курс і як ти їх тепер знаходиш."),
  ("Зірочка ⭐", "Дізнайся про <b>умовні точки зупинки</b> (правий клік на номер рядка → Add conditional breakpoint) і використай для пошуку конкретного елемента в циклі.")],
 [("Код працює без червоних помилок, але середня оцінка неправильна. Що це за помилка?", ["Синтаксична", "Runtime", "Логічна", "Мережева"], 2, "Логічні помилки не видно в Console."),
  ("Що означає «X is not defined»?", ["X дорівнює 0", "Змінну або функцію X не оголошено (або написано інакше)", "X — порожній рядок", "Немає інтернету"], 1, "Перевір назву й регістр."),
  ("Що робить точка зупинки?", ["Видаляє рядок", "Ставить програму на паузу на цьому рядку, щоб подивитися значення", "Прискорює код", "Виправляє помилку"], 1, "Breakpoint = пауза.")]), "debug")

# ───── Дані (29–33)
add(src("sql"), "sql")

add(new("sql2", "db", "SQL-практикум: підрахунки, пошук і зв'язки",
 "Вчимося ставити базі складні питання: скільки, яка середня, хто найкращий, і як з'єднати дві таблиці.",
 ["рахувати через count, avg, sum, max, min", "групувати через group by", "шукати за шаблоном через like", "пов'язувати таблиці через зовнішній ключ і join"],
 [
  H("Підрахунки (агрегатні функції)"),
  CODE("sql", r'''
select count(*) from items;                      -- скільки всього
select avg(rating) from items;                   -- середня оцінка
select max(rating), min(rating) from items;      -- найкраща й найгірша

-- скільки ігор з оцінкою 5?
select count(*) from items where category = 'гра' and rating = 5;'''),
  H("Групування"),
  CODE("sql", r'''
-- скільки речей і яка середня оцінка в кожній категорії
select category, count(*) as total, round(avg(rating), 1) as avg_rating
from items
group by category
order by total desc;''', note="<code>as</code> дає стовпцю зрозумілу назву. Результат — маленька таблиця: категорія | total | avg_rating."),
  H("Пошук за шаблоном і обмеження"),
  CODE("sql", r'''
-- назви, що містять «craft» (без різниці великі/малі літери)
select * from items where title ilike '%craft%';

-- топ-3 найновіших
select title, created_at from items order by created_at desc limit 3;'''),
  H("Дві таблиці: відгуки до речей"),
  P("Одна гра може мати багато відгуків від різних людей. Тримати їх усі в одному рядку незручно, тому робимо <b>другу таблицю</b> і зв'язуємо через <b>зовнішній ключ</b> (foreign key):"),
  CODE("sql", r'''
create table reviews (
  id bigint generated always as identity primary key,
  item_id bigint references items(id) on delete cascade,   -- зв'язок!
  author text not null,
  text text,
  stars int check (stars between 1 and 5)
);

insert into reviews (item_id, author, text, stars) values
  (1, 'Марія', 'Найкраща гра для творчості', 5),
  (1, 'Богдан', 'Трохи нудно самому', 4);

-- JOIN: показати відгуки разом з назвою гри
select items.title, reviews.author, reviews.stars
from reviews
join items on items.id = reviews.item_id;''', title="SQL Editor"),
  FIG(TABLEFIG, "Таблиця items. Кожен відгук у reviews «посилається» на рядок звідси через item_id."),
  TIP("<code>on delete cascade</code>: якщо видалити гру, її відгуки видаляться автоматично. Без цього база не дасть видалити гру, на яку є посилання."),
 ],
 "У своїй базі напиши й збережи в <code>sql/queries.sql</code> 6 запитів: кількість, середня, групування за категоріями, пошук за шаблоном, топ-3, і створи таблицю <code>reviews</code> з 5+ відгуками та join-запитом.",
 ["Supabase → Table Editor: таблиця reviews має стрілку-зв'язок з items", "Спробуй додати відгук з item_id = 9999: база має відмовити", "Кожен запит у файлі має коментар-пояснення"],
 [("Базовий", "SQLBolt: уроки 7–12."),
  ("Середній", "Запит: середня оцінка кожної гри за відгуками (join + group by)."),
  ("Зірочка ⭐", "Спроєктуй базу для шкільної бібліотеки з 3 таблиць (книги, учні, видачі). Намалюй зв'язки і напиши create table.")],
 [("Що поверне select count(*) from items?", ["Усі записи", "Кількість записів", "Перший запис", "Назви стовпців"], 1, "count = скільки."),
  ("Навіщо group by category?", ["Відсортувати", "Порахувати окремо для кожної категорії", "Видалити дублікати", "Створити категорію"], 1, "Групування."),
  ("Що таке зовнішній ключ?", ["Пароль", "Поле, що посилається на id в іншій таблиці", "Перший стовпець", "Ключ API"], 1, "Зв'язок між таблицями.")]), "sql2")

add(src("fetch"), "fetch")
add(src("express"), "express")
add(src("supa"), "supa")

# ───── Git, AI і фінал (34–38)
add(new("git", "ai", "Git і GitHub: історія коду й командна робота",
 "Машина часу для коду, синхронізація школа ↔ дім і робота в команді. Інструмент, яким користується кожен програміст у світі.",
 ["пояснити, що таке репозиторій, коміт, push і pull", "працювати з GitHub Desktop або з терміналу", "писати гарні повідомлення комітів", "використовувати .gitignore і README"],
 [
  H("Навіщо Git"),
  CARDS([("⏪", "Машина часу", "Зламав щось? Повертаєшся до будь-якої попередньої версії."),
         ("🏠", "Школа ↔ дім", "Один репозиторій на GitHub, з якого працюєш з будь-якого комп'ютера."),
         ("👥", "Команда", "Кілька людей працюють над одним проєктом і не затирають роботу одне одного.")]),
  H("Основні поняття"),
  CODE("text", r'''
  твоя папка          Git (локально)           GitHub (хмара)
  ──────────          ──────────────           ──────────────
  змінив файли  ──→   commit (знімок)   ──→    push (надіслати)
                                        ←──    pull (забрати)''', title="Шлях змін"),
  H("Варіант 1: GitHub Desktop (кнопками)"),
  STEPS(["Встанови <a href='https://desktop.github.com' target='_blank'>GitHub Desktop</a>, увійди в GitHub.", "<b>File → Add local repository</b> → обери папку полиці → якщо пропонує, <b>create a repository</b>.", "Змінені файли видно зліва. Внизу напиши повідомлення («Додав пошук») → <b>Commit to main</b>.", "<b>Publish repository</b> (перший раз) або <b>Push origin</b>.", "Вдома: <b>File → Clone repository</b>. Далі щоразу перед роботою: <b>Fetch → Pull</b>."]),
  H("Варіант 2: термінал"),
  CODE("bash", r'''
git init                          # почати стежити за папкою
git add .                         # підготувати всі зміни
git commit -m "Додав пошук"       # зробити знімок
git log --oneline                 # історія комітів

git remote add origin https://github.com/логін/polytsia.git
git push -u origin main           # надіслати на GitHub (перший раз)
git push                          # далі — просто так
git pull                          # забрати зміни з GitHub''', title="Термінал VS Code"),
  TIP("У VS Code є вкладка <b>Source Control</b> (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>G</kbd>): ті самі коміти й push кнопками, не виходячи з редактора."),
  H("Гарний коміт"),
  TABLE(["❌ Погано", "✅ Добре"], [["«fix»", "«Виправив пошук: тепер не залежить від регістру»"], ["«asdf»", "«Додав темну тему»"], ["«зміни» (50 файлів)", "Маленькі коміти: одна зміна — один коміт"]]),
  H(".gitignore і README"),
  CODE("text", r'''
node_modules/
.env
.DS_Store''', title=".gitignore — що НЕ завантажувати", note="<code>node_modules</code> — тисячі файлів бібліотек (їх можна встановити знову через npm install). <code>.env</code> — секрети. Вони ніколи не мають потрапити на GitHub!"),
  CODE("text", r'''
# 📚 Полиця Олекси
Моя колекція улюблених ігор з оцінками й пошуком.

**Сайт:** https://логін.github.io/polytsia
**Технології:** HTML, CSS, JavaScript, Supabase

![Скріншот](images/screenshot.png)''', title="README.md"),
  WARN("Публічний репозиторій бачить увесь світ. Перед push перевір: жодних паролів, secret key, особистих даних."),
 ],
 "Створи репозиторій полиці на GitHub, додай <code>.gitignore</code> і <code>README.md</code>. Зроби мінімум 3 осмислені коміти. Склонуй репозиторій вдома (або на іншому комп'ютері) і зроби звідти ще один коміт.",
 ["GitHub → вкладка <b>Commits</b>: видно всі коміти з повідомленнями", "Клацни на коміт — зеленим додане, червоним видалене", "На GitHub нема папки node_modules і файлу .env"],
 [("Базовий", "Пройди перші 2 розділи <a href='https://learngitbranching.js.org/?locale=uk' target='_blank'>Learn Git Branching</a> (є українською)."),
  ("Середній", "Поверни один файл до попередньої версії через історію (GitHub Desktop → History → правий клік → Revert)."),
  ("Зірочка ⭐", "Попрацюйте в парі в одному репозиторії: кожен створює гілку (branch), робить зміни і відкриває Pull Request.")],
 [("Що таке коміт?", ["Файл", "Збережений знімок змін з описом", "Сайт", "Помилка"], 1, "Commit — знімок."),
  ("Що робить git push?", ["Забирає зміни з GitHub", "Надсилає коміти на GitHub", "Видаляє репозиторій", "Створює файл"], 1, "Push = надіслати."),
  ("Що має бути в .gitignore?", ["index.html", "node_modules і .env", "README.md", "style.css"], 1, "Бібліотеки й секрети.")]), "git")

add(src("ai"), "ai")

add(new("ai-practice", "ai", "Практикум з AI: дебаг, рев'ю, нова функція",
 "Практичний урок: використовуємо AI як професіонали — для пошуку помилок, рефакторингу, тестових даних і нових можливостей полиці.",
 ["описувати помилку так, щоб AI швидко допоміг", "просити рев'ю без готового рішення", "генерувати тестові дані", "додавати функцію разом з AI, розуміючи кожен рядок"],
 [
  H("Станції практикуму"),
  P("Клас ділиться на пари. Кожна пара проходить 4 станції по 10 хвилин на своєму проєкті. На кожній станції — завдання, шаблон промпту і критерій «зараховано»."),
  CARDS([("🐞", "Станція 1: Дебаг", "Сусід навмисно ламає твій код. Ти копіюєш помилку з Console + шматок коду в AI і просиш пояснити причину, а не просто виправити."),
         ("🔍", "Станція 2: Рев'ю", "AI шукає 3 слабкі місця в app.js, але НЕ переписує код. Ти обираєш одне й виправляєш сам."),
         ("🎲", "Станція 3: Дані", "AI генерує SQL insert на 20 реалістичних записів для твоєї теми. Ти перевіряєш і запускаєш у Supabase."),
         ("✨", "Станція 4: Нова функція", "Разом з AI додаєш одну функцію: сортування, статистику, «випадкова річ» чи пошук за автором.")]),
  H("Шаблони промптів"),
  CODE("text", r'''
🐞 ДЕБАГ
Я вчу JavaScript. Мій сайт-каталог видає помилку:
[встав помилку з Console]
Ось код навколо рядка з помилкою:
[код]
Поясни простими словами, ЧОМУ виникає помилка.
Не давай виправлений код — я спробую сам.

🔍 РЕВ'Ю
Ось мій app.js (учнівський проєкт, рівень: DOM, події, fetch).
Знайди 3 місця, які можна покращити (читабельність, повтори, безпека).
Для кожного: що не так і чому, без готового коду.

🎲 ДАНІ
Згенеруй SQL insert для таблиці items (title, author, category, rating, review)
на 20 [книг / ігор / фільмів], переважно українських. category лише:
'гра', 'книга', 'фільм'. rating від 1 до 5. Відгуки короткі, як писав би підліток.

✨ ФУНКЦІЯ
Хочу додати [опис]. Ось мій render() і масив items: [код].
Дай план у 3–4 кроки. Потім код лише для кроку 1 з поясненням кожного рядка.''', title="Скопіюй і заповни"),
  H("Критерій «зараховано» на кожній станції"),
  LIST(["Ти можеш пояснити вчителю, що змінилось і чому, <b>без підглядання</b> в чат.", "Код працює, Console чиста.", "У <code>AI-LOG.md</code> є запис: промпт → що відповів AI → що ти прийняв, що відхилив і чому."]),
  IDEA("Помітив, що AI помилився? Це не провал, а найкращий момент уроку! Запиши в AI-LOG.md: що AI сказав, як ти зрозумів, що це неправда, і як знайшов правильну відповідь."),
  WARN("Тестові дані від AI перевіряй: AI може вигадати книгу, якої не існує, або неправильного автора. Для навчального проєкту це не страшно, але для справжнього — критично."),
 ],
 "Пройди 4 станції, впровадь результати в полицю і заповни AI-LOG.md (мінімум 4 записи). Зроби коміт «AI-практикум».",
 ["Нова функція працює й не зламала старі", "Тестові дані з'явились у Supabase, а на сайті 20+ карток", "Console чиста"],
 [("Обов'язково", "Заверши станції, які не встиг на уроці."),
  ("Середній", "Попроси AI пояснити один складний для тебе рядок з уроку ⟦supa⟧ трьома різними способами (для 10-річного, через аналогію, технічно). Який зрозуміліший?"),
  ("Зірочка ⭐", "Додай з AI другу функцію, але цього разу спочатку напиши свій план, а AI попроси лише оцінити його.")],
 [("Як правильно просити AI допомогти з помилкою?", ["«не працює»", "Помилка з Console + код + прохання пояснити причину", "Надіслати весь проєкт без слів", "«виправ усе»"], 1, "Контекст + конкретика."),
  ("Що робити з тестовими даними від AI?", ["Одразу в продакшн", "Перевірити: AI може вигадати неіснуючі факти", "Видалити", "Нічого"], 1, "Галюцинації можливі."),
  ("Що означає «зараховано» на станції?", ["AI написав код", "Ти можеш пояснити зміни без підглядання, і все працює", "Код довгий", "Вчитель не помітив"], 1, "Розуміння — головне.")], mins=90), "ai-practice")

add(src("agents"), "agents")
add(src("final"), "final")

assert len(L) == 38, len(L)
for i, l in enumerate(L, 1): l["n"] = i
