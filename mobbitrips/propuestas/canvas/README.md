# Mobbitrips — Lienzo de 10 propuestas gráficas

Maquetas visuales de las **10 propuestas de contenido gráfico** (ver
`../../propuestas-contenido.md`) para revisar **estilo y estructura** antes de
producir en Canva.

## Lienzo publicado (revisable / editable / exportable)
- **URL:** https://claude.ai/code/artifact/68942082-cebf-4a1c-afbf-38b19429c1b3
- Es un lienzo de diseño (11 artboards: portada + 10 propuestas) en una sola vista.
- Se puede revisar, editar a mano (donde la cuenta lo permita) y exportar a PNG/PDF.

## Contenido
| Artboard | Propuesta | Formato |
|----------|-----------|---------|
| `Main` | Portada / índice + leyenda | 1500×1500 |
| `Prop01` | ¿Para qué viajas? | Carrusel 4:5 |
| `Prop02` | Home office con vista | Post 4:5 |
| `Prop03` | Lo primero que ves al llegar | Historia 9:16 |
| `Prop04` | Un día en tu estancia | Carrusel 4:5 |
| `Prop05` | Qué hacer cerca · Xalapa | Carrusel 4:5 |
| `Prop06` | Modo desconexión | Post 4:5 |
| `Prop07` | Check-in inteligente | Carrusel 4:5 |
| `Prop08` | Reseña de huésped | Post 4:5 |
| `Prop09` | ¿Cuánto genera tu propiedad? | Post 4:5 (fondo oscuro, B2B) |
| `Prop10` | Detrás de una estancia perfecta | Carrusel 4:5 |

## Identidad aplicada
- Coral `#ED6864` (acento) · Gris `#706F6F` (soporte) · base blanca cálida.
- Títulos en Comfortaa; cuerpo en sans humanista (equivalente al font de marca).
- CTA a WhatsApp y wordmark "mobbitrips" constantes.
- **Solo imágenes reales en producción:** las zonas `[ Foto real ]` son marcadores
  etiquetados con la toma que va en cada una (banco de fotos pendiente). No se usan
  imágenes falsas; los mockups fijan jerarquía, tipografía y color.

## Cómo se construye / edita
Archivos fuente: `Main.dc.html` + `Prop01..Prop10.dc.html` + `canvas.json`
(artboards de "Design Components"). Se ensamblan con el skill `design` de Claude Code
y se publican como Artifact. Para cambios: editar el `.dc.html`, re-ensamblar y
re-publicar a la misma URL.

## Siguiente paso
Elegir cuáles propuestas avanzan y recrearlas **editables en Canva** con el Brand Kit
de Mobbitrips (ver `../../brand-kit-canva.md`) y fotos reales.
