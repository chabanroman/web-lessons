import json, sys, copy, re, os, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
os.chdir(HERE)
sys.path.insert(0, HERE)
import helpers
import c1, c2, c3, c4
from c5 import TESTS, TEST_JS1
from c6 import PAGES
from gloss import G
from tags import GROUPS
import c38
from testcrypt import secure

ID25 = c38.ID25
PARENT = {"links": "text", "tables": "semantic", "colors": "css-intro", "responsive": "grid", "anim": "grid", "landing": "grid",
          "loops": "arrays", "array-methods": "objects", "forms-js": "events", "debug": "shelf", "sql2": "sql", "git": "agents", "ai-practice": "ai"}

BLOCKS = [
 {"id": "html", "name": "HTML", "sub": "Скелет сторінки", "icon": "🦴", "color": "#F0622E", "soft": "#FFE3D6"},
 {"id": "css", "name": "CSS", "sub": "Стиль і вигляд", "icon": "🎨", "color": "#2F6FEB", "soft": "#DCE8FF"},
 {"id": "js", "name": "JavaScript", "sub": "Логіка й інтерактив", "icon": "⚡", "color": "#D99A00", "soft": "#FFF3CC"},
 {"id": "db", "name": "Дані й бекенд", "sub": "SQL, API, сервер, хмара", "icon": "🗄️", "color": "#18A058", "soft": "#D7F5E3"},
 {"id": "ai", "name": "AI і фінал", "sub": "Напарник, агенти, захист", "icon": "🤖", "color": "#8B5CF6", "soft": "#EDE5FF"},
]

def build(version, edition):
    blocks = copy.deepcopy(BLOCKS)
    if version == 25:
        lessons = copy.deepcopy(sorted(helpers.LESSONS, key=lambda l: l["n"]))
        for l in lessons: l["id"] = ID25[l["n"] - 1]
        tdefs = [(t, a) for t, a in zip(TESTS, ["forms", "grid", "shelf", "supa", "final"])]
        gmap = lambda i: PARENT.get(i, i)
    else:
        lessons = copy.deepcopy(c38.L)
        blocks[4]["name"] = "Git, AI і фінал"; blocks[4]["sub"] = "Git, AI-напарник, агенти, захист"
        T = {t["key"]: t for t in TESTS}
        tdefs = [(T["html"], "forms"), (T["css"], "landing"), (TEST_JS1, "func"), (T["js"], "debug"), (T["db"], "supa"), (T["final"], "final")]
        gmap = lambda i: i
    num = {l["id"]: l["n"] for l in lessons}
    total = len(lessons)

    # tests
    tests, prev = [], 0
    for k, (t, after) in enumerate(tdefs, 1):
        t = copy.deepcopy(t); a = num[after]
        t["n"] = k; t["after"] = a
        if t["name"] == "FINAL":
            t["title"] = "Підсумкова контрольна"; t["sub"] = f"Увесь курс · {len(t['q'])} питань · {t['mins']} хвилин"
        else:
            t["title"] = f"Контрольна №{k}: {t['name']}"; t["sub"] = f"Уроки {prev+1}–{a} · {len(t['q'])} питань · {t['mins']} хвилин"
        t["from"] = prev + 1
        prev = a
        tests.append(t)

    # auto homework hints
    for l in lessons:
        t = next((t for t in tests if t["after"] == l["n"]), None)
        if t and l["id"] != "final":
            l["hw"].append({"lvl": "Підготовка", "v": f"Наступного уроку — <b>{t['title']}</b>. Повтори уроки {t['from']}–{t['after']}."})
        if l["n"] == num["final"] - 1:
            l["hw"].append({"lvl": "Підготовка", "v": f"Підготуй 3-хвилинний захист проєкту за планом з уроку {num['final']}."})

    # glossary
    gl = []
    for term, d, lid in G:
        n = num[gmap(lid)]
        gl.append({"t": term, "d": d, "n": n})
    for l in lessons:
        l["terms"] = [g for g in gl if g["n"] == l["n"]]

    pages = copy.deepcopy(PAGES)
    if edition == "student":
        pages.pop("teacher")

    long = [str(l["n"]) for l in lessons if l["mins"] > 45]
    fmt = f"{total} уроків по 45 хв. Уроки {', '.join(long)} розраховані на 90 хв: проводьте їх як подвійні або діліть на два заняття."

    tg = [{"id": gid, "name": gname, "desc": gdesc, "items": [{"tag": t, "name": nm, "why": why, "ex": ex, "n": num.get(lid) or num[gmap(lid)], "kind": kind} for t, nm, why, ex, lid, kind in items]} for gid, gname, gdesc, items in GROUPS]
    data = {"tags": tg, "blocks": blocks, "lessons": lessons, "tests": tests, "pages": pages, "gloss": gl, "edition": edition, "version": version}
    data = secure(data, edition, f"course{version}")
    js = json.dumps(data, ensure_ascii=False)

    def tok(m):
        k = m.group(1)
        if k == "FMT": return fmt
        if k.startswith("r:"):
            b = k[2:]; ns = [l["n"] for l in lessons if l["block"] == b]
            return f"{min(ns)}–{max(ns)}"
        return str(num.get(k) or num[gmap(k)])
    js = re.sub(r"⟦([^⟧]+)⟧", tok, js)
    assert "⟦" not in js
    js = js.replace("</", "<\\/")

    shell = open("shell.html", encoding="utf-8").read()
    out = shell.replace("/*__DATA__*/", "const DATA = " + js + ";")
    name = f"out/course{version}-{edition}.html"
    open(name, "w", encoding="utf-8").write(out)
    print(name, len(out), "lessons", total, "tests", len(tests), "terms", len(gl))

os.makedirs("out", exist_ok=True)
for v in (25, 38):
    for e in ("teacher", "student"):
        build(v, e)
    # учнівське видання — на сайт (папки 25/ і 38/ у корені репозиторію)
    shutil.copy(f"out/course{v}-student.html", f"../{v}/index.html")
print("Готово: учнівські видання оновлено в 25/ і 38/, видання для вчителя — у src/out/ (не потрапляє в git)")
