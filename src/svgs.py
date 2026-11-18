F = "font-family='Golos Text, system-ui, sans-serif'"
M = "font-family='JetBrains Mono, monospace'"

WEB = f"""<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" {F}>
<defs><marker id="ar" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1D1B26"/></marker></defs>
<rect x="20" y="40" width="210" height="170" rx="16" fill="#fff" stroke="#1D1B26" stroke-width="2"/>
<rect x="20" y="40" width="210" height="32" rx="16" fill="#F0622E"/><rect x="20" y="58" width="210" height="14" fill="#F0622E"/>
<circle cx="40" cy="56" r="5" fill="#fff"/><circle cx="56" cy="56" r="5" fill="#fff"/><circle cx="72" cy="56" r="5" fill="#fff"/>
<rect x="40" y="88" width="120" height="12" rx="6" fill="#1D1B26"/><rect x="40" y="110" width="170" height="8" rx="4" fill="#E7E1D6"/><rect x="40" y="126" width="150" height="8" rx="4" fill="#E7E1D6"/><rect x="40" y="148" width="80" height="40" rx="8" fill="#2F6FEB"/><rect x="130" y="148" width="80" height="40" rx="8" fill="#E8A400"/>
<text x="125" y="236" text-anchor="middle" font-size="16" font-weight="700" fill="#1D1B26">Браузер (клієнт)</text>
<rect x="530" y="40" width="210" height="170" rx="16" fill="#fff" stroke="#1D1B26" stroke-width="2"/>
<rect x="555" y="64" width="160" height="30" rx="6" fill="#1D1B26"/><circle cx="572" cy="79" r="5" fill="#18A058"/>
<rect x="555" y="104" width="160" height="30" rx="6" fill="#1D1B26"/><circle cx="572" cy="119" r="5" fill="#18A058"/>
<rect x="555" y="144" width="160" height="30" rx="6" fill="#1D1B26"/><circle cx="572" cy="159" r="5" fill="#E8A400"/>
<text x="635" y="236" text-anchor="middle" font-size="16" font-weight="700" fill="#1D1B26">Сервер</text>
<line x1="240" y1="100" x2="520" y2="100" stroke="#1D1B26" stroke-width="2.5" marker-end="url(#ar)"/>
<text x="380" y="88" text-anchor="middle" font-size="15" fill="#1D1B26">① Запит: «дай мені index.html»</text>
<line x1="520" y1="160" x2="240" y2="160" stroke="#F0622E" stroke-width="2.5" marker-end="url(#ar)"/>
<text x="380" y="186" text-anchor="middle" font-size="15" fill="#F0622E">② Відповідь: HTML + CSS + JS</text>
<text x="380" y="30" text-anchor="middle" font-size="14" fill="#6B6878">Інтернет</text>
</svg>"""

TAG = f"""<svg viewBox="0 0 760 210" xmlns="http://www.w3.org/2000/svg" {F}>
<rect x="10" y="60" width="740" height="70" rx="14" fill="#1D1B26"/>
<text x="40" y="106" font-size="30" {M} fill="#fff"><tspan fill="#F0622E">&lt;p</tspan> <tspan fill="#E8A400">class</tspan><tspan fill="#fff">=</tspan><tspan fill="#7EE2A8">"note"</tspan><tspan fill="#F0622E">&gt;</tspan>Привіт, світе!<tspan fill="#F0622E">&lt;/p&gt;</tspan></text>
<path d="M40 140 v14 h150 v-14" fill="none" stroke="#F0622E" stroke-width="2"/><text x="115" y="176" text-anchor="middle" font-size="15" fill="#1D1B26">відкривальний тег</text>
<path d="M88 50 v-14 h165 v14" fill="none" stroke="#E8A400" stroke-width="2"/><text x="170" y="26" text-anchor="middle" font-size="15" fill="#1D1B26">атрибут = значення</text>
<path d="M290 140 v14 h250 v-14" fill="none" stroke="#18A058" stroke-width="2"/><text x="415" y="176" text-anchor="middle" font-size="15" fill="#1D1B26">вміст (те, що бачить людина)</text>
<path d="M560 50 v-14 h105 v14" fill="none" stroke="#F0622E" stroke-width="2"/><text x="612" y="26" text-anchor="middle" font-size="15" fill="#1D1B26">закривальний тег</text>
<text x="380" y="204" text-anchor="middle" font-size="14" fill="#6B6878">Весь цей рядок разом — це ЕЛЕМЕНТ</text>
</svg>"""

