# -*- coding: utf-8 -*-
from h import box, src, table, module, path, hg

S = "Shooting"; E = "Exposure/Color"; F = "Focus"; P = "Playback"; N = "Network"; U = "Setup"


def p(*a):
    return path("MENU", *a)


# (EN, UA, path, що означає, значення, початківцю, коли змінювати, рівень)
MENU = [
    # ---- Відразу
    ("Language", "Мова", p(U, "Area/Date", "Language"), "мова інтерфейсу", "список мов камери", "English (у курсі всі назви англійські)", "—", 1),
    ("Area/Date/Time Setting", "Регіон, дата, час", p(U, "Area/Date", "Area/Date/Time Setting"), "часовий пояс, літній час, дата", "регіон, DST On/Off, дата/час", "Київ (GMT+2), правильний час", "подорожі в інший часовий пояс", 1),
    ("Format", "Форматування", p(S, "Media", "Format"), "повністю очищає карту й готує її під камеру", "Slot 1 / Slot 2", "форматуйте кожну нову карту в камері", "після перенесення й резервування фото", 1),
    ("File Format (still)", "Формат файлу", p(S, "Image Quality", "Image Quality Settings", "File Format"), "у чому зберігати фото", "RAW · RAW & JPEG · RAW & HEIF · JPEG · HEIF", "<b>RAW & JPEG</b>", "JPEG — щоб заощадити місце на подорожі", 1),
    ("RAW File Type", "Тип RAW", p(S, "Image Quality", "Image Quality Settings", "RAW File Type"), "стиснення RAW", "Uncompressed · Lossless Comp (L/M/S) · Compressed", "<b>Lossless Comp (L)</b>: якість без втрат, файл менший", "Compressed — для дуже довгих серій", 1),
    ("JPEG Quality / JPEG Image Size", "Якість і розмір JPEG", p(S, "Image Quality", "Image Quality Settings", "JPEG Quality"), "стиснення та роздільність JPEG", "Extra fine / Fine / Standard / Light; L / M / S", "Fine, L", "Extra fine — для друку з JPEG", 1),
    ("JPEG/HEIF Switch", "JPEG чи HEIF", p(S, "Image Quality", "JPEG/HEIF Switch"), "що писати поруч із RAW", "JPEG / HEIF", "JPEG (максимальна сумісність)", "HEIF 10-bit — для HDR-екранів Apple", 1),
    ("Aspect Ratio", "Співвідношення сторін", p(S, "Image Quality", "Aspect Ratio"), "форма кадру JPEG/HEIF (RAW завжди 3:2)", "3:2 · 4:3 · 16:9 · 1:1", "3:2", "16:9 — для заставок, 1:1 — для Instagram", 1),
    ("Recording Media", "Карта для запису", p(S, "Media", "Rec. Media Settings", "Recording Media"), "на який слот писати", "Slot 1 · Slot 2 · Simult. Recording · Sort Recording", "Slot 1 (заводське)", "друга карта → Simult. для важливих подій", 1),
    ("Release w/o Card", "Спуск без карти", p(S, "Shutter/Silent", "Release w/o Card"), "чи знімати, коли карти немає", "Enable / Disable", "<b>Disable</b>: щоб не «знімати в нікуди»", "—", 1),
    ("SteadyShot", "Стабілізація", p(S, "Image Stabilization", "SteadyShot"), "стабілізація матрицею", "On / Off (фото); для відео — окремо", "On. На штативі — Off", "штатив", 1),
    ("ISO / ISO Range Limit", "ISO / межі ISO AUTO", p(E, "Exposure", "ISO Range Limit"), "межі, в яких камера обирає ISO", "мінімум і максимум", "ISO AUTO 100–12800", "у темряві — до 25600", 1),
    ("ISO AUTO Min. SS", "Мінімальна витримка для ISO AUTO", p(E, "Exposure", "ISO AUTO Min. SS"), "за якої витримки камера починає піднімати ISO (режими P/A)", "SLOWER · SLOW · STD · FAST · FASTER (крок 1 EV) або конкретне 1/8000–30 с", "<b>FAST</b> або 1/250 для людей", "1/500 для дітей, 1/60 для статики", 1),
    ("White Balance", "Баланс білого", p(E, "White Balance", "White Balance"), "колір світла", "AWB, денне світло, тінь, хмарно, лампи, температура K, Custom", "AWB", "змішане світло → Custom", 1),
    ("Focus Mode", "Режим фокусування", p(F, "AF/MF", "Focus Mode"), "модуль 5.1", "AF-S · AF-A · AF-C · DMF · MF", "AF-C", "статика — AF-S", 1),
    ("Focus Area", "Зона фокусування", p(F, "Focus Area", "Focus Area"), "модуль 5.3", "Wide · Zone · Center Fix · Spot XL/L/M/S · Expand Spot · Custom · Tracking", "Wide", "предмети — Spot", 1),
    ("Face/Eye Prior. in AF", "Пріоритет обличчя/очей", p(F, "Face/Eye AF", "Face/Eye Prior. in AF"), "шукати обличчя й очі", "On / Off", "On", "пейзаж — можна Off", 1),
    ("Face/Eye Subject", "Об'єкт розпізнавання", p(F, "Face/Eye AF", "Face/Eye Subject"), "кого шукати", "Human · Animal · Bird", "Human", "тварини, птахи", 1),
    ("Drive Mode", "Режим протяжки", p(S, "Drive Mode", "Drive Mode"), "один кадр, серія, автоспуск, брекетинг", "Single · Cont. (Hi+/Hi/Mid/Lo) · Self-timer · Bracket · Focus Bracket", "Single; для руху — Cont. Mid", "діти, спорт — Hi", 1),
    ("Grid Line Display / Type", "Сітка", p(S, "Shooting Display", "Grid Line Display"), "лінії для композиції", "Off / On; Rule of 3rds, Square, Diag. + Square", "On, Rule of 3rds", "архітектура — Square", 1),
    ("DISP (Screen Disp) Set", "Вигляди екрана", p(U, "Operation Customize", "DISP (Screen Disp) Set"), "які екрани перемикає DISP", "з інформацією, гістограма, рівень, без інформації…", "увімкніть варіант з гістограмою", "—", 1),
    ("Touch Operation", "Сенсорне керування", p(U, "Touch Operation", "Touch Operation"), "дозволити дотики", "On / Off (+ Touch Panel/Pad)", "On", "якщо носом зсуваєте фокус — вимкніть Touch Panel у видошукачі", 1),
    # ---- Корисно знати
    ("Exposure Comp.", "Експокорекція", p(E, "Exposure Comp.", "Exposure Comp."), "світліше/темніше в P/A/S і M з ISO AUTO", "±5 EV", "0, змінюйте за потреби", "сніг, контрове світло", 2),
    ("Exposure step", "Крок експозиції", p(E, "Exposure Comp.", "Exposure step"), "крок змін", "0.3EV / 0.5EV", "0.3EV", "—", 2),
    ("Metering Mode", "Режим заміру", p(E, "Metering", "Metering Mode"), "як камера оцінює яскравість", "Multi · Center · Spot · Entire Screen Avg. · Highlight", "Multi", "сцена з прожектором — Highlight або Spot", 2),
    ("Face Priority in Multi Metering", "Пріоритет обличчя під час заміру", p(E, "Metering", "Face Priority in Multi Metering"), "експозиція «на обличчя»", "On / Off", "On", "—", 2),
    ("AEL w/ Shutter", "AEL кнопкою спуску", p(E, "Metering", "AEL w/ Shutter"), "чи фіксує напівнатискання експозицію", "Auto / On / Off", "Auto", "—", 2),
    ("D-Range Optimizer", "Оптимізатор динамічного діапазону", p(E, "Color/Tone", "D-Range Optimizer"), "вирівнює контраст у JPEG/HEIF", "Off · Auto · Lv1–Lv5", "Auto для JPEG. Якщо працюєте з RAW — Off", "контрове світло без RAW", 2),
    ("Creative Look", "Стиль зображення", p(E, "Color/Tone", "Creative Look"), "колір і тон JPEG/HEIF", "ST · PT · NT · VV · VV2 · FL · IN · SH · BW · SE + 6 Custom; Contrast, Highlights, Shadows, Fade, Saturation, Sharpness, Sharpness Range, Clarity", "ST або PT для людей", "FL, IN — для настрою", 2),
    ("Soft Skin Effect", "Згладжування шкіри", p(E, "Color/Tone", "Soft Skin Effect"), "розмиває дрібні вади шкіри в JPEG", "Off / Low / Mid / High", "Off або Low", "—", 2),
    ("Priority Set in AWB", "Пріоритет AWB", p(E, "White Balance", "Priority Set in AWB"), "поведінка AWB у теплому світлі", "Standard / Ambience / White", "Standard", "свічки — Ambience", 2),
    ("Lens Compensation", "Корекція об'єктива", p(S, "Image Quality", "Lens Compensation"), "корекція віньєтування, хроматичних аберацій, дисторсії (Tamron підтримує)", "Shading / Chro. Aberration / Distortion: Auto / Off", "Auto", "—", 2),
    ("High ISO NR / Long Exposure NR", "Шумозаглушення", p(S, "Image Quality", "High ISO NR"), "шумозаглушення JPEG / темновий кадр на довгій витримці", "Normal / Low / Off; On / Off", "Normal; Long Exp. NR On", "серії нічних кадрів — Long Exp. NR Off", 2),
    ("Color Space", "Колірний простір", p(S, "Image Quality", "Color Space"), "sRGB для екранів, AdobeRGB для друку", "sRGB / AdobeRGB", "sRGB", "друк у професійній лабораторії", 2),
    ("Zebra Display / Level", "Зебра", p(E, "Zebra Display", "Zebra Display"), "смуги на пересвічених ділянках", "Off / On; рівні", "On, рівень 100+ (для фото)", "—", 2),
    ("Peaking Display", "Пікінг", p(F, "Peaking Display", "Peaking Display"), "підсвітка різких контурів у MF/DMF", "On / Off; Level; Color", "On, Mid, Red", "—", 2),
    ("Auto Magnifier in MF", "Автозбільшення в MF", p(F, "Focus Assistant", "Auto Magnifier in MF"), "збільшення при обертанні кільця", "On / Off", "On", "—", 2),
    ("AF w/ Shutter", "AF кнопкою спуску", p(F, "AF/MF", "AF w/ Shutter"), "чи фокусує спуск", "On / Off", "On (до переходу на BBF)", "BBF — Off", 2),
    ("Shutter Type", "Тип затвора", p(S, "Shutter/Silent", "Shutter Type"), "механічний чи електронний (тільки P/A/S/M)", "Mechanical Shutter / Electronic Shutter", "Mechanical", "Electronic — тиша, 1/8000 на сонці. Без спалаху й Bulb", 2),
    ("e-Front Curtain Shut.", "Електронна передня шторка", p(S, "Shutter/Silent", "e-Front Curtain Shut."), "менше вібрацій і затримки", "On / Off", "On", "довгі витримки чи спалах HSS — інколи Off", 2),
    ("Silent Mode Settings", "Безшумний режим", p(S, "Shutter/Silent", "Silent Mode Settings"), "набір налаштувань для тиші", "On / Off + деталі", "Off; On — у церкві, на концерті", "див. сценарії", 2),
    ("Anti-flicker Set.", "Захист від мерехтіння", p(S, "Shutter/Silent", "Anti-flicker Set."), "захист від смуг під LED-лампами", "Anti-flicker Shoot. (фото); Var. Shutter (S/M)", "Off; On у спортзалах і школах", "модуль 14", 2),
    ("Auto Review", "Автоперегляд", p(U, "Display Option", "Auto Review"), "показувати кадр одразу після зйомки", "Off / 2 с / 5 с / 10 с", "Off або 2 с", "—", 2),
    ("Power Save Start Time", "Час до енергозбереження", p(U, "Power Setting Option", "Power Save Start Time"), "через скільки хвилин камера засинає", "кілька варіантів", "1 хв", "—", 2),
    ("Audio signals", "Звукові сигнали", p(U, "Sound Option", "Audio signals"), "біп підтвердження фокуса", "On / Off", "Off для подій", "—", 2),
    ("Monitor / Viewfinder Brightness", "Яскравість екрана й видошукача", p(U, "Finder/Monitor", "Monitor Brightness"), "яскравість екрана, а не фото", "Manual / Sunny Weather", "Manual 0 (інакше фото на ПК здадуться темнішими)", "на сонці — тимчасово", 2),
    ("Fn Menu Settings", "Вміст меню Fn", p(U, "Operation Customize", "Fn Menu Settings"), "які функції в Fn", "набір клітинок для фото й для відео", "модуль 7.15", "—", 2),
    ("Custom Key/Dial Set.", "Кнопки та диски", p(U, "Operation Customize", "Custom Key/Dial Set."), "призначення C1–C4, AF-ON, AEL, дисків, кнопки об'єктива", "сотні функцій", "модуль 7.14", "—", 2),
    ("My Menu Setting", "Моє меню", p("My Menu", "My Menu Setting", "Add Item"), "власна сторінка меню", "Add / Sort / Delete Item, Display From My Menu", "модуль 7.16", "—", 2),
    ("Camera Set. Memory", "Збереження режимів 1/2/3", p(S, "Shooting Mode", "Camera Set. Memory"), "запам'ятати набір у слот диска", "1, 2, 3 (+ M1–M4 на карті)", "модуль 4.8", "—", 2),
    ("Smartphone Connection", "Підключення до смартфона", p(N, "Cnct./Remote Sht.", "Smartphone Connection"), "сполучення з Creators' App", "—", "модуль 12", "—", 2),
    ("Airplane Mode", "Режим польоту", p(N, "Network Option", "Airplane Mode"), "вимикає Wi-Fi/Bluetooth", "On / Off", "Off; On — щоб заощадити батарею", "—", 2),
    ("Copyright Info", "Авторське право", p(S, "File", "Copyright Info"), "ім'я автора в EXIF", "Write On/Off, Photographer, Copyright", "впишіть ім'я", "—", 2),
    ("Version", "Версія прошивки", p(U, "Setup Option", "Version"), "показує версії камери й об'єктива, оновлення", "Body / …", "перевірте: 6.02 (на 27.11.2026)", "—", 2),
    ("Setting Reset / Save/Load Settings", "Скидання / збереження налаштувань", p(U, "Reset/Save Settings"), "повернути заводські або зберегти свої на карту", "Camera Settings Reset, Initialize; Save / Load", "збережіть налаштування на карту після модуля 7", "щось зламали — Reset", 2),
    # ---- Досвідченим
    ("APS-C S35 Shooting", "Кроп APS-C / Super 35", p(S, "Image Quality", "APS-C S35 Shooting"), "обрізає кадр до APS-C (кут ≈ ×1,5)", "On / Auto / Off", "Off (у фото)", "потрібно «довше» за 75 мм", 3),
    ("HLG Still Image", "HDR-фото HLG", p(S, "Image Quality", "HLG Still Image"), "HDR-фото HEIF для HDR-екранів", "On / Off", "Off", "—", 3),
    ("Interval Shoot Func.", "Інтервальна зйомка", p(S, "Drive Mode", "Interval Shoot Func."), "таймлапс", "початок, інтервал, кількість", "—", "захід сонця, хмари", 3),
    ("Bracket Settings / Focus Bracket", "Брекетинг", p(S, "Drive Mode", "Bracket Settings"), "серія з різною експозицією чи фокусом", "кроки, кількість", "—", "HDR-пейзаж, предмети", 3),
    ("Face Memory / Regist. Faces Priority", "Запам'ятати обличчя", p(F, "Face/Eye AF", "Face Memory"), "пріоритет обличчям рідних", "до 8 облич", "зареєструйте дітей", "свята", 3),
    ("Focus Area Limit", "Обмеження зон", p(F, "Focus Area", "Focus Area Limit"), "сховати непотрібні зони", "галочки", "залиште Wide, Zone, Spot M, Expand Spot, Tracking", "—", 3),
    ("Switch V/H AF Area", "Зона для вертикалі/горизонталі", p(F, "Focus Area", "Switch V/H AF Area"), "окрема точка AF для вертикальних кадрів", "Off / AF Point Only / AF Point + AF Area", "Off", "портрети вертикально", 3),
    ("AF Tracking Sensitivity", "Чутливість стеження", p(F, "AF/MF", "AF Tracking Sensitivity"), "наскільки «чіпко» тримати об'єкт", "1 (Locked on) – 5 (Responsive)", "3", "спорт — 2", 3),
    ("Picture Profile (stills)", "Профілі зображення", p(E, "Color/Tone", "Picture Profile"), "PP1–PP11 (переважно для відео)", "Off / PP1–PP11", "Off для фото", "—", 3),
    ("Lock Operation Parts", "Блокування органів керування", p(U, "Dial Customize", "Lock Operation Parts"), "щоб диски не крутилися випадково", "Off / On", "Off", "—", 3),
    ("My Dial Settings", "Мої диски", p(U, "Dial Customize", "My Dial Settings"), "тимчасово змінити функції дисків кнопкою", "3 набори", "—", "—", 3),
    ("Anti-dust / Pixel Mapping", "Очищення матриці / мапінг пікселів", p(U, "Setup Option", "Anti-dust Function"), "вібраційне очищення, виправлення «гарячих» пікселів", "Shutter When Pwr OFF, Cleaning Mode; Pixel Mapping", "Shutter When Pwr OFF — On (шторка закриває матрицю при вимкненні)", "плями на фото", 3),
    ("USB Connection Mode / USB Power Supply", "Режим USB / живлення через USB", p(U, "USB"), "як камера поводиться з комп'ютером", "Select When Connect, Mass Storage, MTP, PC Remote…", "Select When Connect", "тетеринг — PC Remote", 3),
    # ---- Відео
    ("File Format (movie)", "Формат відео", p(S, "Image Quality", "File Format") + " <small>(у режимі відео)</small>", "кодек і роздільність", "XAVC HS 4K · XAVC S 4K · XAVC S HD · XAVC S-I 4K · XAVC S-I HD", "XAVC S 4K", "модуль 11", 4),
    ("Movie Settings", "Частота кадрів і бітрейт", p(S, "Image Quality", "Movie Settings"), "Rec Frame Rate, Record Setting", "60p/50p, 30p/25p, 24p, 120p/100p (HD)", "25p, 100M 4:2:0 8bit або 140M 4:2:2 10bit", "модуль 11", 4),
    ("S&Q Settings", "Сповільнення / прискорення", p(S, "Image Quality", "S&Q Settings"), "кадри зйомки vs відтворення", "1–120 fps", "модуль 11.11", "—", 4),
    ("Proxy Settings", "Проксі-файли", p(S, "Image Quality", "Proxy Settings"), "легка копія для монтажу", "On / Off", "Off", "монтаж на слабкому ПК", 4),
    ("NTSC/PAL Selector", "Стандарт PAL / NTSC", p(U, "Area/Date", "NTSC/PAL Selector"), "50p/25p (PAL) або 60p/30p/24p (NTSC)", "NTSC / PAL", "PAL (Україна, 50 Гц)", "24p — лише в NTSC", 4),
    ("SteadyShot (movie)", "Стабілізація відео", p(S, "Image Stabilization", "SteadyShot") + " <small>(у відео)</small>", "стабілізація відео", "Active / Standard / Off", "Active з рук, Off на штативі", "—", 4),
    ("Audio Rec Level / Wind Noise Reduct.", "Рівень звуку / захист від вітру", p(S, "Audio Recording", "Audio Rec Level"), "чутливість мікрофона", "0–31; Auto / On / Off", "рівень так, щоб піки були близько −12 dB", "—", 4),
    ("AF Transition Speed / AF Subj. Shift Sensitivity", "Швидкість / чутливість переходу фокуса", p(F, "AF/MF", "AF Transition Speed"), "наскільки плавно й охоче фокус переходить на новий об'єкт", "1–7 / 1–5", "5 / 5 (живе відео); для «кіно» — 2–3 / 2–3", "—", 4),
    ("Gamma Display Assist", "Допомога для S-Log", p(U, "Display Option", "Gamma Display Assist"), "нормальна картинка на екрані під час S-Log/HLG", "On / Off", "On, якщо знімаєте S-Log3", "—", 4),
    ("Marker Display", "Маркери кадру", p(S, "Marker Display", "Marker Display"), "центр, рамки 9:16/1:1 тощо", "On / Off", "Aspect Marker 9:16, якщо робите Reels", "—", 4),
    ("Auto Slow Shutter", "Автоподовження витримки", p(E, "Exposure", "Auto Slow Shutter"), "у темряві камера подовжує витримку відео", "On / Off", "Off (зберігає плавність руху)", "—", 4),
]


