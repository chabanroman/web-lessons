# -*- coding: utf-8 -*-
"""Збирання фотокурсу Sony A7 IV + Tamron 28-75 G2.
python3 src/photo/build.py        → photo/index.html, photo/cheatsheets.html
python3 src/photo/build.py --pdf  → також photo/*.pdf (потрібен playwright + chromium)"""
import os, sys, re
sys.path.insert(0, os.path.dirname(__file__))
import svg
from h import box
from c1 import M1, M2
from c2 import M3, M4, M5
from c3 import M6, M7
from c4 import M8, M9, M10
from c5 import M11, M12
from c6 import M13, M14
from c7 import M15, APXA, APXB, SHEETS

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
OUT = os.path.join(ROOT, "photo")
os.makedirs(OUT, exist_ok=True)

TOC = [("m1", "1", "Знайомство з фотоапаратом"), ("m2", "2", "Об'єктив Tamron і Lens Utility"), ("m3", "3", "Основи фотографії"),
       ("m4", "4", "Режими зйомки"), ("m5", "5", "Автофокус і різкість"), ("m6", "6", "Путівник меню"),
       ("m7", "7", "Перше налаштування"), ("m8", "8", "Готові налаштування: 27 ситуацій"), ("m9", "9", "Як використовувати 28–75 мм"),
       ("m10", "10", "Композиція і світло"), ("m11", "11", "Основи відео"), ("m12", "12", "Перенесення й обробка"),
       ("m13", "13", "Курс на 14 днів"), ("m14", "14", "Проблеми та рішення"), ("m15", "15", "Шпаргалки"),
       ("apxA", "А", "Види об'єктивів"), ("apxB", "Б", "Словник термінів")]

