import socket
serverPort = 12000
#AF_INET -> internet (IP) , SOCK_DGRAM -> UDP .... Automatically given a port number by the OS
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#set the port number manually
serverSocket.bind(('', serverPort))
print("The server is ready to receive")
while 1:
#receiving the data             2048 -> max number of bytes to receive
#it returns the data & the address of the sender
    data, clientAddress = serverSocket.recvfrom(2048)
#decoding the message
    message = data.decode("UTF-8")
    print(message)
    modifiedMessage = message.upper()
#send the new message with the modified data
    serverSocket.sendto(modifiedMessage.encode("UTF-8"), clientAddress)