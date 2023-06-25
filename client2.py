import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import pickle
import subprocess

# Соединяемся с сервером
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 5000))

# Создание публичного ключа
command = "openssl rsa -pubout -in privatekey.pem -out publickey_user2.pem"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- public key created ---")

# Получаем зашифрованный документ от клиента

file = open("message_user2.enc", "wb")
print("receiving data from server")
while True:
    file_data = s.recv(4096)
    file.write(file_data)
    if not file_data:
        break
file.close()
print("file downloaded")

# Расшифровываем документ
command = "openssl pkeyutl -decrypt -inkey privatekey.pem -in message_server.enc -out message_user2.dec"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- message deciphered ---")

# Верификация цифровой подписи файла
command = "openssl dgst -sha256 -verify publickey_user2.pem -signature signature.bin message_user2.dec"
result = subprocess.run(command, shell=True, capture_output=True)
print(f"--- verification {'passed' if result.returncode == 0 else 'failed'} ---")