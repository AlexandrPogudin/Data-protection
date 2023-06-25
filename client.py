import socket
import subprocess

# соединяемся с сервером
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5000))

# Создание приватного ключа
command = "openssl rsa -pubout -in privatekey.pem -out publickey.pem"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- public key created ---")

# вводим свой голос
message = open("message.txt", "w+")
message.write(input('согласен или не согласен: '))
message.close()

# Шифруем голос
command = "openssl rsautl -encrypt -inkey publickey.pem -pubin -in message.txt -out message.enc"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- message encrypted ---")

# отправляем зашифрованный голос на сервер
client_socket.send("The choice is made".encode())

# заканчиваем работу
client_socket.close()


# Получение ответа от регистратора
# создаем сокет и настраиваем его
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.bind(('localhost', 5001))
client_socket.listen(1)

# ждем новых подключений
print('Client is listening...')
connection, address = client_socket.accept()
print('Connection from', address)

# получаем зашифрованный ответ от пользователя
data = connection.recv(1024).decode()
print('Ответ от регистратора:', data)

# заканчиваем работу
client_socket.close()


# Отправка message и подписи в счетчик
# соединяемся с сервером
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 5002))

# отправляем готовность
client_socket.send(data.encode())

# заканчиваем работу
client_socket.close()
