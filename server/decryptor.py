import os
from cryptography.fernet import Fernet

# Dynamically resolve the absolute path to secret.key
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
KEY_PATH = os.path.join(BASE_DIR, "secret.key")

with open(KEY_PATH, "rb") as file:
    key = file.read()

fernet = Fernet(key)

def decrypt_file(input_path, output_path):
    with open(input_path, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(output_path, "wb") as output_file:
        output_file.write(decrypted_data)