CSS = r"""
:root{--bg:#FBF8F3;--ink:#1D1B26;--mut:#6B6878;--line:#E7E1D6;--card:#fff;--acc:#E8590C;--acc2:#2F6FEB;--ok:#18A058;--warn:#C9302C;--nv:#B7791F}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font:400 16.5px/1.62 'Golos Text',Inter,system-ui,-apple-system,sans-serif}
a{color:var(--acc2)}
h1,h2,h3,h4{line-height:1.2}
h2{font:800 clamp(26px,4vw,40px)/1.1 'Unbounded','Inter',sans-serif;margin:.2em 0 .3em;letter-spacing:-.01em}
h3{font-size:22px;margin:2em 0 .6em;padding-top:.4em;border-top:1px solid var(--line)}
h4{font-size:17.5px;margin:0 0 .5em}
code{background:#F1ECE3;padding:1px 6px;border-radius:6px;font-size:.9em}
.layout{display:grid;grid-template-columns:290px 1fr;min-height:100vh}
nav.side{position:sticky;top:0;height:100vh;overflow:auto;background:#1D1B26;color:#EDEAF2;padding:22px 16px}
nav.side .brand{font:800 16px 'Unbounded',Inter,sans-serif;color:#fff;margin:0 0 4px}
nav.side .sub{font-size:13px;color:#A9A5B8;margin-bottom:16px}
nav.side a{display:flex;gap:10px;align-items:baseline;color:#D7D3E0;text-decoration:none;padding:7px 10px;border-radius:10px;font-size:14.5px}
nav.side a:hover,nav.side a.act{background:#2E2B3A;color:#fff}
nav.side a b{min-width:22px;color:var(--acc);font-weight:700}
nav.side a.d::after{content:"✓";margin-left:auto;color:#6BD49A}
nav.side .dl{margin-top:16px;border-top:1px solid #34313F;padding-top:14px}
nav.side .dl a{background:#2E2B3A;margin-bottom:6px}
.prog{height:6px;background:#34313F;border-radius:9px;margin:8px 0 14px;overflow:hidden}.prog i{display:block;height:100%;width:0;background:var(--acc);transition:.3s}
main{max-width:1000px;padding:34px 44px 120px;width:100%;min-width:0}
.cover{background:linear-gradient(135deg,#1D1B26,#3A2A4A);color:#fff;border-radius:28px;padding:48px 44px;margin-bottom:28px;position:relative;overflow:hidden}
.cover h1{font:800 clamp(30px,5vw,52px)/1.05 'Unbounded',Inter,sans-serif;margin:8px 0 14px}
.cover .kit{display:flex;flex-wrap:wrap;gap:8px;margin-top:18px}.cover .kit span{background:rgba(255,255,255,.12);padding:6px 12px;border-radius:99px;font-size:14px}
.cover .tag{color:#FFB287;font-weight:600;letter-spacing:.08em;text-transform:uppercase;font-size:13px}
.cover .lens{position:absolute;right:-60px;top:-60px;width:280px;height:280px;border-radius:50%;background:radial-gradient(circle at 40% 40%,#6E5BA8 0,#2A2340 40%,#0E0C14 62%,#3A3644 63%,#1A1820 70%,transparent 71%);opacity:.7}
.module{background:var(--card);border:1px solid var(--line);border-radius:26px;padding:34px 38px;margin:26px 0}
.mh .mnum{color:var(--acc);font-weight:700;letter-spacing:.08em;text-transform:uppercase;font-size:13px}
.lead{font-size:18px;color:var(--mut);margin:.2em 0 1em}
label.done{display:inline-flex;gap:8px;align-items:center;font-size:14px;color:var(--mut);background:#F5F1EA;padding:6px 12px;border-radius:99px;cursor:pointer}
.box{border-radius:16px;padding:14px 18px;margin:16px 0;border:1px solid;break-inside:avoid}
.box-t{font-weight:700;font-size:14px;margin-bottom:4px}
.box p{margin:.3em 0}.box ul,.box ol{margin:.3em 0;padding-left:1.3em}
.b-off{background:#EEF4FF;border-color:#C9D9FB}.b-off .box-t{color:#1F4FB8}
.b-pro{background:#FFF4EC;border-color:#F7CDB0}.b-pro .box-t{color:#B5440A}
.b-nv{background:#FFF8E6;border-color:#F1D79A}.b-nv .box-t{color:#8A5A00}
.b-tip{background:#EFFAF3;border-color:#BDE7CD}.b-tip .box-t{color:#137A42}
.b-warn{background:#FDEEEE;border-color:#F3C2C1}.b-warn .box-t{color:#A32420}
.b-ex{background:#F3F0FF;border-color:#D7CEFB}.b-ex .box-t{color:#5B3FD1}
.b-key{background:#1D1B26;color:#F3F1F7;border-color:#1D1B26}.b-key .box-t{color:#FFB287}
.legend{display:grid;grid-template-columns:repeat(3,1fr);gap:10px}.legend .box{margin:0}
.nv-inline{background:#FFF8E6;padding:1px 6px;border-radius:6px}
.path{display:inline;background:#F1ECE3;border-radius:8px;padding:1px 7px;font-size:.88em;font-family:Inter,system-ui,sans-serif;white-space:normal}
.path i{font-style:normal;color:var(--acc)}
.tw{overflow-x:auto;margin:14px 0}
table{border-collapse:collapse;width:100%;font-size:14.5px;background:#fff}
th{background:#1D1B26;color:#fff;text-align:left;padding:9px 10px;font-weight:600}
td{border-bottom:1px solid var(--line);padding:8px 10px;vertical-align:top}
tr:nth-child(even) td{background:#FCFAF6}
table.fill td:nth-child(2),table.fill td:nth-child(3){min-width:180px}
table.menu td:first-child{min-width:170px}
.ctrls{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.ctrl{border:1px solid var(--line);border-radius:18px;padding:16px 18px;background:#FFFDF9;break-inside:avoid}
.ctrl.rare{opacity:.92}.ctrl.rare h4::after{content:"рідко";font-size:11px;background:#EEE;color:#777;padding:2px 8px;border-radius:99px;margin-left:8px;vertical-align:middle}
.ctrl h4 small{display:block;color:var(--mut);font-weight:500;font-size:13px;margin-top:2px}
.cn{display:inline-grid;place-items:center;min-width:26px;height:26px;padding:0 6px;border-radius:99px;background:var(--acc);color:#fff;font-size:13px;margin-right:8px;vertical-align:1px}
dl{margin:0}.ctrl dl,.mode dl,.day dl,.scard dl{display:grid;grid-template-columns:auto 1fr;gap:4px 12px;font-size:14.5px}
dt{font-weight:600;color:#45414F;white-space:nowrap}dd{margin:0}
.mode,.day{border:1px solid var(--line);border-radius:18px;padding:16px 20px;margin:12px 0;background:#FFFDF9;break-inside:avoid}
.days{display:grid;grid-template-columns:1fr 1fr;gap:14px}.day .dn{color:var(--acc);font-weight:700;font-size:13px;text-transform:uppercase}
.day dd ol{margin:0;padding-left:1.2em}
figure{margin:16px 0}
figure.diagram{background:#F6F3EE;border-radius:18px;padding:14px;break-inside:avoid}
figure.diagram svg{width:100%;height:auto;display:block}
figcaption{font-size:13px;color:var(--mut);margin-top:6px}
.strip{display:grid;grid-auto-flow:column;grid-auto-columns:1fr;gap:10px;margin:14px 0 4px}
.strip figure.scene{margin:0;flex:1 1 150px}
figure.scene svg{width:100%;height:auto;border-radius:12px;display:block}
figure.scene figcaption{text-align:center;font-weight:700;color:var(--ink);font-size:14px}
figure.scene.wide svg{max-width:640px}
figure.before svg{filter:saturate(.75) hue-rotate(12deg) contrast(.9)}
.strip-cap{font-size:12.5px;color:var(--mut);margin:2px 0 16px}
figure.histo{flex:1 1 200px;margin:0}figure.histo svg{width:100%;border-radius:10px}
.cmp{display:grid;grid-template-columns:1fr 1fr;gap:14px}.cmp figure{margin:0}.cmp svg{width:100%;border-radius:12px;display:block}
.cmp .ok figcaption{color:var(--ok);font-weight:600}.cmp .no figcaption{color:var(--warn);font-weight:600}
ol.steps li,ol.bigsteps li{margin:6px 0}
ol.bigsteps{counter-reset:s;list-style:none;padding:0}ol.bigsteps>li{counter-increment:s;position:relative;padding:12px 16px 12px 60px;border:1px solid var(--line);border-radius:16px;margin:10px 0;background:#FFFDF9;break-inside:avoid}
ol.bigsteps>li::before{content:counter(s);position:absolute;left:14px;top:12px;width:32px;height:32px;border-radius:10px;background:var(--acc);color:#fff;display:grid;place-items:center;font-weight:700}
ol.bigsteps h4{margin:2px 0 4px}ol.bigsteps p{margin:0}
.fn-grid{display:grid;grid-template-columns:repeat(6,1fr);gap:6px}.fn-grid span{background:#fff;border:1px solid #F7CDB0;border-radius:10px;padding:8px;font-size:12.5px;text-align:center}
.scards{display:grid;grid-template-columns:1fr 1fr;gap:14px}
.scard{border:1px solid var(--line);border-radius:18px;padding:16px 18px;background:#FFFDF9;break-inside:avoid}
.scard h4{display:flex;gap:10px;align-items:center}.scard h4 span{font-size:24px}
.params{display:grid;grid-template-columns:repeat(3,1fr);gap:6px;margin:6px 0 10px}
.params div{background:#F5F1EA;border-radius:10px;padding:6px 8px}.params i{display:block;font-style:normal;font-size:11px;color:var(--mut);text-transform:uppercase;letter-spacing:.03em}.params b{font-size:13.5px;font-weight:600}
.fix{display:grid;gap:4px;margin-top:8px;font-size:13.5px}.fix span{background:#EEF4FF;border-radius:8px;padding:4px 8px}
details.srcs{margin:18px 0 0;background:#F6F3EE;border-radius:14px;padding:10px 16px;font-size:14px}
details.srcs summary{cursor:pointer;font-weight:600}details.srcs ul{margin:6px 0 0;padding-left:1.2em;columns:2}
.small{font-size:13.5px;color:var(--mut)}
.print-only{display:none}
.vcam,.dof,.calc180{background:#1D1B26;color:#fff;border-radius:22px;padding:18px;margin:18px 0}
.vcam .stage{position:relative}.vcam .stage svg{width:100%;height:auto;border-radius:14px;display:block}
.vcam .ctl{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;margin-top:14px}
.vcam label,.dof label,.calc180 label{font-size:13px;color:#BDB8CC;display:block}
.vcam output,.dof output{font-weight:700;color:#fff;font-size:16px}
input[type=range]{width:100%;accent-color:var(--acc)}
.meter{display:flex;align-items:center;gap:10px;margin-top:12px;font-size:14px}.meter .bar{flex:1;height:10px;background:linear-gradient(90deg,#2F6FEB,#18A058 45%,#18A058 55%,#E8590C);border-radius:9px;position:relative}
.meter .bar i{position:absolute;top:-5px;width:4px;height:20px;background:#fff;border-radius:2px;left:50%}
.vcam .hint{font-size:13px;color:#BDB8CC;margin-top:8px}
.dof .row,.calc180 .row{display:grid;grid-template-columns:repeat(3,1fr);gap:12px}
.dof .res{margin-top:12px;font-size:15px}
.dof select,.calc180 select{width:100%;padding:6px;border-radius:8px}
.sheets{display:grid;gap:16px}
.sheet{border:2px solid var(--ink);border-radius:20px;padding:18px 22px;background:#fff;break-inside:avoid}
.sheet h3{border:0;margin:0 0 8px;padding:0;font:800 20px 'Unbounded',Inter,sans-serif}
.sheet-foot{font-size:11px;color:var(--mut);margin-top:8px;text-align:right}
ul.check{list-style:none;padding:0;columns:1}ul.check li{padding:5px 0 5px 30px;position:relative;border-bottom:1px dashed var(--line)}ul.check li::before{content:"";position:absolute;left:2px;top:7px;width:16px;height:16px;border:2px solid var(--ink);border-radius:4px}
.glsearch{width:100%;padding:12px 16px;border-radius:14px;border:1px solid var(--line);font-size:16px;margin:6px 0 14px}
dl.gloss{display:grid;grid-template-columns:1fr 1fr;gap:8px 18px}dl.gloss div{border-bottom:1px solid var(--line);padding:6px 0;break-inside:avoid}dl.gloss dt{white-space:normal}dl.gloss dt small{color:var(--mut);font-weight:500}dl.gloss dd{font-size:14.5px}
.menu-btn{display:none}
.toc-print{display:none}
.intro p{margin:.5em 0}
@media screen and (max-width:900px){html,body{overflow-x:hidden}.layout{grid-template-columns:minmax(0,1fr)}nav.side{position:fixed;z-index:20;inset:0 30% 0 0;transform:translateX(-105%);transition:.25s}nav.side.open{transform:none}
.menu-btn{display:block;position:fixed;z-index:30;right:14px;bottom:14px;background:var(--acc);color:#fff;border:0;border-radius:99px;padding:12px 18px;font-weight:700;box-shadow:0 8px 24px rgba(0,0,0,.25)}
main{padding:16px 14px 100px}.strip{grid-auto-flow:row;grid-template-columns:1fr 1fr}.module{padding:22px 18px}.ctrls,.scards,.days,.legend,.cmp,dl.gloss{grid-template-columns:1fr}.vcam .ctl{grid-template-columns:1fr 1fr}.params{grid-template-columns:1fr 1fr}.fn-grid{grid-template-columns:repeat(3,1fr)}details.srcs ul{columns:1}.cover{padding:30px 22px}}
@page{size:A4;margin:14mm 12mm 16mm}
@media print{body{background:#fff;font-size:11pt}nav.side,.menu-btn,label.done,.vcam,.dof,.calc180,.glsearch,noscript{display:none!important}.layout{display:block}main{max-width:none;padding:0}
.print-only{display:block}.module{border:0;padding:0;margin:0;border-radius:0;break-before:page}.cover{break-after:page;border-radius:0;min-height:255mm;display:flex;flex-direction:column;justify-content:center;-webkit-print-color-adjust:exact;print-color-adjust:exact}
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}h3{break-after:avoid}table{font-size:9.5pt}tr,figure,.box{break-inside:avoid}.ctrls,.scards,.days{display:block}.ctrl,.scard,.day,.mode{margin:8px 0}details.srcs ul{columns:1}
a{color:#1F4FB8;text-decoration:none}.toc-print{display:block!important;break-after:page}.sheet{break-before:page;border-width:1.5px}.sheets .sheet:first-child{break-before:auto}}
"""

