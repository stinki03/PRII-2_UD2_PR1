import socket
import time as t
host = 'localhost'
port = 10000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
while True:
    data,addr = s.recvfrom(1024)
    stime = str(s.time())
    print(f" Connected by {addr} > {data.decode('utf-8')}")
    s.sendto(stime.encode(encoding='utf-8'),addr)
