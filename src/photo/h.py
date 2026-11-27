# -*- coding: utf-8 -*-
"""Будівельні блоки сторінок фотокурсу."""

HG = "https://helpguide.sony.net/ilc/2110/v1/en/contents/"


def hg(code, title):
    return (title, HG + code + ".html")


def box(kind, body, title=None):
    names = {
        "off": "📘 Офіційно: документація виробника",
        "fab": "🏭 Заводське значення",
        "pro": "📷 Порада фотографа (власна рекомендація, не з документації)",
        "nv": "⚠️ Не підтверджено офіційною документацією",
        "tip": "💡 Порада",
        "warn": "⛔ Обережно",
        "ex": "🎯 Практика",
        "key": "🔑 Головне",
    }
    t = title or names[kind]
    return f'<div class="box b-{kind}"><div class="box-t">{t}</div>{body}</div>'


def src(*links):
    lis = "".join(f'<li><a href="{u}" target="_blank" rel="noopener">{t}</a></li>' for t, u in links)
    return f'<details class="srcs" open><summary>🔗 Офіційні джерела до розділу</summary><ul>{lis}</ul></details>'


def table(head, rows, cls=""):
    th = "".join(f"<th>{h}</th>" for h in head)
    trs = "".join("<tr>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f'<div class="tw"><table class="{cls}"><thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'


def ctrl(n, name, en, where, what, how, when, rec, err, lvl="core"):
    """Картка органу керування: 7 обов'язкових пунктів."""
    num = f'<span class="cn">{n}</span>' if n else ''
    return f'''<article class="ctrl {lvl}"><h4>{num}{name} <small>{en}</small></h4>
<dl><dt>📍 Де</dt><dd>{where}</dd><dt>🎯 Для чого</dt><dd>{what}</dd><dt>🖐 Як користуватися</dt><dd>{how}</dd>
<dt>🕐 Коли корисно</dt><dd>{when}</dd><dt>✅ Початківцю</dt><dd>{rec}</dd><dt>❌ Типові помилки</dt><dd>{err}</dd></dl></article>'''


def module(num, mid, title, lead, body):
    return f'''<section class="module" id="{mid}" data-num="{num}"><header class="mh"><div class="mnum">Модуль {num}</div><h2>{title}</h2><p class="lead">{lead}</p>
<label class="done"><input type="checkbox" data-done="{mid}"> Модуль пройдено</label></header>{body}</section>'''


def path(*parts):
    return '<span class="path">' + ' <i>→</i> '.join(parts) + '</span>'
