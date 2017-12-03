from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
#print("The server  ready to receive")
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    rev_message=message[::-1]
    capi_message =rev_message.swapcase()
    modifiedMessage = capi_message.decode()
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)


