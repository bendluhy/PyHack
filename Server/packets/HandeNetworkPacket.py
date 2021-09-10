import pickle
import sys
class NetworkPacket:
    def __init__(self,packet):
        try:
            self.senderName = packet.get("senderUsername")
            self.senderUUID = packet.get("senderUUID")
            self.disconnet = packet.get("disconnect")
            self.connect = packet.get("connect")
            print("Recieved Valid Network Packet From " + self.senderName)
        except:
            print("Packet is not a valid packet")

    def execute(self):
        pass

    def undo(self):
        pass

    def authenticate(self):
        print("Nothing done Because network packet is not needed")
        pass