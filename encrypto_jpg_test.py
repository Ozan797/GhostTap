from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()
    
with open("logs/2025-07-26_10-52-41.jpg", "rb") as image:
    data = image.read()

f = Fernet(key)

encrypted_data = f.encrypt(data)

with open("logs/filename.jpg.enc", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)