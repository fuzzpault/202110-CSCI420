"""
UDP-SErver.py
Paul Talaga
Feb 7, 2020
Desc: UDP Client/Server Demo

"""
import socket
import threading

serverIP = '0.0.0.0' # Listen on all adapters
serverPort = 1201

def listenForMessage(client_socket, addr):
    print("New thread listen for {}".format(addr))
    counter = 0
    while True:
        counter += 1
        newMessage = client_socket.recv(2048)
        if not newMessage:
            break
        print("Got: {}".format(newMessage))
        
        newMessage = str(newMessage).upper() + str(counter)
        
        client_socket.send(newMessage.encode('utf-8'))
    client_socket.close()
    print("Closed connection to {}".format(addr))

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
        thread = threading.Thread(target=listenForMessage, args=[client_socket, addr] )
        thread.start()
        
        
    
    server.close()
    