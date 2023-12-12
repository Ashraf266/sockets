import socket

# Create a TCP/IP socket                TCP -> SOCK_STREAM
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port: 10000
serverAddress = ('localhost', 10000)

# Connect to the server
sock.connect(serverAddress)

# receive the welcome message
data = sock.recv(1024)
print(data.decode('UTF-8'))

print("(Type quit to exit the program)")
while True:
    message = input("Input lowercase sentence : ")
    sock.send(message.encode('UTF-8'))
    data = sock.recv(1024)
    print(f"Received: {data.decode('UTF-8')}")
    if message == 'quit':
        break

sock.close()

