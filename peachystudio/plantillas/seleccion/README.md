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
python3 ../render.py     # o ../../render.py desde seleccion/
```

> No basta con `chrome --screenshot --window-size=1080,1920`: Chrome recorta todo lo que
> cae bajo el viewport cuando `html`/`body` llevan `overflow:hidden`, y deja una franja
> del color de fondo al pie. `render.py` renderiza con ventana alta y recorta a 1080×1920.
