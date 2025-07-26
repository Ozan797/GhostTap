from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()

with open("logs/filename.jpg.enc", "rb") as encrypted_file:
    data = encrypted_file.read()
    
f = Fernet(key)
decrypted_data = f.decrypt(data)

with open("restored.jpg", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)