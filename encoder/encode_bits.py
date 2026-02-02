from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

# -------- CONFIG (LOCKED) --------
BASE_FONT_PATH = "../fonts/base.ttf"
OUTPUT_FONT_PATH = "../output/stego_font.ttf"

GLYPHS = ["क", "ख", "ग", "घ"]
BITSTREAM = "1010"   # Must match length of GLYPHS
# --------------------------------

def encode_bits():
    font = TTFont(BASE_FONT_PATH)
    cmap = font["cmap"].getBestCmap()
    glyf = font["glyf"]

    for char, bit in zip(GLYPHS, BITSTREAM):
        glyph_name = cmap[ord(char)]

        if bit == "0":
            # Keep original glyph
            continue

        # Create variant glyph
        base_glyph = glyf[glyph_name]

        pen = TTGlyphPen(font.getGlyphSet())
        transform_pen = TransformPen(pen, (1, 0, 0, 1, 1, 0))  # ε = +1 unit x-shift
        base_glyph.draw(transform_pen, glyf)
        variant_glyph = pen.glyph()

        variant_name = glyph_name + "_variant"
        glyf[variant_name] = variant_glyph
        font["hmtx"][variant_name] = font["hmtx"][glyph_name]

        # Update cmap mapping
        for table in font["cmap"].tables:
            if ord(char) in table.cmap:
                table.cmap[ord(char)] = variant_name

    font.save(OUTPUT_FONT_PATH)
    print("Phase 2 encoding complete. Bitstream:", BITSTREAM)

if __name__ == "__main__":
    encode_bits()