LAYOUT = f"""<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" {F} font-size="16" font-weight="700">
<rect x="10" y="10" width="740" height="56" rx="10" fill="#FFE3D6" stroke="#F0622E" stroke-width="2"/><text x="30" y="44" fill="#1D1B26">&lt;header&gt; — шапка: логотип, назва</text>
<rect x="430" y="20" width="300" height="36" rx="8" fill="#fff" stroke="#F0622E" stroke-width="2"/><text x="450" y="44" fill="#1D1B26" font-size="14">&lt;nav&gt; — меню</text>
<rect x="10" y="78" width="530" height="180" rx="10" fill="#DCE8FF" stroke="#2F6FEB" stroke-width="2"/><text x="30" y="106" fill="#1D1B26">&lt;main&gt; — головний вміст</text>
<rect x="30" y="120" width="235" height="120" rx="8" fill="#fff" stroke="#2F6FEB" stroke-width="2"/><text x="46" y="148" font-size="14" fill="#1D1B26">&lt;section&gt;</text><text x="46" y="170" font-size="13" font-weight="400" fill="#6B6878">розділ сторінки</text>
<rect x="285" y="120" width="235" height="120" rx="8" fill="#fff" stroke="#2F6FEB" stroke-width="2"/><text x="301" y="148" font-size="14" fill="#1D1B26">&lt;article&gt;</text><text x="301" y="170" font-size="13" font-weight="400" fill="#6B6878">самостійна картка/стаття</text>
<rect x="552" y="78" width="198" height="180" rx="10" fill="#FFF3CC" stroke="#E8A400" stroke-width="2"/><text x="570" y="106" fill="#1D1B26">&lt;aside&gt;</text><text x="570" y="128" font-size="13" font-weight="400" fill="#6B6878">бічна панель,</text><text x="570" y="146" font-size="13" font-weight="400" fill="#6B6878">додаткове</text>
<rect x="10" y="270" width="740" height="50" rx="10" fill="#D7F5E3" stroke="#18A058" stroke-width="2"/><text x="30" y="301" fill="#1D1B26">&lt;footer&gt; — підвал: контакти, автор, рік</text>
</svg>"""

RULE = f"""<svg viewBox="0 0 760 230" xmlns="http://www.w3.org/2000/svg" {F}>
<rect x="10" y="50" width="740" height="130" rx="14" fill="#1D1B26"/>
<text x="40" y="100" font-size="30" {M} fill="#7FB0FF">.card <tspan fill="#fff">{{</tspan></text>
<text x="80" y="140" font-size="30" {M} fill="#E8A400">background<tspan fill="#fff">:</tspan> <tspan fill="#7EE2A8">white</tspan><tspan fill="#fff">;</tspan></text>
<text x="500" y="140" font-size="30" {M} fill="#fff">}}</text>
<path d="M40 40 v-12 h96 v12" fill="none" stroke="#2F6FEB" stroke-width="2"/><text x="88" y="20" text-anchor="middle" font-size="15" fill="#1D1B26">селектор: КОГО стилізуємо</text>
<path d="M80 190 v12 h180 v-12" fill="none" stroke="#E8A400" stroke-width="2"/><text x="170" y="224" text-anchor="middle" font-size="15" fill="#1D1B26">властивість: ЩО міняємо</text>
<path d="M290 190 v12 h110 v-12" fill="none" stroke="#18A058" stroke-width="2"/><text x="420" y="224" text-anchor="middle" font-size="15" fill="#1D1B26">значення: ЯК саме</text>
<text x="560" y="100" font-size="14" fill="#9C98A8">{{ }} — блок правил</text><text x="560" y="124" font-size="14" fill="#9C98A8">; — кінець рядка</text>
</svg>"""

