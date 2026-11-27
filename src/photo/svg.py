# -*- coding: utf-8 -*-
"""SVG-ілюстрації фотокурсу: демонстраційні сцени та схеми корпусу."""
import math

_uid = [0]


def _id(p):
    _uid[0] += 1
    return f"{p}{_uid[0]}"


def scene(f=None, ss=None, iso=None, focal=50, ev=0.0, compress=False, w=300, label=None,
          subject_moves=False, demo=True):
    """Демонстраційна сцена: людина на передньому плані, місто/дерева позаду, рухомий м'яч.
    f — діафрагма (розмиття фону), ss — витримка в секундах (змащування м'яча),
    iso — шум, focal — кут огляду, ev — яскравість (стопи), compress — однаковий масштаб обличчя."""
    fid = _id("s")
    H = int(w * 2 / 3)
    # кут огляду: світ 600 одиниць завширшки = 28 мм
    vw = 600 * 28 / focal if not compress else 600
    vh = vw * 2 / 3
    vx = 300 - vw / 2
    vy = 210 - vh * 0.62
    if compress:
        vx, vy, vh = 0, 0, 400
    # розмиття фону ~ f^2 / N
    N = f or 8
    bl = 7.5 * (focal / 75) ** 2 * (2.8 / N)
    if compress:
        bl = 7.5 * (focal / 75) ** 2 * (2.8 / N) * 0.8
    bl = max(0, round(bl, 2))
    mb = 0
    if ss:
        mb = min(60, 900 * ss) if not subject_moves else min(25, 400 * ss)
    noise = 0
    if iso:
        noise = max(0, min(0.55, (math.log2(iso / 100)) * 0.085))
    bright = ev
    bg_scale = (focal / 28) if compress else 1
    sky1, sky2 = "#8EC5F0", "#E8F3FB"
    bg = f'''<g filter="url(#{fid}b)"><g transform="translate(300 250) scale({bg_scale:.3f}) translate(-300 -250)">
<rect x="-400" y="-200" width="1400" height="460" fill="url(#{fid}sky)"/>
<circle cx="470" cy="70" r="26" fill="#FFF3C4"/>
<g fill="#9AAFC2">
<rect x="20" y="120" width="60" height="140"/><rect x="90" y="90" width="45" height="170"/><rect x="145" y="140" width="70" height="120"/>
<rect x="380" y="100" width="55" height="160"/><rect x="445" y="130" width="80" height="130"/><rect x="535" y="80" width="50" height="180"/>
<rect x="-120" y="110" width="120" height="150"/><rect x="600" y="120" width="140" height="140"/></g>
<g fill="#FFFFFF" opacity=".55">
<rect x="30" y="135" width="10" height="10"/><rect x="55" y="135" width="10" height="10"/><rect x="30" y="165" width="10" height="10"/><rect x="55" y="165" width="10" height="10"/>
<rect x="100" y="105" width="8" height="10"/><rect x="118" y="105" width="8" height="10"/><rect x="100" y="135" width="8" height="10"/><rect x="118" y="135" width="8" height="10"/>
<rect x="392" y="118" width="9" height="11"/><rect x="414" y="118" width="9" height="11"/><rect x="392" y="150" width="9" height="11"/><rect x="414" y="150" width="9" height="11"/>
<rect x="548" y="95" width="9" height="11"/><rect x="566" y="95" width="9" height="11"/><rect x="548" y="125" width="9" height="11"/></g>
<g fill="#5E9E6E"><circle cx="250" cy="200" r="34"/><circle cx="335" cy="190" r="40"/><circle cx="215" cy="215" r="24"/><circle cx="365" cy="215" r="26"/></g>
<rect x="296" y="210" width="8" height="50" fill="#6B4F3A"/>
<rect x="-400" y="255" width="1400" height="200" fill="#C9B79C"/>
<g fill="#F7D35C"><circle cx="160" cy="200" r="5"/><circle cx="470" cy="190" r="5"/><circle cx="520" cy="215" r="4"/></g>
</g></g>'''
    person = f'''<g>
<ellipse cx="300" cy="400" rx="95" ry="110" fill="#3C5A8A"/>
<rect x="285" y="250" width="30" height="40" fill="#E9B48F"/>
<ellipse cx="300" cy="232" rx="42" ry="50" fill="#F2C29E"/>
<path d="M258 222 Q262 178 300 176 Q340 176 344 224 Q336 196 300 196 Q266 196 258 222Z" fill="#3B2A20"/>
<circle cx="286" cy="234" r="4" fill="#2A2A2A"/><circle cx="314" cy="234" r="4" fill="#2A2A2A"/>
<path d="M288 258 Q300 266 312 258" stroke="#B0654A" stroke-width="3" fill="none" stroke-linecap="round"/>
</g>'''
    ball = ""
    if ss is not None:
        bx = 410 if not compress else 470
        by = 190 if not compress else 300
        ball = f'''<g filter="url(#{fid}m)"><circle cx="{bx}" cy="{by}" r="18" fill="#E2552B"/>
<path d="M{bx-18} {by} H{bx+18} M{bx} {by-18} V{by+18}" stroke="#fff" stroke-width="3"/></g>'''
    noise_layer = ""
    if noise > 0:
        noise_layer = f'<rect x="-400" y="-200" width="1400" height="800" filter="url(#{fid}n)" opacity="{noise:.2f}"/>'
    light = ""
    if bright > 0:
        light = f'<rect x="-400" y="-200" width="1400" height="800" fill="#fff" opacity="{min(.92, 1 - 0.5 ** bright):.2f}"/>'
    elif bright < 0:
        light = f'<rect x="-400" y="-200" width="1400" height="800" fill="#000" opacity="{min(.93, 1 - 0.5 ** (-bright)):.2f}"/>'
    lbl = ""
    if label:
        lbl = f'<figcaption>{label}</figcaption>'
    demo_tag = '<text x="{x}" y="{y}" font-size="{fs}" fill="#fff" opacity=".85" font-family="Inter,sans-serif">ДЕМО</text>'.format(
        x=vx + vw - vw * 0.13, y=vy + vh * 0.08, fs=vw * 0.04) if demo else ""
    svg = f'''<svg viewBox="{vx:.1f} {vy:.1f} {vw:.1f} {vh:.1f}" width="{w}" height="{H}" xmlns="http://www.w3.org/2000/svg" role="img" preserveAspectRatio="xMidYMid slice">
<defs><linearGradient id="{fid}sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{sky1}"/><stop offset="1" stop-color="{sky2}"/></linearGradient>
<filter id="{fid}b" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="{bl}"/></filter>
<filter id="{fid}m" x="-200%" y="-50%" width="500%" height="200%"><feGaussianBlur stdDeviation="{mb:.1f} 0"/></filter>
<filter id="{fid}n"><feTurbulence type="fractalNoise" baseFrequency="1.6" numOctaves="1" seed="{_uid[0]}"/><feColorMatrix type="saturate" values="0"/></filter>
</defs>{bg}{person}{ball}{noise_layer}{light}{demo_tag}</svg>'''
    return f'<figure class="scene">{svg}{lbl}</figure>'


