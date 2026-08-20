# Aurora Salones — Plantillas de posts de Facebook (PNG + HTML)

**8 plantillas nuevas** de feed (**1080 × 1350 px, 4:5**) construidas sobre la línea
gráfica real de la marca (ver `../linea-grafica-existente.md` y `../visual.md`).

Cubren los formatos que **no existían** en el material ya publicado: disponibilidad,
paquete, capacidad y agenda de visita; más versiones nuevas de los formatos que sí
funcionan (portada de instalaciones, temporada, tip y testimonio).

## Archivos

| # | Archivo | Modo | Formato | Alimenta los posts de `../posts-facebook.md` |
|---|---------|------|---------|------------------------------------------|
| 1 | `01-fechas-disponibles.png` | Crema | Chips de fecha | 15 Fechas libres |
| 2 | `02-todo-incluido.png` | Crema | Lista con flor | 13 Todo incluido · 18 Entre semana |
| 3 | `03-tip-5-preguntas.png` | Crema | Lista numerada | 19 Qué preguntar · 20 Cuándo apartar · 22 Invitados |
| 4 | `04-capacidad.png` | Crema | Número grande + polaroid | 08 Capacidad |
| 5 | `05-instalaciones.png` | Foto | Portada con pill | 05 Tour · 06 Pista · 07 Ubicación |
| 6 | `06-temporada-diciembre.png` | Foto | Titular + apoyo | 17 Temporada alta |
| 7 | `07-agenda-visita.png` | Foto + barra sólida | Conversión | 16 Agenda una visita |
| 8 | `08-testimonio.png` | Crema + barra sólida | Cita + estrellas | 10 Testimonio · 12 Agradecimiento |

Con estas 8 se cubren las 12 publicaciones del mes del calendario de rotación.

## Antes de publicar (importante)

Cada plantilla trae **una guía de edición que hay que borrar**: la línea
*"Campos editables: …"* del pie. En el HTML es el `<div class="guia">`.

Las fotos que traen son **ejemplos tomados del propio material del cliente**
(evento de diciembre). Hay que cambiarlas por la foto que toque en cada publicación
—y sobre todo por material sin temporada marcada cuando el post no sea navideño.

## Cómo editarlas

Cada plantilla vive como **HTML autocontenido** en `html/`: tipografías, logo y fotos
van incrustados en base64, así que el archivo abre igual sin internet y sin fuentes
instaladas.

1. Abre el `.html` en `html/`.
2. Cambia los textos entre `[corchetes]` y el resto del copy.
3. Para cambiar la foto, sustituye el `src` del `<img class="foto">` (fondo) o del
   `<img>` dentro del `.polaroid`.
4. Borra el `<div class="guia">`.
5. Re-renderiza:
   ```bash
   NODE_PATH=/opt/node22/lib/node_modules node shot.js
   ```
   o con Chrome headless:
   ```bash
   chromium --headless --window-size=1080,1350 --screenshot=salida.png html/01-fechas-disponibles.html
   ```

## Piezas de la línea que se respetaron

- Logo centrado arriba (con badge blanco cuando hay foto detrás).
- Trama de curvas de nivel en todos los fondos crema.
- Polaroid girado 2° con marco blanco para las fotos.
- Barra de contacto en las dos variantes: hairline y bloque sólido café.
- Playfair Display para titulares, Poppins para cuerpo.
- Paleta vino / terracota / crema, sin colores nuevos.

## Pendientes
- **Logo vectorial** del cliente: hoy se usa un PNG de 209 px extraído de una pieza
  publicada. Sirve al tamaño del feed, no para más.
- **Sesión de fotos propia** del salón, vacío y montado, sin decoración de temporada.
- **Versión editable en Canva** (ver `../brand-kit-canva.md`).
- **Set de historias 9:16**: no existe todavía ningún formato vertical de historia.