BOX = f"""<svg viewBox="0 0 760 330" xmlns="http://www.w3.org/2000/svg" {F} font-weight="700">
<rect x="20" y="10" width="720" height="310" rx="6" fill="#FFF3CC" stroke="#E8A400" stroke-dasharray="8 6" stroke-width="2"/><text x="40" y="38" font-size="16" fill="#9A6B00">margin — зовнішній відступ (простір між сусідами)</text>
<rect x="80" y="55" width="600" height="230" rx="6" fill="#1D1B26"/><text x="100" y="80" font-size="16" fill="#fff">border — рамка</text>
<rect x="92" y="90" width="576" height="183" rx="4" fill="#D7F5E3"/><text x="112" y="116" font-size="16" fill="#0E6B39">padding — внутрішній відступ (від рамки до вмісту)</text>
<rect x="200" y="135" width="360" height="110" rx="4" fill="#DCE8FF" stroke="#2F6FEB" stroke-width="2"/><text x="380" y="185" text-anchor="middle" font-size="20" fill="#1D1B26">content — вміст</text><text x="380" y="212" text-anchor="middle" font-size="14" font-weight="400" fill="#2F6FEB">width × height</text>
</svg>"""

FLEX = f"""<svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" {F}>
<defs><marker id="a2" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#F0622E"/></marker><marker id="a3" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#2F6FEB"/></marker></defs>
<rect x="60" y="30" width="640" height="180" rx="14" fill="#fff" stroke="#1D1B26" stroke-width="2"/>
<text x="76" y="56" font-size="14" {M} fill="#6B6878">display: flex</text>
<rect x="90" y="80" width="140" height="100" rx="10" fill="#F0622E"/><text x="160" y="137" text-anchor="middle" fill="#fff" font-size="20" font-weight="700">1</text>
<rect x="250" y="80" width="140" height="100" rx="10" fill="#2F6FEB"/><text x="320" y="137" text-anchor="middle" fill="#fff" font-size="20" font-weight="700">2</text>
<rect x="410" y="80" width="140" height="100" rx="10" fill="#E8A400"/><text x="480" y="137" text-anchor="middle" fill="#fff" font-size="20" font-weight="700">3</text>
<text x="240" y="76" text-anchor="middle" font-size="12" fill="#6B6878">gap</text>
<line x1="60" y1="240" x2="700" y2="240" stroke="#F0622E" stroke-width="3" marker-end="url(#a2)"/><text x="380" y="262" text-anchor="middle" font-size="15" font-weight="700" fill="#F0622E">головна вісь → justify-content</text>
<line x1="30" y1="30" x2="30" y2="210" stroke="#2F6FEB" stroke-width="3" marker-end="url(#a3)"/><text x="20" y="120" font-size="15" font-weight="700" fill="#2F6FEB" transform="rotate(-90 20 120)" text-anchor="middle">поперечна → align-items</text>
</svg>"""

