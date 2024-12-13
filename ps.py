import socket
import datetime

HOST = "158.42.133.220"
PORT = 20001
with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
    s.bind((HOST,PORT))
    
    while True:
        data, addr = s.recvfrom(1024)
        t2 = datetime.datetime.now()
        time = t2.strftime("%H:%M:%S.%f")[:-3]

        print(f"Connected by {addr}", t2)
        print(data);
        if data:
            s.sendto(time.encode(), addr)

    s.close()
