# -*- coding: utf-8 -*-
"""Genera las plantillas HTML del kit de marca de Coach Ro."""
import os, pathlib

OUT = pathlib.Path(__file__).parent / "pages"
OUT.mkdir(exist_ok=True)
# Ruta relativa desde pages/*.html hacia la carpeta fonts/ (portable en cualquier equipo)
FONTS = "../fonts"

CSS = (pathlib.Path(__file__).parent / "brand.css").read_text().replace("FONTS", FONTS)

def sparkle(x, y, size, color="#FFFFFF", op=1.0, rot=0):
    return (f'<svg class="spark" style="left:{x}px;top:{y}px;width:{size}px;height:{size}px;'
            f'opacity:{op};transform:rotate({rot}deg)" viewBox="0 0 24 24" fill="{color}">'
            f'<path d="M12 0c.7 5.5 2.5 8 12 12-9.5 4-11.3 6.5-12 12-.7-5.5-2.5-8-12-12 9.5-4 11.3-6.5 12-12z"/></svg>')

# --- Logotipo Coach Ro (lockup reutilizable) ---
def logo(scale=1.0, color="var(--carbon)", accent="var(--rosa)", tagline=True, context=True):
    s = scale
    tag = (f'<div style="font-family:\'Poppins\';font-weight:600;letter-spacing:{2*s}px;'
           f'font-size:{16*s}px;color:{accent};text-transform:uppercase;margin-top:{6*s}px">'
           f'Entrenamos jugando</div>') if tagline else ""
    ctx = (f'<div style="font-family:\'Poppins\';font-weight:600;letter-spacing:{5*s}px;'
           f'font-size:{13*s}px;color:{color};opacity:.55;text-transform:uppercase;margin-top:{2*s}px">'
           f'Alpha Fitness · Xalapa</div>') if context else ""
    return f'''
    <div style="display:inline-flex;flex-direction:column;align-items:center;line-height:1">
      <div style="font-family:'Poppins';font-weight:700;letter-spacing:{10*s}px;
                  font-size:{22*s}px;color:{color};text-transform:uppercase;
                  margin-bottom:{-2*s}px;margin-left:{10*s}px">Coach</div>
      <div style="position:relative;display:inline-block">
        <span class="display" style="font-size:{120*s}px;color:{accent}">Ro</span>
        {sparkle(118*s, -6*s, 34*s, accent)}
        {sparkle(150*s, 34*s, 18*s, accent, .8)}
      </div>
      {tag}{ctx}
    </div>'''

def page(name, body, extra_css=""):
    html = f'''<!doctype html><html lang="es"><head><meta charset="utf-8">
<style>{CSS}{extra_css}</style></head><body>{body}</body></html>'''
    (OUT / f"{name}.html").write_text(html)
    print("wrote", name)

# ==========================================================================
#  DATOS
# ==========================================================================
WA = "228 127 19 74"
IG = "@alphafitness.kids"
DIR = "Av. Orizaba #79, Altos · Xalapa"

# Colores por disciplina
CLASE = {
    "acond": {"nom":"Acondicionamiento físico","sub":"Circuitos · obstáculos · juegos con propósito",
              "edad":"Niños","c1":"#FF6FAC","c2":"#FF2E86","emoji":"🏃‍♀️"},
    "cali":  {"nom":"Calistenia para niños","sub":"Fuerza · coordinación · retos que encantan",
              "edad":"Niños","c1":"#C6B2FF","c2":"#8E6DFF","emoji":"💪"},
    "aerea": {"nom":"Danza aérea","sub":"Telas · figuras · romper miedos en las alturas",
              "edad":"Niñas y mujeres","c1":"#9FE7DC","c2":"#38C7B4","emoji":"🎀"},
}

