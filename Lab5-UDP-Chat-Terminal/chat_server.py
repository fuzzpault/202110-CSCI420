"""
chat_server.py
Paul Talaga
Oct 15, 2020
Desc: UDP Chat Server with features for Lab 5

"""
import socket
import pickle

serverIP = '0.0.0.0' # Listen on all adapters
serverPort = 1200

print("Server Started.  Listening...")

def getLastMessages(clients):
    # clients is a dictionary
    ret = ""
    for v in clients.values():
        ret += v['name'] + ": " + v['msg'] + "\n"
    return ret
    

if __name__ == "__main__":
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    server.bind(  (serverIP,serverPort) )

    clients = {}

    while True:
        (msg, clientAddress) = server.recvfrom(2048)
        msg = msg.decode('utf-8')

        if clientAddress not in clients.keys(): # new user!
            print("New user: {}".format(msg))
            clients[clientAddress] = {'name':msg, 'msg':''}
            msg = getLastMessages(clients)
            server.sendto(msg.encode('utf-8'), clientAddress)
        elif msg == 'exit':
            print("{} leaving".format(clients[clientAddress]['name']))
            clients.pop(clientAddress)
            server.sendto("Bye!".encode('utf-8'), clientAddress)

        elif msg == '?':
            print("{} getting all names".format(clients[clientAddress]['name']))
            userList = ", ".join( [v['name'] for v in clients.values()] )
            server.sendto(userList.encode('utf-8'), clientAddress)

        elif msg == '.':
            print("{} getting last messages".format(clients[clientAddress]['name']))
            # Don't put the . in the last message
            msg = getLastMessages(clients)
            server.sendto(msg.encode('utf-8'), clientAddress)

        else:
            print("{} said {}".format(clients[clientAddress]['name'], msg))
            clients[clientAddress]['msg'] = msg
            msg = getLastMessages(clients)
            server.sendto(msg.encode('utf-8'), clientAddress)
    
    server.close()