from helpers import *
from svgs import *

DEMO = r'''<!DOCTYPE html>
<html lang="uk">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Полиця Олекси</title>
<style>
  :root { --bg:#fbf8f3; --card:#fff; --text:#1d1b26; --muted:#6b6878; --accent:#f0622e; --radius:16px; }
  body.dark { --bg:#16151c; --card:#22212b; --text:#f3f0ea; --muted:#a8a4b4; }
  * { box-sizing: border-box; }
  body { margin:0; font-family: system-ui, sans-serif; background:var(--bg); color:var(--text); transition:.3s; }
  header { display:flex; justify-content:space-between; align-items:center; padding:14px 20px; background:var(--text); color:var(--bg); }
  header strong { font-size:20px; }
  header button { background:none; border:2px solid var(--bg); color:var(--bg); border-radius:99px; padding:6px 12px; cursor:pointer; }
  main { max-width:900px; margin:0 auto; padding:20px; }
  .tools { display:flex; gap:10px; flex-wrap:wrap; margin-bottom:8px; }
  .tools input, .tools select, form input, form select { padding:10px 12px; border-radius:10px; border:2px solid #d9d3c7; font:inherit; background:var(--card); color:var(--text); }
  .tools input { flex:1; min-width:180px; }
  #count { color:var(--muted); font-size:14px; }
  .cards { display:grid; grid-template-columns:repeat(auto-fill, minmax(190px, 1fr)); gap:16px; }
  .card { position:relative; background:var(--card); border-radius:var(--radius); padding:16px; box-shadow:0 6px 18px rgba(0,0,0,.08); transition:transform .2s, box-shadow .2s; }
  .card:hover { transform:translateY(-5px) rotate(-1deg); box-shadow:0 14px 28px rgba(0,0,0,.14); }
  .cover { height:90px; border-radius:10px; display:grid; place-items:center; font-size:42px; margin-bottom:10px; }
  .tag { font-size:12px; background:var(--accent); color:#fff; padding:2px 9px; border-radius:99px; }
  .card h3 { margin:10px 0 2px; font-size:17px; }
  .card p { margin:0; color:var(--muted); font-size:14px; }
  .stars { color:#e8a400 !important; letter-spacing:2px; margin-top:6px !important; }
  .del { position:absolute; top:10px; right:10px; border:none; background:none; cursor:pointer; opacity:.4; font-size:16px; }
  .del:hover { opacity:1; }
  form { display:flex; flex-wrap:wrap; gap:10px; margin-top:28px; padding:16px; background:var(--card); border-radius:var(--radius); }
  form input { flex:1; min-width:140px; }
  form button { background:var(--accent); color:#fff; border:none; border-radius:10px; padding:10px 18px; font-weight:700; cursor:pointer; }
</style>
</head>
<body>
<header>
  <strong>📚 Полиця Олекси</strong>
  <button id="theme">🌙</button>
</header>
<main>
  <div class="tools">
    <input id="search" placeholder="🔍 Пошук...">
    <select id="filter"><option>усі</option><option>гра</option><option>книга</option><option>фільм</option></select>
  </div>
  <p id="count"></p>
  <div class="cards" id="cards"></div>

  <form id="add-form">
    <input id="title" placeholder="Назва" required>
    <input id="author" placeholder="Автор / студія">
    <select id="category"><option>гра</option><option>книга</option><option>фільм</option></select>
    <select id="rating"><option value="5">★★★★★</option><option value="4">★★★★</option><option value="3">★★★</option><option value="2">★★</option><option value="1">★</option></select>
    <button>Додати</button>
  </form>
</main>
<script>
  const icons = { 'гра': '🎮', 'книга': '📖', 'фільм': '🎬' };
  const colors = { 'гра': '#DCE8FF', 'книга': '#FFE3D6', 'фільм': '#D7F5E3' };
  let items = [
    { id: 1, title: 'Minecraft', author: 'Mojang', category: 'гра', rating: 5 },
    { id: 2, title: 'Кобзар', author: 'Т. Шевченко', category: 'книга', rating: 5 },
    { id: 3, title: 'Мавка. Лісова пісня', author: 'Animagrad', category: 'фільм', rating: 4 },
    { id: 4, title: 'Stardew Valley', author: 'ConcernedApe', category: 'гра', rating: 5 },
    { id: 5, title: 'Тигролови', author: 'І. Багряний', category: 'книга', rating: 4 },
    { id: 6, title: 'S.T.A.L.K.E.R. 2', author: 'GSC Game World', category: 'гра', rating: 4 }
  ];

  const $ = (s) => document.querySelector(s);
  const stars = (n) => '★'.repeat(n) + '☆'.repeat(5 - n);

  function render() {
    const q = $('#search').value.toLowerCase();
    const cat = $('#filter').value;
    const visible = items
      .filter(i => i.title.toLowerCase().includes(q))
      .filter(i => cat === 'усі' || i.category === cat);
    $('#count').textContent = `Показано ${visible.length} з ${items.length}`;
    $('#cards').innerHTML = visible.map(i => `
      <article class="card">
        <button class="del" data-id="${i.id}" title="Видалити">✕</button>
        <div class="cover" style="background:${colors[i.category]}">${icons[i.category]}</div>
        <span class="tag">${i.category}</span>
        <h3>${i.title}</h3>
        <p>${i.author}</p>
        <p class="stars">${stars(i.rating)}</p>
      </article>`).join('') || '<p>Нічого не знайдено 🤷</p>';
  }

  $('#search').addEventListener('input', render);
  $('#filter').addEventListener('change', render);
  $('#theme').addEventListener('click', (e) => {
    document.body.classList.toggle('dark');
    e.target.textContent = document.body.classList.contains('dark') ? '☀️' : '🌙';
  });
  $('#add-form').addEventListener('submit', (e) => {
    e.preventDefault();
    items.unshift({ id: Date.now(), title: $('#title').value, author: $('#author').value || '—',
      category: $('#category').value, rating: Number($('#rating').value) });
    e.target.reset();
    render();
  });
  $('#cards').addEventListener('click', (e) => {
    if (!e.target.classList.contains('del')) return;
    items = items.filter(i => i.id !== Number(e.target.dataset.id));
    render();
  });
  render();
</script>
</body>
</html>'''