def strip(items, caption=None):
    """Ряд сцен для порівняння."""
    cap = f'<p class="strip-cap">🧪 Демонстраційні ілюстрації (згенеровані схеми, не знімки з нашого обладнання). {caption or ""}</p>'
    return '<div class="strip">' + "".join(items) + '</div>' + cap


# ---------- Схеми корпусу ----------

def _num(n, x, y, tx=None, ty=None):
    line = ""
    if tx is not None:
        line = f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty}" stroke="#E8590C" stroke-width="1.6"/>'
        x, y = tx, ty
    return f'{line}<circle cx="{x}" cy="{y}" r="11" fill="#E8590C"/><text x="{x}" y="{y+4.5}" text-anchor="middle" font-size="12" font-weight="700" fill="#fff" font-family="Inter,sans-serif">{n}</text>'


BODY = 'fill="#2B2B30" stroke="#16161A" stroke-width="2"'
PART = 'fill="#3E3E46" stroke="#16161A" stroke-width="1.5"'
BTN = 'fill="#55555F" stroke="#16161A" stroke-width="1.2"'


def _wrap(svg, title, src):
    return f'''<figure class="diagram">{svg}<figcaption><b>{title}</b> — схематичне зображення, не фотографія й не в масштабі. Номери збігаються з офіційним розділом «Identifying parts» Sony Help Guide, де є оригінальна ілюстрація: <a href="{src}" target="_blank" rel="noopener">відкрити ілюстрацію Sony</a>.</figcaption></figure>'''