JS = r"""
(function(){
const store={get(k){try{return localStorage.getItem(k)}catch(e){return null}},set(k,v){try{localStorage.setItem(k,v)}catch(e){}}};
// прогрес
const boxes=[...document.querySelectorAll('input[data-done]')];
function prog(){const mods=boxes.filter(b=>/^m\d+$/.test(b.dataset.done));const d=mods.filter(b=>b.checked).length;const p=document.querySelector('.prog i');if(p)p.style.width=(mods.length?d/mods.length*100:0)+'%';
mods.forEach(b=>{const a=document.querySelector('nav.side a[href="#'+b.dataset.done+'"]');if(a)a.classList.toggle('d',b.checked)});const t=document.getElementById('progt');if(t)t.textContent=d+' з '+mods.length+' модулів'}
boxes.forEach(b=>{b.checked=store.get('photo:'+b.dataset.done)==='1';b.addEventListener('change',()=>{store.set('photo:'+b.dataset.done,b.checked?'1':'0');prog()})});prog();
// активний пункт меню
const links=[...document.querySelectorAll('nav.side a[href^="#"]')];
const obs=new IntersectionObserver(es=>{es.forEach(e=>{if(e.isIntersecting){links.forEach(l=>l.classList.toggle('act',l.getAttribute('href')==='#'+e.target.id))}})},{rootMargin:'-40% 0px -55% 0px'});
document.querySelectorAll('section.module').forEach(s=>obs.observe(s));
const nb=document.querySelector('.menu-btn'),nav=document.querySelector('nav.side');if(nb){nb.onclick=()=>nav.classList.toggle('open');links.forEach(l=>l.addEventListener('click',()=>nav.classList.remove('open')))}
// словник
const gs=document.querySelector('.glsearch');if(gs)gs.addEventListener('input',()=>{const q=gs.value.toLowerCase();document.querySelectorAll('dl.gloss>div').forEach(d=>d.style.display=d.textContent.toLowerCase().includes(q)?'':'none')});
// віртуальна камера
const vc=document.getElementById('vcam');
if(vc){vc.innerHTML='<div class="stage">'+VCAM_SVG+'</div><div class="ctl">'+
'<div><label>Діафрагма <output id="o-f"></output></label><input type="range" id="r-f" min="0" max="6" step="1" value="0"></div>'+
'<div><label>Витримка <output id="o-s"></output></label><input type="range" id="r-s" min="0" max="7" step="1" value="3"></div>'+
'<div><label>ISO <output id="o-i"></output></label><input type="range" id="r-i" min="0" max="7" step="1" value="2"></div>'+
'<div><label>Фокусна <output id="o-l"></output></label><input type="range" id="r-l" min="28" max="75" step="1" value="50"></div></div>'+
'<div class="meter"><span>темно</span><div class="bar"><i id="mi"></i></div><span>світло</span> <b id="ev"></b></div>'+
'<div class="hint">🧪 Демонстраційна модель. Норма для цієї сцени: f/2.8 · 1/125 · ISO 400. Зверніть увагу, як кожен параметр змінює яскравість <i>і</i> свій побічний ефект.</div>';
const F=[2.8,4,5.6,8,11,16,22],S=[1/15,1/30,1/60,1/125,1/250,1/500,1/1000,1/2000],SL=['1/15','1/30','1/60','1/125','1/250','1/500','1/1000','1/2000'],I=[100,200,400,800,1600,3200,6400,12800];
const svg=vc.querySelector('svg'),blurs=svg.querySelectorAll('feGaussianBlur'),noise=svg.querySelector('rect[filter]'),light=[...svg.querySelectorAll('rect')].pop(),tag=svg.querySelector('text');
function upd(){const n=F[+rf.value],s=S[+rs.value],iso=I[+ri.value],fl=+rl.value;
document.getElementById('o-f').textContent='f/'+n;document.getElementById('o-s').textContent=SL[+rs.value]+' с';document.getElementById('o-i').textContent=iso;document.getElementById('o-l').textContent=fl+' мм';
const vw=600*28/fl,vh=vw*2/3,vx=300-vw/2,vy=210-vh*.62;svg.setAttribute('viewBox',vx+' '+vy+' '+vw+' '+vh);
if(tag){tag.setAttribute('x',vx+vw*.87);tag.setAttribute('y',vy+vh*.08);tag.setAttribute('font-size',vw*.04)}
blurs[0].setAttribute('stdDeviation',(7.5*Math.pow(fl/75,2)*2.8/n).toFixed(2));blurs[1].setAttribute('stdDeviation',Math.min(60,900*s).toFixed(1)+' 0');
noise.setAttribute('opacity',Math.max(0,Math.min(.55,Math.log2(iso/100)*.085)).toFixed(2));
const ev=Math.log2(Math.pow(2.8/n,2)*(s*125)*(iso/400));const e=Math.max(-4,Math.min(4,ev));
light.setAttribute('fill',e>=0?'#fff':'#000');light.setAttribute('opacity',(e>=0?Math.min(.92,1-Math.pow(.5,e)):Math.min(.93,1-Math.pow(.5,-e))).toFixed(2));
document.getElementById('mi').style.left=(50+e*12)+'%';document.getElementById('ev').textContent=(ev>0?'+':'')+ev.toFixed(1)+' EV'}
const rf=document.getElementById('r-f'),rs=document.getElementById('r-s'),ri=document.getElementById('r-i'),rl=document.getElementById('r-l');[rf,rs,ri,rl].forEach(r=>r.addEventListener('input',upd));upd()}
// ГРІП
const df=document.getElementById('dof');
if(df){df.innerHTML='<b>📐 Калькулятор глибини різкості (повний кадр, CoC 0,03 мм)</b><div class="row" style="margin-top:10px">'+
'<div><label>Фокусна <output id="d-lo"></output></label><input type="range" id="d-l" min="28" max="75" value="75"></div>'+
'<div><label>Діафрагма</label><select id="d-f">'+[2.8,3.5,4,5.6,8,11,16,22].map(v=>'<option>'+v+'</option>').join('')+'</select></div>'+
'<div><label>Дистанція <output id="d-so"></output></label><input type="range" id="d-s" min="0.38" max="20" step="0.01" value="2"></div></div><div class="res" id="d-r"></div>';
function d(){const f=+document.getElementById('d-l').value,N=+document.getElementById('d-f').value,s=+document.getElementById('d-s').value*1000,c=.03;
document.getElementById('d-lo').textContent=f+' мм';document.getElementById('d-so').textContent=(s/1000).toFixed(2)+' м';
const H=f*f/(N*c)+f,near=s*(H-f)/(H+s-2*f),far=s<H?s*(H-f)/(H-s):Infinity;const m=x=>x===Infinity?'∞':(x/1000).toFixed(2)+' м';
document.getElementById('d-r').innerHTML='Різко від <b>'+m(near)+'</b> до <b>'+m(far)+'</b> · глибина: <b>'+(far===Infinity?'до нескінченності':((far-near)/10).toFixed(1)+' см')+'</b> · гіперфокальна: '+m(H)+(f<=28&&s<180?'<br>⚠️ ближче за MOD на 28 мм (0,18 м)':'')+(f>=75&&s<380?'<br>⚠️ ближче за MOD на 75 мм (0,38 м)':'')}
df.querySelectorAll('input,select').forEach(x=>x.addEventListener('input',d));d()}
// 180
const c1=document.getElementById('calc180');
if(c1){c1.innerHTML='<b>🎬 Правило 180°</b><div class="row" style="margin-top:10px"><div><label>Частота кадрів</label><select id="c-f"><option>24</option><option selected>25</option><option>30</option><option>50</option><option>60</option><option>100</option><option>120</option></select></div><div style="grid-column:span 2"><label>Рекомендована витримка</label><div id="c-r" style="font-size:22px;font-weight:800"></div></div></div>';
const sel=document.getElementById('c-f');function c(){const f=+sel.value;document.getElementById('c-r').textContent='1/'+(2*f)+' с'+(f%25===0?' · PAL':' · NTSC')}sel.onchange=c;c()}
})();
"""


