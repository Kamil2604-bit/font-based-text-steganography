from fontTools.ttLib import TTFont

# -------- CONFIG (LOCKED) --------
STEGO_FONT_PATH = "../output/stego_font.ttf"
CUSTOM_NAME_ID = 255
MESSAGE_LENGTH = 2  # "OK"
# --------------------------------

def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits), 8):
        chars.append(chr(int(bits[i:i+8], 2)))
    return ''.join(chars)

def decode_message():
    font = TTFont(STEGO_FONT_PATH)
    name_table = font["name"]

    record = name_table.getName(
        CUSTOM_NAME_ID,
        platformID=3,
        platEncID=1,
        langID=0x409
    )

    bits = str(record)
    bits = bits[:MESSAGE_LENGTH * 8]

    message = bits_to_text(bits)
    print("Decoded message:", message)

if __name__ == "__main__":
    decode_message()

