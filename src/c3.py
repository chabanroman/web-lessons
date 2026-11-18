from helpers import *
from svgs import *

# ───────────── БЛОК 3: JavaScript ─────────────
lesson(11, "js", "Перший JavaScript: змінні й типи даних",
 "Сторінка вчиться думати. Підключаємо скрипт, говоримо з консоллю, зберігаємо дані у змінних.",
 ["підключати файл app.js", "виводити повідомлення в консоль", "створювати змінні через let і const", "розрізняти рядки, числа й логічні значення"],
 [
  H("Що вміє JavaScript"),
  CARDS([("🖱️", "Реагувати", "На кліки, введення тексту, прокрутку."),
         ("🧮", "Рахувати й вирішувати", "Середня оцінка, сортування, перевірка форми."),
         ("🌐", "Говорити з сервером", "Завантажувати й зберігати дані без перезавантаження сторінки.")]),
  H("Підключаємо скрипт"),
  CODE("html", r'''
<head>
  ...
  <link rel="stylesheet" href="css/style.css">
  <script src="js/app.js" defer></script>
</head>''', note="<code>defer</code> = «запусти скрипт, коли HTML уже завантажиться». Без нього скрипт може не знайти елементи сторінки."),
  CODE("javascript", r'''
console.log('Полиця запущена! 🚀');''', title="js/app.js"),
  P("Відкрий сторінку → <kbd>F12</kbd> → вкладка <b>Console</b>. Там твоє повідомлення! Консоль — головний друг програміста: сюди виводиш, що відбувається, і тут бачиш помилки (червоним)."),
  H("Змінні: коробки з наліпками"),
  CODE("javascript", r'''
let score = 10;          // let — можна змінювати
const name = 'Олекса';   // const — не можна змінювати

score = score + 5;
console.log(name, 'має', score, 'балів');

// Типи даних
const title = 'Minecraft';   // string — рядок (у лапках)
const rating = 5;            // number — число
const isFavorite = true;     // boolean — так/ні
let comment;                 // undefined — ще нічого не поклали

console.log(typeof title, typeof rating, typeof isFavorite);''', run=True),
  TIP("Правило: пиши <code>const</code> завжди, а <code>let</code> лише коли значення точно буде змінюватися. <code>var</code> — застарілий спосіб, не використовуй."),
  H("Рядки та шаблонні рядки"),
  CODE("javascript", r'''
const game = 'Terraria';
const hours = 120;

// Старий спосіб — склеювання через +
console.log('Я грав у ' + game + ' ' + hours + ' годин');

// Новий спосіб — шаблонний рядок у `зворотних лапках`
console.log(`Я грав у ${game} ${hours} годин`);

console.log(game.length);         // кількість символів
console.log(game.toUpperCase());  // ВЕЛИКИМИ''', run=True, note="Зворотна лапка ` — клавіша зліва від 1 (англійська розкладка)."),
  TRY(r'''<script>
  const myName = 'Твоє імʼя';
  const age = 14;
  const hobby = 'програмування';
  console.log(`Привіт! Я ${myName}, мені ${age}, люблю ${hobby}.`);
  console.log(`Через 10 років мені буде ${age + 10}`);
</script>''', "Познайомся з консоллю"),
  WARN("JavaScript чутливий до регістру: <code>myName</code> і <code>myname</code> — різні змінні. Назви змінних пиши англійською в стилі <b>camelCase</b>: <code>userName</code>, <code>totalScore</code>."),
 ],
 "Створи <code>js/app.js</code>, підключи з <code>defer</code>. Створи змінні: <code>shelfName</code> (назва полиці), <code>owner</code> (твоє ім'я), <code>itemsCount</code> (скільки речей у колекції). Виведи в консоль привітання через шаблонний рядок.",
 ["F12 → Console: твоє повідомлення є, червоних помилок нема", "Якщо помилка — клацни по посиланню справа (app.js:3) і побачиш рядок з помилкою", "Спробуй писати JS прямо в Console: <code>2 + 2</code>, <code>'аба'.length</code>"],
 [("Базовий", "Скрипт-візитка: 5 змінних про себе й 3 повідомлення в консоль через шаблонні рядки."),
  ("Середній", "Калькулятор кишенькових: змінні «гроші на тиждень» і «ціна піци». Виведи, скільки піц можна купити (підказка: <code>Math.floor()</code>) і скільки залишиться (<code>%</code>)."),
  ("Зірочка ⭐", "Дізнайся, що виведе <code>'5' + 3</code> і <code>'5' - 3</code>. Поясни в коментарі, чому так.")],
 [("Що виведе console.log(`2 + 2 = ${2 + 2}`)?", ["2 + 2 = ${2 + 2}", "2 + 2 = 4", "4 = 4", "Помилку"], 1, "У ${} обчислюється вираз."),
  ("Коли використовувати const?", ["Ніколи", "Коли значення не буде змінюватися", "Лише для чисел", "Лише для тексту"], 1, "const за замовчуванням, let — якщо змінюєш."),
  ("Який тип у значення true?", ["string", "number", "boolean", "undefined"], 2, "true/false — boolean.")])

