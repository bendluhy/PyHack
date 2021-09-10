import socket
import sys

import configreader
import threading
import pickle
from packets import CombatPacket, HandleMovementPacket, PlayerPacket, WorldPacket, HandeNetworkPacket

cfg = configreader.Config("config/config.txt")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((cfg.getHost(), cfg.getPort()))

encoding = "utf-8"
def acceptClient(client, addr):
    connected = True
    infoPacket = client.recv(2048)
    infoPacket = pickle.loads(infoPacket)
    print(infoPacket.get("senderUsername") + " joined")
    while connected:
        packet = client.recv(2048)
        x = pickle.loads(packet)
        if x.get("type") == "network":
            if x.get("disconnect") == True:
                connected = False
        connected = False
    print(infoPacket.get("senderUsername") + " disconnected")
    client.close()
while True:
    s.listen()
    clientsocket, address = s.accept()
    thrd = threading.Thread(target=acceptClient,args=(clientsocket,address))
    thrd.start()