def rear():
    s = f'''<svg viewBox="0 0 660 400" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Задня частина Sony A7 IV, схема">
<path d="M40 110 Q40 90 60 90 H220 L240 40 H360 L380 90 H600 Q625 90 625 115 V350 Q625 370 600 370 H60 Q40 370 40 350Z" {BODY}/>
<rect x="255" y="50" width="90" height="62" rx="18" {PART}/><rect x="275" y="62" width="50" height="36" rx="8" fill="#101014"/>
<circle cx="360" cy="70" r="5" fill="#101014"/>
<circle cx="236" cy="82" r="8" {BTN}/>
<rect x="70" y="108" width="40" height="18" rx="9" {BTN}/><rect x="122" y="108" width="54" height="18" rx="9" {BTN}/>
<text x="149" y="121" text-anchor="middle" font-size="9" fill="#ddd" font-family="Inter">MENU</text><text x="90" y="121" text-anchor="middle" font-size="9" fill="#ddd" font-family="Inter">C3</text>
<rect x="62" y="140" width="330" height="215" rx="10" fill="#141418" stroke="#16161A"/><rect x="74" y="152" width="306" height="190" rx="4" fill="#26303E"/>
<text x="227" y="252" text-anchor="middle" font-size="13" fill="#9FB3C8" font-family="Inter">поворотний сенсорний екран</text>
<rect x="420" y="98" width="34" height="18" rx="9" {BTN}/><text x="437" y="111" text-anchor="middle" font-size="9" fill="#ddd" font-family="Inter">C1</text>
<rect x="470" y="98" width="46" height="20" rx="10" fill="#E3E3E8" stroke="#16161A"/><text x="493" y="112" text-anchor="middle" font-size="9" fill="#222" font-family="Inter" font-weight="700">AF-ON</text>
<rect x="528" y="98" width="40" height="20" rx="10" {BTN}/><text x="548" y="112" text-anchor="middle" font-size="9" fill="#ddd" font-family="Inter">AEL</text>
<rect x="575" y="70" width="40" height="22" rx="6" {PART}/>
<circle cx="520" cy="172" r="17" {BTN}/><circle cx="520" cy="172" r="6" fill="#77777F"/>
<rect x="440" y="196" width="34" height="18" rx="9" {BTN}/><text x="457" y="209" text-anchor="middle" font-size="9" fill="#ddd" font-family="Inter">Fn</text>
<circle cx="520" cy="262" r="46" {PART}/><circle cx="520" cy="262" r="19" {BTN}/>
<circle cx="586" cy="328" r="4" fill="#E04040"/>
<circle cx="470" cy="330" r="12" {BTN}/><circle cx="560" cy="338" r="12" {BTN}/>
<text x="470" y="334" text-anchor="middle" font-size="10" fill="#ddd">🗑</text><text x="560" y="342" text-anchor="middle" font-size="10" fill="#ddd">▶</text>
{_num(1,300,80,300,22)}{_num(2,262,104,214,22)}{_num(3,90,117,62,62)}{_num(4,149,117,150,62)}{_num(5,140,300,20,300)}
{_num(6,360,70,395,30)}{_num(7,236,82,236,22)}{_num(8,437,107,420,62)}{_num(9,493,108,480,62)}{_num(10,548,108,545,62)}
{_num(11,520,172,640,165)}{_num(12,457,205,410,205)}{_num(13,520,262,640,255)}{_num(14,586,328,640,330)}{_num(15,470,330,430,380)}{_num(16,560,338,560,390)}
</svg>'''
    return _wrap(s, "Задня частина", "https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000660240.html")