lesson(12, "js", "Умови й оператори: програма приймає рішення",
 "if, else, порівняння й логіка. Вчимо програму реагувати на різні ситуації.",
 ["використовувати арифметичні оператори й оператори порівняння", "писати умови if / else if / else", "поєднувати умови через && і ||", "використовувати тернарний оператор"],
 [
  H("Оператори"),
  TABLE(["Група", "Оператори", "Приклад"], [
    ["Арифметика", "<code>+ - * / %</code> (остача) <code>**</code> (степінь)", "<code>17 % 5</code> → 2"],
    ["Порівняння", "<code>=== !== &gt; &lt; &gt;= &lt;=</code>", "<code>5 === 5</code> → true"],
    ["Логіка", "<code>&amp;&amp;</code> (і), <code>||</code> (або), <code>!</code> (не)", "<code>age &gt; 12 &amp;&amp; age &lt; 18</code>"]]),
  WARN("<code>=</code> — це «поклади в змінну». <code>===</code> — це «чи дорівнює?». Завжди порівнюй через <b>три</b> знаки: <code>==</code> робить дивні перетворення (<code>'1' == 1</code> → true)."),
  H("if / else"),
  CODE("javascript", r'''
const rating = 4;

if (rating === 5) {
  console.log('🔥 Шедевр!');
} else if (rating >= 3) {
  console.log('👍 Непогано');
} else {
  console.log('😐 Так собі');
}''', run=True),
  H("Кілька умов одразу"),
  CODE("javascript", r'''
const age = 14;
const hasTicket = true;

if (age >= 12 && hasTicket) {
  console.log('Проходь у кінотеатр 🎬');
}

const day = 'субота';
if (day === 'субота' || day === 'неділя') {
  console.log('Вихідний! 🎉');
}

// Тернарний оператор — коротке if для вибору значення
const label = age >= 18 ? 'дорослий' : 'підліток';
console.log(label);''', run=True),
  TRY(r'''<script>
  const score = 87;   // зміни число та подивись результат

  if (score >= 90) {
    console.log('Оцінка: 12');
  } else if (score >= 75) {
    console.log('Оцінка: 10');
  } else if (score >= 50) {
    console.log('Оцінка: 7');
  } else {
    console.log('Треба ще попрацювати');
  }
</script>''', "Перетвори бали в оцінку"),
  IDEA("Справжня програма — це мільйони таких маленьких рішень. Банк: «якщо грошей вистачає — провести оплату». Гра: «якщо здоров'я 0 — Game Over»."),
 ],
 "У <code>app.js</code> створи змінну <code>rating</code> і напиши умову, що виводить у консоль мітку: 5 → «🔥 Шедевр», 4 → «👍 Рекомендую», 3 → «🙂 Нормально», менше → «👎 Не моє».",
 ["Змінюй rating і перезавантажуй: мітка змінюється правильно", "Перевір крайні випадки: 0, 5, 6, -1. Що виводить програма?", "Console: якщо помилка <code>Unexpected token</code> — шукай пропущену дужку"],
 [("Базовий", "Програма «Світлофор»: змінна color, і для кожного кольору своє повідомлення."),
  ("Середній", "Перевірка пароля: довжина ≥ 8 і не дорівнює '12345678'. Виведи «надійний» або причину, чому ні."),
  ("Зірочка ⭐", "Визнач, чи рік високосний (ділиться на 4, але не на 100, або ділиться на 400). Перевір на 2024, 1900, 2000.")],
 [("Що поверне 10 % 3?", ["3", "1", "0", "3.33"], 1, "Остача від ділення 10 на 3 — це 1."),
  ("Яке порівняння правильне?", ["if (a = 5)", "if (a === 5)", "if (a => 5)", "if a == 5"], 1, "=== — строге порівняння."),
  ("true && false дорівнює…", ["true", "false", "undefined", "Помилка"], 1, "&& вимагає, щоб обидва були true.")])