# Horario semanal (de cuestionario + video)
SEMANA = [
    ("Lunes",     [("acond","6:00 PM","$1,000/mes")]),
    ("Martes",    [("cali","5:00 PM","$850/mes"), ("aerea","6:00 PM","$850/mes")]),
    ("Miércoles", [("acond","6:00 PM","$1,000/mes")]),
    ("Jueves",    [("cali","5:00 PM","$850/mes"), ("aerea","6:00 PM","$850/mes")]),
    ("Viernes",   [("acond","6:00 PM","$1,000/mes")]),
]

# Iconos SVG (línea, redondeados)
def ic(kind, size=40, color="currentColor", sw=2.4):
    p = {
      "wa":'<path d="M12 2a10 10 0 0 0-8.6 15l-1.3 4.6 4.7-1.2A10 10 0 1 0 12 2z" fill="none" stroke="{c}" stroke-width="{sw}"/><path d="M8.5 7.5c-.4 0-.8.2-1 .6-.3.5-.6 1.3-.2 2.4.5 1.5 1.7 3.2 3.4 4.4 1.9 1.4 3.4 1.6 4.2 1.4.7-.2 1.2-.9 1.3-1.4.1-.4 0-.6-.2-.8l-1.7-.9c-.2-.1-.5-.1-.7.2l-.5.7c-.1.1-.3.2-.5.1a5.6 5.6 0 0 1-2.8-2.6c-.1-.2 0-.4.1-.5l.5-.5c.2-.2.2-.4.1-.6l-.7-1.6c-.1-.3-.4-.4-.6-.4z" fill="{c}"/>',
      "ig":'<rect x="3" y="3" width="18" height="18" rx="5.5" fill="none" stroke="{c}" stroke-width="{sw}"/><circle cx="12" cy="12" r="4" fill="none" stroke="{c}" stroke-width="{sw}"/><circle cx="17.2" cy="6.8" r="1.3" fill="{c}"/>',
      "pin":'<path d="M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7z" fill="none" stroke="{c}" stroke-width="{sw}"/><circle cx="12" cy="9" r="2.6" fill="none" stroke="{c}" stroke-width="{sw}"/>',
      "clock":'<circle cx="12" cy="12" r="9" fill="none" stroke="{c}" stroke-width="{sw}"/><path d="M12 7v5l3.5 2" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linecap="round"/>',
      "star":'<path d="M12 3l2.6 5.6 6.1.7-4.5 4.1 1.2 6-5.4-3-5.4 3 1.2-6L3.3 9.3l6.1-.7z" fill="none" stroke="{c}" stroke-width="{sw}" stroke-linejoin="round"/>',
    }[kind]
    p = p.replace("{c}", color).replace("{sw}", str(sw))
    return f'<svg viewBox="0 0 24 24" width="{size}" height="{size}" style="display:block">{p}</svg>'

def sparks_field(specs):
    return "".join(sparkle(*s) for s in specs)

# ==========================================================================
#  1 · HOJA DE LOGOTIPO (para el manual)
# ==========================================================================
page("logo-lockup", f'''
<div class="story" style="background:var(--grad-nube);display:flex;align-items:center;justify-content:center">
  {sparks_field([(150,300,60,"#FFD9EC",1,10),(880,360,42,"#C6B2FF",.9,-8),(120,1500,50,"#9FE7DC",.8,20),(900,1560,64,"#FFD9EC",.9,0),(540,220,30,"#FF9EC7",.9,15)])}
  <div style="text-align:center">{logo(2.4)}</div>
</div>''')

