from cryptography.fernet import Fernet

with open("secret.key", "rb") as file:
    key = file.read()

f = Fernet(key)

token = f.encrypt(b"GhostTap is live")
print(token)

plain_text = f.decrypt(token)
print(plain_text)