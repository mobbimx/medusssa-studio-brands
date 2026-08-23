# -*- coding: utf-8 -*-
import sys, calendar
RAW = sys.argv[1] if len(sys.argv) > 1 else "./assets/"

ROSA="#fe42a2"; ROSACL="#ffb7f0"; LILA="#f7daff"; MORADO="#5e17eb"
AMA="#fec900"; BL="#ffffff"; TINTA="#7a1050"; CREMA="#fff7fb"
DISPLAY="'Retro Vintage','Bagel Fat One',cursive"
SCRIPT="'Adam Script','Yellowtail',cursive"
PIXEL="'Retropix','Pixelify Sans',monospace"
SANS="'Poppins','Fredoka',sans-serif"

def img(src,l,t,w,h):
    return '<img src="%s%s" alt="" style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx">' % (RAW,src,l,t,w,h)

def shape(l,t,w,h,bg,r=0,bw=0,bc=BL):
    b = ";border:%dpx solid %s" % (bw,bc) if bw else ""
    return '<div style="position:absolute;left:%dpx;top:%dpx;width:%dpx;height:%dpx;background:%s;border-radius:%dpx%s;box-sizing:border-box"></div>' % (l,t,w,h,bg,r,b)

def text(l,t,w,txt,size,color,font=SANS,weight="400",align="center",lh=1.14,ls="0"):
    return ('<p style="position:absolute;left:%dpx;top:%dpx;width:%dpx;margin:0;font-family:%s;'
            'font-size:%dpx;line-height:%s;font-weight:%s;color:%s;text-align:%s;letter-spacing:%s">%s</p>'
            ) % (l,t,w,font,size,lh,weight,color,align,ls,txt)

def ctext(l,t,w,h,txt,size,color,font=SANS,weight="400",ls="0"):
    "texto centrado verticalmente dentro de una caja de alto h"
    return text(l, int(t + (h - size*1.14)/2), w, txt, size, color, font, weight, "center", 1.14, ls)

def logo(l,t,w):
    return img("logo-wordmark.png", l, t, w, int(w*382/752))

def page(label, bgcolor, body):
    return ('<div data-document-role="page" data-label="%s" style="position:relative;width:1080px;height:1920px;'
            'background:%s;overflow:hidden">\n%s\n</div>' % (label, bgcolor, body))

PAGES = []

# ─────────────────────────────────────────── S1 · CALENDARIO DEL MES
b  = img("bg-checker.png",0,0,1080,1920)
b += img("deco-spark.png",900,246,130,141)
b += shape(268,300,544,88,BL,44,8,MORADO) + ctext(268,300,544,88,"DISPONIBILIDAD DEL MES",36,MORADO,PIXEL,"700",".08em")
b += text(0,408,1080,"SEPTIEMBRE",118,ROSA,DISPLAY,"400","center",1.0,"-.01em")
b += text(0,556,1080,"2026",34,MORADO,PIXEL,"700","center",1.0,".3em")
CW,CH,GAP,L0 = 122,112,9,86
for i,d in enumerate(["L","M","M","J","V","S","D"]):
    b += ctext(L0+i*(CW+GAP),638,CW,46,d,34,MORADO,PIXEL,"700")
calendar.setfirstweekday(0)
LLENO={3,4,5,10,11,12,18,19,25,26}
for r,week in enumerate(calendar.monthcalendar(2026,9)):
    top = 700 + r*(CH+GAP)
    for c,d in enumerate(week):
        if d==0: continue
        l = L0 + c*(CW+GAP)
        if c==6:      b += shape(l,top,CW,CH,LILA,26,6,ROSACL);  b += ctext(l,top,CW,CH,str(d),40,"#b98fc4",SANS,"700")
        elif d in LLENO: b += shape(l,top,CW,CH,ROSA,26,6,BL);   b += ctext(l,top,CW,CH,str(d),40,BL,SANS,"700")
        else:         b += shape(l,top,CW,CH,BL,26,6,ROSACL);    b += ctext(l,top,CW,CH,str(d),40,MORADO,SANS,"700")
for i,(lab,bg,bc) in enumerate([("Libre",BL,ROSACL),("Lleno",ROSA,BL),("Cerrado",LILA,ROSACL)]):
    x = 268 + i*192
    b += shape(x,1352,34,34,bg,11,5,bc) + text(x+46,1345,150,lab,34,TINTA,SANS,"600","left")
