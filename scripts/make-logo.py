"""Tekent het Slim-Mobiel logo na als SVG (vectorpaden, dus scherp op elk scherm).

Gebruik: pip install fonttools brotli
         python3 scripts/make-logo.py <Marcellus.woff2> <Barlow-500.woff2>
Marcellus (SIL OFL) benadert de schreefletter van het originele logo; door een
lijn in dezelfde kleur eromheen wordt hij net zo vet als het origineel.
"""
import sys
from pathlib import Path

from fontTools.pens.boundsPen import BoundsPen
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

ROOT = Path(__file__).resolve().parent.parent
YELLOW = "#ffe000"


def layout(font, text, size, tracking=0.0):
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    scale = size / font["head"].unitsPerEm
    out, x = [], 0.0
    for ch in text:
        g = gs[cmap[ord(ch)]]
        out.append((g, x))
        x += g.width * scale + tracking
    return out, x - tracking, scale


def path(font, text, size, ox, oy, tracking=0.0):
    glyphs, width, scale = layout(font, text, size, tracking)
    pen = SVGPathPen(font.getGlyphSet())
    for g, x in glyphs:
        g.draw(TransformPen(pen, (scale, 0, 0, -scale, ox + x, oy)))
    return pen.getCommands(), width


def cap_height(font, size):
    gs, cmap = font.getGlyphSet(), font.getBestCmap()
    bp = BoundsPen(gs)
    gs[cmap[ord("H")]].draw(bp)
    return bp.bounds[3] * size / font["head"].unitsPerEm


def build(title_font, sub_font, sub_color, outline):
    size, embolden = 46, 2.4
    pad = 3
    top = cap_height(title_font, size)
    title_d, title_w = path(title_font, "SLIM - MOBIEL B.V.", size, pad, pad + top)
    sub_size = 13.2
    left = "IMPORTEUR BROMMOBIELEN"
    right = "PERSONEN EN TRANSPORTERS"
    _, lw, _ = layout(sub_font, left, sub_size, 0.6)
    _, rw, _ = layout(sub_font, right, sub_size, 0.6)
    gap = title_w - lw - rw
    sub_y = pad + top + 8 + cap_height(sub_font, sub_size) + 6
    l_d, _ = path(sub_font, left, sub_size, pad + 1, sub_y, 0.6)
    r_d, _ = path(sub_font, right, sub_size, pad + 1 + lw + gap, sub_y, 0.6)
    w, h = round(title_w + pad * 2 + 2), round(sub_y + 4)
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w * 4}" height="{h * 4}" '
        f'role="img" aria-label="Slim-Mobiel B.V., importeur brommobielen, personen en transporters">'
        f'<path d="{title_d}" fill="{outline}" stroke="{outline}" stroke-width="{embolden + 1.1}" stroke-linejoin="round"/>'
        f'<path d="{title_d}" fill="{YELLOW}" stroke="{YELLOW}" stroke-width="{embolden}" stroke-linejoin="round"/>'
        f'<path d="{l_d} {r_d}" fill="{sub_color}"/></svg>\n'
    ), w, h


def main():
    title_font, sub_font = TTFont(sys.argv[1]), TTFont(sys.argv[2])
    svg, w, h = build(title_font, sub_font, "#616161", "#9a9a9a")
    (ROOT / "images" / "logo-slim-mobiel.svg").write_text(svg)
    svg, _, _ = build(title_font, sub_font, "#d6d6d2", "#3a3a3a")
    (ROOT / "images" / "logo-slim-mobiel-inverse.svg").write_text(svg)
    print(f"logo {w}x{h}")


if __name__ == "__main__":
    main()
