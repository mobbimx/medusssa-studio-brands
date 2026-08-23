# -*- coding: utf-8 -*-
"""Renderiza HTML de 1080x1920 a PNG sin la franja de recorte del viewport.
Chrome recorta lo que cae bajo el viewport cuando html/body llevan overflow:hidden,
asi que se renderiza con ventana alta y se recorta con Pillow."""
import os, subprocess, sys
from PIL import Image
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"
TALL = 2600

def render(html, out, w=1080, h=1920, transparent=False, trim=False):
    tmp = out + ".tmp.png"
    cmd = [CHROME, "--headless", "--no-sandbox", "--disable-gpu", "--hide-scrollbars",
           "--force-device-scale-factor=1", "--virtual-time-budget=5000",
           "--window-size=%d,%d" % (w, TALL), "--screenshot=" + tmp, html]
    if transparent:
        cmd.insert(-2, "--default-background-color=00000000")
    subprocess.run(cmd, capture_output=True)
    im = Image.open(tmp).convert("RGBA")
    im = im.crop(im.getbbox()) if trim else im.crop((0, 0, w, h))
    im.save(out)
    os.remove(tmp)
    return im.size

def check(path, w=1080, h=1920):
    """Devuelve la primera fila de una banda plana final, o None si esta limpio."""
    im = Image.open(path).convert("RGB")
    flat = None
    for y in range(int(h*0.55), h):
        row = set(im.getpixel((x, y)) for x in range(0, w, 40))
        if len(row) == 1:
            if flat is None: flat = y
        else:
            flat = None
    return flat

if __name__ == "__main__":
    for d, out in [("/home/user/medusssa-studio-brands/peachystudio/plantillas/html",
                    "/home/user/medusssa-studio-brands/peachystudio/plantillas/png"),
                   ("/home/user/medusssa-studio-brands/peachystudio/plantillas/seleccion",
                    "/home/user/medusssa-studio-brands/peachystudio/plantillas/seleccion/png")]:
        os.chdir(d)
        for f in sorted(x for x in os.listdir(".") if x.endswith(".html")):
            render(f, os.path.join(out, f[:-5] + ".png"))
        print(d.split("/")[-1], "->", len([x for x in os.listdir(out) if x.endswith(".png")]), "PNG")