PAGES = {}

PAGES["tools"] = {"title": "Де працювати і як усе налаштувати", "sub": "Однакове середовище в школі й удома. Усе безкоштовне.", "sections": [
  H("Короткий список"),
  TABLE(["Інструмент", "Для чого", "Коли знадобиться"], [
    ["<b>VS Code</b> + Live Server", "Редактор коду + автооновлення сторінки", "З уроку 1"],
    ["<b>Chrome</b> / Edge / Firefox", "Перегляд і перевірка сторінки (DevTools)", "З уроку 1"],
    ["<b>GitHub</b>", "Зберігання коду, синхронізація школа ↔ дім, публікація сайту", "Бажано з уроку 1, обов'язково з уроку ⟦agents⟧"],
    ["<b>Node.js</b> (LTS)", "Запуск власного сервера", "Урок ⟦express⟧"],
    ["<b>Supabase</b>", "Хмарна база даних", "Уроки ⟦sql⟧, ⟦supa⟧"],
    ["<b>AI-асистент</b>", "Помічник: пояснення, пошук помилок", "Уроки ⟦ai⟧–⟦agents⟧"]]),
  H("1. VS Code — головний редактор"),
  STEPS(["Завантаж з <a href='https://code.visualstudio.com' target='_blank'>code.visualstudio.com</a> (Windows, macOS, Linux) і встанови з галочками за замовчуванням. На Windows додатково постав <b>«Add to PATH»</b> і <b>«Open with Code»</b>.",
         "Відкрий вкладку <b>Extensions</b> (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>X</kbd>) і встанови розширення: <b>Live Server</b> (Ritwick Dey), <b>Prettier</b> (форматує код), <b>Error Lens</b> (показує помилки прямо в рядку), за бажанням <b>Ukrainian Language Pack</b>.",
         "<b>File → Preferences → Settings</b> → знайди <i>Auto Save</i> → <code>afterDelay</code>. Тепер файли зберігаються самі.",
         "Там же знайди <i>Format On Save</i> і увімкни, а <i>Default Formatter</i> → Prettier. Код завжди буде охайним.",
         "Перевірка: створи папку, файл <code>index.html</code>, напиши <code>!</code> + <kbd>Tab</kbd>, потім правий клік → <b>Open with Live Server</b>. Відкрилось у браузері за адресою <code>127.0.0.1:5500</code>? Готово ✅"]),
  TABLE(["Гаряча клавіша", "Дія"], [
    ["<kbd>Ctrl</kbd>+<kbd>S</kbd>", "Зберегти"], ["<kbd>Ctrl</kbd>+<kbd>/</kbd>", "Закоментувати рядок"],
    ["<kbd>Alt</kbd>+<kbd>↑/↓</kbd>", "Перемістити рядок"], ["<kbd>Shift</kbd>+<kbd>Alt</kbd>+<kbd>↓</kbd>", "Дублювати рядок"],
    ["<kbd>Ctrl</kbd>+<kbd>D</kbd>", "Виділити наступне таке саме слово (мультикурсор)"], ["<kbd>Ctrl</kbd>+<kbd>`</kbd>", "Відкрити термінал"],
    ["<kbd>Ctrl</kbd>+<kbd>P</kbd>", "Швидко відкрити файл за назвою"]]),
  TIP("На macOS замість <kbd>Ctrl</kbd> — <kbd>Cmd</kbd>, замість <kbd>Alt</kbd> — <kbd>Option</kbd>."),
  H("2. Як працювати однаково в школі й удома"),
  CARDS([("⭐", "Варіант А: GitHub (рекомендуємо)", "Проєкт живе в репозиторії. У школі: зробив зміни → Commit → Push. Удома: Pull → працюєш далі. Зручно через <b>GitHub Desktop</b> (desktop.github.com) — кнопки замість команд."),
         ("☁️", "Варіант Б: хмарний диск", "Папка проєкту в Google Drive / OneDrive. Простіше, але легко отримати дві різні версії файлу. Не відкривай проєкт одночасно у двох місцях."),
         ("💾", "Варіант В: флешка", "Працює завжди, навіть без інтернету. Мінус: забув флешку — забув проєкт. Роби копію в хмару.")]),
  STEPS(["Зареєструйся на <a href='https://github.com' target='_blank'>github.com</a> (від 13 років; молодші працюють через акаунт вчителя або Варіант Б).",
         "Встанови <b>GitHub Desktop</b>, увійди в акаунт.",
         "<b>File → New repository</b> → Name: <code>polytsia</code>, Local path — де зберігати → Create.",
         "Відкрий папку у VS Code, працюй. Повернись у GitHub Desktop: бачиш змінені файли → внизу напиши, що зробив («урок 6: додав стилі») → <b>Commit to main</b> → <b>Publish / Push origin</b>.",
         "На іншому комп'ютері: <b>File → Clone repository</b> → обери <code>polytsia</code>. Далі щоразу перед роботою натискай <b>Fetch / Pull origin</b>."]),
  WARN("Золоте правило синхронізації: <b>почав роботу — Pull, закінчив — Commit + Push</b>. Тоді вдома завжди буде шкільна версія, і навпаки."),
  H("3. Якщо не можна нічого встановлювати"),
  TABLE(["Сервіс", "Що дає", "Обмеження"], [
    ["<a href='https://vscode.dev' target='_blank'>vscode.dev</a>", "VS Code прямо в браузері. Відкриває папку на комп'ютері (Chrome/Edge) або репозиторій з GitHub", "Нема терміналу й Live Server"],
    ["<a href='https://github.com/codespaces' target='_blank'>GitHub Codespaces</a>", "Повний VS Code у хмарі з терміналом, Node.js і переглядом сайту", "Безкоштовний ліміт годин на місяць, потрібен акаунт GitHub"],
    ["<a href='https://codepen.io' target='_blank'>CodePen</a>", "Швидкі експерименти: HTML, CSS, JS у трьох вікнах, результат одразу", "Для одного «шматочка», не для всього проєкту"],
    ["Пісочниці цього курсу", "Блоки «Спробуй сам» в уроках", "Нема інтернету й файлів, лише для вправ"]]),
  H("4. Node.js (урок ⟦express⟧)"),
  STEPS(["<a href='https://nodejs.org' target='_blank'>nodejs.org</a> → завантаж версію <b>LTS</b> → встанови з налаштуваннями за замовчуванням (потрібні права адміністратора).",
         "Перезапусти VS Code, відкрий термінал (<kbd>Ctrl</kbd>+<kbd>`</kbd>) і виконай <code>node -v</code> і <code>npm -v</code>. Мають з'явитися номери версій.",
         "Якщо на шкільних ПК встановити не можна — відкрий репозиторій у <b>GitHub Codespaces</b>: Node.js там уже є."]),
  H("5. Supabase (урок ⟦sql⟧)"),
  P("<a href='https://supabase.com' target='_blank'>supabase.com</a> → <b>Start your project</b> → увійти через GitHub → New project. Регіон — Central EU (Frankfurt). Пароль бази запиши в надійне місце (не в код!). Безкоштовний проєкт засинає після тижня без активності — розбуди кнопкою Restore."),
  H("6. Телефон"),
  P("Повноцінно програмувати на телефоні незручно, але <b>перевіряти</b> сайт — обов'язково. Після публікації на GitHub Pages відкривай свою полицю з телефона. А ще у VS Code Live Server можна відкрити з телефона в тій самій Wi-Fi мережі за IP комп'ютера (наприклад, <code>http://192.168.0.15:5500</code>)."),
  H("7. AI-асистенти (уроки ⟦ai⟧–⟦agents⟧)"),
  P("Claude, ChatGPT, Gemini, GitHub Copilot. У кожного сервісу свої умови та <b>вікові обмеження</b> (від 13 до 18 років залежно від сервісу й країни). Учні, яким ще не можна, працюють з AI разом із вчителем на спільному екрані. Агенти (Claude Code, Replit Agent) потребують акаунта й часто платної підписки — на уроці ⟦agents⟧ їх показує вчитель."),
]}