b += logo(258,1440,300) + text(578,1492,340,"228-848-5375",42,ROSA,SANS,"700","left")
PAGES.append(page("S1 · Calendario del mes", LILA, b))

# ─────────────────────────────────────────── S2 · CITAS DISPONIBLES
b  = img("deco-smiley.png",62,250,132,132)
b += shape(288,300,504,84,AMA,42,7,BL) + ctext(288,300,504,84,"HOY · MIÉRCOLES 26",34,MORADO,PIXEL,"700",".07em")
b += text(0,408,1080,"HORARIOS",112,BL,DISPLAY,"400","center",1.0)
b += text(0,520,1080,"LIBRES",112,BL,DISPLAY,"400","center",1.0)
HORAS=[("10:00 am","LIBRE",1),("11:30 am","APARTADA",0),("1:00 pm","LIBRE",1),
       ("2:30 pm","LIBRE",1),("4:00 pm","APARTADA",0),("5:30 pm","ÚLTIMA",2)]
for i,(h,e,s) in enumerate(HORAS):
    top = 668 + i*110
    bg  = BL if s==1 else ("#ff7ec4" if s==0 else AMA)
    ct  = MORADO if s!=0 else BL
    ce  = ROSA if s==1 else (BL if s==0 else MORADO)
    b += shape(84,top,912,96,bg,48,7,BL)
    b += text(128,top+22,400,h,46,ct,SANS,"700","left")
    b += text(552,top+28,400,e,34,ce,PIXEL,"700","right",1.14,".06em")
b += shape(240,1352,600,110,AMA,55,8,BL) + ctext(240,1352,600,110,"Aparta el tuyo por WhatsApp",40,MORADO,SANS,"700")
b += logo(268,1494,260) + text(556,1540,360,"228-848-5375",42,BL,SANS,"700","left")
PAGES.append(page("S2 · Citas disponibles", ROSA, b))

# ─────────────────────────────────────────── S3 · LISTA DE PRECIOS
b  = img("bg-checker-wave.png",0,0,1080,1920)
b += img("deco-daisy.png",884,248,132,132)
b += logo(330,296,420)
b += shape(300,528,480,80,BL,40,7,MORADO) + ctext(300,528,480,80,"LISTA DE PRECIOS",34,MORADO,PIXEL,"700",".07em")
SERV=[("Manicura Rusa","$50"),("Manicura Spa","$70"),("Polish","$80"),("Kapping / Rubber","$100"),
      ("Soft Gel","$150"),("Poly Gel","$170"),("Retoque","$90"),("Retiro","$60")]
for i,(s,p) in enumerate(SERV):
    top = 656 + i*84
    b += text(84,top,560,s,58,ROSA,SCRIPT,"400","left",1.0)
    b += shape(84,top+76,832,6,ROSACL,3)
    b += text(756,top,240,p,58,MORADO,SCRIPT,"400","right",1.0)
b += text(84,1352,912,"Servicio base a 1 color. El diseño se cotiza aparte.",30,TINTA,SANS,"500","center")
b += shape(196,1412,320,76,BL,38,6,ROSA) + ctext(196,1412,320,76,"Cotiza tu diseño",34,ROSA,SANS,"700")
b += shape(564,1412,320,76,BL,38,6,MORADO) + ctext(564,1412,320,76,"Agenda tu cita",34,MORADO,SANS,"700")
b += text(0,1520,1080,"WhatsApp 228-848-5375",44,ROSA,SANS,"700","center")
PAGES.append(page("S3 · Lista de precios", LILA, b))

# ─────────────────────────────────────────── S4 · INFORMACIÓN DEL STUDIO
b  = img("bg-checker.png",0,0,1080,1920)
b += img("deco-heart.png",64,252,124,106)
b += logo(340,290,400)
b += shape(268,506,544,78,BL,39,7,MORADO) + ctext(268,506,544,78,"TODO LO QUE NECESITAS SABER",30,MORADO,PIXEL,"700",".06em")
b += shape(84,626,912,720,BL,60,10,ROSA)
BLOQ=[("HORARIO","Lunes a sábado · 10:00 am – 7:00 pm<br>Domingo cerrado"),
      ("DÓNDE ESTAMOS","Av. Américas casi esquina Miguel Alemán<br>Xalapa, Veracruz"),
      ("FORMAS DE PAGO","Efectivo · Transferencia · Tarjeta"),
      ("PARA APARTAR","Anticipo $50 · Tolerancia 15 min<br>Cancelaciones con 24 h de aviso")]