# ==========================================================================
#  2 · RESUMEN SEMANAL (historia)
# ==========================================================================
rows = ""
for dia, clases in SEMANA:
    chips = ""
    for key, hora, _ in clases:
        c = CLASE[key]
        chips += f'''<div style="display:flex;align-items:center;gap:14px;background:{c['c1']}22;
            border:2px solid {c['c1']};border-radius:22px;padding:12px 22px">
            <span style="font-size:30px">{c['emoji']}</span>
            <div style="text-align:left"><div style="font-family:'Poppins';font-weight:700;font-size:26px;color:var(--carbon)">{c['nom']}</div>
            <div style="font-family:'Poppins';font-weight:600;font-size:22px;color:{c['c2']}">{hora}</div></div></div>'''
    rows += f'''<div style="display:flex;align-items:center;gap:26px;width:100%">
        <div class="display" style="font-size:46px;color:var(--rosa);width:230px;text-align:right">{dia}</div>
        <div style="flex:1;display:flex;flex-direction:column;gap:12px">{chips}</div></div>'''

page("historia-semanal", f'''
<div class="story" style="background:var(--grad-nube);padding:96px 70px;display:flex;flex-direction:column">
  {sparks_field([(70,120,44,"#FFD9EC"),(960,180,34,"#C6B2FF",.9),(950,1720,50,"#9FE7DC",.8),(80,1740,40,"#FFD9EC",.9)])}
  <div style="text-align:center;margin-bottom:20px">
    <div class="eyebrow" style="font-size:24px;color:var(--rosa)">Agenda tu semana</div>
    <div class="display" style="font-size:96px;color:var(--carbon);margin-top:8px">Horario<br><span style="color:var(--rosa)">de clases</span></div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:34px">{rows}</div>
  <div style="text-align:center;margin-top:20px">
    <div style="display:inline-flex;align-items:center;gap:16px;background:var(--grad-rosa);color:#fff;
         padding:24px 46px;border-radius:60px;box-shadow:var(--sombra-suave)">
      {ic("wa",44,"#fff")}<span style="font-family:'Poppins';font-weight:700;font-size:38px">{WA}</span></div>
    <div style="font-family:'Poppins';font-weight:600;font-size:26px;color:var(--carbon);opacity:.7;margin-top:18px">{IG} · {DIR}</div>
  </div>
</div>''')

