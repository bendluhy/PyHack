import socket
import pickle
from Server.packets import CombatPacket, PlayerPacket, WorldPacket, HandeNetworkPacket, Packet
import sys
import sys
import os
encoding = "utf-8"
username = "benji"
class NewServer:
    def __init__(self, ip : str, port : int, username : str):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            self.s.connect((ip, port))
            self.username = username
        except ConnectionRefusedError:
            print("Connection was refused either server is not running or a real server or your connection was refused")
            sys.exit()
        self.authenticate()
    def disconnect(self):
        disconnectPacket = Packet.createNetworkPacket("network", username, 1, disconnect=True, connect=False)
        self.s.send(pickle.dumps(disconnectPacket))
    def sendPacket(self, packet):
        pass
    def authenticate(self):
        networkPacket = Packet.createNetworkPacket("network", username, 1, connect=True, disconnect=False)
        self.s.send(pickle.dumps(networkPacket))
