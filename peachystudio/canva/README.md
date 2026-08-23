# Peachy Studio — Plantillas editables en Canva

Las 6 plantillas maestras ya existen en Canva como un diseño de **6 páginas, 1080 × 1920 px**.

| | |
|---|---|
| **Diseño** | [Peachy Studio · Plantillas de historia](https://www.canva.com/d/QeVZFGdnbw4dmRS) |
| **Solo lectura** | https://www.canva.com/d/Mdw1WNPJDD27jye |
| **Carpeta** | [PEACHY STUDIO — Plantillas maestras](https://www.canva.com/folder/FAHTJE4UmQU) |
| **ID del diseño** | `DAHTJF9Edf8` |

| Página | Plantilla |
|--------|-----------|
| 1 | S1 · Calendario del mes |
| 2 | S2 · Citas disponibles |
| 3 | S3 · Lista de precios |
| 4 | S4 · Información del studio |
| 5 | S5 · Diseño del día |
| 6 | S6 · Aviso o promoción |

Todo el texto entró como **texto editable** de Canva y las píldoras, tarjetas y marcos
como **formas editables**. Los fondos, el logotipo y los adornos son imágenes de
`assets/`, servidas desde este mismo repositorio.

## Cómo se generó

`plantillas-peachy-canva.html` es un HTML con seis páginas anotadas
(`data-document-role="page"` y `data-label`), cada una de 1080 × 1920 px y con todos
los elementos posicionados en absoluto. Canva lo importa y lo convierte en un diseño
nativo. Para regenerarlo:

```bash
python3 canva.py "https://raw.githubusercontent.com/mobbimx/medusssa-studio-brands/<sha>/peachystudio/canva/assets/"
```

y después importarlo desde la URL pública del HTML.

> Los recursos se referencian por **SHA del commit**, no por rama, para que el diseño
> importado no cambie si el repositorio se mueve.

## Recursos (`assets/`)

| Archivo | Uso |
|---------|-----|
| `bg-checker.png` | Cuadrícula lila — S1, S4, S5 |
| `bg-checker-wave.png` | Cuadrícula ondulada — S3 |
| `bg-swirl-rosa.png` | Espiral rosa — S6 |
| `logo-wordmark.png` | Logotipo (reconstrucción) |
| `deco-smiley.png` · `deco-daisy.png` · `deco-heart.png` · `deco-spark.png` | Adornos de marca |

## Qué falta hacer dentro de Canva

1. **Cambiar el logotipo** por el archivo real del Brand Kit. El de las maquetas es una
   reconstrucción tipográfica, no el original.
2. **Revisar las tres fuentes de marca.** Al importar, Canva sustituye por las más
   parecidas; hay que asignar Retro Vintage, Adam Script y Retropix donde corresponda.
3. **Bloquear** (candado) fondo, logotipo y pie de contacto para que no se muevan al editar.
4. **Nombrar las capas de texto** con el campo que representan (`TITULAR`, `PRECIO`, `FECHA`…).
5. **Publicar como plantilla de marca** — menú del diseño → *Publicar como plantilla de marca*.
   (Por API no se pudo: el conector no tiene el permiso `brandtemplate:content:write`.)
6. **Sustituir el marco de foto de S5** por la foto real; el círculo punteado es solo el hueco.

## Nota sobre el render de los PNG

Chrome recorta lo que queda por debajo del viewport cuando `html`/`body` llevan
`overflow:hidden`, y eso dejaba una franja del color de fondo al pie de cada pieza.
Los PNG se generan con ventana alta y recorte posterior — ver `render.py` en la raíz de
`plantillas/`.
