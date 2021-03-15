"""
Попробуйте сделать то же самое с помощью XMLRPC.
"""
from xmlrpc.server import SimpleXMLRPCServer
from datetime import datetime
import time

host = '127.0.0.1'
port = 6789

print('Start the server at ', datetime.now())


def req(command):
    if command == 'time':
        print('Client: time request\n')
        return time.asctime()
    elif command == 'q':
        print('Client: disconnect request')
        print('Server close')
        return True
    else:
        print('Client: sent UNKNOWN data\n')
        return 'UNKNOWN command, please try again.'


server = SimpleXMLRPCServer((host, port))
server.register_function(req, "req")
res = server.serve_forever()
