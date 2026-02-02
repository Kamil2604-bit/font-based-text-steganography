📘 Font-Based Text Steganography for Covert Communication (Devanagari Script)
🔒 Overview

This repository presents a font-based text steganography framework for covert communication using font-internal metadata, with a specific focus on the Devanagari script.
Unlike traditional text steganography techniques that rely on rendered text, layout variations, or OCR-based processing, the proposed system uses the font file itself as the carrier of hidden information.

The approach is:

Deterministic

OCR-free

Rendering-independent

Script-aware

The system is designed for stable, imperceptible, and reproducible covert communication under font-preserving environments.

✨ Key Contributions

✅ Font-internal metadata as a covert channel

✅ Deterministic encoding and decoding (no heuristics)

✅ OCR-independent hidden communication

✅ Script-aware design for Devanagari

✅ Robust against common font installation and rendering workflows

✅ Practical implementation with web-based interface

✅ Academic-grade evaluation and validation

🧠 Motivation

Most existing text steganography methods suffer from:

dependence on OCR accuracy

instability due to rendering or layout changes

low embedding capacity

lack of script awareness (especially for non-Latin scripts)

This project overcomes these limitations by embedding secret information directly inside font metadata tables, ensuring the hidden message survives normal font usage.

🏗️ System Architecture

The framework follows a layered architecture:

1️⃣ Steganography Core Engine

Direct manipulation of font internals

Deterministic embedding and extraction

No dependency on document rendering

2️⃣ Automation Layer

Message preprocessing and framing

Binary conversion and length encoding

Invokes encoding/decoding pipelines

3️⃣ Interface Layer

Command-Line Interface (CLI)

Local web application (Flask-based)

User-friendly encode/decode workflow

⚠️ The interface layer does not modify steganographic logic.

🔁 Encoding Workflow

User inputs secret text

Message converted to binary

Fixed-length header added

Bitstream embedded into font metadata

Stego font generated (visually identical)

🔓 Decoding Workflow

Stego font uploaded

Metadata tables accessed

Header extracted to determine message length

Bitstream reconstructed

Original message recovered deterministically

🧪 Experimental Validation

The system was evaluated on the following metrics:

Correctness: 100% message recovery under tested conditions

Imperceptibility: No visible glyph or layout differences

Determinism: Identical outputs across repeated executions

Capacity: Thousands of characters via metadata embedding

Robustness: Survives font installation, rendering, and reuse

🛠️ Technologies Used

Python 3.10

FontTools – font manipulation

FontForge – robustness testing

Flask – web interface

HTML / CSS – UI

LaTeX – research paper & thesis documentation

🚀 Getting Started
📦 Prerequisites
Python >= 3.10
pip install fonttools flask


(Optional for robustness testing)

Install FontForge (Windows/Linux)

▶️ Run the Web Application
python app.py


Open browser:

http://127.0.0.1:5000

🔐 Encode a Message

Enter secret text (or upload .txt)

Download generated stego font (.ttf)

🔓 Decode a Message

Upload stego font

Recover hidden message

📁 Repository Structure
font-based-text-steganography/
│
├── app.py
├── encoder/
│   └── encode_auto.py
├── decoder/
│   └── decode_auto.py
├── templates/
│   └── HTML files
├── static/
│   └── CSS
├── screenshots/
│   └── UI screenshots
├── thesis/
│   └── LaTeX source
└── README.md

📊 Comparison with Existing Methods
Method Type	OCR Dependent	Deterministic	Capacity	Script Aware
Linguistic-based	❌	❌	Low	Partial
Unicode-based	❌	⚠️ Partial	Low	Limited
OCR-based	✅	❌	High	Script-sensitive
Proposed Method	❌	✅	High	✅ Devanagari
⚠️ Threat Model & Limitations
In Scope

Passive adversaries

Font-preserving operations

Normal rendering and installation

Out of Scope

Font sanitization

Rasterization

OCR-based transformations

Aggressive font normalization

These limitations are explicitly documented in the research.

📚 Academic Context

This work is part of:

M.Tech Thesis

Research Paper on Covert Communication

Focused on non-Latin script steganography

If you use this work, please cite appropriately.

📄 Citation
Mohd Kamil, Hitesh Singh, Aditee Mattoo,
"Covert Communication in Devanagari Script Using Font-Based Text Steganography",
M.Tech Thesis, NIET Greater Noida, 2026.

👤 Author

Mohd Kamil
M.Tech (CSE – Integrated)
Noida Institute of Engineering and Technology
📧 mohdkamil439529@gmail.com

⭐ Final Note

This repository represents a complete research-to-implementation pipeline, demonstrating how theoretical steganography concepts can be translated into robust, reproducible, and deployable systems.
