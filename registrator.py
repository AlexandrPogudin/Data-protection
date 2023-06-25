import socket
import subprocess

# создаем сокет и настраиваем его
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5000))
server_socket.listen(1)

# Создание приватного ключа
command = "openssl genpkey -algorithm RSA -out privatekey.pem -pkeyopt rsa_keygen_bits:1024"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- private key created ---")

# ждем новых подключений
print('Server is listening...')
connection, address = server_socket.accept()
print('Connection from', address)

# получаем зашифрованный ответ от пользователя
data = connection.recv(1024).decode()
print('Ответ от пользователя:', data)

# расшифровываем голос
command = "openssl pkeyutl -decrypt -inkey privatekey.pem -in message.enc -out message.dec"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- message deciphered ---")

# вычисляем цифровой подписи
command = "openssl dgst -sha256 -sign privatekey.pem -out signature.bin message.dec"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- message signed ---")

# отправляем свой голос в следующий сервер (счетчик)
next_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
next_server_socket.connect(('localhost', 5001))
next_server_socket.send("Signature received".encode())
