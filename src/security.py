from cryptography.fernet import Fernet
import os
import logging

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, 'wb') as f:
        f.write(key)
    logging.info("Çelësi i enkriptimit u gjenerua.")
    return key

def load_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    return generate_key()

def encrypt_data(text):
    key = load_key()
    f = Fernet(key)
    encrypted = f.encrypt(text.encode())
    return encrypted.decode()

def decrypt_data(encrypted_text):
    try:
        key = load_key()
        f = Fernet(key)
        decrypted = f.decrypt(encrypted_text.encode())
        return decrypted.decode()
    except Exception as e:
        logging.error(f"Gabim gjatë dekriptimit: {e}")
        return None