DOM = f"""<svg viewBox="0 0 760 300" xmlns="http://www.w3.org/2000/svg" {F} font-size="15" font-weight="700">
<g stroke="#9C98A8" stroke-width="2"><line x1="380" y1="48" x2="380" y2="80"/><line x1="380" y1="110" x2="200" y2="150"/><line x1="380" y1="110" x2="560" y2="150"/><line x1="200" y1="180" x2="200" y2="220"/><line x1="560" y1="180" x2="440" y2="220"/><line x1="560" y1="180" x2="560" y2="220"/><line x1="560" y1="180" x2="680" y2="220"/></g>
<rect x="310" y="18" width="140" height="32" rx="16" fill="#1D1B26"/><text x="380" y="39" text-anchor="middle" fill="#fff">document</text>
<rect x="320" y="80" width="120" height="32" rx="16" fill="#F0622E"/><text x="380" y="101" text-anchor="middle" fill="#fff">html</text>
<rect x="140" y="150" width="120" height="32" rx="16" fill="#F0622E"/><text x="200" y="171" text-anchor="middle" fill="#fff">head</text>
<rect x="500" y="150" width="120" height="32" rx="16" fill="#F0622E"/><text x="560" y="171" text-anchor="middle" fill="#fff">body</text>
<rect x="140" y="220" width="120" height="32" rx="16" fill="#fff" stroke="#F0622E" stroke-width="2"/><text x="200" y="241" text-anchor="middle" fill="#1D1B26">title</text>
<rect x="390" y="220" width="100" height="32" rx="16" fill="#fff" stroke="#F0622E" stroke-width="2"/><text x="440" y="241" text-anchor="middle" fill="#1D1B26">h1</text>
<rect x="510" y="220" width="100" height="32" rx="16" fill="#fff" stroke="#F0622E" stroke-width="2"/><text x="560" y="241" text-anchor="middle" fill="#1D1B26">form</text>
<rect x="630" y="220" width="100" height="32" rx="16" fill="#E8A400"/><text x="680" y="241" text-anchor="middle" fill="#fff">#list</text>
<text x="680" y="285" text-anchor="middle" font-weight="400" font-size="13" fill="#6B6878">querySelector('#list')</text>
</svg>"""

TABLEFIG = f"""<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" {F} font-size="15">
<text x="20" y="26" font-weight="700" fill="#18A058" font-size="17">Таблиця items</text>
<rect x="20" y="40" width="720" height="40" rx="8" fill="#18A058"/>
<g fill="#fff" font-weight="700"><text x="40" y="66">id</text><text x="110" y="66">title</text><text x="350" y="66">category</text><text x="500" y="66">rating</text><text x="600" y="66">created_at</text></g>
<g fill="#1D1B26">
<rect x="20" y="84" width="720" height="38" fill="#fff" stroke="#E7E1D6"/><text x="40" y="108">1</text><text x="110" y="108">Тіні забутих предків</text><text x="350" y="108">книга</text><text x="500" y="108">5</text><text x="600" y="108">2026-11-01</text>
<rect x="20" y="122" width="720" height="38" fill="#F3FBF6" stroke="#E7E1D6"/><text x="40" y="146">2</text><text x="110" y="146">Minecraft</text><text x="350" y="146">гра</text><text x="500" y="146">4</text><text x="600" y="146">2026-11-02</text>
<rect x="20" y="160" width="720" height="38" fill="#fff" stroke="#E7E1D6"/><text x="40" y="184">3</text><text x="110" y="184">Мавка. Лісова пісня</text><text x="350" y="184">фільм</text><text x="500" y="184">5</text><text x="600" y="184">2026-11-03</text>
</g>
<text x="380" y="232" text-anchor="middle" fill="#6B6878">↔ рядок = один запис       ↕ стовпець = одна властивість       id = унікальний ключ</text>
</svg>"""

