from fontTools.ttLib import TTFont
import os
import sys

# -------- CONFIG (LOCKED) --------
CUSTOM_NAME_ID = 255
# --------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIR = os.path.dirname(BASE_DIR)

BASE_FONT_PATH = os.path.join(PROJECT_DIR, "fonts", "base.ttf")
OUTPUT_FONT_PATH = os.path.join(PROJECT_DIR, "output", "stego_font.ttf")

def text_to_bits(text):
    return ''.join(format(ord(c), '08b') for c in text)

def int_to_16bit(n):
    return format(n, '016b')

def encode_auto(secret_text):
    message_bits = text_to_bits(secret_text)
    length_bits = int_to_16bit(len(secret_text))
    framed_bits = length_bits + message_bits

    font = TTFont(BASE_FONT_PATH)
    name_table = font["name"]

    name_table.setName(
        framed_bits,
        CUSTOM_NAME_ID,
        platformID=3,
        platEncID=1,
        langID=0x409
    )

    font.save(OUTPUT_FONT_PATH)

    print("\n✅ Encoding successful.")
    print("Characters encoded:", len(secret_text))
    print("Stego font saved to output/ directory.")

def load_secret_from_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read().strip()
            if not content:
                raise ValueError("File is empty.")
            return content
    except FileNotFoundError:
        print("❌ Error: File not found.")
    except UnicodeDecodeError:
        print("❌ Error: File must be UTF-8 encoded.")
    except Exception as e:
        print("❌ Error:", e)
    return None

def show_menu():
    print("\n===================================")
    print(" FONT STEGANOGRAPHY – ENCODER MENU ")
    print("===================================")
    print("1. Encode secret (manual input)")
    print("2. Encode secret from file")
    print("3. Exit")

def main():
    while True:
        show_menu()
        choice = input("\nEnter choice (1/2/3): ").strip()

        if choice == "1":
            secret = input("\nEnter secret message:\n> ").strip()
            if not secret:
                print("❌ Error: Secret message cannot be empty.")
            else:
                encode_auto(secret)

        elif choice == "2":
            file_path = input("\nEnter path to secret file:\n> ").strip()
            secret = load_secret_from_file(file_path)
            if secret:
                encode_auto(secret)

        elif choice == "3":
            print("\nExiting encoder.")
            sys.exit(0)

        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()

