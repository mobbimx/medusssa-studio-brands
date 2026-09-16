# Pitch beta restaurantes — Medusa OS · Panel Promocional

Presentación de ventas (12 slides, ~15–20 min) para captar restaurantes a la **prueba beta
gratuita** del Panel Promocional de Medusa OS, anclada a la sede de **Mobbitrips** (radio 1 km).
Sirve igual en **virtual** (compartir pantalla / PDF) que **presencial** (pantalla completa).

## Archivos
| Archivo | Qué es |
|---------|--------|
| `index.html` | **Fuente editable** del deck (autocontenida, 16:9). Es lo que se edita. |
| `deck.pdf` | Render de 12 páginas para revisar, enviar o proyectar sin depender del navegador. |
| `guion.md` | Guion del presentador: qué decir por slide, tiempos y manejo de objeciones. |
| *(pendiente)* `panel-real.png`, `dashboard-real.png` | **Capturas reales** que reemplazan los mockups (ver abajo). |

## Cómo presentar
1. Abre `index.html` en el navegador.
2. Tecla **F** → pantalla completa.
3. **←/→** (o clic en ‹ ›) para avanzar · **P** para imprimir/exportar PDF · **Home/End** para saltar.

## Cómo exportar el PDF de nuevo
Requiere Node + Playwright (ya disponible en el entorno del estudio):
```bash
node scripts/render.mjs   # o vuelve a correr el script usado para generar deck.pdf
```
O manualmente: abre `index.html`, tecla **P**, "Guardar como PDF", tamaño horizontal.

## ⚠️ Reemplazar los mockups por capturas reales
El brief pide **imágenes reales del panel**. Hoy las slides **5** (el panel) y **7** (dashboard de
métricas) llevan **mockups on-brand** claramente marcados con la etiqueta *"Mockup · reemplazar
con captura real"*. Para dejarlos definitivos:

1. Toma capturas reales:
   - **Panel** (slide 5): captura vertical del panel como lo ve el cliente. Ideal ~**1080×1920** (9:16).
   - **Dashboard** (slide 7): captura del panel de métricas. Ideal ~**1600×1000** (16:10).
2. Guarda los archivos en esta carpeta como `panel-real.png` y `dashboard-real.png`.
3. En `index.html`, dentro del marco `.mockframe` de cada slide, sustituye el `<svg>` del mockup por:
   ```html
   <img src="panel-real.png" alt="Panel de Medusa OS" style="width:100%;height:100%;object-fit:cover;border-radius:16px;">
   ```
   y quita la etiqueta `badge mock`.
4. Vuelve a exportar el PDF.

> Mientras tanto, el mockup comunica bien el concepto para revisar la propuesta.

## Llevarlo a Canva (flujo del estudio)
El `deck.pdf` se puede **importar a Canva** como base y volver editable con el Brand Kit de
Medusa OS cuando exista (colores/tipografías provisionales en `../../panel-promocional.md`).

## Pendientes de negocio (para cerrar contigo)
Ver **[POR CONFIRMAR]** en `../../panel-promocional.md`: duración de la beta, cupos por
categoría, superficie real del panel, CTA de registro y grafía oficial de la marca.