def menu_tables():
    titles = {1: "🟥 Необхідно налаштувати відразу", 2: "🟧 Корисно знати", 3: "🟦 Для досвідчених фотографів", 4: "🟪 Для відеозйомки"}
    out = []
    for lvl in (1, 2, 3, 4):
        rows = [[f"<b>{en}</b><br><small>{ua}</small>", pt, what, vals, rec, chg] for en, ua, pt, what, vals, rec, chg, l in MENU if l == lvl]
        out.append(f'<h3>{titles[lvl]}</h3>' + table(["Пункт меню (EN / UA)", "Шлях у меню", "Що означає", "Значення", "Початківцю", "Коли змінювати"], rows, "menu"))
    return "".join(out)


m6 = [f'''<p>Довідник складено за офіційним деревом меню Sony Help Guide для ILCE-7M4 (сторінка «Finding functions from MENU»). Головне меню має вкладки: <b>Main</b> (швидкий список параметрів зйомки), <b>Shooting</b>, <b>Exposure/Color</b>, <b>Focus</b>, <b>Playback</b>, <b>Network</b>, <b>Setup</b> і <b>My Menu</b>. Кожна вкладка поділена на групи: наприклад, Shooting → Image Quality, Media, File, Shooting Mode, Drive Mode, Shutter/Silent, Audio Recording, TC/UB, Image Stabilization, Zoom, Shooting Display, Marker Display.</p>
{box("off", "<p>Вкладка <b>Main</b> зі списком параметрів зйомки з'являється з <b>прошивкою Ver. 6.00</b>, а Spot XL і зони Custom — теж з 6.00. Lossless Compressed RAW з'явився з Ver. 1.10. Для старіших прошивок частина шляхів інша. Оновіться до актуальної версії 6.02.</p>")}
{box("nv", "<p>Колонку «Початківцю» склали ми, у документації Sony такої немає. Повного переліку заводських значень для ILCE-7M4 у Help Guide ми не знайшли. Заводські значення наведено лише там, де Sony їх прямо називає.</p>")}
<p class="small">Порада: у вкладці або групі натисніть на камері кнопку <b>?</b> або торкніться значка довідки, щоб побачити вбудований опис пункту (In-Camera Guide).</p>''', menu_tables(),
      src(hg("TP1001803623", "Finding functions from MENU (повне дерево меню)"), hg("TP1002102430", "Main menu (shooting setting list)"),
          hg("TP1000640145", "Using the MENU button"), hg("TP1000659396", "File Format (still)"), hg("TP1000659395", "RAW File Type"),
          hg("TP1000659384", "Recording Media (still)"), hg("TP1000653537", "Shutter Type"), hg("TP1000659392", "Anti-flicker Set."),
          hg("TP1000640160", "In-Camera Guide"))]
