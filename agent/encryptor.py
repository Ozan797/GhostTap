import os
from cryptography.fernet import Fernet

# Always get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "secret.key")

with open(KEY_PATH, "rb") as file:
    key = file.read()

fernet = Fernet(key)

def encrypt_file(input_path, output_path):
    with open(input_path, "rb") as image:
        data = image.read()
    encrypted_data = fernet.encrypt(data)
    with open(output_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