PAGES["browser"] = {"title": "Як працювати й перевіряти сторінку в браузері", "sub": "DevTools — рентген, лабораторія і детектор помилок в одному. Тримай цю сторінку під рукою.", "sections": [
  FIG(DEVTOOLS, "Інструменти розробника: <kbd>F12</kbd> або <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>I</kbd> (Mac: <kbd>Cmd</kbd>+<kbd>Option</kbd>+<kbd>I</kbd>)."),
  H("Робочий процес"),
  STEPS(["Зліва VS Code, справа браузер (<kbd>Win</kbd>+<kbd>←</kbd> / <kbd>Win</kbd>+<kbd>→</kbd> ділить екран навпіл).",
         "Сторінка відкрита через <b>Live Server</b>: зберіг файл → сторінка оновилась сама.",
         "DevTools завжди відкриті. Спочатку дивишся в <b>Console</b>: нема червоного? Добре.",
         "Хочеш змінити вигляд — експериментуй у <b>Elements → Styles</b>, вдале значення переносиш у CSS-файл.",
         "Перед здачею — <b>мобільний режим</b> і <b>Lighthouse</b>."]),
  H("Вкладки DevTools"),
  TABLE(["Вкладка", "Що там", "Коли відкривати"], [
    ["<b>Elements</b>", "Живий HTML (DOM) і CSS кожного елемента. Можна змінювати наживо", "«Чому воно не там?», «Звідки цей колір?»"],
    ["<b>Console</b>", "Повідомлення <code>console.log</code>, помилки JS, можна писати JS-команди", "Завжди, особливо з уроку ⟦js-intro⟧"],
    ["<b>Network</b>", "Усі файли й запити: статус (200, 404…), розмір, час", "«Картинка/CSS не завантажились», запити до API"],
    ["<b>Application</b>", "localStorage, cookies", "Урок ⟦shelf⟧: подивитися збережені дані"],
    ["<b>📱 Device toolbar</b>", "Як сайт виглядає на телефоні/планшеті", "Після кожної зміни верстки"],
    ["<b>Lighthouse</b>", "Автоматична перевірка: швидкість, доступність, SEO", "Перед здачею проєкту"]]),
  H("Корисні прийоми"),
  LIST(["🎯 <b>Вибрати елемент</b>: іконка стрілочки зліва вгорі DevTools (<kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>C</kbd>), потім клік по сторінці.",
        "🎨 <b>Колір</b>: клацни на квадратик кольору в Styles — відкриється піпетка й палітра.",
        "☑️ <b>Вимкнути властивість</b>: зніми галочку біля неї в Styles. Так легко знайти, яке правило «ламає» верстку.",
        "📦 <b>Блокова модель</b>: Elements → Computed. Видно margin, border, padding з цифрами.",
        "🔁 <b>Жорстке оновлення</b> (якщо зміни CSS «не підхоплюються»): <kbd>Ctrl</kbd>+<kbd>Shift</kbd>+<kbd>R</kbd>.",
        "🐢 <b>Повільний інтернет</b>: Network → No throttling → Slow 4G. Видно, як сайт вантажиться в людей з поганим зв'язком.",
        "🧪 <b>Console як калькулятор</b>: можна писати будь-який JS: <code>items.length</code>, <code>document.querySelector('h1')</code>."]),
  H("Детектор помилок: чекліст «Не працює!»"),
  TABLE(["Симптом", "Де дивитися", "Найчастіша причина"], [
    ["Стилі не застосовуються", "Network → style.css: 404?", "Неправильний шлях у <code>&lt;link href&gt;</code> або друкарська помилка в селекторі"],
    ["Картинки нема", "Network → картинка: 404?", "Шлях, регістр літер (<code>Cat.JPG</code> ≠ <code>cat.jpg</code>), файл не в тій папці"],
    ["Кнопка нічого не робить", "Console", "Помилка JS вище в коді, скрипт не підключено, нема <code>defer</code>"],
    ["<code>Cannot read properties of null</code>", "Console → клік на рядок", "<code>querySelector</code> не знайшов елемент: перевір id/клас"],
    ["<code>X is not defined</code>", "Console", "Змінна/функція не оголошена або написана з помилкою (регістр!)"],
    ["<code>Unexpected token</code>", "Console", "Пропущена або зайва дужка, лапка, кома"],
    ["Сторінка перезавантажується після кнопки форми", "—", "Забув <code>event.preventDefault()</code>"],
    ["Запит до API не працює", "Network → Fetch/XHR → запит → Response", "Статус 4xx/5xx: читай текст помилки у відповіді"],
    ["Верстка «їде» на телефоні", "📱 Device toolbar", "Фіксована <code>width</code>, нема meta viewport"]]),
  TIP("Метод «гумової качки» 🦆: поясни свій код рядок за рядком уголос (качці, другу, коту). У 50% випадків помилку знаходиш сам, ще не закінчивши пояснення."),
  H("Зовнішні перевірки"),
  LIST(["<a href='https://validator.w3.org/#validate_by_input' target='_blank'>validator.w3.org</a> — перевірка HTML: незакриті теги, помилки вкладення.",
        "<a href='https://jigsaw.w3.org/css-validator/#validate_by_input' target='_blank'>CSS Validator</a> — перевірка CSS.",
        "<a href='https://wave.webaim.org' target='_blank'>WAVE</a> — доступність: контраст, alt, підписи полів.",
        "<a href='https://pagespeed.web.dev' target='_blank'>PageSpeed Insights</a> — швидкість опублікованого сайту."]),
]}

