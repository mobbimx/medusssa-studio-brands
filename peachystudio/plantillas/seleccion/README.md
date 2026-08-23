# Peachy Studio — Selección de 6 plantillas base

Las seis plantillas maestras que cubren los 22 usos del catálogo.
Detalle completo en [`../../plantillas-seleccion-6.md`](../../plantillas-seleccion-6.md).

| Archivo | Plantilla | Absorbe |
|---------|-----------|---------|
| `S1-calendario-mes` | Calendario del mes | 16 |
| `S2-citas-disponibles` | Citas disponibles | 10 · 11 · 17 · 22 |
| `S3-lista-precios` | Lista de precios | 09 |
| `S4-info-studio` | Información del studio | 13 · 18 · 19 · 20 |
| `S5-diseno-del-dia` | Diseño del día | 01 · 02 · 03 · 04 · 15 |
| `S6-aviso-promo` | Aviso o promoción | 05 · 06 · 07 · 08 · 12 · 14 · 21 |

Comparten el sistema de diseño de [`../html/_base.css`](../html/_base.css).
Para regenerar los PNG:

```bash
for f in *.html; do
  chrome --headless --no-sandbox --hide-scrollbars \
    --window-size=1080,1920 --virtual-time-budget=4000 \
    --screenshot="png/${f%.html}.png" "$f"
done
```
