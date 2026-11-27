#!/usr/bin/env python3
"""Genera el PDF de producción de videos de Navidad 2026 de Mobbitrips.

Para agregar un video: añadir un diccionario a VIDEOS (con estado "listo") y volver a correr
    python3 generar_guiones_pdf.py
El PDF se escribe junto a este archivo: guiones-navidad-2026.pdf
"""
from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (BaseDocTemplate, Frame, KeepTogether, PageBreak,
                                PageTemplate, Paragraph, Spacer, Table, TableStyle)

CORAL = colors.HexColor("#ED6864")
CORAL_SUAVE = colors.HexColor("#FCE9E8")
GRIS = colors.HexColor("#706F6F")
CREMA = colors.HexColor("#FAF8F5")
TINTA = colors.HexColor("#3D3D3D")
VERDE = colors.HexColor("#3E9B6B")
AMBAR = colors.HexColor("#D9922E")

ACTUALIZADO = "27 de noviembre de 2026"
SALIDA = Path(__file__).with_name("guiones-navidad-2026.pdf")

# ---------------------------------------------------------------- estilos
base = dict(fontName="Helvetica", textColor=TINTA, leading=14, fontSize=10)
S = {
    "h1": ParagraphStyle("h1", **{**base, "fontName": "Helvetica-Bold", "fontSize": 24, "leading": 28, "textColor": CORAL}),
    "h2": ParagraphStyle("h2", **{**base, "fontName": "Helvetica-Bold", "fontSize": 15, "leading": 19, "textColor": CORAL, "spaceBefore": 4, "spaceAfter": 6}),
    "h3": ParagraphStyle("h3", **{**base, "fontName": "Helvetica-Bold", "fontSize": 11, "leading": 14, "textColor": GRIS, "spaceBefore": 8, "spaceAfter": 3}),
    "p": ParagraphStyle("p", **base),
    "small": ParagraphStyle("small", **{**base, "fontSize": 8.5, "leading": 11, "textColor": GRIS}),
    "cell": ParagraphStyle("cell", **{**base, "fontSize": 9, "leading": 11.5}),
    "cellb": ParagraphStyle("cellb", **{**base, "fontSize": 9, "leading": 11.5, "fontName": "Helvetica-Bold"}),
    "head": ParagraphStyle("head", **{**base, "fontSize": 9, "leading": 11, "fontName": "Helvetica-Bold", "textColor": colors.white}),
    "voz": ParagraphStyle("voz", **{**base, "fontName": "Helvetica-Bold", "fontSize": 17, "leading": 22, "textColor": TINTA}),
    "bullet": ParagraphStyle("bullet", **{**base, "leftIndent": 14, "bulletIndent": 2, "spaceAfter": 2}),
}


def P(txt, st="p"):
    return Paragraph(txt, S[st])


def bullets(items):
    return [Paragraph(t, S["bullet"], bulletText="-") for t in items]


def tabla(filas, anchos, cabecera=True, zebra=True):
    data = []
    for i, fila in enumerate(filas):
        est = "head" if (cabecera and i == 0) else "cell"
        data.append([c if not isinstance(c, str) else Paragraph(c, S[est]) for c in fila])
    t = Table(data, colWidths=anchos, repeatRows=1 if cabecera else 0)
    estilo = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5), ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, colors.HexColor("#E3DED8")),
    ]
    if cabecera:
        estilo.append(("BACKGROUND", (0, 0), (-1, 0), CORAL))
    if zebra:
        for r in range(1 if cabecera else 0, len(data)):
            if r % 2 == 0:
                estilo.append(("BACKGROUND", (0, r), (-1, r), CREMA))
    t.setStyle(TableStyle(estilo))
    return t


