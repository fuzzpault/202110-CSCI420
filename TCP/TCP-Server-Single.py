"""
UDP-SErver.py
Paul Talaga
Feb 7, 2020
Desc: UDP Client/Server Demo

"""
import socket

serverIP = '0.0.0.0' # Listen on all adapters
serverPort = 1200

clients = {}
print("Server Started.  Listening...")

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    server.bind(  (serverIP,serverPort) )
    server.listen()

    while True:
        print("Waiting for connect")
        client_socket, addr = server.accept()
        print("Got new connection from {}".format(addr))

        newMessage = server.recv(2048)
         
        print("Got: {}".format(newMessage))
        
        newMessage = str(newMessage).upper()
        
        client_socket.send(newMessage.encode('utf-8'))
        client_socket.close()
        print("Closed connection to {}".format(addr))
    
    server.close()
    