# Pitch beta negocios — Medusa OS · Panel Promocional

Presentación de ventas (**9 slides**, ~12–14 min) para captar **negocios** a la **prueba beta
gratuita** del Panel Promocional de Medusa OS, anclada a la sede de **Mobbitrips** (radio 1 km).
Sirve igual en **virtual** (compartir pantalla / PDF) que **presencial** (pantalla completa).

## Orden de las diapositivas
1. Portada — **GRATIS** (oferta beta)
2. La oportunidad (clientes a <1 km)
3. El problema
4. Qué es (resumen)
5. El panel en pantalla — **2 pantallas** (principal + recomendaciones)
6. El flujo (TV → info → QR → llega)
7. Las métricas (dashboard)
8. La beta gratis
9. Cómo empiezas (cierre + CTA)

## Archivos
| Archivo | Qué es |
|---------|--------|
| `deck-editable.pptx` | **PowerPoint editable** (texto y tarjetas nativos). Se edita en PowerPoint **y** se importa a Canva. |
| `index.html` | Fuente HTML del deck (autocontenida, 16:9), para render/PDF. |
| `deck.pdf` | Render de 9 páginas para revisar, enviar o proyectar sin navegador. |
| `guion.md` | Guion del presentador: qué decir por slide, tiempos y manejo de objeciones. |
| `scripts/render.mjs` | Regenera `deck.pdf` desde el HTML. |
| `scripts/build-pptx.mjs` | Regenera `deck-editable.pptx` (usa `assets-pptx/`). |
| `assets-pptx/` | Ilustraciones/íconos usados por el `.pptx` (mapa, pantallas, dashboard, íconos). |
| *(pendiente)* imágenes reales | Ver abajo. |

## Cómo presentar
1. Abre `index.html` en el navegador.
2. Tecla **F** → pantalla completa.
3. **←/→** (o clic en ‹ ›) para avanzar · **P** para exportar PDF · **Home/End** para saltar.

## Cómo exportar el PDF de nuevo
Requiere Node + Playwright (ya disponible en el entorno del estudio):
```bash
node scripts/render.mjs
```
O manualmente: abre `index.html`, tecla **P**, "Guardar como PDF", tamaño horizontal.

## ⚠️ Reemplazar los placeholders por imágenes reales
El brief pide **imágenes reales del panel**. Hay **3 placeholders** marcados con la etiqueta
*"Reemplazar con imagen real"* / *"Mockup"*:

| Slide | Placeholder | Archivo sugerido | Proporción ideal |
|-------|-------------|------------------|------------------|
| 5 | Pantalla **principal** | `pantalla-principal.png` | 16:9 (pantalla/TV) |
| 5 | Pantalla de **recomendaciones** (con anuncios) | `pantalla-recomendaciones.png` | 16:9 (pantalla/TV) |
| 7 | **Dashboard** de métricas | `dashboard-real.png` | ~16:10 |

Para dejarlos definitivos:
1. Guarda las capturas en esta carpeta con esos nombres.
2. En `index.html`, dentro del `.mockframe` correspondiente, sustituye el `<svg>` del mockup por:
   ```html
   <img src="pantalla-principal.png" alt="Pantalla principal" style="width:100%;height:100%;object-fit:cover;border-radius:12px;">
   ```
   (para la slide 5 son dos `<svg>`; para la slide 7 es el bloque oscuro del dashboard).
3. Quita el badge `badge mock` de cada marco reemplazado.
4. Vuelve a exportar el PDF.

> Mientras tanto, los mockups comunican bien el concepto para revisar la propuesta.

## Editar en PowerPoint / Canva
**`deck-editable.pptx`** es el archivo para modificar:
- **PowerPoint / Google Slides / Keynote:** ábrelo directamente. Texto, tarjetas, badges y
  CTAs son elementos **nativos editables**. Las ilustraciones (mapa, pantallas, dashboard,
  íconos) van como imagen.
- **Canva:** *Crear diseño → Subir → Importar archivo* (o arrastra el `.pptx`). Canva lo
  convierte en un diseño editable. Ahí aplicas el Brand Kit de Medusa OS cuando exista
  (colores/tipografías provisionales en `../../panel-promocional.md`).
  - Fuentes: el deck usa **Space Grotesk** (títulos) e **Inter** (texto), ambas disponibles
    en Canva. Si abres en PowerPoint sin esas fuentes, se sustituyen (fácil de re-elegir).

Regenerar el `.pptx` (si cambian los assets o el contenido):
```bash
npm i pptxgenjs        # una vez
node scripts/build-pptx.mjs
```

## Pendientes de negocio (para cerrar)
Ver **[POR CONFIRMAR]** en `../../panel-promocional.md`: duración de la beta, cupos por
categoría, CTA de registro y grafía oficial de la marca.
