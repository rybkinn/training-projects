"""
Используйте объект класса socket, чтобы реализовать сервис,
сообщающий текущее время. Когда клиент отправляет на сервер строку 'time',
верните текущие дату и время как строку ISO.
"""
import socket
from datetime import datetime

server_address = ('localhost', 6789)
max_size = 4096

print('Starting the client at', datetime.now())
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    client_input = input('Enter the command(q to quit): ')
    if client_input == 'q':
        client.sendto(client_input.encode(), server_address)
    client.sendto(client_input.encode(), server_address)
    data, server = client.recvfrom(max_size)
    if data == b'disconnect':
        print('Client close')
        client.close()
        break
    print('Server msg:', data.decode(), '\n')
