from flask import Flask, render_template, request, send_file
import os
import tempfile

from encoder.encode_auto import encode_auto
from decoder.decode_auto import decode_auto

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FONT_PATH = os.path.join(BASE_DIR, "output", "stego_font.ttf")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/encode", methods=["GET", "POST"])
def encode():
    if request.method == "POST":
        secret_text = ""

        if request.form.get("secret_text"):
            secret_text = request.form.get("secret_text").strip()

        elif request.files.get("secret_file"):
            file = request.files["secret_file"]
            if file.filename:
                secret_text = file.read().decode("utf-8").strip()

        if not secret_text:
            return render_template(
                "encode.html",
                error="Secret message cannot be empty."
            )

        encode_auto(secret_text)

        return send_file(
            OUTPUT_FONT_PATH,
            as_attachment=True,
            download_name="stego_font.ttf"
        )

    return render_template("encode.html")

@app.route("/decode", methods=["GET", "POST"])
def decode():
    if request.method == "POST":
        file = request.files.get("stego_font")
        if not file or file.filename == "":
            return render_template(
                "decode.html",
                error="Please upload a stego font file."
            )

        with tempfile.NamedTemporaryFile(delete=False, suffix=".ttf") as tmp:
            file.save(tmp.name)
            recovered = decode_auto(tmp.name)

        return render_template(
            "decode.html",
            recovered=recovered
        )

    return render_template("decode.html")

if __name__ == "__main__":
    app.run(debug=True)