lesson(13, "js", "Масиви й цикли",
 "Масив — це список даних, а цикл — спосіб пройтися по кожному елементу. Разом вони обробляють хоч мільйон записів.",
 ["створювати масиви й отримувати елементи за індексом", "додавати й видаляти елементи", "проходити масив циклами for і for...of", "рахувати суму та середнє"],
 [
  H("Масив — список у квадратних дужках"),
  CODE("javascript", r'''
const games = ['Minecraft', 'Terraria', 'Portal 2'];

console.log(games[0]);        // перший — індекс 0!
console.log(games.length);    // скільки елементів: 3

games.push('Celeste');        // додати в кінець
console.log(games);

console.log(games.includes('Terraria'));   // чи є? true
console.log(games.indexOf('Portal 2'));    // на якому місці? 2

games.pop();                  // видалити останній
console.log(games.join(' · '));''', run=True),
  WARN("Індекси починаються з <b>0</b>. Останній елемент: <code>arr[arr.length - 1]</code>."),
  H("Цикл for: повтори N разів"),
  CODE("javascript", r'''
for (let i = 1; i <= 5; i++) {
  console.log('⭐'.repeat(i));
}
// i = 1 — звідки починаємо
// i <= 5 — поки виконується умова
// i++ — що робимо після кожного кроку (i = i + 1)''', run=True),
  H("for...of: пройтися по кожному"),
  CODE("javascript", r'''
const ratings = [5, 4, 3, 5, 4];
let sum = 0;

for (const r of ratings) {
  sum += r;              // те саме, що sum = sum + r
}

const avg = sum / ratings.length;
console.log('Середня оцінка:', avg.toFixed(1));''', run=True),
  TRY(r'''<script>
  const classmates = ['Аня', 'Богдан', 'Віка', 'Денис'];

  for (const name of classmates) {
    console.log(`Привіт, ${name}! 👋`);
  }

  // Завдання: додай себе в масив і виведи, скільки людей у списку
</script>''', "Привітай весь клас"),
  P("Є ще цикл <code>while (умова) { ... }</code>: повторює, поки умова true. Корисний, коли наперед невідомо, скільки буде кроків. Але обережно: якщо умова ніколи не стане false — сторінка «зависне»!"),
 ],
 "У <code>app.js</code> створи масив <code>titles</code> з назвами 6+ речей твоєї колекції і масив <code>ratings</code> з оцінками. Виведи кожну назву з номером («1. Minecraft») і середню оцінку колекції.",
 ["Console: усі назви з правильними номерами (з 1, а не з 0)", "Середня рахується правильно — перевір на калькуляторі", "У Console можна написати <code>titles</code> і подивитися масив, розгорнувши стрілочкою"],
 [("Базовий", "Масив з 7 днів тижня. Виведи лише робочі дні (підказка: цикл for з i від 0 до 4)."),
  ("Середній", "Масив оцінок за семестр. Знайди максимальну, мінімальну й середню без <code>Math.max</code>."),
  ("Зірочка ⭐", "Таблиця множення на 1–9 у консоль через два вкладені цикли.")],
 [("Що виведе ['a','b','c'][1]?", ["a", "b", "c", "undefined"], 1, "Індекс 1 — другий елемент."),
  ("Який метод додає елемент у кінець?", ["pop()", "push()", "add()", "shift()"], 1, "push — «заштовхнути» в кінець."),
  ("Скільки разів виконається for (let i = 0; i < 3; i++)?", ["2", "3", "4", "Безкінечно"], 1, "i = 0, 1, 2 → три рази.")])

