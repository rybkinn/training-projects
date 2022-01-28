"""
Используйте объект класса socket, чтобы реализовать сервис,
сообщающий текущее время. Когда клиент отправляет на сервер строку 'time',
верните текущие дату и время как строку ISO.
"""
from datetime import datetime
import time
import socket

server_address = ('localhost', 6789)
max_size = 4096

print('Start the server at ', datetime.now())

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_address)

while True:
    print('Waiting for a client call.')

    data, client = server.recvfrom(max_size)

    if data == b'time':
        print('Client:', client, 'time request\n')
        server.sendto(time.asctime().encode(), client)
    elif data == b'q':
        server.sendto(b'disconnect', client)
        print('Client:', client, 'disconnect request')
        print('Server close')
        server.close()
        break
    else:
        server.sendto(b'UNKNOWN command, please try again.', client)
        print('Client:', client, 'sent UNKNOWN data\n')
