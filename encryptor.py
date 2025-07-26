from cryptography.fernet import Fernet
with open("secret.key", "rb") as file:
    key = file.read()
fernet = Fernet(key)
def encrypt_file(input_path, output_path):
    with open(input_path, "rb") as image: # read the image and save it in binary
        data = image.read()
    encrypted_data = fernet.encrypt(data) # encrypt the data
    with open(output_path, "wb") as encrypted_file: # write the encrypted data into the image
        encrypted_file.write(encrypted_data)
def decrypt_file(input_path, output_path):
    with open(input_path, "rb") as file:
        data = file.read()
    decrypted_data = fernet.decrypt(data)
    with open(output_path, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)