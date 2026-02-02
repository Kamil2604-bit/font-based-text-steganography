import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

ENCODER_PATH = os.path.join(BASE_DIR, "encoder", "encode_auto.py")
DECODER_PATH = os.path.join(BASE_DIR, "decoder", "decode_auto.py")

print("===================================")
print(" FONT STEGANOGRAPHY DEMO MODE ")
print("===================================\n")

print("[1] Running Encoder...\n")
subprocess.run(["python", ENCODER_PATH], check=True)

print("\n[2] Running Decoder...\n")
subprocess.run(["python", DECODER_PATH], check=True)

print("\n===================================")
print(" DEMO COMPLETE ")
print("===================================")