lesson(14, "js", "Функції: свої команди",
 "Функція — це рецепт: написав один раз, використовуєш скільки завгодно. Основа чистого коду.",
 ["оголошувати функції з параметрами", "повертати результат через return", "писати стрілкові функції", "розбивати задачу на маленькі функції"],
 [
  H("Оголошення та виклик"),
  CODE("javascript", r'''
// оголошуємо
function greet(name) {
  console.log(`Привіт, ${name}!`);
}

// викликаємо
greet('Олекса');
greet('Марія');''', run=True),
  H("return — функція повертає результат"),
  CODE("javascript", r'''
function stars(rating) {
  return '★'.repeat(rating) + '☆'.repeat(5 - rating);
}

console.log(stars(5));   // ★★★★★
console.log(stars(3));   // ★★★☆☆

function average(numbers) {
  let sum = 0;
  for (const n of numbers) sum += n;
  return sum / numbers.length;
}

console.log(average([5, 4, 4, 3]));''', run=True, note="Функція <code>stars</code> знадобиться нам у проєкті: вона перетворює число на зірочки."),
  IDEA("Параметр — це «отвір» у функції, куди щоразу кладеш нове значення. Як блендер: функція одна, а смузі виходить різне, залежно від того, що поклав."),
  H("Стрілкові функції"),
  CODE("javascript", r'''
// звичайна
function double(x) {
  return x * 2;
}

// стрілкова — те саме, коротше
const double2 = (x) => x * 2;

const sayHi = () => console.log('Hi!');

console.log(double(4), double2(4));
sayHi();''', run=True),
  TRY(r'''<script>
  // Допиши функцію: повертає емодзі залежно від оцінки
  function moodEmoji(rating) {
    if (rating >= 5) return '🔥';
    // додай свої варіанти для 4, 3 і менше
    return '🤔';
  }

  console.log(moodEmoji(5), moodEmoji(4), moodEmoji(2));
</script>''', "Функція-емодзі"),
  TIP("Хороша функція робить <b>одну</b> річ і має назву-дієслово: <code>getStars</code>, <code>calcAverage</code>, <code>showMessage</code>. Якщо функція довша за екран — розбий її на кілька."),
 ],
 "Напиши у <code>app.js</code> функції <code>stars(rating)</code> (повертає ★★★☆☆) і <code>average(numbers)</code>. Виведи в консоль кожну річ колекції зі зірочками і загальну середню.",
 ["Console: <code>stars(0)</code> і <code>stars(5)</code> працюють правильно", "Виклич функцію прямо в Console: <code>stars(2)</code>", "Помилка <code>stars is not defined</code> = функцію не оголошено або написано з помилкою"],
 [("Базовий", "Функції <code>celsiusToFahrenheit(c)</code> і навпаки. Перевір на 0, 100, 36.6."),
  ("Середній", "Функція <code>isPalindrome(word)</code>: перевіряє, чи слово читається однаково в обидва боки («козак з казок»)."),
  ("Зірочка ⭐", "Функція <code>randomPick(array)</code>: повертає випадковий елемент. Зроби «рандомайзер» — хто сьогодні відповідає біля дошки 😈 (<code>Math.random</code>).")],
 [("Що робить return?", ["Виводить у консоль", "Повертає результат з функції й завершує її", "Повторює функцію", "Видаляє функцію"], 1, "return — результат роботи."),
  ("Як викликати функцію stars з числом 4?", ["stars[4]", "stars(4)", "call stars 4", "stars = 4"], 1, "Круглі дужки = виклик."),
  ("Що еквівалентне const f = (x) => x + 1?", ["function f(x) { x + 1 }", "function f(x) { return x + 1 }", "f = x + 1", "function(x + 1)"], 1, "Без фігурних дужок стрілка повертає вираз автоматично.")])