def top():
    s = f'''<svg viewBox="0 0 660 330" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Верхня частина Sony A7 IV, схема">
<path d="M40 160 Q40 140 60 140 H600 Q628 140 628 170 V250 Q628 270 600 270 H60 Q40 270 40 250Z" {BODY}/>
<path d="M240 140 L258 95 H372 L390 140Z" {PART}/>
<rect x="278" y="104" width="74" height="26" rx="4" fill="#4A4A52" stroke="#16161A"/>
<circle cx="250" cy="190" r="8" fill="none" stroke="#bbb" stroke-width="1.5"/><line x1="240" y1="190" x2="260" y2="190" stroke="#bbb" stroke-width="1.5"/>
<rect x="180" y="200" width="52" height="40" rx="3" fill="#101014"/>
<ellipse cx="500" cy="300" rx="70" ry="28" fill="#2B2B30" stroke="#16161A" stroke-width="2"/>
<circle cx="440" cy="195" r="36" {PART}/><circle cx="440" cy="195" r="26" {BTN}/><text x="440" y="200" text-anchor="middle" font-size="11" fill="#eee" font-family="Inter">P A S M</text>
<rect x="410" y="232" width="60" height="10" rx="4" fill="#888"/>
<circle cx="560" cy="185" r="26" {PART}/>
<rect x="588" y="225" width="40" height="22" rx="6" {PART}/><circle cx="608" cy="236" r="5" fill="#aaa"/>
<circle cx="520" cy="240" r="9" fill="#C0392B" stroke="#16161A"/>
<circle cx="500" cy="200" r="8" {BTN}/>
<ellipse cx="548" cy="296" rx="22" ry="14" fill="#9A9AA3" stroke="#16161A"/>
<text x="330" y="315" text-anchor="middle" font-size="11" fill="#888" font-family="Inter">↓ перед камери (об'єктив) ↓</text>
{_num(1,440,236,400,300)}{_num(2,440,195,395,175)}{_num(3,560,185,560,135)}{_num(4,608,236,645,236)}{_num(5,520,240,520,285)}
{_num(6,500,200,480,135)}{_num(7,315,117,315,62)}{_num(8,250,190,250,135)}
</svg>'''
    return _wrap(s, "Верхня частина", "https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000660253.html")


def front():
    s = f'''<svg viewBox="0 0 660 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Передня частина Sony A7 IV без об'єктива, схема">
<path d="M40 120 Q40 100 60 100 H250 L268 50 H392 L410 100 H600 Q625 100 625 125 V340 Q625 360 600 360 H60 Q40 360 40 340Z" {BODY}/>
<path d="M40 120 Q40 100 60 100 H150 V360 H60 Q40 360 40 340Z" fill="#232327" stroke="#16161A" stroke-width="2"/>
<circle cx="330" cy="230" r="108" fill="#1D1D22" stroke="#9A9AA3" stroke-width="7"/>
<rect x="262" y="185" width="136" height="92" rx="3" fill="#5D4A7A"/><rect x="262" y="185" width="136" height="92" rx="3" fill="url(#gl)" opacity=".5"/>
<defs><linearGradient id="gl" x1="0" x2="1"><stop offset="0" stop-color="#8FA8FF"/><stop offset="1" stop-color="#E37BFF"/></linearGradient></defs>
<g fill="#D4AF37">{''.join(f'<rect x="{300+i*9}" y="{322}" width="5" height="9" rx="1"/>' for i in range(7))}</g>
<circle cx="330" cy="116" r="5" fill="#fff"/>
<circle cx="452" cy="300" r="11" {BTN}/>
<circle cx="210" cy="120" r="7" fill="#D86A2B"/>
<ellipse cx="100" cy="86" rx="38" ry="12" fill="#9A9AA3" stroke="#16161A"/>
<rect x="120" y="110" width="60" height="14" rx="5" {PART}/>
<g fill="#111">{''.join(f'<circle cx="{298+i*8}" cy="78" r="1.8"/>' for i in range(8))}</g>
{_num(1,100,86,100,30)}{_num(2,150,117,175,150)}{_num(3,452,300,520,330)}{_num(4,326,78,360,22)}{_num(5,210,120,210,62)}
{_num(6,330,116,450,62)}{_num(7,330,230,560,215)}{_num(8,410,165,560,165)}{_num(9,330,326,330,372)}
</svg>'''
    return _wrap(s, "Передня частина (без об'єктива)", "https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000660241.html")