def vcam_svg():
    s = svg.scene(f=2.8, ss=1 / 125, iso=200, focal=50, ev=0.01, w=640)
    s = s.replace('<figure class="scene">', '').replace('</figure>', '')
    return s


def shell(title, body, nav=True, extra_js=""):
    navhtml = ""
    if nav:
        items = "".join(f'<a href="#{i}"><b>{n}</b>{t}</a>' for i, n, t in TOC)
        navhtml = f'''<nav class="side"><div class="brand">📷 Фотокурс</div><div class="sub">Sony A7 IV · Tamron 28–75 G2</div>
<div class="prog"><i></i></div><div class="sub" id="progt"></div><a href="#top"><b>★</b>Початок</a>{items}
<div class="dl"><a href="sony-a7iv-course.pdf" download><b>⬇</b>PDF курсу (iPad / друк)</a><a href="cheatsheets.pdf" download><b>⬇</b>PDF шпаргалок</a><a href="cheatsheets.html"><b>↗</b>Шпаргалки онлайн</a><a href="../"><b>←</b>Усі курси</a></div></nav><button class="menu-btn">☰ Зміст</button>'''
    return f'''<!DOCTYPE html><html lang="uk"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title><link rel="icon" type="image/svg+xml" href="../favicon.svg">
<link href="https://fonts.googleapis.com/css2?family=Golos+Text:wght@400;500;600;700&family=Unbounded:wght@800&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body><div class="layout">{navhtml}<main id="top">{body}</main></div>
<script>const VCAM_SVG={vcam_svg()!r};</script><script>{JS}{extra_js}</script></body></html>'''


