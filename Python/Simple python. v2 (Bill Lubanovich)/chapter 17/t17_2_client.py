"""
Задействуйте сокеты ZeroMQ REQ и REP, чтобы сделать то же самое.
"""
import zmq
from datetime import datetime

host = '127.0.0.1'
port = 6789

context = zmq.Context()

print('Starting the client at', datetime.now())
client = context.socket(zmq.REQ)
client.connect(f'tcp://{host}:{port}')

while True:
    client_input = input('Enter the command(q to quit): ')
    if client_input == 'q':
        client.send(client_input.encode())
        print('Client close')
        break
    client.send(client_input.encode())
    reply_bytes = client.recv()
    reply_str = reply_bytes.decode('utf-8')
    print('Server msg:', reply_str, '\n')