def sides():
    s = f'''<svg viewBox="0 0 660 340" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Бокові частини Sony A7 IV, схема">
<text x="160" y="22" text-anchor="middle" font-size="13" fill="#666" font-family="Inter">Ліва сторона (роз'єми, кришка відкрита)</text>
<rect x="60" y="40" width="200" height="270" rx="16" {BODY}/>
<rect x="78" y="62" width="164" height="200" rx="8" fill="#1A1A1F"/>
<circle cx="120" cy="90" r="9" fill="#111" stroke="#E46B8E" stroke-width="3"/><circle cx="200" cy="90" r="9" fill="#111" stroke="#47A6E0" stroke-width="3"/>
<rect x="96" y="124" width="48" height="16" rx="3" fill="#111" stroke="#777"/><rect x="172" y="124" width="40" height="14" rx="7" fill="#111" stroke="#777"/>
<rect x="96" y="172" width="30" height="12" rx="3" fill="#111" stroke="#777"/><circle cx="200" cy="178" r="4" fill="#F0A030"/>
<g fill="#111">{''.join(f'<circle cx="{110+i*10}" cy="232" r="2"/>' for i in range(6))}</g>
<rect x="140" y="288" width="40" height="10" rx="4" fill="#777"/>
<text x="500" y="22" text-anchor="middle" font-size="13" fill="#666" font-family="Inter">Права сторона (кришка карт відкрита)</text>
<rect x="400" y="40" width="200" height="270" rx="16" {BODY}/>
<rect x="418" y="80" width="164" height="170" rx="8" fill="#1A1A1F"/>
<rect x="436" y="108" width="128" height="16" rx="2" fill="#666"/><rect x="436" y="190" width="128" height="16" rx="2" fill="#666"/>
<text x="500" y="100" text-anchor="middle" font-size="10" fill="#ccc" font-family="Inter">SLOT 1 · CFexpress A / SD</text><text x="500" y="182" text-anchor="middle" font-size="10" fill="#ccc" font-family="Inter">SLOT 2 · SD</text>
<rect x="480" y="288" width="40" height="10" rx="4" fill="#777"/>
{_num(1,120,132,30,132)}{_num(2,130,232,30,232)}{_num(3,120,90,30,80)}{_num(4,200,90,290,80)}{_num(5,192,131,290,131)}
{_num(6,200,178,290,178)}{_num(7,111,178,30,182)}{_num(8,160,293,160,328)}{_num(9,500,116,630,116)}{_num(10,500,198,630,198)}
</svg>'''
    return _wrap(s, "Бокові частини", "https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000660239.html")


def bottom():
    s = f'''<svg viewBox="0 0 660 240" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Нижня частина Sony A7 IV, схема">
<rect x="40" y="40" width="580" height="150" rx="22" {BODY}/>
<rect x="430" y="60" width="160" height="110" rx="10" {PART}/><rect x="450" y="80" width="120" height="70" rx="6" fill="#26262B"/>
<rect x="470" y="150" width="40" height="12" rx="4" fill="#999"/>
<rect x="398" y="95" width="22" height="40" rx="5" fill="#A0A0A8" stroke="#16161A"/>
<circle cx="250" cy="115" r="16" fill="#111" stroke="#999" stroke-width="4"/>
{_num(1,409,115,409,215)}{_num(2,510,115,510,22)}{_num(3,560,150,620,215)}{_num(4,250,115,250,22)}
</svg>'''
    return _wrap(s, "Нижня частина", "https://helpguide.sony.net/ilc/2110/v1/en/contents/TP1000660237.html")