lesson(15, "js", "Об'єкти та масиви об'єктів: міні-база даних",
 "Об'єкт описує одну річ з її властивостями. Масив об'єктів — це вже справжня колекція даних.",
 ["створювати об'єкти й звертатися до властивостей", "зберігати колекцію як масив об'єктів", "використовувати filter, map, find, sort", "читати формат JSON"],
 [
  H("Об'єкт: властивості в одному місці"),
  CODE("javascript", r'''
const game = {
  title: 'Minecraft',
  studio: 'Mojang',
  year: 2011,
  rating: 5,
  tags: ['пісочниця', 'виживання']
};

console.log(game.title);        // крапка — доступ до властивості
console.log(game['year']);      // або так
game.rating = 4;                // змінити
game.played = true;             // додати нову
console.log(game);''', run=True),
  H("Масив об'єктів = таблиця"),
  P("Пам'ятаєш таблицю з уроку ⟦tables⟧? Ось вона в JavaScript: кожен об'єкт — рядок, кожна властивість — стовпець."),
  CODE("javascript", r'''
const items = [
  { title: 'Minecraft',   category: 'гра',    rating: 5 },
  { title: 'Кобзар',      category: 'книга',  rating: 5 },
  { title: 'Мавка',       category: 'фільм',  rating: 4 },
  { title: 'Terraria',    category: 'гра',    rating: 4 },
  { title: 'Портал 2',    category: 'гра',    rating: 3 }
];

console.table(items);   // гарна таблиця в консолі (відкрий F12!)''', run=True),
  H("Суперсили масивів"),
  CODE("javascript", r'''
const items = [
  { title: 'Minecraft', category: 'гра',   rating: 5 },
  { title: 'Кобзар',    category: 'книга', rating: 5 },
  { title: 'Мавка',     category: 'фільм', rating: 4 },
  { title: 'Terraria',  category: 'гра',   rating: 4 }
];

// filter — відібрати ті, що підходять
const games = items.filter(item => item.category === 'гра');
console.log('Ігри:', games.length);

// map — перетворити кожен
const names = items.map(item => item.title.toUpperCase());
console.log(names);

// find — знайти перший
const found = items.find(item => item.title === 'Мавка');
console.log(found);

// sort — відсортувати (тут від кращого до гіршого)
const best = [...items].sort((a, b) => b.rating - a.rating);
console.log(best[0].title);

// forEach — просто зробити щось з кожним
items.forEach(item => console.log(`${item.title}: ${item.rating}`));''', run=True),
  TABLE(["Метод", "Повертає", "Коли"], [
    ["<code>filter</code>", "новий масив (менший)", "пошук, фільтри"],
    ["<code>map</code>", "новий масив (такий самий за довжиною)", "перетворити дані → HTML"],
    ["<code>find</code>", "один елемент або undefined", "знайти за id"],
    ["<code>sort</code>", "той самий масив, відсортований", "рейтинги, алфавіт"],
    ["<code>forEach</code>", "нічого", "просто пройтися"]]),
  H("JSON — мова обміну даними"),
  CODE("json", r'''
[
  { "title": "Minecraft", "category": "гра", "rating": 5 },
  { "title": "Кобзар", "category": "книга", "rating": 5 }
]''', note="JSON схожий на об'єкти JS, але ключі завжди в подвійних лапках. Саме в такому вигляді сервер і база даних передаватимуть нам дані."),
 ],
 "Створи <code>js/data.js</code> з масивом <code>items</code>: 6–8 об'єктів з полями <code>title, author, category, rating, review, image</code>. Підключи його <b>перед</b> app.js. В app.js виведи <code>console.table(items)</code> і кількість речей кожної категорії через filter.",
 ["Console: <code>console.table</code> показує гарну таблицю", "Напиши в Console <code>items.filter(i =&gt; i.rating === 5)</code>, щоб знайти шедеври", "Якщо <code>items is not defined</code> — перевір порядок підключення скриптів"],
 [("Базовий", "Масив 5 учнів <code>{name, grade, score}</code>. Виведи тих, у кого score &gt; 80, і середній бал класу."),
  ("Середній", "Масив товарів магазину. Відсортуй за ціною, знайди найдешевший, порахуй вартість кошика (усі товари)."),
  ("Зірочка ⭐", "Дізнайся про <code>reduce</code> і порахуй через нього суму оцінок колекції одним рядком.")],
 [("Як отримати title з об'єкта game?", ["game(title)", "game.title", "game->title", "title.game"], 1, "Через крапку."),
  ("Що поверне items.filter(i => i.rating > 4)?", ["Один об'єкт", "Новий масив з об'єктів, де rating більше 4", "Число", "true/false"], 1, "filter завжди повертає масив."),
  ("Чим JSON відрізняється від об'єкта JS?", ["Нічим", "Ключі обов'язково в подвійних лапках, це текстовий формат", "У JSON не можна числа", "JSON працює лише в Python"], 1, "JSON — текстовий формат обміну даними.")])

