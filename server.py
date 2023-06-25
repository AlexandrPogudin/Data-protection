import socket
from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
from Crypto.Cipher import PKCS1_OAEP
import pickle
import subprocess

# Создание приватного ключа
command = "openssl genpkey -algorithm RSA -out privatekey.pem -pkeyopt rsa_keygen_bits:1024"
result = subprocess.run(command, shell=True, capture_output=True)
print("--- private key created ---")

def main():
    # Создаем сокет и слушаем порт
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 5000))
    server_socket.listen(10)

    # Подключение клиентов
    print('Server is listening...')
    connection1, address1 = server_socket.accept()
    print(f"New client connected: {address1}")

    # Получаем зашифрованный документ от клиента
    # Расшифровываем документ
    file = open("message_server.enc", "wb")
    print("receiving data from server")
    file_data = connection1.recv(4096)
    file.write(file_data)
    file.close()
    print("file downloaded")

    # расшифровываем документ
    command = "openssl pkeyutl -decrypt -inkey privatekey.pem -in message_server.enc -out message_server.dec"
    result = subprocess.run(command, shell=True, capture_output=True)
    print("--- message deciphered ---")

    # вычисляем цифровой подписи
    command = "openssl dgst -sha256 -sign privatekey.pem -out signature.bin message_server.dec"
    result = subprocess.run(command, shell=True, capture_output=True)
    print("--- message signed ---")

    connection1.send("Message signed".encode())

    print('Server is listening...')
    connection2, address2 = server_socket.accept()
    print(f"New client connected: {address2}")


    file = open("message_server.enc", "rb")
    while True:
        file_data = file.read(4096)
        connection2.send(file_data)
        if not file_data:
            break
    print("file sended")


if __name__ == "__main__":
    main()