def lens():
    s = f'''<svg viewBox="0 0 700 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Tamron 28-75mm F/2.8 Di III VXD G2 A063, схема">
<path d="M40 70 L130 90 V210 L40 230Z" fill="#26262B" stroke="#111" stroke-width="2"/>
<rect x="130" y="85" width="380" height="130" rx="6" fill="#2F2F35" stroke="#111" stroke-width="2"/>
<rect x="150" y="85" width="60" height="130" fill="#3A3A42"/>
<g stroke="#4D4D57" stroke-width="3">{''.join(f'<line x1="{224+i*7}" y1="88" x2="{224+i*7}" y2="212"/>' for i in range(24))}</g>
<g stroke="#4D4D57" stroke-width="3">{''.join(f'<line x1="{400+i*7}" y1="88" x2="{400+i*7}" y2="212"/>' for i in range(12))}</g>
<text x="250" y="80" font-size="11" fill="#666" font-family="Inter">28 35 50 75</text><rect x="388" y="86" width="2" height="12" fill="#fff"/>
<circle cx="372" cy="160" r="9" fill="#55555F" stroke="#111"/>
<rect x="510" y="98" width="45" height="104" rx="4" fill="#3A3A42" stroke="#111"/>
<rect x="555" y="105" width="30" height="90" fill="#9A9AA3" stroke="#111"/>
<rect x="570" y="133" width="10" height="20" rx="3" fill="#111"/>
<circle cx="548" cy="100" r="4" fill="#fff"/>
<g fill="#D4AF37">{''.join(f'<rect x="586" y="{120+i*9}" width="6" height="5"/>' for i in range(6))}</g>
<rect x="141" y="88" width="3" height="8" fill="#fff"/><path d="M48 76 L60 80" stroke="#fff" stroke-width="3"/><circle cx="125" cy="98" r="3" fill="#E04040"/>
<text x="320" y="270" text-anchor="middle" font-size="11" fill="#888" font-family="Inter">← перед (бленда, фільтри) · · · · · · · · · · · · байонет Sony E (до камери) →</text>
{_num(1,70,150,70,40)}{_num(2,54,78,20,40)}{_num(3,125,98,110,40)}{_num(4,135,150,135,255)}{_num(5,142,92,180,40)}
{_num(6,300,150,300,255)}{_num(7,280,77,260,30)}{_num(8,389,92,400,30)}{_num(9,372,160,372,255)}{_num(10,440,150,440,255)}
{_num(11,575,143,640,255)}{_num(12,548,100,560,30)}{_num(13,589,135,670,135)}
</svg>'''
    return f'''<figure class="diagram">{s}<figcaption><b>Tamron 28–75mm F/2.8 Di III VXD G2 (A063)</b> — схематичне зображення, не фотографія. Номери збігаються з офіційною інструкцією Tamron (Owner's manual, Fig. 1). Точне розташування кільця фокусування й кільця зуму дивіться на фото виробника: <a href="https://www.tamron.com/global/consumer/lenses/a063/" target="_blank" rel="noopener">сторінка A063 на tamron.com</a>.</figcaption></figure>'''


