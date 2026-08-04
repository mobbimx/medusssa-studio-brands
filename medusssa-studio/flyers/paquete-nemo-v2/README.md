# Paquete Nemo — Flyer v2 (estilo editorial retro)

Versión alternativa del flyer del **Paquete Nemo**, con dirección de arte opuesta a la v1 (oscura/oceánica con medusa brillante).

## Dirección de arte

| Elemento | v1 (original) | v2 (esta versión) |
|----------|---------------|-------------------|
| Fondo | Azul profundo con gradientes y collage de analytics | Crema papel (#F6F1E7), plano |
| Estilo | Tech/acuático, glow, 3D | Póster editorial retro, tipografía gigante, bordes de tinta |
| Tipografía | Sans redondeada | Archivo Black (display) + Space Grotesk (texto) |
| Acento | Turquesa neón | Coral (#FF5A3C) + tinta (#131A22) |
| Ilustración | Medusa 3D luminosa + pez realista | Pez payaso flat line-art + medusa lineal en el header |
| Layout | Centrado, lista con iconos | Retícula con marco, lista numerada 01–05, franja de precio |

## Archivos

- `flyer-nemo-v2.html` — fuente del diseño (1080×1350, formato 4:5). Editable: textos, precio y teléfono están en el HTML.
- `flyer-nemo-v2.png` — export final en 2160×2700 (2x), listo para Instagram/Facebook.
- `fonts/` — tipografías usadas (Google Fonts, licencia libre OFL).

## Cómo regenerar el PNG

Abrir el HTML en un navegador a 1080×1350 y capturar, o con Playwright:

```js
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
await page.goto('file://.../flyer-nemo-v2.html');
await page.screenshot({ path: 'flyer-nemo-v2.png' });
```
