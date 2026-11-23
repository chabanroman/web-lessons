"""Збирання курсів «Google Sheets» і «Python» (учнівське й учительське видання)."""
import json, sys, copy, re, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE); sys.path.insert(0, HERE)

import s14, p1, p2, p3
from dpages import S_TESTS, P_TESTS, S_GLOSS, P_GLOSS, S_REF, P_REF
from dpages2 import SHEETS_PAGES, PY_PAGES, KLAS_CSV
from helpers import H, P, IDEA
from testcrypt import secure

def build_course(key, lessons, blocks, tests_def, gloss, pages, ref, ref_kind, meta, files=None):
    lessons = copy.deepcopy(lessons)
    for i, l in enumerate(lessons, 1): l["n"] = i
    num = {l["id"]: l["n"] for l in lessons}
    tests, prev = [], 0
    for k, (name, _, after, mins, qs) in enumerate(tests_def, 1):
        a = num[after]
        t = {"n": k, "after": a, "block": next(l["block"] for l in lessons if l["n"] == a), "mins": mins, "q": qs, "from": prev + 1}
        if name == "FINAL":
            t["title"] = "Підсумкова контрольна"; t["sub"] = f"Увесь курс · {len(qs)} питань · {mins} хвилин"
        else:
            t["title"] = f"Контрольна №{k}: {name}"; t["sub"] = f"Уроки {prev+1}–{a} · {len(qs)} питань · {mins} хвилин"
        prev = a; tests.append(t)
    final_n = len(lessons)
    for l in lessons:
        t = next((t for t in tests if t["after"] == l["n"]), None)
        if t and l["n"] != final_n:
            l["hw"].append({"lvl": "Підготовка", "v": f"Наступного уроку — <b>{t['title']}</b>. Повтори уроки {t['from']}–{t['after']}."})
        if l["n"] == final_n - 1:
            l["hw"].append({"lvl": "Підготовка", "v": f"Підготуй 3-хвилинний захист проєкту за планом з уроку {final_n}."})
    gl = [{"t": t, "d": d, "n": num[i]} for t, d, i in gloss]
    for l in lessons: l["terms"] = [g for g in gl if g["n"] == l["n"]]
    tg = [{"id": gid, "name": gn, "desc": gd, "items": [{"tag": a, "name": b, "why": c, "ex": d, "n": num[e], "kind": ref_kind} for a, b, c, d, e in items]} for gid, gn, gd, items in ref]
    long = [str(l["n"]) for l in lessons if l["mins"] > 45]
    fmt = f"{len(lessons)} уроків по 45 хв." + (f" Уроки {', '.join(long)} розраховані на 90 хв: проводьте їх як подвійні або діліть на два заняття." if long else "")
    shell = open("shell.html", encoding="utf-8").read()
    for edition in ("teacher", "student"):
        pg = copy.deepcopy(pages)
        if edition == "student": pg.pop("teacher", None)
        data = {"meta": meta, "files": files or {}, "tags": tg, "blocks": blocks, "lessons": lessons, "tests": copy.deepcopy(tests), "pages": pg, "gloss": gl, "edition": edition}
        data = secure(data, edition, key)
        js = json.dumps(data, ensure_ascii=False).replace("⟦FMT⟧", fmt)
        assert "⟦" not in js
        js = js.replace("</", "<\\/")
        out = shell.replace("/*__DATA__*/", "const DATA = " + js + ";")
        name = f"out/{key}-{edition}.html"
        open(name, "w", encoding="utf-8").write(out)
        print(name, len(out), "уроків", len(lessons), "тестів", len(tests), "термінів", len(gl))

os.makedirs("out", exist_ok=True)

# ── Google Sheets
SB = [
 {"id": "sheets", "name": "Основи", "sub": "Таблиці, формати, формули", "icon": "📗", "color": "#0F9D58", "soft": "#D7F5E3"},
 {"id": "sheets2", "name": "Пошук і аналіз", "sub": "Текст, дати, діаграми, зведені", "icon": "📊", "color": "#1A73E8", "soft": "#DCE8FF"},
 {"id": "sheets3", "name": "Дані й проєкт", "sub": "Forms, QUERY, автоматизація", "icon": "🚀", "color": "#8B5CF6", "soft": "#EDE5FF"},
]
SLS = copy.deepcopy(s14.SL)
for l in SLS:
    l["block"] = "sheets" if l["n"] <= 6 else "sheets2" if l["n"] <= 10 else "sheets3"
sp = copy.deepcopy(SHEETS_PAGES)
sp["ref"] = {"title": "📗 Довідник функцій", "sub": "Найпотрібніші функції Google Sheets з поясненнями й прикладами.", "catalog": True, "searchPh": "🔍 Пошук функції… (наприклад: IF, середнє, пошук)", "sections": [
  P("Усі функції пишуться після знака <code>=</code>. В українських налаштуваннях аргументи розділяються <code>;</code>, в англійських — <code>,</code>."),
  IDEA("Не пам'ятаєш точно? Почни писати назву функції в клітинці — Google Sheets покаже підказку з описом і прикладом."), H("Каталог функцій")]}
