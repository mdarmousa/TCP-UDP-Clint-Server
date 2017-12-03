from socket import *

serverPort = 9191
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
#print("The server is ready to receive")
while True:
    connectionSocket, addr = serverSocket.accept()

    sentence = connectionSocket.recv(1024)
    rev_sentence = sentence[::-1]
    capi_sentence = rev_sentence.swapcase()
    final_output = capi_sentence
    connectionSocket.send(final_output)
    connectionSocket.close()

