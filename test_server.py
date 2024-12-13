import socket
import time

def main():
    server_address = ('', 20001)
    buffer_size = 1024

    # Crear socket UDP
    udp_server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_server_socket.bind(server_address)

    print("Servidor UDP a la escucha en el puerto 20001...")

    while True:
        message, client_address = udp_server_socket.recvfrom(buffer_size)
        current_time = time.time()
        print(f"Mensaje recibido: {message.decode()} de {client_address}")

        response = str(current_time).encode()
        udp_server_socket.sendto(response, client_address)

if __name__ == "__main__":
    main()
