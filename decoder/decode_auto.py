from fontTools.ttLib import TTFont
import os

# -------- CONFIG (LOCKED) --------
CUSTOM_NAME_ID = 255
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

STEGO_FONT_PATH = os.path.join(PROJECT_DIR, "output", "stego_font.ttf")

def bits_to_text(bits):
    chars = []
    for i in range(0, len(bits), 8):
        chars.append(chr(int(bits[i:i+8], 2)))
    return ''.join(chars)

def decode_auto(font_path=None):
    path = font_path if font_path else STEGO_FONT_PATH

    font = TTFont(path)
    name_table = font["name"]

    record = name_table.getName(
        CUSTOM_NAME_ID,
        platformID=3,
        platEncID=1,
        langID=0x409
    )

    bitstream = str(record)

    length_bits = bitstream[:16]
    message_length = int(length_bits, 2)

    message_bits = bitstream[16:16 + message_length * 8]
    message = bits_to_text(message_bits)

    return message

if __name__ == "__main__":
    recovered = decode_auto()
    print("Automation decoding complete.")
    print("Recovered secret text:", recovered)