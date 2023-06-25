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
command = "openssl rsa -pubout -in privatekey.pem -out publickey_user1.pem"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- public key created ---")

# Шифруем документ
command = "openssl rsautl -encrypt -inkey publickey_user1.pem -pubin -in message_user1.txt -out message_user1.enc"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- message encrypted ---")

# Отправляем зашифрованный документ серверу
file = open("message_user1.enc", "rb")
file_data = file.read(4096)
s.send(file_data)
print("file sended")

data = s.recv(1024).decode()
print('Ответ от сервера:', data)

# Верификация цифровой подписи файла
command = "openssl dgst -sha256 -verify publickey_user1.pem -signature signature.bin message_user1.txt"
result = subprocess.run(command, shell=True, capture_output=True)
print(f"--- verification {'passed' if result.returncode == 0 else 'failed'} ---")


