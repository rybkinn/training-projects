"""
Попробуйте сделать то же самое с помощью XMLRPC.
"""
import xmlrpc.client
from datetime import datetime

host = '127.0.0.1'
port = 6789

print('Starting the client at', datetime.now())
proxy = xmlrpc.client.ServerProxy(f'http://{host}:{port}/')

while True:
    client_input = input('Enter the command(q to quit): ')
    if client_input == 'q':
        proxy.req(client_input)
        print('Client close')
        break
    result = proxy.req(client_input)
    print('Server msg:', result, '\n')
