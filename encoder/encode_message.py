from fontTools.ttLib import TTFont

# -------- CONFIG (LOCKED) --------
BASE_FONT_PATH = "../fonts/base.ttf"
OUTPUT_FONT_PATH = "../output/stego_font.ttf"
SECRET_MESSAGE = "OK"
CUSTOM_NAME_ID = 255  # safe private range
# --------------------------------

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def encode_message():
    bits = text_to_bits(SECRET_MESSAGE)

    font = TTFont(BASE_FONT_PATH)
    name_table = font["name"]

    # Store bitstream in custom name record
    name_table.setName(
        bits,
        CUSTOM_NAME_ID,
        platformID=3,
        platEncID=1,
        langID=0x409
    )

    font.save(OUTPUT_FONT_PATH)
    print("Phase 3 encoding complete. Secret message:", SECRET_MESSAGE)

if __name__ == "__main__":
    encode_message()

