#UDP Server
from socket import *
serverPort = 12000
#create UDP socket
serverSocket = socket(AF_INET, SOCK_DGRAM)
#bind socket to local port number 12000
serverSocket.bind(('', serverPort))
#print("The server  ready to receive")

while True:
    #Read from UDP socket into message, getting client’s address (client IP and port)
    message, clientAddress = serverSocket.recvfrom(2048)
    #reverse message
    rev_message=message[::-1]
    # swap case from Upper to Lower And vice versa
    capi_message =rev_message.swapcase()
    modifiedMessage = capi_message.decode()
    #send Final string back to this client
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)


