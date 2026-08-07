# Generador de recibos de pago Medusssa.Studio — réplica del formato REC-AUR-003
# Requiere: reportlab + fuentes Poppins (Light, Regular, Medium, Bold) en ./fonts
import os
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import HexColor

# ---------------- Datos del recibo ----------------
DATOS = {
    "folio": "REC-AUR-004",
    "fecha": "7 de agosto de 2026",
    "lugar": "Xalapa, Veracruz",
    "recibi_de": "Salones Aurora",
    "cantidad": "1,000.00",
    "cantidad_letra": "Mil pesos",
    "centavos": "00/100 M.N.",
    "concepto": "Servicios de marketing · Septiembre 2026",
    "metodo": "Transferencia electrónica",
    "archivo": "Recibo_Salones_Aurora_REC-AUR-004_Servicios_Septiembre_2026.pdf",
}
# --------------------------------------------------

W, H = 612.96, 792.96
NAVY = HexColor("#23263A")
BLUE = HexColor("#009CFF")
RED = HexColor("#E5384E")
GRAY = HexColor("#8A8FA3")
BODY = HexColor("#2B2E3F")
LINE = HexColor("#E7E9F0")
CARD = HexColor("#F6F8FC")
FOOT = HexColor("#B9BECF")
WHITE = HexColor("#FFFFFF")

BASE = os.path.dirname(os.path.abspath(__file__))
for w in ("Light", "Regular", "Medium", "Bold"):
    pdfmetrics.registerFont(TTFont(f"Poppins-{w}", os.path.join(BASE, "fonts", f"Poppins-{w}.ttf")))

c = canvas.Canvas(os.path.join(BASE, DATOS["archivo"]), pagesize=(W, H))
c.setTitle(f"Recibo de pago {DATOS['folio']} — {DATOS['recibi_de']}")


def text(x, y, s, font, size, color, cs=0):
    c.setFillColor(color)
    c.setFont(font, size)
    c.drawString(x, y, s, charSpace=cs)
    return pdfmetrics.stringWidth(s, font, size) + cs * max(len(s) - 1, 0)


def tracked(x, y, s, font, size, color, target_w):
    cs = (target_w - pdfmetrics.stringWidth(s, font, size)) / max(len(s) - 1, 1)
    return text(x, y, s, font, size, color, cs)


def tracked_right(right, y, s, font, size, color, target_w):
    tracked(right - target_w, y, s, font, size, color, target_w)


def right(rx, y, s, font, size, color):
    w = pdfmetrics.stringWidth(s, font, size)
    text(rx - w, y, s, font, size, color)
    return w


def diamond(cx, cy, r, color):
    c.setFillColor(color)
    p = c.beginPath()
    p.moveTo(cx - r, cy)
    p.lineTo(cx, cy + r)
    p.lineTo(cx + r, cy)
    p.lineTo(cx, cy - r)
    p.close()
    c.drawPath(p, stroke=0, fill=1)


# Fondo
c.setFillColor(WHITE)
c.rect(0, 0, W, H, stroke=0, fill=1)

# ---- Encabezado ----
c.setFillColor(NAVY)
c.rect(0, H - 89.2, W, 89.2, stroke=0, fill=1)
c.setFillColor(BLUE)
c.rect(0, H - 89.2, 433.0, 3.0, stroke=0, fill=1)
c.setFillColor(RED)
c.rect(433.0, H - 89.2, W - 433.0, 3.0, stroke=0, fill=1)

diamond(40.5, 751.71, 7.4, RED)
x = 54.75
x += text(x, 752.46, "Medusssa", "Poppins-Bold", 15.75, WHITE)
x += text(x, 752.46, ".", "Poppins-Bold", 15.75, BLUE)
text(x, 752.46, "Studio", "Poppins-Bold", 15.75, WHITE)
tracked(54.75, 736.71, "MARKETING DIGITAL", "Poppins-Light", 7.12, WHITE, 95.45)

right(577.5, 757.71, "RECIBO", "Poppins-Bold", 14.25, WHITE)
right(577.5, 741.96, "DE PAGO", "Poppins-Bold", 14.25, WHITE)
tracked_right(577.1, 727.71, "COMPROBANTE", "Poppins-Light", 7.12, FOOT, 63.23)

