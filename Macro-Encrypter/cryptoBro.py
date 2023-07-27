from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Hash import SHA256
from base64 import b64encode, b64decode
import tkinter as tk
from tkinter import ttk


def pad_message(message):
    padding_length = AES.block_size - (len(message) % AES.block_size)
    padding = bytes([padding_length] * padding_length)
    return message + padding


def unpad_message(padded_message):
    padding_length = padded_message[-1]
    return padded_message[:-padding_length]


def encrypt_AES_GCM(msg, password):
    salt = get_random_bytes(16)
    kdf = PBKDF2(password, salt, dkLen=32,
                 count=100000, hmac_hash_module=SHA256)
    key = kdf[:16]
    cipher = AES.new(key, AES.MODE_GCM)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(msg)
    return b64encode(salt + nonce + ciphertext + tag).decode('utf-8')


def decrypt_AES_GCM(enc_msg, password):
    enc_msg = b64decode(enc_msg)
    salt = enc_msg[:16]
    nonce = enc_msg[16:32]
    ciphertext = enc_msg[32:-16]
    tag = enc_msg[-16:]
    kdf = PBKDF2(password, salt, dkLen=32,
                 count=100000, hmac_hash_module=SHA256)
    key = kdf[:16]
    cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
    plaintext = cipher.decrypt_and_verify(ciphertext, tag)
    return plaintext


def encrypt_message(message):
    password = 'BombardeenTalaveraDeLaReinaPorfa'
    encrypted_msg = encrypt_AES_GCM(message.encode('utf-8'), password)
    return encrypted_msg


def decrypt_message(encrypted_msg):
    password = 'BombardeenTalaveraDeLaReinaPorfa'
    decrypted_msg = decrypt_AES_GCM(encrypted_msg, password)
    return decrypted_msg.decode('utf-8')


class MyApp:
    def __init__(self, root):
        self.root = root
        self.root.title('over complicated RSA Encryption')
        self.root.geometry('400x400')
        self.mensajeoriginal = ""
        self.mensajecifrado = ""
        self.mensajedescifrado = ""
        self.mensajerecifrado = ""

        self.label = ttk.Label(
            self.root, text="over complicated\n\rAES Encryption", font=("Helvetica", 16, "bold"))
        self.label.pack(pady=15)

        self.label_mensaje_original = ttk.Label(
            self.root, text="Mensaje original:")
        self.label_mensaje_original.pack()
        self.label_mensaje_cifrado = ttk.Label(
            self.root, text="Mensaje cifrado:")
        self.label_mensaje_cifrado.pack()
        self.label_mensaje_recifrado = ttk.Label(
            self.root, text="Mensaje re-cifrado:")
        self.label_mensaje_recifrado.pack()
        self.label_mensaje_descifrado = ttk.Label(
            self.root, text="Mensaje descifrado:")
        self.label_mensaje_descifrado.pack()

        self.mensaje_entry = ttk.Entry(self.root)
        self.mensaje_entry.pack(pady=5)

        self.button_enviar = ttk.Button(
            self.root, text="Enviar", command=self.encriptar)
        self.button_enviar.pack(pady=10)

    def encriptar(self):
        mensaje = self.mensaje_entry.get()
        self.mensajeoriginal = mensaje
        encrypted_msg = encrypt_message(mensaje)
        self.mensajecifrado = encrypted_msg
        decrypted_msg = decrypt_message(encrypted_msg)
        self.mensajedescifrado = decrypted_msg

        self.label_mensaje_original.config(
            text=f"Mensaje original: {self.mensajeoriginal}")
        self.label_mensaje_cifrado.config(
            text=f"Mensaje cifrado: {self.mensajecifrado}")
        self.label_mensaje_recifrado.config(
            text=f"Mensaje re-cifrado: {self.mensajerecifrado}")
        self.label_mensaje_descifrado.config(
            text=f"Mensaje descifrado: {self.mensajedescifrado}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MyApp(root)
    root.mainloop()
