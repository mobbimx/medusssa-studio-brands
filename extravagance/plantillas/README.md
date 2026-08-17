# Extravagance — Plantillas de Historias (PNG + HTML)

Set de **7 plantillas** de historias (9:16 · 1080×1920) listas para publicar a diario.
Diseñadas con la identidad de marca (amarillo `#F8D808` sobre negro, isotipo y wordmark)
y fondos reales del venue (primera visita).

## Archivos
| # | Archivo | Uso (día sugerido) |
|---|---------|--------------------|
| 1 | `01-cuenta-regresiva.png` | Lunes — anticipación al finde |
| 2 | `02-ambiente-venue.png` | Martes — aspiracional del lugar |
| 3 | `03-botella-promo.png` | Miércoles — promo/botella del día |
| 4 | `04-espectaculo.png` | Jueves — show (sugerido, no explícito) |
| 5 | `05-hoy-abrimos.png` | Viernes — reserva inmediata |
| 6 | `06-reserva-privado.png` | Sábado — privados (mayor ticket) |
| 7 | `07-comunidad-after.png` | Domingo — comunidad / cierre |

> Detalle de copy, campos editables y rotación: ver `../plantillas-historias.md`.

## Cómo editarlas (replicable)
Cada plantilla vive también como **HTML autocontenido** en `html/` (imágenes embebidas
en base64). Para generar una variación:

1. Abre el `.html` correspondiente en `html/`.
2. Cambia los textos: `eyebrow`, `title`, `sub` y `cta`.
3. Para cambiar el fondo, reemplaza el `src` de `<img class="bg">` por otra foto
   (usa las de `../referencias/fotos/`).
4. Re-renderiza a PNG 1080×1920 (Chrome headless):

```bash
chrome --headless --window-size=1080,1920 \
  --screenshot=salida.png archivo.html
```

La línea inferior *"Campos editables: …"* es una guía para quien edita; puede quitarse
en la versión final borrando el `<div class="hint">` del HTML.

## Notas
- Fondos tomados de la primera visita; se recomienda re-shoot siguiendo la
  `Guia_Contenido_Rodaje_Extravagance.docx` para material más limpio.
- Alternativa no-código: recrear este set en Canva como plantillas reutilizables
  (pendiente: crear brand kit de Extravagance en Canva).