COVER = f'''<header class="cover"><div class="lens"></div><div class="tag">Навчальний курс · українською</div>
<h1>Sony A7 IV<br>і Tamron 28–75 G2<br>від нуля до впевненості</h1>
<p style="max-width:620px;font-size:18px;color:#DCD6EA">Курс для тих, хто вперше взяв до рук професійну бездзеркальну камеру. 15 модулів, 27 готових сценаріїв зйомки, програма на 14 днів, шпаргалки і словник. Усе перевірено за офіційною документацією Sony і Tamron.</p>
<div class="kit"><span>📷 Sony α7 IV (ILCE-7M4) · 33 Мп · Full Frame</span><span>🔭 Tamron 28-75mm F/2.8 Di III VXD G2 (A063) · Sony E</span><span>💾 Kingston Canvas React Plus V60 · 256 GB</span></div>
<p style="font-size:13px;color:#A9A5B8;margin-top:22px">Перевірено станом на 27.11.2026: прошивка камери 6.02, прошивка об'єктива — версія 4, TAMRON Lens Utility 5.0.</p></header>'''

INTRO = f'''<section class="module intro" id="intro"><header class="mh"><div class="mnum">Перед стартом</div><h2>Як користуватися курсом</h2></header>
<p><b>Порядок.</b> Модулі 1–2 — знайомство з технікою. 3–5 — основи фотографії та фокусу. 6–7 — меню і перше налаштування (виконайте 7-й модуль, щойно відкриєте коробку). 8–10 — практичні рецепти, фокусні відстані й композиція. 11–12 — відео й обробка. 13 — програма на 14 днів, 14 — довідник проблем, 15 — шпаргалки. Наприкінці — додатки «Види об'єктивів» і «Словник термінів».</p>
<p><b>Звідки інформація.</b> Технічну частину взято з <a href="https://helpguide.sony.net/ilc/2110/v1/en/index.html" target="_blank" rel="noopener">офіційного Sony Help Guide для ILCE-7M4</a>, <a href="https://www.sony.com/electronics/support/e-mount-body-ilce-7-series/ilce-7m4" target="_blank" rel="noopener">сторінки підтримки Sony</a>, <a href="https://www.tamron.com/global/consumer/lenses/a063/" target="_blank" rel="noopener">сторінки Tamron A063</a>, інструкції A063, <a href="https://www.tamron.com/global/consumer/soft/lensutility.html" target="_blank" rel="noopener">TAMRON Lens Utility</a> та <a href="https://www.tamron.com/global/consumer/support/download/firmware/a063/sony_e/" target="_blank" rel="noopener">сторінки прошивок A063</a>. Кожен технічний розділ закінчується прямими посиланнями.</p>
<div class="legend">{box("off", "<p>Перевірені факти з документації: назви, шляхи меню, характеристики, заводські значення.</p>")}{box("pro", "<p>Наші рекомендації. Виробник їх не дає, вони спираються на практику.</p>")}{box("nv", "<p>Чого немає в документації. Ми чесно позначаємо, що перевірити.</p>")}</div>
<p><b>Ілюстрації.</b> Схеми камери й об'єктива намальовано спеціально для курсу. Вони не є фотографіями й не передають масштаб, але їхня нумерація збігається з офіційною. Під кожною схемою є посилання на оригінальну ілюстрацію Sony чи Tamron. Сцени-порівняння (діафрагма, витримка, ISO тощо) — <b>демонстраційні моделі</b>, а не знімки з нашого обладнання. На них стоїть позначка «ДЕМО».</p>
<p><b>Назви меню</b> подано англійською, як вони виглядають на камері, з українським перекладом поруч.</p>
<label class="done"><input type="checkbox" data-done="intro"> Прочитано</label></section>'''