lesson(16, "js", "DOM: JavaScript керує сторінкою",
 "Знаходимо елементи, змінюємо текст і стилі, створюємо нові елементи прямо з коду.",
 ["пояснити, що таке DOM-дерево", "знаходити елементи через querySelector", "змінювати textContent, innerHTML, classList", "створювати й додавати елементи на сторінку"],
 [
  H("DOM — сторінка очима JavaScript"),
  P("Браузер перетворює HTML на <b>дерево об'єктів</b> — DOM (Document Object Model). Кожен тег — вузол, у якого є батьки й діти. JavaScript може знайти будь-який вузол і змінити його."),
  FIG(DOM, "DOM-дерево. Вкладка Elements у DevTools показує саме його."),
  H("Знайти елемент"),
  CODE("javascript", r'''
// за CSS-селектором — як у CSS!
const title = document.querySelector('h1');        // перший h1
const list  = document.querySelector('#list');     // id="list"
const card  = document.querySelector('.card');    // перший з class="card"
const all   = document.querySelectorAll('.card');  // УСІ картки (список)'''),
  H("Змінити елемент"),
  CODE("html", r'''
<h1 id="title">Моя полиця</h1>
<p class="info">Завантаження...</p>
<style>.highlight { background: #fff3cc; padding: 8px; border-radius: 8px; }</style>

<script>
  const title = document.querySelector('#title');
  title.textContent = '📚 Полиця Олекси';      // змінити текст
  title.style.color = '#f0622e';               // змінити стиль

  const info = document.querySelector('.info');
  info.innerHTML = 'У колекції <b>8</b> речей'; // вставити HTML
  info.classList.add('highlight');             // додати клас
</script>''', run=True),
  TIP("<code>textContent</code> — лише текст (безпечно). <code>innerHTML</code> — розуміє теги. Дані, які ввела людина, вставляй через textContent, бо хтось може ввести шкідливий код."),
  H("Створити нові елементи"),
  CODE("html", r'''
<ul id="list"></ul>
<script>
  const games = ['Minecraft', 'Terraria', 'Celeste'];
  const list = document.querySelector('#list');

  for (const g of games) {
    const li = document.createElement('li');  // створити
    li.textContent = g;                       // наповнити
    list.append(li);                          // додати на сторінку
  }
</script>''', run=True),
  H("Швидкий спосіб: map + шаблонні рядки"),
  TRY(r'''<div id="cards"></div>
<style>
  #cards { display: grid; gap: 10px; font-family: sans-serif; }
  .card { background: #fff; border: 2px solid #1d1b26; border-radius: 12px; padding: 12px; }
</style>
<script>
  const items = [
    { title: 'Minecraft', rating: 5 },
    { title: 'Кобзар', rating: 5 },
    { title: 'Мавка', rating: 4 }
  ];

  document.querySelector('#cards').innerHTML = items.map(item => `
    <div class="card">
      <b>${item.title}</b><br>
      ${'★'.repeat(item.rating)}
    </div>
  `).join('');
</script>''', "Масив → картки на сторінці"),
  IDEA("Ось вона, магія: <b>дані</b> (масив) окремо, <b>вигляд</b> (HTML-шаблон) окремо, а JavaScript їх з'єднує. Саме так працюють YouTube, Instagram і будь-який інтернет-магазин."),
 ],
 "Видали з <code>index.html</code> картки, написані вручну, залиш порожній <code>&lt;div class=\"cards\" id=\"cards\"&gt;&lt;/div&gt;</code>. В app.js згенеруй картки з масиву <code>items</code> (data.js) через map. Додай над сіткою лічильник «У колекції: N».",
 ["F12 → Elements: картки з'явились у DOM, хоча в index.html їх нема", "Додай об'єкт у data.js → після перезавантаження з'явилась нова картка", "Помилка <code>Cannot set properties of null</code> = querySelector нічого не знайшов (перевір id і defer)"],
 [("Базовий", "Сторінка-«хамелеон»: JS змінює заголовок, колір фону й текст абзацу при завантаженні."),
  ("Середній", "Згенеруй таблицю розкладу з масиву об'єктів <code>{day, lessons: [...]}</code>."),
  ("Зірочка ⭐", "Виведи картки, відсортовані за рейтингом, і дай найкращій клас <code>.top</code> з короною 👑.")],
 [("Що таке DOM?", ["Мова програмування", "Дерево об'єктів, на яке браузер перетворює HTML", "Сервер", "Тип файлу"], 1, "Document Object Model."),
  ("Як знайти елемент з id=\"list\"?", ["document.querySelector('list')", "document.querySelector('#list')", "document.get(list)", "#list.find()"], 1, "Селектор як у CSS: #id."),
  ("Чим безпечніше вставляти текст від користувача?", ["innerHTML", "textContent", "document.write", "Неважливо"], 1, "textContent не виконує теги.")])