# ==========================================================================
#  3 · PLANTILLA DIARIA (una por día que trabaja)
# ==========================================================================
def dia_story(dia, clases):
    # gradiente principal segun primera clase
    main = CLASE[clases[0][0]]
    cards = ""
    for key, hora, precio in clases:
        c = CLASE[key]
        cards += f'''
        <div style="background:#fff;border-radius:34px;padding:38px 42px;box-shadow:var(--sombra-card);
             display:flex;align-items:center;gap:28px;border:3px solid {c['c1']}55">
          <div style="width:110px;height:110px;border-radius:26px;background:{c['c1']}22;
               display:flex;align-items:center;justify-content:center;font-size:56px;flex:0 0 auto">{c['emoji']}</div>
          <div style="flex:1;text-align:left">
            <div style="font-family:'Poppins';font-weight:700;font-size:40px;color:var(--carbon);line-height:1.1">{c['nom']}</div>
            <div style="font-family:'Poppins';font-weight:500;font-size:24px;color:var(--carbon);opacity:.6;margin:4px 0 10px">{c['sub']}</div>
            <div style="display:flex;gap:14px;flex-wrap:wrap">
              <span style="display:inline-flex;align-items:center;gap:8px;background:{c['c1']}22;color:{c['c2']};
                    font-family:'Poppins';font-weight:700;font-size:26px;padding:8px 20px;border-radius:16px">{ic("clock",26,c['c2'])} {hora}</span>
              <span style="display:inline-flex;align-items:center;background:{c['c1']}22;color:{c['c2']};
                    font-family:'Poppins';font-weight:700;font-size:26px;padding:8px 20px;border-radius:16px">{precio}</span>
            </div>
          </div>
        </div>'''
    body = f'''
    <div class="story" style="background:var(--grad-nube);display:flex;flex-direction:column">
      <!-- Cabecera con gradiente de disciplina -->
      <div style="background:linear-gradient(160deg,{main['c1']} 0%,{main['c2']} 100%);
           padding:90px 70px 70px;border-radius:0 0 60px 60px;position:relative;overflow:hidden">
        {sparks_field([(60,70,44,"#ffffff",.5),(940,110,30,"#ffffff",.5),(880,300,40,"#ffffff",.35)])}
        <div style="display:flex;justify-content:space-between;align-items:flex-start">
          <div>
            <div class="eyebrow" style="font-size:26px;color:#fff;opacity:.9">Hoy hay clase</div>
            <div class="display" style="font-size:150px;color:#fff;margin-top:6px">{dia}</div>
          </div>
          <div style="text-align:center;color:#fff">{logo(0.7,"#fff","#fff",tagline=False,context=False)}</div>
        </div>
      </div>
      <!-- Tarjetas -->
      <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:30px;padding:40px 70px">
        <div style="text-align:center;position:relative">
          <span style="display:inline-block;font-family:'Baloo 2';font-weight:800;font-size:52px;color:var(--carbon)">
            ¡Te esperamos hoy! <span style="color:{main['c2']}">Entrenamos jugando</span></span>
          {sparkle(-10,-6,30,main['c1'])}
        </div>
        {cards}
        <!-- Cupos -->
        <div style="display:flex;align-items:center;justify-content:center;gap:18px;margin-top:6px">
          <span style="font-family:'Poppins';font-weight:600;font-size:30px;color:var(--carbon);opacity:.7">Lugares disponibles:</span>
          <span class="round" style="font-weight:800;font-size:56px;color:var(--rosa);background:#fff;
                border:4px solid var(--rosa);border-radius:24px;padding:2px 34px;box-shadow:var(--sombra-suave)">3</span>
        </div>
      </div>
      <!-- Pie contacto -->
      <div style="background:var(--grad-rosa);padding:44px 70px;display:flex;align-items:center;justify-content:center;gap:22px">
        {ic("wa",50,"#fff")}
        <div style="text-align:left;color:#fff">
          <div style="font-family:'Poppins';font-weight:700;font-size:44px;line-height:1">{WA}</div>
          <div style="font-family:'Poppins';font-weight:500;font-size:24px;opacity:.9;margin-top:4px">Aparta tu lugar · {IG}</div>
        </div>
      </div>
    </div>'''
    page(f"historia-{dia.lower().replace('é','e').replace('á','a')}", body)

for dia, clases in SEMANA:
    dia_story(dia, clases)

# ==========================================================================
#  4 · OVERLAYS DE CONTACTO (PNG transparente para historias)
# ==========================================================================
# 4a · Barra inferior (lower-third) — se coloca sobre foto/video
page("overlay-contacto", f'''
<div class="story" style="background:transparent">
  <!-- Sello superior con logo -->
  <div style="position:absolute;top:70px;left:50%;transform:translateX(-50%);
       background:rgba(255,255,255,.92);border-radius:40px;padding:22px 44px;
       box-shadow:var(--sombra-suave);backdrop-filter:blur(6px);text-align:center">
    {logo(0.62,"var(--carbon)","var(--rosa)",tagline=False,context=False)}
  </div>
  <!-- Barra inferior de contacto -->
  <div style="position:absolute;left:40px;right:40px;bottom:150px;
       background:linear-gradient(160deg,rgba(255,111,172,.96),rgba(255,46,134,.96));
       border-radius:44px;padding:48px 56px;box-shadow:0 24px 60px rgba(255,46,134,.4);
       backdrop-filter:blur(4px);color:#fff">
    <div style="display:flex;align-items:center;gap:22px;margin-bottom:26px">
      <div style="width:76px;height:76px;border-radius:22px;background:rgba(255,255,255,.2);
           display:flex;align-items:center;justify-content:center">{ic("wa",46,"#fff")}</div>
      <div><div style="font-family:'Poppins';font-weight:500;font-size:24px;opacity:.85">WhatsApp · aparta tu lugar</div>
      <div style="font-family:'Poppins';font-weight:700;font-size:52px;line-height:1">{WA}</div></div>
    </div>
    <div style="height:2px;background:rgba(255,255,255,.25);margin:22px 0"></div>
    <div style="display:flex;gap:40px">
      <div style="display:flex;align-items:center;gap:14px">{ic("ig",38,"#fff")}
        <span style="font-family:'Poppins';font-weight:600;font-size:30px">{IG}</span></div>
      <div style="display:flex;align-items:center;gap:14px">{ic("pin",38,"#fff")}
        <span style="font-family:'Poppins';font-weight:500;font-size:26px">{DIR}</span></div>
    </div>
  </div>
</div>''')