build_course("sheets", SLS, SB, S_TESTS, S_GLOSS, sp, S_REF, "fx", {
  "brand": "Таблиці-майстерня", "logo": "fx", "favicon": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#0F9D58"/><text x="32" y="33" text-anchor="middle" dominant-baseline="central" font-family="Menlo,Consolas,monospace" font-weight="700" font-size="30" fill="#fff">fx</text></svg>', "kicker": "Курс Google Sheets",
  "hero": "Від першої клітинки до дашборду, що оновлюється сам. Формули, логіка, пошук, діаграми, зведені таблиці, Google Forms і автоматизація. Крок за кроком, з наочними прикладами.",
  "deco": "=SUM(D2:D30)\n=IF(E2>=8;\"ок\";\"⚠️\")\n=XLOOKUP(A2;Учні!A:A;Учні!F:F)\n=QUERY(A1:F;\"select B, avg(E)\n  group by B\")\n=UNIQUE(C2:C)",
  "projectName": "Наш клас у цифрах", "projectBlurb": "Наскрізний проєкт «Наш клас у цифрах»: опитування в Google Forms → таблиця з формулами → аналіз → дашборд, що оновлюється сам.",
  "checkTitle": "Перевір себе", "workCard": "Google-акаунт, налаштування регіону, школа ↔ дім →",
  "nav": [["tools", "🛠️ Де працювати"], ["project", "📊 Проєкт «Наш клас у цифрах»"], ["ref", "📗 Довідник функцій"], ["glossary", "📘 Словник термінів"], ["homework", "🏠 Домашні завдання"]]})

# ── Python
PB = [
 {"id": "pybase", "name": "Основи", "sub": "print, змінні, умови, цикли, рядки", "icon": "🐍", "color": "#3776AB", "soft": "#DCE8FF"},
 {"id": "pystruct", "name": "Структури й функції", "sub": "Списки, словники, функції, модулі", "icon": "🧩", "color": "#D99A00", "soft": "#FFF3CC"},
 {"id": "pydata", "name": "Python і дані", "sub": "Файли, CSV, pandas, графіки", "icon": "📊", "color": "#18A058", "soft": "#D7F5E3"},
 {"id": "pyai", "name": "Інтернет, AI і фінал", "sub": "Google Sheets, API, AI, дослідження", "icon": "🤖", "color": "#8B5CF6", "soft": "#EDE5FF"},
]
pp = copy.deepcopy(PY_PAGES)
pp["ref"] = {"title": "🐍 Довідник Python", "sub": "Головні команди Python з прикладами, які можна запустити прямо тут.", "catalog": True, "searchPh": "🔍 Пошук команди… (наприклад: list, цикл, pandas)", "sections": [
  P("Кожен приклад запускається кнопкою «▶ Показати» прямо в браузері. Файл <code>klas.csv</code> для прикладів з даними вже на місці."), H("Каталог команд")]}
build_course("python", p3.PL, PB, P_TESTS, P_GLOSS, pp, P_REF, "py", {
  "brand": "Python-майстерня", "logo": "py", "favicon": '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="14" fill="#3776AB"/><text x="32" y="33" text-anchor="middle" dominant-baseline="central" font-family="Menlo,Consolas,monospace" font-weight="700" font-size="30" fill="#FFD43B">py</text></svg>', "kicker": "Курс Python",
  "hero": "Від першого print() до власного дослідження з даними й графіками. Змінні, умови, цикли, функції, файли, pandas і AI. Кожен приклад запускається прямо в браузері.",
  "deco": "def stars(n):\n    return '★' * n\n\nfor s in students:\n    print(s['name'])\n\ndf.groupby('class')\\\n  ['sleep'].mean()",
  "projectName": "Дослідження класу", "projectBlurb": "Три проєкти: гра-вікторина, текстова пригода і фінальне «Дослідження класу» з даними, pandas і графіками.",
  "checkTitle": "Перевір себе", "workCard": "Цей сайт, Thonny, VS Code чи Google Colab: однаково в школі й удома →",
  "nav": [["tools", "🛠️ Де працювати"], ["project", "🔬 Проєкт «Дослідження класу»"], ["ref", "🐍 Довідник Python"], ["glossary", "📘 Словник термінів"], ["homework", "🏠 Домашні завдання"]]},
  files={"klas.csv": KLAS_CSV})

for key in ("sheets", "python"):
    dst = os.path.join(HERE, "..", key)
    if os.path.isdir(os.path.join(HERE, "..", "25")):
        os.makedirs(dst, exist_ok=True)
        shutil.copy(f"out/{key}-student.html", os.path.join(dst, "index.html"))
