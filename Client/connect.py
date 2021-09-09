import socket
import pickle
from Server.packets import CombatPacket, MovementPacket, PlayerPacket, WorldPacket, DisconnectPacket
ENCODING = "utf-8"
"""HEADERSIZE = 10
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 5525))
class test:
    def __init__(self, glizzy):
        self.gliz = glizzy
    def glizz(self):
        print(self.gliz)

packet = s.recv(100)
pickle.loads(packet).glizz()"""
encoding = "utf-8"
class NewServer:
    def __init__(self, ip : str, port : int, username : str):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.connect((ip, port))
        self.username = username
        self.authenticate()
    def sendPacket(self, packet):
        pass
    def authenticate(self):
        usernamePacket = PlayerPacket.PlayerPacket("Username", "Benji")
        self.s.send(pickle.dumps(usernamePacket))