M6 = module(6, "m6", "Повний путівник меню Sony A7 IV", "Понад 80 пунктів: оригінальна назва, переклад, точний шлях, значення та рекомендації за рівнями важливості.", "".join(m6))

# ======================= МОДУЛЬ 7 =======================
m7 = [f'''<ol class="bigsteps">
<li><h4>Заряджіть акумулятор</h4><p>Вставте NP-FZ100 у камеру й підключіть кабель USB-C до адаптера живлення. Поки йде заряджання, світиться індикатор заряджання (CHARGE). Заряджайте при <b>вимкненій</b> камері. Якщо в комплекті є зовнішній зарядний пристрій, можна зарядити й ним. Перед першою зйомкою — до 100 %.</p></li>
<li><h4>Встановіть об'єктив</h4><p>Як описано в модулі 2.6: камера вимкнена, білі мітки суміщені, поворот за годинниковою стрілкою до клацання. Одразу поставте бленду.</p></li>
<li><h4>Вставте карту Kingston у SLOT 1</h4><p>Відкрийте кришку праворуч і вставте карту до клацання так, як показано на кришці. Kingston Canvas React Plus — це UHS-II, U3, <b>V60</b>, 280/150 МБ/с. Для A7 IV такої карти досить для всіх фото й усіх відеорежимів <b>крім XAVC S-I</b> (Intra), де Sony вимагає SDXC V90 або CFexpress A VPG200 (модуль 11).</p></li>
<li><h4>Відформатуйте карту</h4><p>{p(S,"Media","Format")} → Slot 1 → Enter. Форматування стирає <b>все</b>, зокрема захищені файли.</p></li>
<li><h4>Мова, дата, час</h4><p>{p(U,"Area/Date","Language")}; {p(U,"Area/Date","Area/Date/Time Setting")}. Правильний час потрібен для сортування фото й синхронізації зі смартфоном.</p></li>
<li><h4>Перевірте прошивку</h4><p>{p(U,"Setup Option","Version")}. На 27.11.2026 найновіша прошивка камери — <b>6.02</b> (28.05.2026). Як оновити (за інструкцією Sony): повністю заряджений NP-FZ100; батарейну ручку зняти; файл <code>BODYDATA.DAT</code> скопіювати в корінь відформатованої карти й вставити її в <b>SLOT 1</b> (камера читає оновлення лише з нього); {p(U,"Setup Option","Version","Body")} → <i>Software Update</i> → <i>Execute</i>. Не вимикайте камеру й не виймайте акумулятор. Якщо у вас версія 1.01 або старіша, спершу оновіться до 1.05, а потім до 6.02. Прошивку <b>об'єктива</b> оновлюйте через TAMRON Lens Utility (модуль 2.8). Найновіша — версія 4.</p></li>
<li><h4>Якість фото</h4><p>{p(S,"Image Quality","Image Quality Settings")}: RAW File Type — <b>Lossless Comp (L)</b>, JPEG Quality — <b>Fine</b>, JPEG Image Size — <b>L</b>, Aspect Ratio — <b>3:2</b>.</p></li>
<li><h4>RAW + JPEG</h4><p>{p(S,"Image Quality","Image Quality Settings","File Format")} → <b>RAW & JPEG</b>. Чому саме так: JPEG одразу можна надіслати рідним, а RAW дає запас для обробки (модуль 12).</p></li>
<li><h4>Автофокус</h4><p>Focus Mode — <b>AF-C</b>, Focus Area — <b>Wide</b>, Priority Set in AF-C — Balanced Emphasis, AF Illuminator — Auto.</p></li>
<li><h4>Розпізнавання очей</h4><p>Face/Eye Prior. in AF — <b>On</b>, Face/Eye Subject — <b>Human</b>, Right/Left Eye Select — Auto, Face/Eye Frame Disp. — On.</p></li>
<li><h4>Auto ISO і мінімальна витримка</h4><p>ISO — <b>ISO AUTO</b>, ISO Range Limit — <b>100–12800</b>, ISO AUTO Min. SS — <b>FAST</b> (або 1/250 для людей у русі).</p></li>
<li><h4>Стабілізація</h4><p>SteadyShot — <b>On</b>. Коли знімаєте зі штатива, вимикайте.</p></li>
<li><h4>Дисплей і видошукач</h4><p>Діоптрії налаштуйте по тексту. Grid Line — Rule of 3rds. DISP: увімкніть вигляд із гістограмою. Monitor Brightness — Manual 0. Touch Operation — On, Touch Func. in Shooting — Touch Focus. Auto Review — Off або 2 с. Audio signals — Off.</p></li>
<li><h4>Кнопки C1–C4</h4><p>{p(U,"Operation Customize","Custom Key/Dial Set.")}. Наш варіант для початківця — у таблиці нижче.</p></li>
<li><h4>Швидке меню Fn</h4><p>{p(U,"Operation Customize","Fn Menu Settings")} → оберіть клітинку → функцію. Пропонований набір — нижче.</p></li>
<li><h4>My Menu</h4><p>{p("My Menu","My Menu Setting","Add Item")}. Додайте те, що потрібно рідко, але терміново: Format, Recording Media, ISO AUTO Min. SS, Anti-flicker Set., Silent Mode Settings, Zebra Display, Peaking Display, Smartphone Connection, Version, Save/Load Settings.</p></li>
<li><h4>Перша фотографія та перевірка</h4><p>Режим <b>A</b>, f/4, 50 мм. Зніміть людину біля вікна з відстані ~2 м. Потім натисніть ▶ і перевірте: (1) збільште кадр через AF-ON і подивіться на око; (2) ввімкніть гістограму через DISP: «гора» не повинна впиратися в краї; (3) подивіться, яку витримку обрала камера (кнопка DISP або інформація на екрані). Якщо витримка довша за 1/80 — підніміть ISO AUTO Min. SS. Наостанок збережіть налаштування: {p(U,"Reset/Save Settings","Save/Load Settings")}.</p></li></ol>''']
m7.append(box("pro", table(["Кнопка / диск", "Пропоноване призначення", "Навіщо"], [
    ["C1", "Focus Magnifier", "миттєво перевірити різкість"], ["C2", "Focus Area (залишити)", "зона AF"],
    ["C3", "Focus Mode", "AF-S ↔ AF-C"], ["C4", "Face/Eye Subject", "Human ↔ Animal ↔ Bird"],
    ["AEL", "AEL hold (залишити)", "фіксація експозиції"], ["AF-ON", "AF On (залишити)", "BBF пізніше"],
    ["Центр джойстика", "Focus Standard", "повернути точку в центр"],
    ["Кнопка Focus Set на Tamron", "Eye AF або Focus Hold", "лівою рукою"]]), "📷 Порада фотографа: кнопки для початківця"))
