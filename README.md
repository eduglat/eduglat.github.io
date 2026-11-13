# eduglat.github.io

Web de todos los proyectos de Eduglat, publicada con GitHub Pages en **https://eduglat.github.io/**.

## Estructura

| Carpeta | Dirección | Qué es |
|---|---|---|
| `/` (`index.html`) | https://eduglat.github.io/ | Portada de Eduglat con sus proyectos |
| `lectio/` | https://eduglat.github.io/lectio/ | Página de LECTIO |
| `lectio-privacidad/` | https://eduglat.github.io/lectio-privacidad/ | Política de privacidad y `terminos.html` de LECTIO |
| `lectio-prueba/` | https://eduglat.github.io/lectio-prueba/ | Instrucciones para los testers (con `noindex`) |
| `img/` | | Imágenes de la portada |

**No cambiar de lugar `lectio-privacidad/` ni `lectio-prueba/`:** esas direcciones están dentro de la app publicada y en Play Console.

**Cada proyecto nuevo** tiene su propio repositorio en `eduglat/<proyecto>` y su carpeta aquí (`/<proyecto>/`). También se agrega su tarjeta en la portada.

`.nojekyll` evita que GitHub procese los archivos: se publican tal cual.

## Imágenes de la portada

Los originales de Gemini van en `_originales/`, que no se sube a GitHub. Se procesan a WebP en `img/`:

| Archivo | Uso | Tamaño final |
|---|---|---|
| `img/eduglat-logo.webp` | Isotipo junto al nombre | 256 × 256, fondo transparente |
| `img/favicon-32.png`, `img/favicon-192.png` | Ícono de la pestaña y del celular | Se sacan del isotipo |
| `img/portada.webp` | Ilustración principal | 1200 × 675 |
| `img/proximamente.webp` | Tarjeta «Nuevos proyectos» | 256 × 256 |

Mientras falte una imagen, la página se ve completa sin ella.

### Prompt maestro (pégalo al empezar la conversación con Gemini)

> Eres ilustrador editorial. Vas a crear una serie de imágenes para la web de Eduglat, un estudio que crea aplicaciones educativas basadas en la ciencia del aprendizaje. **Estilo para toda la serie:** ilustración plana y cálida con textura suave de acuarela, contornos finos y redondeados, formas simples y amables; aspecto cuidado y adulto, no infantil. **Paleta:** verde mar profundo (#2E6B63), verde mar claro (#DCEBE7), coral suave (#D9704F), arena (#F7F3EC) y toques de marrón tierra. Luz suave, sin sombras duras. **Reglas estrictas:** sin texto, letras, números ni logotipos; nada realista ni fotográfico. Responde solo con la imagen. Confirma con «Entendido» y espera mi primera petición.

### Prompts por imagen

1. **`eduglat-logo`**: *Diseña un isotipo simple para la marca Eduglat: un libro abierto visto de frente cuyas páginas se curvan formando las capas de una montaña, y una pequeña planta con dos hojas que brota en la cima. Solo dos colores: verde mar profundo y coral suave. Formas planas y geométricas, sin textura, que se entiendan incluso a 32 píxeles. Centrado, ocupando el 70 % del cuadro, sobre fondo blanco liso. Formato cuadrado 1:1.*
2. **`portada`**: *Ilustra una escena tranquila de aprendizaje: una niña y una persona adulta sentadas en el suelo, de perfil, mirando juntas un libro abierto. A su alrededor, algunos objetos que sugieren curiosidad y ciencia: una lupa sobre una piedra con capas de colores, una planta que crece en una maceta, unas hojas y pequeñas estrellas. Fondo arena liso con una forma orgánica verde mar claro detrás de los personajes. Composición horizontal 16:9 con los personajes un poco a la derecha.*
3. **`proximamente`**: *Dibuja una semilla en la tierra de la que sale un brote pequeño, con una brújula diminuta y una hoja al lado, como símbolo de algo nuevo que está creciendo. Centrado, ocupando el 70 % del cuadro, sobre fondo arena liso (#F7F3EC). Formato cuadrado 1:1.*

Guárdalas en `_originales/` con esos nombres (`eduglat-logo.png`, `portada.png`, `proximamente.png`).