def pie_y_cabecera(canvas, doc):
    canvas.saveState()
    w, h = letter
    canvas.setFillColor(CORAL)
    canvas.rect(0, h - 0.32 * inch, w, 0.32 * inch, stroke=0, fill=1)
    canvas.setFillColor(colors.white)
    canvas.setFont("Helvetica-Bold", 9)
    canvas.drawString(0.6 * inch, h - 0.21 * inch, "MOBBITRIPS  |  Guiones de video - Navidad 2026")
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(GRIS)
    canvas.drawString(0.6 * inch, 0.4 * inch, f"Actualizado: {ACTUALIZADO}  |  Documento de trabajo, se va completando video por video")
    canvas.drawRightString(w - 0.6 * inch, 0.4 * inch, f"Página {doc.page}")
    canvas.restoreState()


# ---------------------------------------------------------------- datos
PROMO = [
    ["Alojamiento", "Precio normal por noche", "Con 30% de descuento"],
    ["Colina Estacionamiento", "<strike>$632</strike>", "<b>$443</b>"],
    ["N20 H1, H2 y H3", "<strike>$631</strike>", "<b>$442</b>"],
    ["Colina 2, 4, 7 y 9", "<strike>$770</strike>", "<b>$539</b>"],
    ["Colina 5", "<strike>$908</strike>", "<b>$636</b>"],
    ["Colina 14", "<strike>$1,057</strike>", "<b>$740</b>"],
]

