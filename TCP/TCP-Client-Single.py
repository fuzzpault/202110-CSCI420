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
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect( (serverIP,serverPort) )
    message = input("Enter a message:")
    clientSocket.send(message.encode('utf-8'))  # .sendall()
    
    # Wait for a response
    newMessage = clientSocket.recv(2048)
    
    print("Translated: {}".format(newMessage))
        
    clientSocket.close()
    
  