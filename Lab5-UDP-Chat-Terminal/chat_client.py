"""
chat_client.py
Paul Talaga
Oct 15, 2020
Desc: UDP Chat Client with features for Lab 5

"""
import socket

serverIP = 'localhost'
serverPort = 1200


if __name__ == "__main__":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    message = input("Enter your name:")
    clientSocket.sendto(message.encode('utf-8'), (serverIP,serverPort))
    (newMessage, serverAddress) = clientSocket.recvfrom(2048)
    print(newMessage.decode('utf-8'))

    while True:
        message = input(">")
        clientSocket.sendto(message.encode('utf-8'), (serverIP,serverPort))
        (newMessage, serverAddress) = clientSocket.recvfrom(2048)
        print(newMessage.decode('utf-8'))
        if(message == 'exit'):
            break
        
    clientSocket.close()
    
