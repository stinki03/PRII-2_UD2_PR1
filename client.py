import socket
import time as t
host = 'localhost'
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    while True:
        s.sendall(b'holaa')
        t.sleep(1)