TOC_PRINT = '<section class="toc-print"><h2>Зміст</h2><ol style="font-size:13pt;line-height:2">' + "".join(f"<li>{('Модуль ' + n + '. ') if n.isdigit() else ('Додаток ' + n + '. ')}{t}</li>" for i, n, t in TOC) + '</ol></section>'

body = COVER + TOC_PRINT + INTRO + "".join([M1, M2, M3, M4, M5, M6, M7, M8, M9, M10, M11, M12, M13, M14, M15, APXA, APXB]) + \
    '<p class="small" style="margin-top:40px">© Навчальний посібник для власного користування. Sony, α, Tamron, Kingston, Adobe Lightroom — торговельні марки відповідних власників. Курс не є офіційною документацією виробників.</p>'
open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(shell("Фотокурс: Sony A7 IV + Tamron 28–75 G2", body))

cs_cover = '''<header class="cover" style="padding:34px"><div class="tag">Шпаргалки фотографа</div><h1 style="font-size:38px">Sony A7 IV · Tamron 28–75 G2</h1><p style="color:#DCD6EA">14 сторінок для друку або телефону. Повний курс: <a style="color:#FFB287" href="index.html">index.html</a></p></header>'''
open(os.path.join(OUT, "cheatsheets.html"), "w", encoding="utf-8").write(
    shell("Шпаргалки: Sony A7 IV + Tamron 28–75 G2", cs_cover + '<div class="sheets">' + "".join(SHEETS) + '</div>', nav=False))
