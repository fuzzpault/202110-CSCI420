"""
UDP-Client.py
Paul Talaga
Feb 7, 2020
Desc: UDP Client/Server Demo

"""
import socket
import threading

serverIP = '10.18.100.150' #localhost'
serverPort = 1201

def listen_worker(socket):
    while socket:
        message = socket.recv(2048)
        print("Translated: {}".format(message.decode('utf-8')))

if __name__ == "__main__":
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientSocket.connect( (serverIP,serverPort) )

    thread = threading.Thread(target=listen_worker, args = [clientSocket])
    thread.start()

    while True:
        message = input("Enter a message:")
        if message == 'exit':
            break
        clientSocket.send(message.encode('utf-8'))  # .sendall()
        
        # Wait for a response
        newMessage = clientSocket.recv(2048)
        
        
        
    clientSocket.close()
    
  