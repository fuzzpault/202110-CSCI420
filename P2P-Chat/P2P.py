"""
P2P.py
Paul Talaga
Feb 2, 2021
Desc: P2P network implemenation using UDP

"""

import socket
import threading
import pickle
import time
import sys
import hashlib, json

serverIP = '0.0.0.0' # Listen on all adapters
serverPort = 1200 + (int(time.time()) % 2000)

# Returns a hash of a dictionary, to know if two dictionaries are different
def dict_hash(dictionary):  #: Dict[str, Any]) -> str:
    """MD5 hash of a dictionary."""
    dhash = hashlib.md5()
    # We need to sort arguments so {'a': 1, 'b': 2} is
    # the same as {'b': 2, 'a': 1}
    encoded = pickle.dumps(dictionary)
    dhash.update(encoded)
    return dhash.hexdigest()

# The server part of the code, listens for update messages and possibly spreads the new information
def listen_worker():
    global big_message
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind(  (serverIP,serverPort) )
    print(f"Server Started.  Listening on {serverIP} {serverPort}...")
    while socket:
        (message, clientAddress) = server.recvfrom(2048)
        try:
            new_big = pickle.loads(message)
            print("Translated: {}".format(new_big))
        except:
            print("Unable to depickle {}".format(message))
            next
        merged = pickle.loads(pickle.dumps(big_message))  # Horrible way to do a deep copy
        merged['clients'].update(new_big['clients'])  # merge the contact list
        # todo - merge messages too!

        if(dict_hash(big_message) != dict_hash(merged)):  # Is this an update or not?
            big_message = merged
            # Send to all others
            for (rip, rport) in big_message['clients']:
                if (rip, rport) != (serverIP,serverPort):
                    clist = pickle.dumps(big_message)
                    server.sendto(clist, (rip,rport))
                    print(f"Sent update to {(rip,rport)} {big_message}")
        else:
            print("Got update, but didn't change")


    socket.close()

clients = {(serverIP,serverPort)} # This is 'me'
big_message = {'clients': clients, 'messages': []}

if __name__ == "__main__":
    
    
    thread = threading.Thread(target=listen_worker)
    thread.start()

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Detect if parameters are given, and if so, send my info to them
    if len(sys.argv) > 1:
        peerIP = sys.argv[1]
        peerPort = int(sys.argv[2])

        
        clist = pickle.dumps(big_message)

        clientSocket.sendto(clist, (peerIP,peerPort))
    
    while True:
        # Where the user input should go
        pass
    