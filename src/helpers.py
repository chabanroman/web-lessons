LESSONS = []

def H(t): return {"t": "h", "v": t}
def P(t): return {"t": "p", "v": t}
def CODE(lang, code, run=False, title=None, note=None):
    return {"t": "code", "lang": lang, "v": code.strip("\n"), "run": run, "title": title, "note": note}
def TRY(code, title="Спробуй сам"):
    return {"t": "try", "v": code.strip("\n"), "title": title}
def FIG(svg, cap): return {"t": "fig", "v": svg, "cap": cap}
def TIP(t): return {"t": "tip", "v": t}
def WARN(t): return {"t": "warn", "v": t}
def IDEA(t): return {"t": "idea", "v": t}
def LIST(items): return {"t": "list", "v": items}
def STEPS(items): return {"t": "steps", "v": items}
def CARDS(items): return {"t": "cards", "v": [{"i": a, "h": b, "p": c} for a, b, c in items]}
def TABLE(head, rows): return {"t": "table", "head": head, "rows": rows}

def make(n, block, title, sub, goals, sections, project, check, hw, quiz, mins=45, id=None):
    return ({
        "n": n, "block": block, "title": title, "sub": sub, "goals": goals,
        "sections": sections, "project": project, "check": check,
        "hw": [{"lvl": a, "v": b} for a, b in hw],
        "quiz": [{"q": q, "o": o, "a": a, "w": w} for q, o, a, w in quiz],
        "mins": mins, "id": id,
    })

def lesson(*a, **k):
    LESSONS.append(make(*a, **k))

def Q(q, o, a, w): return {"q": q, "o": o, "a": a, "w": w}