STACK = f"""<svg viewBox="0 0 760 250" xmlns="http://www.w3.org/2000/svg" {F}>
<defs><marker id="a4" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1D1B26"/></marker></defs>
<rect x="15" y="50" width="200" height="130" rx="16" fill="#FFE3D6" stroke="#F0622E" stroke-width="2"/><text x="115" y="95" text-anchor="middle" font-size="18" font-weight="700" fill="#1D1B26">Фронтенд</text><text x="115" y="120" text-anchor="middle" font-size="13" fill="#6B6878">HTML · CSS · JS</text><text x="115" y="140" text-anchor="middle" font-size="13" fill="#6B6878">в браузері</text>
<rect x="280" y="50" width="200" height="130" rx="16" fill="#DCE8FF" stroke="#2F6FEB" stroke-width="2"/><text x="380" y="95" text-anchor="middle" font-size="18" font-weight="700" fill="#1D1B26">Бекенд</text><text x="380" y="120" text-anchor="middle" font-size="13" fill="#6B6878">сервер, правила,</text><text x="380" y="140" text-anchor="middle" font-size="13" fill="#6B6878">секретні ключі</text>
<rect x="545" y="50" width="200" height="130" rx="16" fill="#D7F5E3" stroke="#18A058" stroke-width="2"/><text x="645" y="95" text-anchor="middle" font-size="18" font-weight="700" fill="#1D1B26">База даних</text><text x="645" y="120" text-anchor="middle" font-size="13" fill="#6B6878">таблиці, що</text><text x="645" y="140" text-anchor="middle" font-size="13" fill="#6B6878">зберігаються назавжди</text>
<line x1="218" y1="98" x2="275" y2="98" stroke="#1D1B26" stroke-width="2" marker-end="url(#a4)"/><line x1="277" y1="132" x2="220" y2="132" stroke="#1D1B26" stroke-width="2" marker-end="url(#a4)"/>
<line x1="483" y1="98" x2="540" y2="98" stroke="#1D1B26" stroke-width="2" marker-end="url(#a4)"/><line x1="542" y1="132" x2="485" y2="132" stroke="#1D1B26" stroke-width="2" marker-end="url(#a4)"/>
<text x="247" y="210" text-anchor="middle" font-size="13" fill="#1D1B26">fetch → JSON</text><text x="512" y="210" text-anchor="middle" font-size="13" fill="#1D1B26">SQL</text>
<text x="380" y="30" text-anchor="middle" font-size="14" fill="#6B6878">Повний стек: що бачить користувач → хто приймає рішення → де лежать дані</text>
<text x="380" y="240" text-anchor="middle" font-size="13" fill="#18A058">Supabase = готовий бекенд + база в одному</text>
</svg>"""

FETCH = f"""<svg viewBox="0 0 760 240" xmlns="http://www.w3.org/2000/svg" {F}>
<defs><marker id="a5" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#1D1B26"/></marker></defs>
<rect x="15" y="20" width="250" height="200" rx="14" fill="#1D1B26"/><text x="35" y="50" font-size="14" fill="#9C98A8" {M}>// браузер</text>
<text x="35" y="80" font-size="14" fill="#7FB0FF" {M}>const res = await</text><text x="35" y="102" font-size="14" fill="#E8A400" {M}>  fetch('/api/items')</text><text x="35" y="132" font-size="14" fill="#7FB0FF" {M}>const data = await</text><text x="35" y="154" font-size="14" fill="#E8A400" {M}>  res.json()</text>
<line x1="275" y1="80" x2="480" y2="80" stroke="#1D1B26" stroke-width="2.5" marker-end="url(#a5)"/><text x="378" y="68" text-anchor="middle" font-size="14" fill="#1D1B26">GET /api/items</text>
<line x1="480" y1="160" x2="275" y2="160" stroke="#18A058" stroke-width="2.5" marker-end="url(#a5)"/><text x="378" y="150" text-anchor="middle" font-size="14" fill="#18A058">200 OK + JSON</text>
<rect x="490" y="20" width="255" height="200" rx="14" fill="#fff" stroke="#1D1B26" stroke-width="2"/><text x="510" y="50" font-size="14" fill="#6B6878" {M}>відповідь (JSON)</text>
<text x="510" y="82" font-size="14" fill="#1D1B26" {M}>[</text><text x="525" y="104" font-size="14" fill="#1D1B26" {M}>{{ "id": 1,</text><text x="540" y="126" font-size="14" fill="#18A058" {M}>"title": "Minecraft",</text><text x="540" y="148" font-size="14" fill="#2F6FEB" {M}>"rating": 4 }}</text><text x="510" y="170" font-size="14" fill="#1D1B26" {M}>]</text>
</svg>"""

