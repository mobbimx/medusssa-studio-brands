# Salones Aurora — Plantillas de posts de Facebook (PNG + HTML)

Set de **8 plantillas** de feed (**1080 × 1350 px, formato 4:5**) construidas con la
identidad visual de `../visual.md` y los copies de `../posts-facebook.md`.

El 4:5 es el formato que más espacio vertical ocupa en el feed de Facebook e Instagram
sin que la plataforma lo recorte.

## Archivos

| # | Archivo | Modo | Alimenta los posts |
|---|---------|------|--------------------|
| 1 | `01-evento-real.png` | Foto | 01 XV años · 02 Boda · 03 Bautizo · 12 Agradecimiento |
| 2 | `02-instalaciones.png` | Foto | 05 Tour · 06 Pista · 07 Ubicación · 08 Capacidad |
| 3 | `03-todo-incluido.png` | Marfil | 13 Todo incluido · 18 Entre semana |
| 4 | `04-fechas-disponibles.png` | Marfil | 15 Fechas libres |
| 5 | `05-agenda-visita.png` | Foto | 16 Agenda una visita · 07 Ubicación |
| 6 | `06-testimonio.png` | Marfil | 10 Testimonio · 11 Testimonio en video (portada) |
| 7 | `07-tip-checklist.png` | Marfil | 19 Qué preguntar · 20 Cuándo apartar · 22 Invitados · 23 Orden del día |
| 8 | `08-temporada.png` | Foto | 17 Temporada alta · 14 Cotización clara |

Con estas 8 se cubren las 12 publicaciones del mes del calendario de rotación
(ver `../posts-facebook.md`).

## Cómo editarlas (replicable)

Cada plantilla vive también como **HTML autocontenido** en `html/` (las tipografías van
incrustadas en base64, así que abren igual sin internet).

1. Abre el `.html` correspondiente en `html/`.
2. Cambia los textos de `eyebrow`, `title`, `sub`, la lista o la cita.
3. En las plantillas de **modo foto**, sustituye el `<div class="bg-ph"></div>` por la
   foto real:
   ```html
   <img class="bg" src="../../referencias/fotos/mi-foto.jpg">
   ```
   El `bg-ph` es solo un fondo cálido de relleno mientras no hay fotografía del salón.
4. Borra el `<div class="ph-tag">` (la etiqueta punteada de "sustituir por foto") y el
   `<div class="hint">` (la línea de "Campos editables"). **Las dos son guías de edición
   y no deben salir publicadas.**
5. Re-renderiza a PNG:
   ```bash
   node shot.js     # Playwright, viewport exacto de 1080×1350
   ```
   o con Chrome headless:
   ```bash
   chromium --headless --window-size=1080,1350 \
     --screenshot=salida.png 01-evento-real.html
   ```

## Pendientes
- **Fotos reales del salón.** Los 4 diseños de modo foto usan un fondo de relleno
  cálido. Con material propio (montaje, pista, fachada, entrada, evento en curso)
  suben mucho de nivel. Es el entregable que más falta hace.
- **Logo oficial.** Se usa la propuesta de `../referencias/`. Si el cliente tiene el
  suyo, se sustituye el lockup en el bloque `.firma` de cada HTML.
- **Versión editable en Canva**, para que el cliente pueda cambiar textos sin código
  (ver `../brand-kit-canva.md`).