PAGES["project"] = {"title": "Проєкт «Полиця»", "sub": "Особиста колекція улюблених речей з оцінками, пошуком і базою даних. Будуємо крок за кроком протягом усього курсу.", "sections": [
  P("Кожен учень обирає <b>свою тему</b>: книги, ігри, фільми, музика, аніме, кросівки, рецепти, футбольні клуби… Структура однакова, а сайти виходять зовсім різні. Ось як виглядає готова полиця (це робоча демоверсія — спробуй пошук, фільтр, додавання й темну тему):"),
  {"t": "demo", "v": DEMO},
  H("Обов'язкові функції"),
  LIST(["Семантична структура: header, nav, main, footer", "Сітка карток з назвою, автором, категорією, оцінкою-зірочками", "Пошук за назвою й фільтр за категорією", "Форма додавання з перевірками", "Дані зберігаються в базі даних (Supabase) і видні з будь-якого пристрою", "Стани «Завантаження…» і повідомлення про помилку", "Адаптивність: телефон, планшет, комп'ютер", "Опубліковано на GitHub Pages"]),
  H("Ідеї для «зірочок»"),
  CARDS([("🌙", "Темна тема", "Перемикач + CSS-змінні"), ("📊", "Статистика", "Скільки в кожній категорії, середня оцінка, топ-3"),
         ("↕️", "Сортування", "За оцінкою, назвою, датою"), ("🗑️", "Видалення й редагування", "Нові політики RLS"),
         ("🖼️", "Обкладинки", "Поле image_url і картинки на картках"), ("⚡", "Realtime", "Нові речі з'являються в усіх без оновлення")]),
  H("Дорожня карта"),
  TABLE(["Уроки", "Етап", "Результат"], [
    ["⟦r:html⟧", "HTML", "Сторінка з топ-5, таблицею колекції й формою"],
    ["⟦r:css⟧", "CSS", "Стильна адаптивна сторінка з картками"],
    ["⟦r:js⟧", "JavaScript", "Інтерактивна полиця: рендер, пошук, фільтр, додавання, localStorage"],
    ["⟦r:db⟧", "Дані й бекенд", "Свій сервер на Express, потім полиця на Supabase"],
    ["⟦r:ai⟧", "AI і фінал", "AI-рев'ю, публікація, захист"]]),
  H("Структура файлів фінальної версії"),
  CODE("text", r'''
polytsia/
├── index.html
├── README.md        ← опис, скріншот, посилання
├── AI-LOG.md        ← журнал роботи з AI
├── css/
│   └── style.css
├── js/
│   └── app.js
├── images/
└── sql/
    └── schema.sql   ← create table + політики''', title="Фінальна структура"),
]}

