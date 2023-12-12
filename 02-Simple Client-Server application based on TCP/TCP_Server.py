import socket

# Create a TCP/IP socket                TCP -> SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port: 10000
serverAddress = ('localhost', 10000)
print(f"Starting up on {serverAddress[0]} port: {serverAddress[1]}")
sock.bind(serverAddress)

# Listen for incoming connections
sock.listen(1)

while True:
    print('Waiting for a connection...')
    connection, clientAddress = sock.accept()
    try:
        print('Client connected:', clientAddress)
        data = "Welcome to the echo server"
        connection.sendall(data.encode('UTF-8'))
        while True:
            data = connection.recv(1024)
            print(f"received data: {data.decode('UTF-8')}")
            if data:
                connection.sendall(data.upper())
            else:
                break
    finally:
        connection.close()

