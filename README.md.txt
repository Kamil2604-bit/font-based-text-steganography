# Font-Based Text Steganography

## Overview
This project implements a novel font-based text steganography system that embeds secret messages into font metadata without altering visual appearance.

## Features
- Metadata-based encoding and decoding
- Resistant to visual inspection
- Web-based interface using Flask
- Compatible with TrueType fonts (.ttf)

## Tech Stack
- Python
- Flask
- FontForge
- HTML/CSS

## How It Works
1. User enters secret text
2. Secret is encoded into font metadata
3. Receiver uploads the font
4. Decoder extracts the hidden message

## How to Run
```bash
pip install -r requirements.txt
python app.py