# 4b · Sticker de esquina (compacto) — transparente
page("overlay-esquina", f'''
<div class="story" style="background:transparent">
  <div style="position:absolute;left:44px;bottom:180px;
       background:rgba(255,255,255,.94);border-radius:36px;padding:34px 40px;
       box-shadow:var(--sombra-card);display:inline-flex;align-items:center;gap:26px">
    <div style="text-align:center">{logo(0.55,"var(--carbon)","var(--rosa)",tagline=False,context=False)}</div>
    <div style="width:2px;height:120px;background:var(--rosa-pastel)"></div>
    <div style="display:flex;flex-direction:column;gap:14px">
      <div style="display:flex;align-items:center;gap:14px">{ic("wa",40,"var(--rosa-vivo)")}
        <span style="font-family:'Poppins';font-weight:700;font-size:34px;color:var(--carbon)">{WA}</span></div>
      <div style="display:flex;align-items:center;gap:14px">{ic("ig",36,"var(--rosa-vivo)")}
        <span style="font-family:'Poppins';font-weight:600;font-size:30px;color:var(--carbon)">{IG}</span></div>
    </div>
  </div>
</div>''')

# ==========================================================================
#  5 · MOCKUPS DE POSTS DE FEED (1080x1350)
# ==========================================================================
POSTCSS = ".post{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:'Poppins',sans-serif;color:var(--carbon)}"

# 5a · Presentación (pilar humano)
page("post-presentacion", f'''
<div class="post" style="background:var(--grad-nube);padding:90px 80px;display:flex;flex-direction:column;justify-content:center">
  {sparks_field([(80,120,44,"#FFD9EC"),(940,160,32,"#C6B2FF",.9),(120,1180,40,"#9FE7DC",.8),(930,1200,50,"#FFD9EC",.9)])}
  <div class="eyebrow" style="font-size:26px;color:var(--rosa)">Mucho gusto, soy</div>
  <div class="display" style="font-size:190px;color:var(--carbon);margin:6px 0 0">Coach<br><span style="color:var(--rosa)">Ro</span></div>
  <div style="font-family:'Poppins';font-weight:600;font-size:40px;color:var(--carbon);opacity:.75;margin-top:24px;line-height:1.35">
    Entrenadora de danza aérea, calistenia y acondicionamiento físico para niños en Xalapa.</div>
  <div style="display:flex;gap:16px;flex-wrap:wrap;margin-top:44px">
    {"".join(f'<span style="background:#fff;border:2px solid var(--rosa-pastel);border-radius:20px;padding:14px 26px;font-family:Poppins;font-weight:700;font-size:28px;color:var(--rosa)">{t}</span>' for t in ["15 años en telas","Cinta roja TKD","Deportista vigente","+10 años pesas"])}
  </div>
  <div style="margin-top:56px;font-family:'Baloo 2';font-weight:800;font-size:44px;color:var(--carbon)">
    "Entrenamos jugando y aquí está <span style="color:var(--rosa)">prohibido decir no puedo</span>."</div>
</div>''', POSTCSS)

