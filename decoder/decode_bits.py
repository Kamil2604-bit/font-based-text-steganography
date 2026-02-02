from fontTools.ttLib import TTFont

# -------- CONFIG (LOCKED) --------
STEGO_FONT_PATH = "../output/stego_font.ttf"
GLYPHS = ["क", "ख", "ग", "घ"]
# --------------------------------

def decode_bits():
    font = TTFont(STEGO_FONT_PATH)
    cmap = font["cmap"].getBestCmap()

    bits = ""

    for char in GLYPHS:
        glyph_name = cmap[ord(char)]
        if glyph_name.endswith("_variant"):
            bits += "1"
        else:
            bits += "0"

    print("Decoded bitstream:", bits)

if __name__ == "__main__":
    decode_bits()
