"""
Задействуйте сокеты ZeroMQ REQ и REP, чтобы сделать то же самое.
"""
import zmq
from datetime import datetime
import time

host = '127.0.0.1'
port = 6789
context = zmq.Context()

print('Start the server at ', datetime.now())

server = context.socket(zmq.REP)
server.bind(f'tcp://{host}:{port}')

while True:
    print('Waiting for a client call.')

    request_bytes = server.recv()
    request_str = request_bytes.decode('utf-8')

    if request_str == 'time':
        print('Client: time request\n')
        server.send(time.asctime().encode())
    elif request_str == 'q':
        print('Client: disconnect request')
        print('Server close')
        break
    else:
        server.send(b'UNKNOWN command, please try again.')
        print('Client: sent UNKNOWN data\n')
