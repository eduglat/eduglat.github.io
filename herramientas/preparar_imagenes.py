"""
Prepara las imágenes de la portada de Eduglat a partir de los originales de Gemini (carpeta _originales/,
que no se sube a GitHub) y las deja en img/.

  eduglat-logo -> img/eduglat-logo.webp (256 px, fondo transparente, recortado al dibujo)
                  img/favicon-32.png y img/favicon-192.png
  portada      -> img/portada.webp (1200 x 675)
  proximamente -> img/proximamente.webp (256 x 256)

Uso:  python herramientas/preparar_imagenes.py      (necesita Pillow y numpy)
"""
import glob
import os

import numpy as np
from PIL import Image

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ORIGEN = os.path.join(RAIZ, '_originales')
DESTINO = os.path.join(RAIZ, 'img')


def original(nombre):
    archivos = [f for f in glob.glob(os.path.join(ORIGEN, nombre + '.*'))
                if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp'))]
    return max(archivos, key=os.path.getmtime) if archivos else None


def sin_fondo_blanco(img):
    """El blanco (y la textura casi blanca que deja Gemini) se vuelve transparente, con borde suave."""
    rgb = np.asarray(img.convert('RGB')).astype(np.float32)
    minimo = rgb.min(axis=2)
    alfa = np.clip((250.0 - minimo) / 40.0, 0.0, 1.0)
    # Quita el blanco mezclado en los bordes para que no quede un halo claro sobre fondos oscuros
    a = np.maximum(alfa, 1e-3)[..., None]
    color = np.clip((rgb - 255.0 * (1 - a)) / a, 0, 255)
    rgba = np.dstack([color, alfa * 255]).astype(np.uint8)
    return Image.fromarray(rgba, 'RGBA')


def recortar_cuadrado(img, margen=0.06):
    caja = img.getchannel('A').point(lambda v: 255 if v > 20 else 0).getbbox()
    img = img.crop(caja)
    lado = int(max(img.size) * (1 + 2 * margen))
    lienzo = Image.new('RGBA', (lado, lado), (0, 0, 0, 0))
    lienzo.paste(img, ((lado - img.width) // 2, (lado - img.height) // 2), img)
    return lienzo


def cubrir(img, ancho, alto):
    """Escala y recorta al centro para llenar ancho x alto."""
    escala = max(ancho / img.width, alto / img.height)
    img = img.resize((round(img.width * escala), round(img.height * escala)), Image.LANCZOS)
    x, y = (img.width - ancho) // 2, (img.height - alto) // 2
    return img.crop((x, y, x + ancho, y + alto))


def guardar(img, nombre, **opciones):
    ruta = os.path.join(DESTINO, nombre)
    img.save(ruta, **opciones)
    print(f'{nombre:20s} {img.size[0]}x{img.size[1]}  {os.path.getsize(ruta) // 1024} KB')


def main():
    os.makedirs(DESTINO, exist_ok=True)

    logo = original('eduglat-logo')
    if logo:
        marca = recortar_cuadrado(sin_fondo_blanco(Image.open(logo)))
        guardar(marca.resize((256, 256), Image.LANCZOS), 'eduglat-logo.webp', quality=90, method=6)
        guardar(marca.resize((192, 192), Image.LANCZOS), 'favicon-192.png', optimize=True)
        guardar(recortar_cuadrado(marca, 0).resize((32, 32), Image.LANCZOS), 'favicon-32.png', optimize=True)

    portada = original('portada')
    if portada:
        guardar(cubrir(Image.open(portada).convert('RGB'), 1200, 675), 'portada.webp', quality=82, method=6)

    pronto = original('proximamente')
    if pronto:
        guardar(cubrir(Image.open(pronto).convert('RGB'), 256, 256), 'proximamente.webp', quality=85, method=6)

    faltan = [n for n in ('eduglat-logo', 'portada', 'proximamente') if not original(n)]
    if faltan:
        print('Sin original (la página se ve igual, sin esa imagen):', ', '.join(faltan))


if __name__ == '__main__':
    main()