AILOOP = f"""<svg viewBox="0 0 760 260" xmlns="http://www.w3.org/2000/svg" {F} font-weight="700" font-size="15">
<defs><marker id="a6" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#8B5CF6"/></marker></defs>
<g fill="none" stroke="#8B5CF6" stroke-width="2.5" marker-end="url(#a6)"><path d="M190 70 Q 300 20 400 60"/><path d="M560 90 Q 640 130 580 185"/><path d="M420 215 Q 330 245 230 210"/><path d="M110 180 Q 60 130 110 90"/></g>
<rect x="40" y="40" width="160" height="60" rx="30" fill="#8B5CF6"/><text x="120" y="66" text-anchor="middle" fill="#fff">1. Опиши задачу</text><text x="120" y="86" text-anchor="middle" fill="#EDE5FF" font-size="12" font-weight="400">контекст + мета</text>
<rect x="400" y="40" width="200" height="60" rx="30" fill="#fff" stroke="#8B5CF6" stroke-width="2"/><text x="500" y="66" text-anchor="middle" fill="#1D1B26">2. Отримай відповідь</text><text x="500" y="86" text-anchor="middle" fill="#6B6878" font-size="12" font-weight="400">код + пояснення</text>
<rect x="430" y="180" width="200" height="60" rx="30" fill="#fff" stroke="#8B5CF6" stroke-width="2"/><text x="530" y="206" text-anchor="middle" fill="#1D1B26">3. Прочитай і запусти</text><text x="530" y="226" text-anchor="middle" fill="#6B6878" font-size="12" font-weight="400">чи я розумію кожен рядок?</text>
<rect x="40" y="170" width="190" height="60" rx="30" fill="#fff" stroke="#8B5CF6" stroke-width="2"/><text x="135" y="196" text-anchor="middle" fill="#1D1B26">4. Уточни / виправ</text><text x="135" y="216" text-anchor="middle" fill="#6B6878" font-size="12" font-weight="400">помилка? покажи її AI</text>
<text x="330" y="140" text-anchor="middle" fill="#8B5CF6" font-size="17">Ти — капітан, AI — штурман</text>
</svg>"""

DEVTOOLS = f"""<svg viewBox="0 0 760 270" xmlns="http://www.w3.org/2000/svg" {F}>
<rect x="10" y="10" width="740" height="250" rx="14" fill="#fff" stroke="#1D1B26" stroke-width="2"/>
<rect x="10" y="10" width="380" height="250" rx="14" fill="#FBF8F3"/><text x="30" y="44" font-size="15" font-weight="700" fill="#1D1B26">Твоя сторінка</text><rect x="30" y="60" width="200" height="16" rx="8" fill="#1D1B26"/><rect x="30" y="90" width="330" height="70" rx="10" fill="#DCE8FF" stroke="#2F6FEB" stroke-width="3" stroke-dasharray="6 4"/><text x="195" y="130" text-anchor="middle" font-size="13" fill="#2F6FEB">виділений елемент</text><rect x="30" y="175" width="160" height="60" rx="10" fill="#FFE3D6"/><rect x="200" y="175" width="160" height="60" rx="10" fill="#FFF3CC"/>
<rect x="390" y="10" width="360" height="36" fill="#1D1B26"/><g font-size="13" font-weight="700"><text x="405" y="33" fill="#E8A400">Elements</text><text x="480" y="33" fill="#fff">Console</text><text x="548" y="33" fill="#fff">Network</text><text x="618" y="33" fill="#fff">📱</text><text x="650" y="33" fill="#fff">Lighthouse</text></g>
<g font-size="13" {M}><text x="405" y="72" fill="#F0622E">&lt;main&gt;</text><rect x="398" y="80" width="345" height="22" fill="#DCE8FF"/><text x="420" y="96" fill="#F0622E">&lt;section class="card"&gt;</text><text x="405" y="122" fill="#F0622E">&lt;/main&gt;</text></g>
<line x1="390" y1="140" x2="750" y2="140" stroke="#E7E1D6" stroke-width="2"/><text x="405" y="162" font-size="12" fill="#6B6878" font-weight="700">Styles</text>
<g font-size="13" {M}><text x="405" y="186" fill="#2F6FEB">.card {{</text><text x="420" y="206" fill="#1D1B26">padding: <tspan fill="#18A058">16px</tspan>;</text><text x="420" y="226" fill="#1D1B26" text-decoration="line-through">color: red;</text><text x="405" y="246" fill="#2F6FEB">}}</text></g>
<text x="620" y="215" font-size="12" fill="#6B6878">← правиш тут,</text><text x="620" y="232" font-size="12" fill="#6B6878">бачиш одразу</text>
</svg>"""
