from socket import socket


def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8080))
    server_socket.listen(1)

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection from {address}")

        data = client_socket.recv(1024)
        print(f"Received: {data.decode()}")

        response = "HTTP/1.1 200 OK\r\n\r\nHello, World!"
        client_socket.send(response.encode())
        client_socket.close()

if __name__ == "__main__":
    main()