def triangle():
    return '''<figure class="diagram"><svg viewBox="0 0 620 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Трикутник експозиції">
<polygon points="310,30 560,320 60,320" fill="#FFF4EC" stroke="#E8590C" stroke-width="3"/>
<text x="310" y="200" text-anchor="middle" font-size="22" font-weight="800" fill="#1D1B26" font-family="Inter">ЕКСПОЗИЦІЯ</text>
<text x="310" y="226" text-anchor="middle" font-size="13" fill="#6B6878" font-family="Inter">скільки світла записала матриця</text>
<circle cx="310" cy="30" r="26" fill="#E8590C"/><text x="310" y="36" text-anchor="middle" font-size="16" font-weight="700" fill="#fff" font-family="Inter">f/</text>
<text x="350" y="26" font-size="15" font-weight="700" fill="#1D1B26" font-family="Inter">ДІАФРАГМА</text><text x="350" y="46" font-size="12" fill="#6B6878" font-family="Inter">+ глибина різкості, боке</text>
<circle cx="60" cy="320" r="26" fill="#2F6FEB"/><text x="60" y="326" text-anchor="middle" font-size="15" font-weight="700" fill="#fff" font-family="Inter">1/s</text>
<text x="20" y="356" font-size="15" font-weight="700" fill="#1D1B26" font-family="Inter">ВИТРИМКА · + рух, змащування</text>
<circle cx="560" cy="320" r="26" fill="#18A058"/><text x="560" y="326" text-anchor="middle" font-size="14" font-weight="700" fill="#fff" font-family="Inter">ISO</text>
<text x="600" y="356" text-anchor="end" font-size="15" font-weight="700" fill="#1D1B26" font-family="Inter">ISO · + цифровий шум</text>
</svg><figcaption>Кожна вершина змінює яскравість і водночас додає свій «побічний ефект». 1 стоп = удвічі більше або менше світла.</figcaption></figure>'''


def histo(kind):
    import random
    random.seed({"dark": 1, "ok": 2, "bright": 3, "contrast": 4}[kind])
    bars = []
    for i in range(64):
        x = i / 63
        if kind == "dark":
            v = math.exp(-((x - .18) ** 2) / .012) + (2.2 if i == 0 else 0)
        elif kind == "bright":
            v = math.exp(-((x - .84) ** 2) / .012) + (2.2 if i == 63 else 0)
        elif kind == "contrast":
            v = math.exp(-((x - .08) ** 2) / .006) + math.exp(-((x - .93) ** 2) / .006) + .12
        else:
            v = math.exp(-((x - .5) ** 2) / .05) * .9 + .08
        v = v * (0.85 + random.random() * .3)
        h = min(110, v * 60)
        bars.append(f'<rect x="{6+i*4.4:.1f}" y="{118-h:.1f}" width="3.6" height="{h:.1f}" fill="#1D1B26"/>')
    names = {"dark": "Недосвітлено: «гора» притиснута ліворуч", "ok": "Нормально: дані по всьому діапазону",
             "bright": "Пересвітлено: «гора» вперлася праворуч", "contrast": "Високий контраст: провали з обох боків"}
    return f'<figure class="histo"><svg viewBox="0 0 296 124" xmlns="http://www.w3.org/2000/svg"><rect width="296" height="124" fill="#F2EFE9"/>{"".join(bars)}<line x1="6" y1="118" x2="290" y2="118" stroke="#999"/></svg><figcaption>{names[kind]}</figcaption></figure>'


def fov():
    """Кути огляду 28/35/50/60/75 на одному кадрі."""
    rects = []
    cols = {28: "#E8590C", 35: "#D99A00", 50: "#18A058", 60: "#2F6FEB", 75: "#8B5CF6"}
    for fl, c in cols.items():
        w = 600 * 28 / fl
        h = w * 2 / 3
        x = 300 - w / 2
        y = 210 - h * .62
        rects.append(f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" fill="none" stroke="{c}" stroke-width="3"/><text x="{x+6:.1f}" y="{y+16:.1f}" font-size="14" font-weight="700" fill="{c}" font-family="Inter">{fl} мм</text>')
    sc = scene(focal=28, f=8, w=600, demo=False)
    inner = sc.replace('<figure class="scene">', '').replace('</figure>', '')
    inner = inner.replace('</svg>', ''.join(rects) + '</svg>', 1)
    return f'<figure class="scene wide">{inner}<figcaption>Демонстраційна ілюстрація: що потрапляє в кадр з однієї точки на кожній фокусній відстані Tamron 28–75 (розраховано для повного кадру 36×24 мм).</figcaption></figure>'
