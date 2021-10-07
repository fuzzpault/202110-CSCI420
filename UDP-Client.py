"""
UDP-Client.py
Paul Talaga
Feb 7, 2020
Desc: UDP Client/Server Demo

"""
import socket

serverIP = '10.18.103.54' #'localhost'
serverPort = 1200


if __name__ == "__main__":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    message = 'nothing' #input("Enter a message:")
    for i in range(5000):
        clientSocket.sendto(message.encode('utf-8'), (serverIP,serverPort))
    
    # Wait for a response
        (newMessage, serverAddress) = clientSocket.recvfrom(2048)
    
    print("Translated: {}".format(newMessage))
        
    clientSocket.close()
    
  