import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 3000  # Port to listen on (non-privileged ports are > 1023)

# Set up a TCP/IP server
tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to server address and port 3000
server_address = (HOST, PORT)
tcp_socket.bind(server_address)

# Listen on port 3000
tcp_socket.listen(1)

while True:
    print("Waiting for connection")
    connection, client = tcp_socket.accept()
    try:
        print("Connected to client IP: {}".format(client))
        data = connection.recv(32)
        while data:
            print("Received data: {}".format(data.decode("utf-8")))
            data = connection.recv(32)

    finally:
        connection.close()