lesson(17, "js", "Події: кліки, введення, форми",
 "Сторінка реагує на людину. Кнопки, пошук під час введення, обробка форми без перезавантаження.",
 ["підписуватися на події через addEventListener", "обробляти click, input, submit", "зупиняти стандартну поведінку форми (preventDefault)", "читати значення полів"],
 [
  H("Слухач подій"),
  CODE("html", r'''
<button id="btn">Клікни мене</button>
<p id="out">Кліків: 0</p>

<script>
  let count = 0;
  const btn = document.querySelector('#btn');
  const out = document.querySelector('#out');

  btn.addEventListener('click', () => {
    count++;
    out.textContent = `Кліків: ${count}`;
  });
</script>''', run=True, note="Схема завжди одна: <b>знайди елемент → підпишись на подію → опиши, що робити</b>."),
  TABLE(["Подія", "Коли спрацьовує"], [
    ["<code>click</code>", "Клік мишкою / дотик"],
    ["<code>input</code>", "Кожна зміна тексту в полі"],
    ["<code>change</code>", "Зміна select, checkbox (після вибору)"],
    ["<code>submit</code>", "Відправка форми (Enter або кнопка)"],
    ["<code>keydown</code>", "Натиснули клавішу"],
    ["<code>mouseover</code>", "Навели мишку"]]),
  H("Темна тема однією кнопкою"),
  CODE("html", r'''
<style>
  body { font-family: sans-serif; transition: .3s; }
  body.dark { background: #16151c; color: #f3f0ea; }
</style>
<button id="theme">🌙 Темна тема</button>
<p>Текст сторінки.</p>
<script>
  document.querySelector('#theme').addEventListener('click', (e) => {
    document.body.classList.toggle('dark');   // toggle = додати/прибрати
    const isDark = document.body.classList.contains('dark');
    e.target.textContent = isDark ? '☀️ Світла тема' : '🌙 Темна тема';
  });
</script>''', run=True),
  H("Обробка форми"),
  CODE("html", r'''
<form id="add-form">
  <input id="title" placeholder="Назва" required>
  <select id="rating">
    <option value="5">★★★★★</option>
    <option value="4">★★★★</option>
    <option value="3">★★★</option>
  </select>
  <button>Додати</button>
</form>
<ul id="list"></ul>

<script>
  const form = document.querySelector('#add-form');

  form.addEventListener('submit', (event) => {
    event.preventDefault();               // НЕ перезавантажувати сторінку!

    const title = document.querySelector('#title').value;
    const rating = Number(document.querySelector('#rating').value);

    const li = document.createElement('li');
    li.textContent = `${title} — ${'★'.repeat(rating)}`;
    document.querySelector('#list').append(li);

    form.reset();                          // очистити форму
    console.log('Додано:', { title, rating });
  });
</script>''', run=True),
  WARN("<code>.value</code> поля — це завжди <b>рядок</b>. Щоб отримати число, загорни в <code>Number(...)</code>."),
  TRY(r'''<input id="name" placeholder="Введи імʼя">
<h2 id="hello">Привіт, ...</h2>
<script>
  document.querySelector('#name').addEventListener('input', (e) => {
    const value = e.target.value;
    document.querySelector('#hello').textContent = `Привіт, ${value || '...'}! 👋`;
  });
</script>''', "Живе введення"),
 ],
 "Додай у шапку кнопку перемикання теми. «Оживи» форму «Додати на полицю»: при submit — <code>preventDefault</code>, зібрати об'єкт з усіх полів і вивести його в консоль через <code>console.log</code>.",
 ["Сторінка НЕ перезавантажується після натискання кнопки форми", "Console: виводиться об'єкт з правильними полями, rating — число (синім кольором, а не в лапках)", "Elements → вибери кнопку → вкладка <b>Event Listeners</b>: видно твій обробник click"],
 [("Базовий", "Лічильник з трьома кнопками: +1, −1, скинути. Число не може бути менше 0."),
  ("Середній", "Генератор привітань: поле імені + select з приводом (день народження, свято) → кнопка показує картку-листівку."),
  ("Зірочка ⭐", "Гра «Вгадай число»: комп'ютер загадує 1–100, людина вводить варіанти, програма каже «більше/менше» і рахує спроби.")],
 [("Що робить event.preventDefault() у submit?", ["Видаляє форму", "Скасовує стандартну дію: перезавантаження сторінки", "Відправляє дані", "Очищає поля"], 1, "Зупиняє стандартну поведінку."),
  ("Яка подія спрацьовує на кожну літеру в полі?", ["click", "change", "input", "submit"], 2, "input — при кожній зміні."),
  ("Що поверне input.value, якщо там 5?", ["Число 5", "Рядок '5'", "true", "undefined"], 1, "value — завжди рядок.")])

