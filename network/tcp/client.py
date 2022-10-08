''' socket programming in Python'''

import socket
import sys


s  = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname('www.github.com')
print(ip)


try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("socket successfully created!")
except Exception as e:
    print(e)

port = 80

try:
    host_ip = socket.gethostbyname('www.github.com')
except socket.gaierror:
    print('error resolving the host')
    sys.exit()
s.connect((host_ip, port))
print(f'Socket has successfully connected to Github on port == {host_ip}')


import socket
s = socket.socket()
port = 5678
s.connect(('127.0.0.1', port))
print(s.recv(1024))
s.close()