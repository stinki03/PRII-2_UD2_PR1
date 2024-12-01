import socket
import time as t

host = 'localhost'
port = 20001
contador=0;

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
while True:
    stime = t.time()
    data = f"{contador} + {stime}"
    data = str(data).encode(encoding="utf-8")
    s.sendto(data,(host,port))
    contador += 1
    data,addr = s.recvfrom(1024)
    RTT = t.time() - stime
    print(f" [+] RTT : {RTT}")
