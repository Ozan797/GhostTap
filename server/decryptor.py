from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()
fernet = Fernet(key)

def decrypt_file(input_path, output_path):
    with open(input_path, "rb") as file:
        data = file.read()
    decrypted_data = fernet.decrypt(data)
    with open(output_path, "wb") as f:
        f.write(decrypted_data)