# ---- Folio / Fecha / Lugar ----
tracked(35.25, 680.46, "FOLIO", "Poppins-Medium", 6.75, BLUE, 23.35)
text(35.25, 663.21, DATOS["folio"], "Poppins-Medium", 9.75, NAVY)
tracked(222.0, 680.46, "FECHA", "Poppins-Medium", 6.75, BLUE, 26.2)
text(222.0, 663.21, DATOS["fecha"], "Poppins-Medium", 9.75, NAVY)
tracked(408.75, 680.46, "LUGAR", "Poppins-Medium", 6.75, BLUE, 26.35)
text(408.75, 663.21, DATOS["lugar"], "Poppins-Medium", 9.75, NAVY)

c.setFillColor(LINE)
c.rect(204.75, H - 134.2, 0.75, 28.5, stroke=0, fill=1)
c.rect(391.5, H - 134.2, 0.75, 28.5, stroke=0, fill=1)
c.rect(0, H - 151.45, W, 0.75, stroke=0, fill=1)

# ---- Recibí de ----
tracked(35.25, 604.71, "RECIBÍ DE", "Poppins-Light", 9.0, GRAY, 42.55)
text(35.25, 576.21, DATOS["recibi_de"], "Poppins-Bold", 20.25, NAVY)
text(35.25, 558.21, "la cantidad que se indica, correspondiente al concepto detallado en este comprobante.",
     "Poppins-Light", 9.75, BODY)

# ---- Tarjeta de cantidad ----
c.setFillColor(BLUE)
c.roundRect(35.25, 444.96, 543.0, 85.5, 8, stroke=0, fill=1)
c.setFillColor(CARD)
c.roundRect(39.0, 444.96, 539.2, 85.5, 8, stroke=0, fill=1)

tracked(61.5, 495.96, "CANTIDAD CON LETRA", "Poppins-Medium", 7.12, GRAY, 99.9)
x = 61.5
x += text(x, 476.46, DATOS["cantidad_letra"], "Poppins-Medium", 10.12, NAVY)
text(x + 2.7, 476.46, DATOS["centavos"], "Poppins-Light", 9.0, GRAY)

mxn_w = pdfmetrics.stringWidth("MXN", "Poppins-Regular", 9.75)
num_w = pdfmetrics.stringWidth(DATOS["cantidad"], "Poppins-Bold", 30.0)
mxn_x = 555.4 - mxn_w
num_x = mxn_x - 4.1 - num_w
text(mxn_x, 477.21, "MXN", "Poppins-Regular", 9.75, GRAY)
text(num_x, 477.21, DATOS["cantidad"], "Poppins-Bold", 30.0, NAVY)
right(num_x - 2.7, 481.71, "$", "Poppins-Medium", 12.0, BLUE)

# ---- Concepto / Método de pago ----
tracked(35.25, 415.71, "CONCEPTO", "Poppins-Medium", 6.75, BLUE, 45.15)
text(35.25, 397.71, DATOS["concepto"], "Poppins-Regular", 9.75, BODY)
tracked(428.25, 415.71, "MÉTODO DE PAGO", "Poppins-Medium", 6.75, BLUE, 74.35)
text(428.25, 397.71, DATOS["metodo"], "Poppins-Regular", 9.75, BODY)

# ---- Firma ----
c.setFillColor(NAVY)
c.rect(383.2, 345.26, 195.0, 0.7, stroke=0, fill=1)
cx = (383.2 + 578.2) / 2
w = pdfmetrics.stringWidth("Medusssa.Studio", "Poppins-Bold", 9.75)
text(cx - w / 2, 328.71, "Medusssa.Studio", "Poppins-Bold", 9.75, NAVY)
w = pdfmetrics.stringWidth("Recibí de conformidad", "Poppins-Light", 7.5)
text(cx - w / 2, 314.46, "Recibí de conformidad", "Poppins-Light", 7.5, GRAY)

# ---- Pie de página ----
c.setFillColor(NAVY)
c.rect(0, 0, W, 34.76, stroke=0, fill=1)
diamond(38.25, 17.46, 4.25, RED)
x = 47.25
x += text(x, 15.21, "Medusssa", "Poppins-Medium", 7.12, WHITE)
x += text(x, 15.21, ".", "Poppins-Medium", 7.12, BLUE)
x += text(x, 15.21, "Studio", "Poppins-Medium", 7.12, WHITE)
text(118.5, 15.21, "·  Xalapa, Veracruz, México", "Poppins-Light", 7.12, FOOT)
right(577.9, 15.21, "Este documento ampara el pago descrito.", "Poppins-Light", 7.12, FOOT)

c.save()
print("Generado:", DATOS["archivo"])
