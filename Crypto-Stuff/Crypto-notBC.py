from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

class EncryptionTool:
    def __init__(self, key=None):
        if key:
            self.key = key
        else:
            self.key = Fernet.generate_key()

    def encrypt_file(self, input_file, output_file, algorithm='fernet'):
        if algorithm == 'fernet':
            with open(input_file, 'rb') as f:
                data = f.read()
            fernet = Fernet(self.key)
            encrypted = fernet.encrypt(data)
            with open(output_file, 'wb') as f:
                f.write(encrypted)
        elif algorithm == 'aes':
            iv = os.urandom(16)
            with open(input_file, 'rb') as f:
                data = f.read()
            padder = padding.PKCS7(algorithms.AES.block_size).padder()
            padded_data = padder.update(data) + padder.finalize()
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            encryptor = cipher.encryptor()
            encrypted = encryptor.update(padded_data) + encryptor.finalize()
            with open(output_file, 'wb') as f:
                f.write(iv + encrypted)
    
    def decrypt_file(self, input_file, output_file, algorithm='fernet'):
        if algorithm == 'fernet':
            with open(input_file, 'rb') as f:
                data = f.read()
            fernet = Fernet(self.key)
            decrypted = fernet.decrypt(data)
            with open(output_file, 'wb') as f:
                f.write(decrypted)
        elif algorithm == 'aes':
            with open(input_file, 'rb') as f:
                iv = f.read(16)
                data = f.read()
            cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
            decryptor = cipher.decryptor()
            padded_data = decryptor.update(data) + decryptor.finalize()
            unpadder = padding.PKCS7(algorithms.AES.block_size).unpadder()
            decrypted = unpadder.update(padded_data) + unpadder.finalize()
            with open(output_file, 'wb') as f:
                f.write(decrypted)

# Ejemplo de uso
et = EncryptionTool()
et.encrypt_file('input.txt', 'output.txt', algorithm='fernet')
et.decrypt_file('output.txt', 'decrypted.txt', algorithm='fernet')
