"""Genereert logo's, favicon, OG-afbeelding en tijdelijke productafbeeldingen.

Gebruik: pip install fonttools pillow && python3 scripts/generate-assets.py
De productafbeeldingen zijn plaatshouders: overschrijf ze met echte foto's
(zelfde bestandsnaam, liefst 1200x800 of groter, verhouding 3:2).
"""
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
IMG = ROOT / "images"
FONT = "/usr/share/fonts/opentype/inter/InterDisplay-BlackItalic.otf"

YELLOW = "#ffdd00"
ASPHALT = "#2b2b2a"
SLATE = "#5d5d5c"
MIST = "#f3f3f1"


def text_path(font, text, size, x, y):
    """SVG-pad voor `text` met de baseline op (x, y). Geeft (pad, breedte)."""
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    pen = SVGPathPen(glyphs)
    cursor = 0
    for ch in text:
        name = cmap[ord(ch)]
        tpen = TransformPen(pen, (scale, 0, 0, -scale, x + cursor * scale, y))
        glyphs[name].draw(tpen)
        cursor += glyphs[name].width
    return pen.getCommands(), cursor * scale


def text_bounds(font, text, size):
    glyphs = font.getGlyphSet()
    cmap = font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    bp = BoundsPen(glyphs)
    cursor = 0
    for ch in text:
        name = cmap[ord(ch)]
        glyphs[name].draw(TransformPen(bp, (scale, 0, 0, scale, cursor * scale, 0)))
        cursor += glyphs[name].width
    return bp.bounds  # xmin, ymin, xmax, ymax (y omhoog)


def logo_svg(font, word_color):
    size = 30
    pad_x = 10
    b_slim = text_bounds(font, "SLIM", size)
    cap_h = b_slim[3]
    block_h = 44
    baseline = (block_h + cap_h) / 2
    slim_path, slim_w = text_path(font, "SLIM", size, pad_x, baseline)
    block_w = slim_w + pad_x * 2
    mob_path, mob_w = text_path(font, "MOBIEL", size, block_w + 8, baseline)
    width = round(block_w + 8 + mob_w + 2)
    # Schuin gele blok: verwijst naar beweging en de gele menubalk van het origineel.
    skew = 6
    block = f"M{skew},0H{block_w:.1f}L{block_w - skew:.1f},{block_h}H0Z"
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {block_h}" '
        f'width="{width * 5}" height="{block_h * 5}" role="img" aria-label="Slim-Mobiel">'
        f'<path fill="{YELLOW}" d="{block}"/>'
        f'<path fill="{ASPHALT}" d="{slim_path}"/>'
        f'<path fill="{word_color}" d="{mob_path}"/>'
        f"</svg>\n"
    ), width, block_h


def favicon_svg(font):
    path, w = text_path(font, "S", 46, 0, 0)
    b = text_bounds(font, "S", 46)
    dx = (64 - (b[2] - b[0])) / 2 - b[0]
    dy = (64 + (b[3] - b[1])) / 2 + b[1]
    path, _ = text_path(font, "S", 46, dx, dy)
    return (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64">'
        f'<rect width="64" height="64" rx="12" fill="{YELLOW}"/>'
        f'<path fill="{ASPHALT}" d="{path}"/></svg>\n'
    )


def pil_font(size):
    return ImageFont.truetype(FONT, size)


def draw_wheel(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=ASPHALT)
    d.ellipse([cx - r * .45, cy - r * .45, cx + r * .45, cy + r * .45], fill="#bdbdb8")


def vehicle(d, kind, ox, oy, s):
    """Eenvoudige zijaanzichten, puur als plaatshouder."""
    def p(x, y):
        return (ox + x * s, oy + y * s)

    if kind == "b8":
        d.rounded_rectangle([p(0, 120), p(520, 230)], radius=40 * s, fill=YELLOW)
        d.polygon([p(110, 125), p(175, 30), p(370, 30), p(450, 125)], fill=YELLOW)
        d.polygon([p(140, 120), p(190, 50), p(268, 50), p(268, 120)], fill="#9fb7c4")
        d.polygon([p(285, 120), p(285, 50), p(360, 50), p(420, 120)], fill="#9fb7c4")
        d.rectangle([p(0, 200), p(520, 212)], fill="#e2c400")
        draw_wheel(d, *p(115, 232), 46 * s)
        draw_wheel(d, *p(410, 232), 46 * s)
    elif kind == "docker":
        d.rounded_rectangle([p(0, 40), p(190, 220)], radius=24 * s, fill="#ffffff", outline=ASPHALT, width=int(4 * s))
        d.rounded_rectangle([p(30, 60), p(170, 130)], radius=10 * s, fill="#9fb7c4")
        d.rectangle([p(200, 110), p(500, 210)], fill=SLATE)
        d.rectangle([p(200, 100), p(500, 116)], fill=ASPHALT)
        d.rectangle([p(0, 190), p(500, 220)], fill=ASPHALT)
        draw_wheel(d, *p(95, 228), 40 * s)
        draw_wheel(d, *p(400, 228), 40 * s)
    else:  # kimsi
        d.rounded_rectangle([p(40, 20), p(420, 220)], radius=60 * s, fill="#ffffff", outline=ASPHALT, width=int(4 * s))
        d.rounded_rectangle([p(90, 50), p(300, 130)], radius=16 * s, fill="#9fb7c4")
        d.polygon([p(420, 120), p(520, 230), p(420, 230)], fill=YELLOW)
        d.rectangle([p(40, 196), p(420, 206)], fill=YELLOW)
        draw_wheel(d, *p(130, 228), 40 * s)
        draw_wheel(d, *p(350, 228), 40 * s)


