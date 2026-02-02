from fontTools.ttLib import TTFont
from fontTools.pens.transformPen import TransformPen
from fontTools.pens.ttGlyphPen import TTGlyphPen

import sys
import copy

# -------- CONFIG (LOCKED) --------
BASE_FONT_PATH = "../fonts/base.ttf"
OUTPUT_FONT_PATH = "../output/stego_font.ttf"
TARGET_CHAR = "क"        # U+0915
BIT_TO_ENCODE = "1"      # CHANGE TO "0" OR "1" ONLY
# --------------------------------

def encode_one_bit(bit):
    font = TTFont(BASE_FONT_PATH)

    cmap = font["cmap"].getBestCmap()
    glyph_name = cmap[ord(TARGET_CHAR)]

    glyf = font["glyf"]
    base_glyph = glyf[glyph_name]

    if bit == "0":
        # Bit 0 → keep original glyph
        font.save(OUTPUT_FONT_PATH)
        print("Encoded bit 0 (original glyph)")
        return

    # Bit 1 → create glyph variant
    pen = TTGlyphPen(font.getGlyphSet())
    transform_pen = TransformPen(pen, (1, 0, 0, 1, 1, 0))  # ε shift (x + 1 unit)
    base_glyph.draw(transform_pen, glyf)
    new_glyph = pen.glyph()

    variant_glyph_name = glyph_name + "_variant"
    glyf[variant_glyph_name] = new_glyph

    # Copy metrics
    font["hmtx"][variant_glyph_name] = font["hmtx"][glyph_name]

    # Replace cmap mapping
    for table in font["cmap"].tables:
        if ord(TARGET_CHAR) in table.cmap:
            table.cmap[ord(TARGET_CHAR)] = variant_glyph_name

    font.save(OUTPUT_FONT_PATH)
    print("Encoded bit 1 (variant glyph)")

if __name__ == "__main__":
    encode_one_bit(BIT_TO_ENCODE)