PAGES["teacher"] = {"title": "Для вчителя", "sub": "Календарний план, оцінювання і поради щодо проведення курсу.", "sections": [
  H("Формат"),
  LIST(["⟦FMT⟧",
        "Структура уроку: 5 хв — повторення/самоперевірка → 15 хв — теорія з живими прикладами (кнопка «Запустити» на проєкторі) → 20 хв — практика «Спробуй сам» + крок проєкту → 5 хв — ДЗ.",
        "Контрольні — на початку наступного уроку після блоку (20–30 хв). Тести інтерактивні: учень одразу бачить бал за 12-бальною шкалою. Для оцінки просіть скріншот результату або проводьте з телефонів у класі.",
        "Кожен урок має три рівні ДЗ: «Базовий» — для всіх, «Середній» — на 10–11, «Зірочка» — для сильних учнів."]),
  H("Календарний план"),
  {"t": "plan"},
  H("Система оцінювання"),
  TABLE(["Що", "Вага", "Коментар"], [
    ["Домашні завдання", "30%", "Базовий рівень = 7–9, середній = 10–11, зірочка = 12"],
    ["Контрольні (5)", "30%", "Бал з інтерактивного тесту"],
    ["Фінальний проєкт", "40%", "Рубрика в уроці ⟦final⟧: функціонал 4, дизайн 3, код 2, розуміння 2, чесність з AI 1"]]),
  H("Поради"),
  CARDS([("🐢", "Темп", "Блок JavaScript (⟦r:js⟧) найскладніший. Якщо група не встигає — урок ⟦shelf⟧ розтягніть на два, а «зірочки» з CSS пропустіть."),
         ("🤝", "Парне програмування", "Один пише, інший підказує, міняються кожні 10 хв. Чудово працює на уроках ⟦dom⟧–⟦shelf⟧ і ⟦express⟧."),
         ("🧯", "Supabase у класі", "Створіть заздалегідь свій демо-проєкт. Якщо в когось не вийде зареєструватися, дайте URL і publishable key свого навчального проєкту."),
         ("🧑‍🏫", "Демо агентів", "Урок ⟦agents⟧: підготуйте сценарій заздалегідь і проженіть його вдома. Агенти працюють непередбачувано — і це теж гарний урок."),
         ("🔒", "Безпека", "Перевіряйте репозиторії учнів на secret key. На GitHub є функція secret scanning, але краще навчити не комітити секрети взагалі."),
         ("🎓", "Доброчесність", "AI дозволений і навіть заохочується, але учень має пояснити кожен рядок. Захист проєкту з питаннями — найкращий антиплагіат.")]),
]}

