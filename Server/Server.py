import socket
import configreader
import threading
import pickle
from packets import CombatPacket, MovementPacket, PlayerPacket, WorldPacket, DisconnectPacket

cfg = configreader.Config("config/config.txt")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((cfg.getHost(), cfg.getPort()))

encoding = "utf-8"
def acceptClient(client, addr):
    connected = True
    while connected:
        packet = client.recv(2048)
        x = pickle.loads(packet)
        connected = False
    client.close()
while True:
    s.listen()
    clientsocket, address = s.accept()
    thrd = threading.Thread(target=acceptClient,args=(clientsocket,address))
    thrd.start()



