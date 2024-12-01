import socket
import time as t
host = 'localhost'
port = 20001

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
while True:
    data,addr = s.recvfrom(1024)
    stime = str(t.time())
    print(f" Connected by {addr} > {data.decode('utf-8')}")
    s.sendto(stime.encode(encoding='utf-8'),addr)
