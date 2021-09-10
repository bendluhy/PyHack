import pickle
import sys

class MovementPacket:
    def __init__(self,packet):
        try:
            self.senderName = packet.get("senderUsername")
            self.senderUUID = packet.get("senderUUID")
            self.dSet1 = packet.get("dataSet1")
            self.dSet2 = packet.get("dataSet2")
            print("Recieved Valid Movement Packet From " + self.senderName)
        except:
            print("Packet is not a valid packet")

    def execute(self):
        pass

    def undo(self):
        pass

    def authenticate(self):
        pass