lesson(18, "js", "Збираємо інтерактивну полицю",
 "Усе разом: рендер карток, додавання, пошук, фільтр, видалення і збереження в браузері. Повноцінний застосунок!",
 ["організувати код навколо функції render()", "реалізувати пошук і фільтр по категорії", "видаляти елементи за id", "зберігати дані в localStorage"],
 [
  H("Архітектура: дані → render → сторінка"),
  P("Головна ідея всіх сучасних застосунків: <b>є масив даних</b>, і <b>є функція render()</b>, яка малює сторінку з цього масиву. Змінились дані — викликали render(). Ніколи не міняємо картки вручну."),
  CODE("text", r'''
  дія людини  →  змінюємо масив items  →  render()  →  оновлена сторінка
  (клік, форма)     (push, filter)          (map → innerHTML)''', title="Цикл застосунку"),
  H("Повний код app.js"),
  CODE("javascript", r'''
// ===== 1. ДАНІ =====
let items = loadItems();

function loadItems() {
  try {
    const saved = localStorage.getItem('polytsia');
    if (saved) return JSON.parse(saved);   // текст → масив
  } catch (e) {}
  return [
    { id: 1, title: 'Minecraft', author: 'Mojang', category: 'гра', rating: 5 },
    { id: 2, title: 'Кобзар', author: 'Т. Шевченко', category: 'книга', rating: 5 },
    { id: 3, title: 'Мавка', author: 'Animagrad', category: 'фільм', rating: 4 }
  ];
}

function saveItems() {
  try {
    localStorage.setItem('polytsia', JSON.stringify(items));  // масив → текст
  } catch (e) {}
}

// ===== 2. ЕЛЕМЕНТИ =====
const cardsEl  = document.querySelector('#cards');
const countEl  = document.querySelector('#count');
const searchEl = document.querySelector('#search');
const filterEl = document.querySelector('#filter');
const formEl   = document.querySelector('#add-form');

// ===== 3. RENDER =====
function stars(n) { return '★'.repeat(n) + '☆'.repeat(5 - n); }

function render() {
  const query = searchEl.value.toLowerCase();
  const cat = filterEl.value;

  const visible = items
    .filter(i => i.title.toLowerCase().includes(query))
    .filter(i => cat === 'усі' || i.category === cat);

  countEl.textContent = `Показано ${visible.length} з ${items.length}`;

  cardsEl.innerHTML = visible.map(i => `
    <article class="card">
      <span class="tag">${i.category}</span>
      <h3>${i.title}</h3>
      <p>${i.author}</p>
      <p class="stars">${stars(i.rating)}</p>
      <button class="del" data-id="${i.id}">🗑️</button>
    </article>
  `).join('') || '<p>Нічого не знайдено 🤷</p>';
}

// ===== 4. ПОДІЇ =====
searchEl.addEventListener('input', render);
filterEl.addEventListener('change', render);

formEl.addEventListener('submit', (e) => {
  e.preventDefault();
  items.push({
    id: Date.now(),                                   // унікальне число
    title: document.querySelector('#title').value,
    author: document.querySelector('#author').value,
    category: document.querySelector('#category').value,
    rating: Number(document.querySelector('#rating').value)
  });
  saveItems();
  render();
  formEl.reset();
});

cardsEl.addEventListener('click', (e) => {          // делегування подій
  if (!e.target.classList.contains('del')) return;
  const id = Number(e.target.dataset.id);
  items = items.filter(i => i.id !== id);
  saveItems();
  render();
});

render();''', title="js/app.js"),
  H("Розбираємо нові штуки"),
  TABLE(["Що", "Навіщо"], [
    ["<code>localStorage</code>", "«Кишеня» браузера: дані залишаються після перезавантаження. Але лише на цьому комп'ютері й у цьому браузері!"],
    ["<code>JSON.stringify / JSON.parse</code>", "localStorage зберігає лише текст: масив → текст і назад"],
    ["<code>id: Date.now()</code>", "Унікальний номер (мілісекунди від 1970 року), щоб точно знати, яку картку видалити"],
    ["<code>data-id</code> + <code>dataset.id</code>", "Свій атрибут у HTML, щоб «приклеїти» id до кнопки"],
    ["Делегування подій", "Один слухач на батьку <code>#cards</code> замість слухача на кожній кнопці. Працює навіть для нових карток"],
    ["<code>try { } catch { }</code>", "«Спробуй, а якщо помилка — не падай». Наприклад, якщо localStorage заборонено"]]),
  CODE("html", r'''
<input id="search" placeholder="🔍 Пошук...">
<select id="filter">
  <option>усі</option><option>гра</option><option>книга</option><option>фільм</option>
</select>
<p id="count"></p>
<div class="cards" id="cards"></div>''', title="index.html — потрібні елементи"),
  WARN("Проблема, яку ми розв'яжемо далі: localStorage живе <b>лише в одному браузері</b>. Друг не побачить твою полицю, а вдома буде порожньо. Щоб дані бачили всі й усюди, потрібен <b>сервер і база даних</b>. До цього ми скоро дійдемо! 🚀"),
 ],
 "Зроби повністю робочу полицю за кодом уроку: рендер, пошук, фільтр, додавання, видалення, збереження. Адаптуй категорії й поля під свою тему. Не копіюй бездумно: перед кожним блоком коду напиши коментар своїми словами.",
 ["Додай річ → онови сторінку (F5) → вона на місці", "F12 → <b>Application</b> → Local Storage → твій сайт: там лежить JSON твоєї полиці", "Пошук не чутливий до регістру: «mine» знаходить «Minecraft»", "Console порожня, без червоного"],
 [("Обов'язково", "Доведи полицю до робочого стану. Принеси на урок і покажи, як працюють пошук і видалення."),
  ("Середній", "Додай сортування: select «За оцінкою / За назвою / Нові спочатку»."),
  ("Зірочка ⭐", "Додай редагування оцінки: клік по зірочках змінює rating.")],
 [("Навіщо JSON.stringify перед localStorage.setItem?", ["Для швидкості", "localStorage зберігає лише текст", "Щоб зашифрувати", "Не потрібно"], 1, "Масив треба перетворити на текст."),
  ("Що робить функція render() у нашій архітектурі?", ["Зберігає дані", "Малює сторінку з поточного масиву даних", "Видаляє картки", "Відправляє на сервер"], 1, "Дані → render → сторінка."),
  ("Головний недолік localStorage?", ["Повільний", "Дані лише в одному браузері на одному пристрої", "Не зберігає українські літери", "Платний"], 1, "Тому далі — база даних.")])