def placeholder(name, kind, label, size=(1200, 800)):
    w, h = size
    im = Image.new("RGB", size, MIST)
    d = ImageDraw.Draw(im)
    d.rectangle([0, h * .78, w, h], fill="#e6e6e2")
    s = w / 1200 * 1.25
    vehicle(d, kind, (w - 520 * s) / 2, h * .78 - 270 * s, s)
    f = pil_font(int(w * .03))
    d.text((w * .04, h * .05), label, font=f, fill=ASPHALT)
    small = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", int(w * .016))
    d.text((w * .04, h * .92), f"Plaatshouder: vervang door een foto met de naam {name}", font=small, fill=SLATE)
    im.save(IMG / name, quality=86, optimize=True, progressive=True)


def og_image():
    im = Image.new("RGB", (1200, 630), YELLOW)
    d = ImageDraw.Draw(im)
    d.rectangle([0, 560, 1200, 630], fill=ASPHALT)
    for x in range(0, 1200, 112):
        d.rectangle([x, 593, x + 56, 597], fill="#f5f5f0")
    d.text((72, 90), "Slim-Mobiel", font=pil_font(56), fill=ASPHALT)
    d.text((72, 190), "Bellier & Ellectra", font=pil_font(96), fill=ASPHALT)
    d.text((72, 300), "brommobielen", font=pil_font(96), fill=ASPHALT)
    body = ImageFont.truetype("/usr/share/fonts/opentype/inter/Inter-SemiBold.otf", 34)
    d.text((72, 440), "Importeur voor Nederland en België. Rijden vanaf 16 jaar.", font=body, fill=ASPHALT)
    im.save(IMG / "og-image.jpg", quality=88, optimize=True)


def apple_icon():
    im = Image.new("RGB", (180, 180), YELLOW)
    d = ImageDraw.Draw(im)
    f = pil_font(130)
    bbox = d.textbbox((0, 0), "S", font=f)
    d.text(((180 - (bbox[2] - bbox[0])) / 2 - bbox[0], (180 - (bbox[3] - bbox[1])) / 2 - bbox[1]), "S", font=f, fill=ASPHALT)
    im.save(IMG / "apple-touch-icon.png")
    big = im.resize((512, 512), Image.LANCZOS)
    big.save(IMG / "icon-512.png")


def logo_png(width, height):
    """PNG-versie van het logo voor schema.org en e-mail."""
    scale = 6
    im = Image.new("RGBA", (width * scale, height * scale), (255, 255, 255, 0))
    d = ImageDraw.Draw(im)
    f = pil_font(30 * scale)
    slim_w = d.textlength("SLIM", font=f)
    block_w = slim_w + 20 * scale
    sk = 6 * scale
    d.polygon([(sk, 0), (block_w, 0), (block_w - sk, height * scale), (0, height * scale)], fill=YELLOW)
    bbox = d.textbbox((0, 0), "SLIM", font=f)
    ty = (height * scale - (bbox[3] - bbox[1])) / 2 - bbox[1]
    d.text((10 * scale, ty), "SLIM", font=f, fill=ASPHALT)
    d.text((block_w + 8 * scale, ty), "MOBIEL", font=f, fill=ASPHALT)
    im = im.resize((width * 2, height * 2), Image.LANCZOS)
    im.save(IMG / "logo-slim-mobiel.png", optimize=True)


def main():
    IMG.mkdir(exist_ok=True)
    font = TTFont(FONT)
    svg, w, h = logo_svg(font, ASPHALT)
    (IMG / "logo-slim-mobiel.svg").write_text(svg)
    svg_inv, _, _ = logo_svg(font, "#ffffff")
    (IMG / "logo-slim-mobiel-inverse.svg").write_text(svg_inv)
    (ROOT / "favicon.svg").write_text(favicon_svg(font))
    logo_png(w, h)
    placeholder("hero-bellier-b8.jpg", "b8", "Bellier B8")
    placeholder("bellier-b8.jpg", "b8", "Bellier B8")
    placeholder("bellier-docker.jpg", "docker", "Bellier Docker")
    placeholder("ellectra-kimsi.jpg", "kimsi", "Ellectra Kimsi")
    og_image()
    apple_icon()
    print(f"Logo {w}x{h}, afbeeldingen geschreven naar {IMG}")


if __name__ == "__main__":
    main()
