import socket
import subprocess

# создаем сокет и настраиваем его
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', 5002))
server_socket.listen(1)


# ждем новых подключений
print('Server is listening...')
connection, address = server_socket.accept()
print('Connection from', address)

# получаем голос от предыдущего сервера (регистратора)
data = connection.recv(1024).decode()
print('Ответ от пользователя:', data)

# Верификация цифровой подписи файла
command = "openssl dgst -sha256 -verify publickey.pem -signature signature.bin message.txt"
result = subprocess.run(command, shell=True, capture_output=True)

if result.returncode == 0:
    print("--- verification passed ---")

    message = open("message.txt")
    text = message.read()
    print(address, text)
else:
    print("--- verification failed ---")

# заканчиваем работу
server_socket.close()