# 5b · Objeción/seguridad (pilar educativo)
_seg_items = ["Colchonetas y piso de seguridad bajo cada tela","Instrucciones claras y supervisión en cada movimiento","Progresión a su ritmo — nadie se salta pasos","15 años de experiencia respaldando cada clase"]
_seg = "".join(
  f'<div style="display:flex;align-items:center;gap:24px;background:rgba(255,255,255,.06);'
  f'border-radius:26px;padding:30px 34px">'
  f'<div style="width:60px;height:60px;border-radius:50%;background:var(--rosa);flex:0 0 auto;'
  f'display:flex;align-items:center;justify-content:center">{ic("star",34,"#fff",2.6)}</div>'
  f'<span style="font-family:Poppins;font-weight:600;font-size:34px;color:#fff">{t}</span></div>'
  for t in _seg_items)
page("post-seguridad", f'''
<div class="post" style="background:var(--carbon);padding:0;display:flex;flex-direction:column">
  <div style="padding:90px 80px 0">
    <div class="eyebrow" style="font-size:26px;color:var(--menta)">Para mamás y papás</div>
    <div class="display" style="font-size:110px;color:#fff;margin-top:14px;line-height:1">¿Es<br><span style="color:var(--rosa)">seguro</span> para<br>mi hija?</div>
  </div>
  <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:26px;padding:60px 80px">
    {_seg}
  </div>
  <div style="background:var(--grad-rosa);padding:50px 80px;display:flex;align-items:center;justify-content:space-between">
    <span style="font-family:'Baloo 2';font-weight:800;font-size:40px;color:#fff">Rompe el miedo, no la confianza.</span>
    {logo(0.5,"#fff","#fff",tagline=False,context=False)}
  </div>
</div>''', POSTCSS)

# 5c · Inscripciones abiertas (conversión)
_insc = "".join(
  f'<div style="display:flex;align-items:center;gap:22px;border-bottom:2px dashed var(--rosa-pastel);padding:18px 4px">'
  f'<span style="font-size:40px">{CLASE[k]["emoji"]}</span>'
  f'<span style="flex:1;font-family:Poppins;font-weight:700;font-size:36px;color:var(--carbon)">{CLASE[k]["nom"]}</span>'
  f'<span style="font-family:Poppins;font-weight:700;font-size:32px;color:var(--rosa)">{h}</span></div>'
  for k,h in [("acond","L·M·V 6PM"),("cali","M·J 5PM"),("aerea","M·J 6PM")])
page("post-inscripciones", f'''
<div class="post" style="background:var(--grad-arcoiris);padding:80px;display:flex;align-items:center;justify-content:center">
  <div style="background:#fff;border-radius:50px;width:100%;height:100%;padding:80px 70px;
       display:flex;flex-direction:column;box-shadow:var(--sombra-card);position:relative">
    {sparks_field([(60,60,40,"#FFD9EC"),(860,90,30,"#C6B2FF",.9),(820,1050,44,"#9FE7DC",.8)])}
    <div style="text-align:center">
      <div class="eyebrow" style="font-size:28px;color:var(--rosa)">Cupos limitados</div>
      <div class="display" style="font-size:130px;color:var(--carbon);margin-top:10px;line-height:.95">Inscripciones<br><span style="color:var(--rosa)">abiertas</span></div>
    </div>
    <div style="flex:1;display:flex;flex-direction:column;justify-content:center;gap:18px">
      {_insc}
    </div>
    <div style="background:var(--grad-rosa);border-radius:36px;padding:36px;text-align:center;color:#fff;box-shadow:var(--sombra-suave)">
      <div style="display:inline-flex;align-items:center;gap:18px">{ic("wa",50,"#fff")}
        <span style="font-family:Poppins;font-weight:700;font-size:52px">{WA}</span></div>
      <div style="font-family:Poppins;font-weight:500;font-size:28px;opacity:.9;margin-top:8px">{IG} · {DIR}</div>
    </div>
  </div>
</div>''', POSTCSS)

print("== TODAS LAS PLANTILLAS GENERADAS ==")
