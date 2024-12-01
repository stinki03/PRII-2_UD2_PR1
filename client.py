import socket

host = 'localhost'
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((host,port))
    s.sendall(b"holaa")
    data = s.recv(1024)
print(f"receiv {data!r}")
