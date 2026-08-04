# Paquete Nemo — Flyer v3 (fondo redes sociales)

Tercera versión del flyer del **Paquete Nemo**, con dirección de arte "social media": gradiente vibrante estilo Instagram y elementos de interfaz de redes flotando en el fondo.

## Dirección de arte

- Fondo: gradiente azul → violeta → magenta → naranja (paleta Instagram) con blobs de luz difuminados
- Elementos flotantes de UI social: chip de "me gusta", "nuevo comentario", badge de cámara con notificación 99+, botón de play y contador de seguidores
- Tarjeta de beneficios con efecto vidrio (glassmorphism) e iconos por servicio
- Precio en tarjeta amarilla + CTA oscuro con WhatsApp en verde
- Tipografías: Archivo Black (display) + Space Grotesk (texto)

## Archivos

- `flyer-nemo-v3.html` — fuente del diseño (1080×1350, formato 4:5). Textos, precio y teléfono editables en el HTML.
- `flyer-nemo-v3.png` — export final 2160×2700 (2x), listo para Instagram/Facebook.
- `fonts/` — tipografías (Google Fonts, licencia OFL).

## Cómo regenerar el PNG

Abrir el HTML en un navegador a 1080×1350 y capturar, o con Playwright:

```js
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 2 });
await page.goto('file://.../flyer-nemo-v3.html');
await page.screenshot({ path: 'flyer-nemo-v3.png' });
```