from tags import ATTRS
PAGES["tags"] = {"title": "🏷️ Довідник HTML-тегів", "sub": "Навіщо потрібні теги, як вони влаштовані і що означає кожен з них. З прикладами, які можна запустити.", "catalog": True, "sections": [
  H("Навіщо взагалі теги?"),
  P("Для людини очевидно, що великий рядок угорі — це заголовок, а список з крапками — меню. А комп'ютер бачить лише <b>послідовність символів</b>. Він не знає, що важливе, що є посиланням, а що картинкою. <b>Теги — це ярлики</b>, якими ми підписуємо кожен шматок сторінки: «це заголовок», «це абзац», «це кнопка»."),
  CODE("html", r'''
Моя полиця
Ігри, які я люблю.
Мій топ-3
Minecraft
Terraria
Celeste
Перейти на Вікіпедію''', run=True, title="Без тегів", note="Запусти: браузер склеїв усе в один рядок! Він не знає, де заголовок, де список, а «посилання» нікуди не веде."),
  CODE("html", r'''
<h1>Моя полиця</h1>
<p>Ігри, які я люблю.</p>
<h2>Мій топ-3</h2>
<ol>
  <li>Minecraft</li>
  <li>Terraria</li>
  <li>Celeste</li>
</ol>
<a href="https://uk.wikipedia.org">Перейти на Вікіпедію</a>''', run=True, title="З тегами", note="Той самий текст, але тепер браузер розуміє структуру: заголовки, абзац, нумерований список, справжнє посилання."),
  H("Хто «читає» теги"),
  CARDS([("🖥️", "Браузер", "Вирішує, як показати: заголовок великим, список з номерами, посилання — клікабельним."),
         ("🔍", "Google та інші пошуковики", "Розуміють, про що сторінка: h1 і title важливіші за звичайний текст. Від цього залежить місце в пошуку."),
         ("🦻", "Програми для незрячих", "Читають сторінку вголос і дозволяють стрибати по заголовках, меню, посиланнях. Без тегів сайт для них — суцільний потік слів."),
         ("🎨", "CSS і JavaScript", "Знаходять елементи за тегами, класами й id, щоб розфарбувати або «оживити» їх.")]),
  H("Як влаштований тег"),
  FIG(TAG, "Відкривальний тег, атрибути, вміст і закривальний тег разом утворюють ЕЛЕМЕНТ."),
  TABLE(["", "Парні теги", "Одиночні (порожні) теги"], [
    ["Вигляд", "<code>&lt;p&gt;вміст&lt;/p&gt;</code>", "<code>&lt;img src=\"...\" alt=\"...\"&gt;</code>"],
    ["Є вміст?", "Так, між тегами", "Ні, вся інформація — в атрибутах"],
    ["Приклади", "p, h1, a, ul, li, div, button", "img, br, hr, input, meta, link"]]),
  H("Правило матрьошки: вкладеність"),
  P("Теги можна класти один в одний, як матрьошки. Головне правило: <b>що відкрилося останнім — закривається першим</b>."),
  CODE("html", r'''
<!-- ✅ правильно: strong повністю всередині p -->
<p>Це <strong>дуже важливо</strong>!</p>

<!-- ❌ неправильно: теги «перехрещуються» -->
<p>Це <strong>дуже важливо</p></strong>'''),
  TIP("Відступи (2 пробіли на кожен рівень вкладеності) роблять структуру видимою. VS Code з Prettier робить це сам при збереженні."),
  H("Блочні й рядкові елементи"),
  CODE("html", r'''
<style>
  div, p, h3 { background: #dce8ff; }
  a, strong, span { background: #ffe3d6; }
</style>
<h3>h3 — блочний</h3>
<p>p — блочний, а всередині <strong>strong</strong>, <a href="#">a</a> і <span>span</span> — рядкові.</p>
<div>div — блочний: займає всю ширину</div>''', run=True, note="Блочні (сині) займають всю ширину й починаються з нового рядка. Рядкові (помаранчеві) стоять у рядку, як слова в реченні."),
  H("Атрибути, що працюють у будь-якого тегу"),
  TABLE(["Атрибут", "Навіщо", "Приклад"], [[f"<code>{a}</code>", b, f"<code>{c.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')}</code>"] for a, b, c in ATTRS]),
  IDEA("У HTML понад 110 тегів, але 90% сайтів у світі зібрані приблизно з 30 найпопулярніших. Нижче — усі, що знадобляться в курсі й трохи більше. Повний список — на <a href='https://developer.mozilla.org/uk/docs/Web/HTML/Element' target='_blank'>MDN</a>."),
  H("Каталог тегів"),
]}
