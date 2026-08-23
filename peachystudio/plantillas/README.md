# Peachy Studio — Maquetas de historias (9:16)

Quince maquetas de plantilla de historia en **1080 × 1920 px**, alineadas al Brand
Kit de la marca. Sirven como propuesta visual y como referencia exacta para
construir las plantillas maestras en Canva.

> El detalle de objetivo, campos editables y frecuencia de cada una está en
> [`../plantillas-historias.md`](../plantillas-historias.md).

## Archivos

| # | Archivo | Chasis | Uso |
|---|---------|--------|-----|
| 01 | `diseno-del-dia` | A · FOTO | Portafolio diario |
| 02 | `antes-despues` | A · FOTO | Transformación |
| 03 | `detras-de-camaras` | A · FOTO | Proceso en video |
| 04 | `esto-o-esto` | C · INTERACCIÓN | Encuesta |
| 05 | `cotiza-tu-diseno` | C · INTERACCIÓN | Caja de preguntas |
| 06 | `tip-de-cuidado` | D · AVISO | Educativo |
| 07 | `mito-verdad` | D · AVISO | Objeciones |
| 08 | `testimonio` | C · INTERACCIÓN | Prueba social |
| 09 | `menu-precios` | D · AVISO | Precios |
| 10 | `agenda-semana` | B · AGENDA | Disponibilidad |
| 11 | `ultimo-lugar` | B · AGENDA | Urgencia |
| 12 | `promo-del-mes` | D · AVISO | Promoción |
| 13 | `como-agendar` | D · AVISO | Proceso y políticas |
| 14 | `recordatorio-retoque` | D · AVISO | Retención |
| 15 | `nuevo-servicio` | A · FOTO | Novedad |

## Cómo se generan

Cada maqueta vive como HTML autocontenido en `html/`, sobre un sistema de diseño
compartido en `html/_base.css` (tokens de color, tipografías embebidas y
componentes: píldoras, tarjetas, marcos de foto, zonas de sticker).

Para regenerar los PNG:

```bash
cd html
for f in *.html; do
  chrome --headless --no-sandbox --hide-scrollbars \
    --window-size=1080,1920 --virtual-time-budget=4000 \
    --screenshot="../png/${f%.html}.png" "$f"
done
```

## Notas

- Los recuadros punteados son **huecos editables**: rosa para foto o video,
  morado para el espacio reservado a los stickers nativos de Instagram y Facebook.
- El logotipo de las maquetas es una **reconstrucción aproximada en CSS**, porque
  las fuentes originales son de Canva. En Canva se usa siempre el archivo real
  del Brand Kit.
- Las fuentes embebidas en `_base.css` son de Google Fonts con licencia SIL OFL
  y funcionan como equivalentes web de las fuentes de marca.
