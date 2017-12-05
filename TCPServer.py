#TCP Server
from socket import *
serverPort = 13000
#create TCP welcoming socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
#server begins listening for  incoming TCP requests
serverSocket.listen(1)
#loop forever
while True:
    #server waits on accept() for incoming requests, new socket created on return
    connectionSocket, addr = serverSocket.accept()
    #read bytes from socket
    sentence = connectionSocket.recv(1024)
    #reverse message
    rev_sentence = sentence[::-1]
    # swap case from Upper to Lower And vice versa
    capi_sentence = rev_sentence.swapcase()
    final_output = capi_sentence
    connectionSocket.send(final_output)
    #close connection to this client
    connectionSocket.close()