print("HTML:", os.path.join(OUT, "index.html"), os.path.getsize(os.path.join(OUT, "index.html")) // 1024, "KB")

if "--pdf" in sys.argv:
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        b = p.chromium.launch(executable_path="/usr/bin/google-chrome") if os.path.exists("/usr/bin/google-chrome") else p.chromium.launch()
        pg = b.new_page()
        pg.route(re.compile(r"https?://fonts\.(googleapis|gstatic)\.com/.*"), lambda r: r.abort())
        foot = '<div style="font-size:8px;color:#888;width:100%;text-align:center;font-family:Inter,sans-serif">Фотокурс · Sony A7 IV + Tamron 28–75 G2 · <span class="pageNumber"></span> / <span class="totalPages"></span></div>'
        for src, dst in (("index.html", "sony-a7iv-course.pdf"), ("cheatsheets.html", "cheatsheets.pdf")):
            pg.goto("file://" + os.path.join(OUT, src), wait_until="load")
            pg.emulate_media(media="print")
            pg.pdf(path=os.path.join(OUT, dst), format="A4", print_background=True, display_header_footer=True,
                   header_template="<div></div>", footer_template=foot, margin={"top": "14mm", "bottom": "16mm", "left": "12mm", "right": "12mm"})
            print("PDF:", dst, os.path.getsize(os.path.join(OUT, dst)) // 1024, "KB")
        b.close()