VIDEOS = [
    {
        "num": 1,
        "titulo": "Hoy empieza el 30%",
        "estado": "SELECCIONADO - listo para grabar",
        "estado_color": VERDE,
        "publicar": "1 de diciembre de 2026",
        "duracion": "20 segundos",
        "formato": "Vertical 9:16 (1080 x 1920), con subtítulos",
        "objetivo": "Anunciar la promoción de Navidad, mostrar precios reales y lograr que escriban por WhatsApp.",
        "gancho": "Opción C: «Hoy empieza el 30% en Mobbitrips.»",
        "interpretacion": [
            "Tono cálido y cercano, como invitar a un amigo a pasar la Navidad en Xalapa. Nada de voz de anuncio de tienda.",
            "Sonríe al hablar: se escucha. Energía alta en el gancho, más tranquilo en los precios, cálido en el cierre.",
            "Ritmo: unas 2 palabras por segundo. Hay una pausa corta entre una frase y la siguiente; es la que cubre el corte de imagen.",
            "Di los precios claro y sin prisa: es lo que la gente va a recordar.",
        ],
        "pronunciacion": [
            "$443 se dice «cuatrocientos cuarenta y tres pesos» (en el video basta «$443»; no hace falta decir «pesos»).",
            "$442: «cuatrocientos cuarenta y dos». $539: «quinientos treinta y nueve».",
            "N20 se dice «ene veinte». Colina 9: «Colina nueve».",
            "El nombre de la marca se dice como siempre se dice en Mobbitrips (confirmar con quien lleva la marca).",
        ],
        "escenas": [
            # n, tiempo, imagen, dice, texto en pantalla, indicación
            ("1", "0-3 s", "Puerta que se abre o entrada del edificio, luz de mañana.",
             "«Hoy empieza el 30% en Mobbitrips.»", "<b>30% DE DESCUENTO</b> (grande, entra con un golpe de zoom)",
             "Energía alta, sonrisa. Mira de frente si va a cámara."),
            ("2", "3-6 s", "Colina Estacionamiento: toma que avanza hacia el interior.",
             "«Desde $443 la noche.»", "Colina Estacionamiento<br/><strike>$632</strike>  <b>$443</b>",
             "Claro y tranquilo. Resalta «$443»."),
            ("3", "6-9 s", "N20: sala y luego recámara, un corte de 1.5 s cada una.",
             "«En N20, $442.»", "N20<br/><strike>$631</strike>  <b>$442</b>",
             "Corto y seguro. Sin acelerar."),
            ("4", "9-12 s", "Colina 9: sala o comedor, movimiento lento.",
             "«En Colina 9, $539.»", "Colina 9<br/><strike>$770</strike>  <b>$539</b>",
             "Igual que la anterior; mismo ritmo."),
            ("5", "12-16 s", "3 o 4 tomas muy cortas de lo más bonito: vista, cama tendida, manta, luz.",
             "«Todo diciembre y enero.»", "<b>TODO DICIEMBRE Y ENERO</b>",
             "Cálido, con sonrisa. Es la frase que suaviza todo."),
            ("6", "16-20 s", "Pantalla final: logo sobre la mejor toma (o fondo coral con el logo).",
             "«Reserva directo por WhatsApp y apartamos tu fecha.»",
             "<b>Reserva directo</b><br/>WhatsApp 228 252 5244<br/>mobbitrips.com",
             "Cierre amable, como una invitación. Baja un poco el tono al terminar."),
        ],
        "tomas": [
            ("1", "Entrada del edificio", "Puerta que se abre (mano que empuja) o fachada con luz de mañana.", "4-5 s", "Avance lento hacia la puerta", "2"),
            ("2", "Colina Estacionamiento", "Interior, toma abierta que avanza.", "5 s", "Avance lento", "2"),
            ("3", "Colina Estacionamiento", "Un detalle (cama, mesa, lámpara).", "4 s", "Casi fija, ligero deslizamiento", "2"),
            ("4", "N20", "Sala (la de H1).", "4 s", "Paneo lento", "2"),
            ("5", "N20", "Recámara (la de H2).", "4 s", "Avance lento", "2"),
            ("6", "Colina 9", "Sala o comedor.", "5 s", "Paneo lento", "2"),
            ("7", "Colina 9", "Un detalle.", "4 s", "Casi fija", "2"),
            ("8", "Ambiente", "Vista por la ventana, cama tendida, manta, lámpara encendida (4 a 6 tomas muy cortas).", "2-3 s c/u", "Fijas o con pequeño movimiento", "1-2 c/u"),
            ("9", "Voz (si es voz en off)", "La letra completa, leída 3 veces con calma. Se elige la mejor.", "-", "En un cuarto sin eco", "3"),
        ],
        "requiere": [
            "Celular o cámara en <b>vertical</b>, 4K a 30 cuadros, con estabilizador o tripié. Lente limpio.",
            "<b>Luz natural de mañana</b>. Cortinas abiertas, luces apagadas salvo lámparas que se vean bonitas.",
            "Los depas <b>ordenados</b>: camas tendidas, sin objetos personales a la vista, cocina limpia.",
            "Solo grabar lo que realmente hay. No inventar ni mostrar cosas de otro depa en el depa del que se habla.",
            "Si el actor sale a cámara: ropa lisa en tonos neutros o coral, sin logos grandes. Nada muy brillante.",
            "Audio: si es voz en off, grabar en un cuarto con ropa o cobijas que quiten el eco; el celular a un palmo de la boca.",
            "Música: instrumental navideña suave, libre de derechos (la elijo en la edición).",
            "<b>Por definir:</b> si el actor habla a cámara o solo es voz en off. La letra es la misma en ambos casos.",
        ],
        "edicion": [
            "El precio normal aparece primero y se tacha con una línea justo antes de mostrar el precio con descuento.",
            "Un corte cada 1.5 a 2 segundos. Sin transiciones elaboradas.",
            "Texto en coral #ED6864 y blanco, tipografía Comfortaa en los títulos. Subtítulos siempre puestos.",
            "Música baja durante la voz y sube un poco en el cierre.",
        ],
        "publicacion": {
            "caption": "Hoy empieza tu Navidad en Xalapa. 30% de descuento todo diciembre y enero, reservando directo. "
                       "Escríbenos por WhatsApp 228 252 5244 y aparta tu fecha. mobbitrips.com",
            "hashtags": "#Xalapa  #Veracruz  #NavidadEnXalapa  #RentaVacacional",
            "portada": "«Hoy empieza el 30%» sobre foto real (pendiente de generar en Canva).",
            "despues": "Compartir en historias con «Hoy empieza. Escríbenos» y enlace a WhatsApp.",
        },
    },
    {
        "num": 2,
        "titulo": "Todos los depas y sus precios",
        "estado": "SELECCIONADO - listo para grabar",
        "estado_color": VERDE,
        "publicar": "Primera semana de diciembre de 2026",
        "duracion": "30 segundos",
        "formato": "Vertical 9:16 (1080 x 1920), con subtítulos",
        "objetivo": "Mostrar todos los departamentos con su precio por noche ya con el 30% de descuento. Directo y claro, sin historia ni contexto.",
        "gancho": "«Todos nuestros depas, con 30% de descuento.»",
        "interpretacion": [
            "Tono claro, amable y seguro, como quien da información útil. Sin humor ni actuación: aquí lo importante es el precio.",
            "Mismo ritmo en todos los depas: nombre, pausa corta, precio. Que el espectador aprenda el patrón y lo siga solo.",
            "Resalta siempre el precio y di el nombre del depa sin prisa, sobre todo los números (Colina 2, 4, 7 y 9).",
            "Sonríe al empezar y al cerrar; en medio, voz tranquila y constante.",
        ],
        "pronunciacion": [
            "$442: «cuatrocientos cuarenta y dos». $443: «cuatrocientos cuarenta y tres». $539: «quinientos treinta y nueve».",
            "$636: «seiscientos treinta y seis». $740: «setecientos cuarenta». En el video basta decir «$442» sin «pesos».",
            "N20: «ene veinte». H1, H2 y H3: «hache uno, hache dos y hache tres».",
            "Todos los precios son por noche y ya incluyen el 30% de descuento.",
        ],
        "escenas": [
            ("1", "0-3 s", "Fachada o entrada del edificio, luz de mañana.",
             "«Todos nuestros depas, con 30% de descuento.»",
             "<b>TODOS LOS DEPAS</b><br/><b>30% DE DESCUENTO</b>",
             "Claro y amable. Sonríe."),
            ("2", "3-8 s", "N20 H1, N20 H2 y N20 H3: tres tomas de unos 1.7 s cada una (sala o recámara).",
             "«N20, H1, H2 y H3: $442 la noche.»",
             "N20 H1 / H2 / H3<br/><strike>$631</strike>  <b>$442</b>",
             "Di los tres nombres sin correr; el precio, firme."),
            ("3", "8-12 s", "Colina Estacionamiento: una toma de unos 3.5 s.",
             "«Colina Estacionamiento: $443.»",
             "Colina Estacionamiento<br/><strike>$632</strike>  <b>$443</b>",
             "Mismo ritmo que la escena anterior."),
            ("4", "12-19 s", "Colina 2, Colina 4, Colina 7 y Colina 9: cuatro tomas de unos 1.75 s cada una.",
             "«Colina 2, 4, 7 y 9: $539.»",
             "Colina 2 / 4 / 7 / 9<br/><strike>$770</strike>  <b>$539</b>",
             "Los números claros, uno por uno."),
            ("5", "19-22 s", "Colina 5: una toma de unos 3.5 s.",
             "«Colina 5: $636.»",
             "Colina 5<br/><strike>$908</strike>  <b>$636</b>",
             "Constante, sin cambiar de tono."),
            ("6", "22-26 s", "Colina 14: una toma de unos 3.5 s.",
             "«Colina 14: $740.»",
             "Colina 14<br/><strike>$1,057</strike>  <b>$740</b>",
             "Igual que las anteriores."),
            ("7", "26-30 s", "Pantalla final: la lista de precios de Navidad (diseño de Canva) con el logo.",
             "«Todo diciembre y enero. Reserva directo por WhatsApp.»",
             "<b>Todo diciembre y enero</b><br/>WhatsApp 228 252 5244<br/>mobbitrips.com",
             "Cálido al cerrar. Baja un poco el tono al terminar."),
        ],
        "tomas": [
            ("1", "Entrada del edificio", "Fachada o puerta, luz de mañana.", "4-5 s", "Avance lento", "2"),
            ("2", "N20 H1", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("3", "N20 H2", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("4", "N20 H3", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("5", "Colina Estac.", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("6", "Colina 2", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("7", "Colina 4", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("8", "Colina 7", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("9", "Colina 9", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("10", "Colina 5", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("11", "Colina 14", "Sala o recámara, mejor toma.", "4-5 s", "Avance lento", "2"),
            ("12", "Voz (voz en off)", "Letra completa, leída 3 veces con calma.", "-", "En un cuarto sin eco", "3"),
        ],
        "requiere": [
            "<b>Los 10 depas listos y ordenados</b> el mismo día, si se puede: camas tendidas, sin objetos personales, cocina limpia.",
            "Celular o cámara en <b>vertical</b>, 4K a 30 cuadros, con estabilizador o tripié.",
            "<b>La misma toma en todos los depas</b>: mismo ángulo, misma altura y mismo avance lento. Así ninguno parece mejor ni peor y la edición se ve ordenada.",
            "Luz natural de mañana, cortinas abiertas.",
            "Grabar siempre el depa del que se habla. Nunca mezclar fotos de uno con el nombre de otro.",
            "Si el actor sale a cámara, solo en el arranque y el cierre; ropa lisa, sin logos grandes.",
            "Música: instrumental navideña suave, libre de derechos; la elijo en la edición.",
            "<b>Fuera de este video:</b> Colina 6a (su descuento es de 15%, por confirmar) y Colina 2a (ya no aparece en el sistema).",
        ],
        "edicion": [
            "Plantilla fija para todos los depas: nombre arriba, precio normal tachado y precio con descuento grande, siempre en el mismo lugar.",
            "Ritmo constante: el espectador debe poder leer cada precio sin esfuerzo.",
            "Orden de precio de menor a mayor, para que el video se sienta ordenado.",
            "Pantalla final con la lista de precios de Navidad (diseño de Canva) durante 4 segundos.",
            "Texto en coral #ED6864 y blanco, tipografía Comfortaa en los títulos. Subtítulos siempre puestos.",
        ],
        "publicacion": {
            "caption": "Todos nuestros depas, con 30% de descuento. Reserva directo todo diciembre y enero. "
                       "Escríbenos por WhatsApp 228 252 5244. mobbitrips.com",
            "hashtags": "#Xalapa  #Veracruz  #NavidadEnXalapa  #RentaVacacional",
            "portada": "«Todos los depas, 30% de descuento» sobre foto real (por generar).",
            "despues": "Compartir en historias con el enlace a WhatsApp y fijar un comentario con la lista de precios.",
        },
    },
    {
        "num": 3,
        "titulo": "Lo que encuentras al llegar",
        "estado": "SELECCIONADO - falta elegir el depa protagonista",
        "estado_color": VERDE,
        "publicar": "Antes del 24 de diciembre de 2026",
        "duracion": "25 segundos",
        "formato": "Vertical 9:16 (1080 x 1920), con subtítulos",
        "objetivo": "Emoción y marca: hacer sentir cómo es llegar a un depa Mobbitrips en Navidad. Es el video más tranquilo de los tres.",
        "gancho": "Opción B: «Así se siente llegar a tu depa en Navidad.»",
        "interpretacion": [
            "Voz suave y cálida, casi como un susurro de bienvenida. Es el video más tranquilo: aquí no hay prisa ni energía de anuncio.",
            "Una frase por espacio, con una pausa corta entre cada una; la pausa es lo que deja ver la imagen.",
            "Sonríe al hablar, aunque no salgas a cámara: se nota en la voz.",
            "La frase de marca del cierre va despacio, como una despedida amable.",
        ],
        "pronunciacion": [
            "«Sobremesa»: sobre-MEsa (la plática después de comer).",
            "Frase de marca: «Descansa, vive y sueña como si estuvieras en casa».",
            "«30%» se dice «treinta por ciento».",
        ],
        "escenas": [
            ("1", "0-3 s", "Una mano abre la puerta del depa y entra la luz de la mañana.",
             "«Así se siente llegar a tu depa en Navidad.»",
             "<b>30% DE DESCUENTO</b>",
             "Suave, con sonrisa. Como dar la bienvenida."),
            ("2", "3-7 s", "Cocina (solo si el depa la tiene).",
             "«Un lugar para el desayuno de mañana.»",
             "Cocina",
             "Tranquilo, con calidez."),
            ("3", "7-11 s", "Sala.",
             "«Para la plática de sobremesa.»",
             "Sala",
             "Tranquilo; una pequeña sonrisa en la voz."),
            ("4", "11-15 s", "Recámara con la cama tendida.",
             "«Y un descanso de verdad.»",
             "Recámara",
             "Más bajito y lento, como quien habla de descansar."),
            ("5", "15-19 s", "Ventana y vista (solo si el depa tiene vista).",
             "«Con Xalapa de fondo.»",
             "Vista",
             "Cálido, con un poco de orgullo por la ciudad."),
            ("6", "19-25 s", "Logo sobre la mejor toma del depa.",
             "«Descansa, vive y sueña como si estuvieras en casa. Reserva directo, con 30%.»",
             "<b>Reserva directo</b><br/>Todo diciembre y enero<br/>WhatsApp 228 252 5244<br/>mobbitrips.com",
             "La frase de marca, despacio. Cierra con calidez."),
        ],
        "tomas": [
            ("1", "Entrada del depa", "Mano que abre la puerta y entra la luz.", "4-5 s", "Fija o avance muy lento", "3"),
            ("2", "Cocina", "Mesa, encimera o ventana (solo si la hay).", "4-5 s", "Avance lento", "2"),
            ("3", "Sala", "Toma amplia con luz natural.", "4-5 s", "Paneo lento", "2"),
            ("4", "Recámara", "Cama tendida, luz suave.", "4-5 s", "Avance lento", "2"),
            ("5", "Vista", "Ventana o balcón (solo si hay vista).", "4-5 s", "Casi fija", "2"),
            ("6", "Detalles", "Manta, lámpara, taza (2 o 3 tomas cortas).", "2-3 s c/u", "Fijas", "1-2 c/u"),
            ("7", "Cierre", "La mejor toma del depa para poner el logo.", "5 s", "Avance lento", "2"),
            ("8", "Voz (voz en off)", "Letra completa, leída 3 veces con calma.", "-", "En un cuarto sin eco", "3"),
        ],
        "requiere": [
            "<b>Un solo depa de protagonista</b>, el más bonito. Por elegir: ______________________.",
            "<b>Lista real de lo que tiene ese depa</b> (cocina, sala, recámara, vista). Solo se graba y se nombra lo que existe; si falta alguno, se sustituye por un detalle (manta, lámpara) sin etiqueta falsa.",
            "Depa ordenado: cama tendida, sin objetos personales, cocina limpia.",
            "Celular o cámara en <b>vertical</b>, 4K a 30 cuadros, con estabilizador o tripié.",
            "Luz natural de mañana, cortinas abiertas; luces apagadas salvo lámparas que se vean bonitas.",
            "Opcional: un detalle navideño discreto (luces o un moño) que se pueda quitar. No cambiar el depa.",
            "Si el actor sale a cámara, solo la mano en la puerta o de espaldas; ropa lisa, sin logos grandes.",
            "<b>Por definir:</b> si el actor habla a cámara o solo es voz en off. La letra es la misma.",
        ],
        "edicion": [
            "Ritmo más lento que los otros videos: cortes cada 4 segundos, con transiciones suaves de disolvencia.",
            "Etiquetas (Cocina, Sala, Recámara, Vista) pequeñas, abajo a la izquierda, en coral y blanco.",
            "Música instrumental navideña, suave y cálida, libre de derechos; baja durante la voz.",
            "La frase de marca del cierre aparece escrita en grande, sobre la mejor toma.",
        ],
        "publicacion": {
            "caption": "Así se siente llegar a tu depa en Navidad. Descansa, vive y sueña como si estuvieras en casa. "
                       "30% de descuento todo diciembre y enero reservando directo. Escríbenos por WhatsApp 228 252 5244.",
            "hashtags": "#Xalapa  #Veracruz  #NavidadEnXalapa  #RentaVacacional",
            "portada": "«Así se siente llegar» sobre la mejor foto del depa (por generar).",
            "despues": "Compartir en historias con enlace a WhatsApp.",
        },
    },
]

PENDIENTES = [
    ["#", "Video", "Estado", "Qué sigue"],
    ["1", "Hoy empieza el 30%", "<font color='#3E9B6B'><b>SELECCIONADO - listo para grabar</b></font>", "Grabar y confirmar si es a cámara o voz en off."],
    ["2", "Todos los depas y sus precios", "<font color='#3E9B6B'><b>SELECCIONADO - listo para grabar</b></font>", "Grabar los 10 depas con la misma toma."],
    ["3", "Lo que encuentras al llegar", "<font color='#3E9B6B'><b>SELECCIONADO - falta elegir depa</b></font>", "Elegir el depa protagonista y confirmar qué tiene."],
    ["4", "Rifa de 3 noches", "<font color='#ED6864'><b>EN PAUSA - no publicar</b></font>", "Falta permiso legal, reglas escritas y costo aprobado."],
]


# ---------------------------------------------------------------- páginas
def portada():
    s = [Spacer(1, 6), P("Guiones de video", "h1"), P("Campaña Navidad 2026 - Mobbitrips", "h2"), Spacer(1, 4)]
    s.append(P("Documento para la producción de los videos. Aquí se va agregando cada guion cuando queda aprobado, con lo que se "
               "tiene que grabar, lo que se necesita y la letra que lee el actor."))
    s.append(Spacer(1, 10))
    s.append(P("La promoción", "h2"))
    s.append(P("<b>30% de descuento todo diciembre y enero, solo por reserva directa.</b><br/>"
               "WhatsApp 228 252 5244  |  mobbitrips.com"))
    s.append(Spacer(1, 6))
    s.append(tabla(PROMO, [2.6 * inch, 2.2 * inch, 2.2 * inch]))
    s.append(P("Precios por noche, según el sistema de reservas al 25 de noviembre de 2026. Verificar antes de publicar.", "small"))
    s.append(Spacer(1, 10))
    s.append(P("Estado de los videos", "h2"))
    s.append(tabla(PENDIENTES, [0.3 * inch, 1.9 * inch, 2.3 * inch, 2.5 * inch]))
    s.append(Spacer(1, 10))
    s.append(P("Reglas para todos los videos", "h2"))
    s += bullets([
        "Vertical 9:16, con subtítulos siempre puestos (mucha gente lo ve sin sonido).",
        "El 30% se ve o se dice en los primeros 3 segundos y otra vez al final, con «todo diciembre y enero», «reserva directo» y el WhatsApp.",
        "Tuteo mexicano, frases cortas, tono cálido y cercano. Nada de «oferta imperdible», «exclusivo» ni «lujo».",
        "Solo mostrar y decir lo que realmente hay en cada depa. No mencionar mascotas, número de camas, capacidades ni amenidades sin confirmarlas.",
        "Frase de marca: «Descansa, vive y sueña como si estuvieras en casa».",
    ])
    return s


def pagina_video_ficha(v):
    s = [PageBreak()]
    s.append(P(f"Video {v['num']}  -  {v['titulo']}", "h1"))
    est = ParagraphStyle("est", parent=S["cellb"], textColor=v["estado_color"], fontSize=11)
    s.append(Paragraph(v["estado"], est))
    s.append(Spacer(1, 6))
    filas = [
        ["Se publica", v["publicar"]],
        ["Duración", v["duracion"]],
        ["Formato", v["formato"]],
        ["Objetivo", v["objetivo"]],
        ["Gancho elegido", f"<b>{v['gancho']}</b>"],
    ]
    t = tabla([[f"<b>{a}</b>", b] for a, b in filas], [1.5 * inch, 5.5 * inch], cabecera=False)
    s.append(t)
    s.append(P("Para el actor: cómo interpretarlo", "h2"))
    s += bullets(v["interpretacion"])
    s.append(P("Pronunciación", "h3"))
    s += bullets(v["pronunciacion"])
    return s


def pagina_letra(v):
    s = [PageBreak(), P(f"Video {v['num']}  -  La letra, de corrido", "h1"), Spacer(1, 4)]
    s.append(P("Lo que dice el actor, en orden. Cada línea es una escena; la pausa corta entre líneas es el corte de imagen.", "small"))
    s.append(Spacer(1, 8))
    for n, tiempo, _img, voz, _txt, nota in v["escenas"]:
        bloque = [
            Paragraph(f"<font color='#ED6864'><b>Escena {n}</b></font>  <font color='#706F6F'>({tiempo})</font>", S["h3"]),
            Paragraph(voz, S["voz"]),
            Paragraph(f"<i>Cómo decirlo: {nota}</i>", S["small"]),
            Spacer(1, 4),
        ]
        s.append(KeepTogether(bloque))
    return s


def pagina_escaleta(v):
    s = [PageBreak(), P(f"Video {v['num']}  -  Escaleta del guion", "h1"), Spacer(1, 4)]
    s.append(P("Qué se ve, qué se dice y qué aparece escrito en pantalla, escena por escena.", "small"))
    s.append(Spacer(1, 6))
    filas = [["#", "Tiempo", "Qué se ve", "Qué dice el actor", "Texto en pantalla"]]
    for n, tiempo, img, voz, txt, _nota in v["escenas"]:
        filas.append([f"<b>{n}</b>", tiempo, img, f"<b>{voz}</b>", txt])
    s.append(tabla(filas, [0.3 * inch, 0.7 * inch, 2.0 * inch, 2.0 * inch, 2.0 * inch]))
    s.append(P("Edición", "h2"))
    s += bullets(v["edicion"])
    return s


def pagina_grabacion(v):
    s = [PageBreak(), P(f"Video {v['num']}  -  Qué grabar y qué se requiere", "h1"), Spacer(1, 4)]
    s.append(P("Lista de tomas", "h2"))
    filas = [["#", "Lugar", "Qué grabar", "Duración", "Movimiento", "Tomas"]]
    for fila in v["tomas"]:
        filas.append(list(fila))
    s.append(tabla(filas, [0.4 * inch, 1.5 * inch, 2.15 * inch, 0.75 * inch, 1.5 * inch, 0.7 * inch]))
    s.append(P("Qué se necesita el día de grabación", "h2"))
    for t in v["requiere"]:
        s.append(Paragraph(t, S["bullet"], bulletText="[  ]"))
    s.append(P("Para publicar", "h2"))
    pub = v["publicacion"]
    s.append(tabla([[f"<b>Caption</b>", pub["caption"]], [f"<b>Hashtags</b>", pub["hashtags"]],
                    [f"<b>Portada</b>", pub["portada"]], [f"<b>Después</b>", pub["despues"]]],
                   [1.2 * inch, 5.8 * inch], cabecera=False))
    return s


def construir():
    doc = BaseDocTemplate(str(SALIDA), pagesize=letter, leftMargin=0.6 * inch, rightMargin=0.6 * inch,
                          topMargin=0.65 * inch, bottomMargin=0.7 * inch,
                          title="Mobbitrips - Guiones de video Navidad 2026", author="Mobbitrips")
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=pie_y_cabecera)])
    historia = portada()
    for v in VIDEOS:
        historia += pagina_video_ficha(v) + pagina_letra(v) + pagina_escaleta(v) + pagina_grabacion(v)
    doc.build(historia)
    print("PDF escrito en", SALIDA)


if __name__ == "__main__":
    construir()
