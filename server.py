import socket

host = 'localhost'
port = 10000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen()
    conn,addr = s.accept()
    with conn :
        print (f"connected at {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)