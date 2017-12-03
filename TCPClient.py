from socket import *
serverName = "127.0.0.1"
serverPort = 9191
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence = input("Input a sentence to process :")
clientSocket.send(sentence.encode('utf-8'))
modifiedSentence = clientSocket.recv(1024)
print ("From Server:", modifiedSentence.decode())
clientSocket.close()
