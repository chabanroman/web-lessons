from helpers import H, P, CODE, TRY, FIG, TIP, WARN, IDEA, LIST, STEPS, CARDS, TABLE, make

DL = []
def dlesson(*a, **k):
    DL.append(make(*a, **k))

def PY(code, run=True, title=None, note=None, inp=None):
    d = CODE("python", code, run=run, title=title, note=note)
    if inp: d["inp"] = inp
    return d

def PYTRY(code, title="Спробуй сам", inp=None):
    d = TRY(code, title); d["lang"] = "python"
    if inp is not None: d["inp"] = inp
    return d

def FX(code, title=None, note=None):
    """Формула Google Sheets."""
    return CODE("sheets", code, run=False, title=title, note=note)

def SHEET(rows, formula=None, sel=None, hl=None, cap=None, name="Аркуш1"):
    """rows: список рядків (рядок 1 = заголовки). hl: {'B2': 'g'|'r'|'y'|'b'}."""
    return {"t": "sheet", "rows": rows, "f": formula, "sel": sel, "hl": hl or {}, "cap": cap, "name": name}