y = 676
for lab,val in BLOQ:
    b += text(136,y,820,lab,32,ROSA,PIXEL,"700","left",1.0,".07em")
    b += text(136,y+46,820,val,38,TINTA,SANS,"500","left",1.26)
    y += 176 if "<br>" in val else 140
b += shape(200,1390,680,108,ROSA,54,8,BL) + ctext(200,1390,680,108,"Agenda por WhatsApp",44,BL,SANS,"700")
b += text(0,1534,1080,"228-848-5375 · @peachystudio.nails",32,TINTA,SANS,"500","center")
PAGES.append(page("S4 · Información del studio", LILA, b))

# ─────────────────────────────────────────── S5 · DISEÑO DEL DÍA
b  = img("bg-checker.png",0,0,1080,1920)
b += img("deco-smiley.png",890,248,128,128)
b += img("deco-heart.png",56,1180,118,101)
b += shape(340,300,400,80,BL,40,7,MORADO) + ctext(340,300,400,80,"DISEÑO DEL DÍA",34,MORADO,PIXEL,"700",".06em")
b += text(0,404,1080,"Soft Gel",128,ROSA,SCRIPT,"400","center",1.0)
b += shape(140,584,800,800,CREMA,380,12,ROSA)
b += text(140,930,800,"FOTO DEL DISEÑO",44,ROSA,PIXEL,"700","center")
b += text(140,996,800,"reemplaza este marco con la foto",30,TINTA,SANS,"500","center")
b += shape(150,1436,540,88,BL,44,8,ROSA) + ctext(150,1436,540,88,"Almendra · 2 colores",42,ROSA,SANS,"700")
b += shape(722,1436,208,88,ROSA,44,8,BL) + ctext(722,1436,208,88,"$150",42,BL,SANS,"700")
b += logo(300,1552,240) + text(566,1592,360,"228-848-5375",38,ROSA,SANS,"700","left")
PAGES.append(page("S5 · Diseño del día", LILA, b))

# ─────────────────────────────────────────── S6 · AVISO O PROMOCIÓN
b  = img("bg-swirl-rosa.png",0,0,1080,1920)
b += img("deco-daisy.png",876,252,136,136)
b += img("deco-spark.png",58,1216,110,120)
b += shape(268,318,544,80,BL,40,7,MORADO) + ctext(268,318,544,80,"PROMO DE SEPTIEMBRE",34,MORADO,PIXEL,"700",".06em")
b += text(0,432,1080,"Soft Gel",122,ROSA,SCRIPT,"400","center",1.0)
b += text(130,606,280,"$150",86,MORADO,SCRIPT,"400","center",1.0)
b += shape(186,668,168,9,MORADO,5)
b += text(400,580,560,"$120",156,ROSA,DISPLAY,"400","center",1.0)
b += text(84,808,912,"Cualquier diseño a dos colores,<br>sin costo extra.",52,TINTA,SANS,"500","center",1.28)
b += shape(196,960,340,76,BL,38,6,MORADO) + ctext(196,960,340,76,"Válido hasta el 30",34,MORADO,SANS,"700")
b += shape(568,960,316,76,BL,38,6,ROSA) + ctext(568,960,316,76,"Cupo limitado",34,ROSA,SANS,"700")
b += shape(240,1110,600,110,ROSA,55,8,BL) + ctext(240,1110,600,110,"Lo quiero",46,BL,SANS,"700")
b += logo(300,1300,240) + text(566,1340,360,"228-848-5375",38,ROSA,SANS,"700","left")
PAGES.append(page("S6 · Aviso o promoción", ROSACL, b))

HTML = """<!doctype html>
<html lang="es"><head><meta charset="utf-8">
<title>Peachy Studio — Plantillas de historia</title>
<style>*{margin:0;padding:0;box-sizing:border-box}body{background:#e9e0ec}
[data-document-role="page"]{margin:0 auto 40px}</style></head>
<body>
%s
</body></html>""" % "\n".join(PAGES)
open("/home/user/medusssa-studio-brands/peachystudio/canva/plantillas-peachy-canva.html","w").write(HTML)
print("HTML de importación generado ·", len(PAGES), "páginas")