m7.append(box("pro", '<div class="fn-grid">' + "".join(f"<span>{x}</span>" for x in [
    "Drive Mode", "Focus Mode", "Focus Area", "Face/Eye Subject", "ISO", "Exposure Comp.",
    "White Balance", "Metering Mode", "Creative Look", "SteadyShot", "Shutter Type", "File Format"]) + '</div><p class="small">12 клітинок, два ряди по 6.</p>', "📷 Порада фотографа: набір Fn для фото"))
m7.append('<h3>7.18. Таблиця стартових налаштувань</h3>')
m7.append(table(["Параметр", "Значення", "Шлях"], [
    ["File Format", "RAW & JPEG", p(S, "Image Quality", "Image Quality Settings", "File Format")],
    ["RAW File Type", "Lossless Comp (L)", p(S, "Image Quality", "Image Quality Settings", "RAW File Type")],
    ["JPEG Quality / Size", "Fine / L", p(S, "Image Quality", "Image Quality Settings")],
    ["Aspect Ratio", "3:2", p(S, "Image Quality", "Aspect Ratio")],
    ["Recording Media", "Slot 1", p(S, "Media", "Rec. Media Settings", "Recording Media")],
    ["Release w/o Card", "Disable", p(S, "Shutter/Silent", "Release w/o Card")],
    ["Drive Mode", "Single (рух — Cont. Mid)", p(S, "Drive Mode", "Drive Mode")],
    ["Shutter Type", "Mechanical", p(S, "Shutter/Silent", "Shutter Type")],
    ["e-Front Curtain Shut.", "On", p(S, "Shutter/Silent", "e-Front Curtain Shut.")],
    ["SteadyShot", "On", p(S, "Image Stabilization", "SteadyShot")],
    ["Lens Compensation", "Auto (усе)", p(S, "Image Quality", "Lens Compensation")],
    ["Grid Line", "On, Rule of 3rds", p(S, "Shooting Display", "Grid Line Display")],
    ["ISO", "ISO AUTO 100–12800", p(E, "Exposure", "ISO Range Limit")],
    ["ISO AUTO Min. SS", "FAST", p(E, "Exposure", "ISO AUTO Min. SS")],
    ["Metering Mode", "Multi", p(E, "Metering", "Metering Mode")],
    ["White Balance", "AWB", p(E, "White Balance", "White Balance")],
    ["DRO", "Auto (для JPEG)", p(E, "Color/Tone", "D-Range Optimizer")],
    ["Creative Look", "ST", p(E, "Color/Tone", "Creative Look")],
    ["Zebra", "On", p(E, "Zebra Display", "Zebra Display")],
    ["Focus Mode", "AF-C", p(F, "AF/MF", "Focus Mode")],
    ["Focus Area", "Wide", p(F, "Focus Area", "Focus Area")],
    ["Face/Eye Prior. in AF", "On", p(F, "Face/Eye AF", "Face/Eye Prior. in AF")],
    ["Face/Eye Subject", "Human", p(F, "Face/Eye AF", "Face/Eye Subject")],
    ["Peaking Display", "On, Mid", p(F, "Peaking Display", "Peaking Display")],
    ["Touch Operation", "On", p(U, "Touch Operation", "Touch Operation")],
    ["Monitor Brightness", "Manual 0", p(U, "Finder/Monitor", "Monitor Brightness")],
    ["Audio signals", "Off", p(U, "Sound Option", "Audio signals")],
    ["NTSC/PAL Selector", "PAL", p(U, "Area/Date", "NTSC/PAL Selector")],
    ["Copyright Info", "Ваше ім'я", p(S, "File", "Copyright Info")]], "menu"))
m7.append(box("nv", "<p>Якщо пункт розташований не там, де описано, у вас, найімовірніше, стара прошивка. Оновіть камеру до 6.02. Або скористайтеся пошуком у Help Guide за англійською назвою пункту.</p>"))
m7.append(src(hg("TP1000616549", "Format"), hg("TP1000660192", "Version"), ("Sony: оновлення ILCE-7M4 до Ver. 6.02 (інструкція)", "https://www.sony.co.uk/electronics/support/e-mount-body-ilce-7-series/ilce-7m4/software/00280503"),
              hg("TP1000655376", "Custom Key/Dial Set."), hg("TP1000657996", "Fn Menu Settings"), hg("TP1000656910", "Save/Load Settings"),
              ("Kingston Canvas React Plus V60 — специфікації", "https://kingston.com/en/memory-cards/canvas-react-plus-sd-v60")))
M7 = module(7, "m7", "Перше налаштування після покупки", "17 кроків від коробки до першої якісної фотографії і таблиця стартових налаштувань.", "".join(m7))
