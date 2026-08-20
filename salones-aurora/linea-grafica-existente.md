# Aurora Salones — Análisis del contenido ya producido

Inventario y lectura de lo que ya existe en Drive
(*salones-aurora / CONTENIDO SALONES AURORA*), que es la base sobre la que se
construyeron las plantillas de `plantillas/`.

## Qué hay publicado

Cuatro piezas, todas en **1080 × 1350 px (4:5)**, numeradas con un esquema `PXX`
que sugiere un plan mayor de ~20 posts:

| Pieza | Formato | Contenido | Estructura |
|-------|---------|-----------|------------|
| **P02** | Carrusel de 7 | Cuenta regresiva para apartar: 6, 4, 3, 2 y 1 mes | portada + 5 pasos + cierre |
| **P08** | Post suelto | Testimonio de Greta del Valle | cita + estrellas + polaroid + barra sólida |
| **P14** | Carrusel de 7 | "Un salón, mil estilos": boda, XV, mexicana, infantil, dulces | portada + 5 estilos + cierre |
| **P19** | Carrusel de 5 | "¿Cómo se aparta una fecha en Aurora?" paso a paso | portada + 3 pasos + cierre |

También hay en Drive: fotos por tipo de evento (XV años, bodas, cumpleaños,
banquetes, salón vacío, mobiliario) y un video de dron.

## Cómo está construida la línea

**Estructura fija de toda pieza**, de arriba abajo:

1. Logo centrado (badge blanco si el fondo es foto)
2. Eyebrow en Playfair mayúsculas espaciadas, vino
3. Titular en Playfair Bold
4. Apoyo: subtítulo en itálica, párrafo Poppins, lista numerada o chips
5. Foto en polaroid girado (en piezas crema)
6. Puntos de carrusel
7. Barra de contacto: hairline (carruseles) o bloque sólido café (posts sueltos)

**Dos modos de fondo:** crema con curvas de nivel, o foto con velo cálido.
El detalle completo de paleta, tipografías y retícula está en `visual.md`.

## Lo que funciona y hay que conservar

- **La trama de curvas de nivel.** Es lo más distintivo del fondo crema; sin ella
  la pieza se ve genérica.
- **El polaroid girado.** Resuelve el problema de que las fotos del salón son de
  celular y de calidad desigual: el marco las vuelve un recurso de diseño.
- **La barra de contacto siempre presente.** WhatsApp y dirección en cada pieza.
- **Los carruseles educativos** (P02, P19). Son contenido de guardado alto y
  encajan perfecto con el arquetipo de El Cuidador.
- **El testimonio con estrellas** (P08). Es la pieza de mayor prueba social.

## Lo que conviene corregir

- **Fotografía.** Todo el material disponible es de teléfono, con montajes
  navideños y bastante desorden de fondo (cajas, mochilas, objetos fuera de
  lugar). Una sesión propia del salón —vacío y montado, sin temporada marcada—
  es la mejor inversión de la marca ahora mismo.
- **Falta el logo vectorial.** Todo se está armando con un PNG de baja resolución.
- **Dos números de WhatsApp.** El repo tenía el 228 113 3683; todas las piezas
  publicadas usan el **228 298 4871**. Se adoptó el de las piezas.
- **No hay formato de historia (9:16).** Toda la producción es de feed.
- **Faltan formatos de conversión directa**: disponibilidad del mes, capacidad,
  qué incluye el paquete. Ese hueco es el que cubren las plantillas nuevas.

## Qué se hizo con esto

Se reconstruyó el sistema completo en `visual.md` y se produjeron **8 plantillas
nuevas** (`plantillas/`) que siguen la línea al pie de la letra y cubren los
formatos que faltaban.
