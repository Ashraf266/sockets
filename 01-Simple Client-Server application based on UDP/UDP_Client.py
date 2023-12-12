import socket
#the server is on the same PC -> same ip address ... 'localhost' == ip address of the server(PC ip address)
serverName = 'localhost'
#server port number 12000
serverPort = 12000
#AF_INET -> internet (IP) , SOCK_DGRAM -> UDP .... Automatically given a port number by the OS
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = input('Input lowercase sentense: ')
#sending the data to the localhost(IP address of this PC) on the port: 12000
#sendto(message, (ip, port)) 
clientSocket.sendto(message.encode('UTF-8'), (serverName, serverPort))
#receive the modified data from the server  .... 2048 max bytes to receive
data, clientAddress = clientSocket.recvfrom(2048)
#print the data
print(data.decode('UTF-8'))
#close the socket connection
clientSocket.close()
message = input('Enter to exit')