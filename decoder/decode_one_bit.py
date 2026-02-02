from fontTools.ttLib import TTFont

# -------- CONFIG (LOCKED) --------
STEGO_FONT_PATH = "../output/stego_font.ttf"
TARGET_CHAR = "क"   # U+0915
# --------------------------------

def decode_one_bit():
    font = TTFont(STEGO_FONT_PATH)
    cmap = font["cmap"].getBestCmap()

    glyph_name = cmap[ord(TARGET_CHAR)]

    if glyph_name.endswith("_variant"):
        print("Decoded bit: 1")
    else:
        print("Decoded bit: 0")

if __name__ == "__main__":
    decode_one_bit()
