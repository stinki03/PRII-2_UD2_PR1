import socket
import time as t

host = 'localhost'
port = 20001
contador=0;

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    data = input(" > ").encode(encoding="utf-8")
    #data = t.time()
    #data = f"{contador} + {t.time()}"
    data = str(data).encode(encoding="utf-8")
    s.sendto(data,(host,port))
    #contador += 1
    data,addr = s.recvfrom(1024)
   
