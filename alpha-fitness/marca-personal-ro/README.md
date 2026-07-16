# Coach Ro — Kit de Marca Personal

Marca personal de **Ro**, entrenadora de danza aérea, calistenia y acondicionamiento
físico para niños en **Alpha Fitness** (Xalapa). Desarrollado por **Medusssa Studio**
dentro del **Plan Esencial**.

## Contenido

| Archivo | Qué es |
|---------|--------|
| `manual-identidad-reducido.md` | Manual de identidad esencial (esencia, tono, color, tipografía, logo, do/don't). |
| `sugerencias-posts.md` | Ideas de posts e historias por pilar de contenido. |
| `horario-y-contacto.md` | Horario semanal de clases + datos de contacto (fuente: cuestionario + video). |
| `entregables/` | Piezas finales en PNG, listas para publicar. |
| `plantillas-fuente/` | Código HTML/CSS + fuentes para editar y re-generar las piezas. |

## Entregables (`entregables/`)

**Historias — calendario de disponibilidad**
- `historia-semanal.png` — resumen del horario de la semana.
- `historia-lunes/martes/miercoles/jueves/viernes.png` — tarjeta por día
  (clase, hora, precio y "lugares disponibles" editable).

**Overlays de contacto** (PNG transparente, se colocan sobre foto/video)
- `overlay-contacto.png` — barra inferior completa (logo + WhatsApp + IG + dirección).
- `overlay-esquina.png` — sticker compacto de esquina.

**Posts de feed de ejemplo** (1080×1350)
- `post-presentacion.png` · `post-seguridad.png` · `post-inscripciones.png`.

**Marca**
- `logo-lockup.png` — logotipo Coach Ro.

## Especificaciones

- Historias / overlays: **1080 × 1920** (exportados a 2×: 2160 × 3840).
- Posts: **1080 × 1350** (4:5).
- Overlays: fondo **transparente**.

## Cómo re-generar o editar las piezas

Requiere Node.js con Playwright/Chromium y Python 3 con Pillow.

```bash
cd plantillas-fuente
python3 gen.py            # genera los HTML en pages/
node render.js "$PWD/pages/historia-lunes.html" salida.png 1080 1920 false
# overlays (transparente): usar 'true' como último parámetro
```

Los datos (horario, contacto, colores) están al inicio de `gen.py`; edítalos ahí y
vuelve a correr para actualizar todas las piezas de golpe.

---

*Medusssa Studio · Xalapa, Veracruz*
