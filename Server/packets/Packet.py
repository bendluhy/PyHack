
def createMovementPacket(pType : str, senderName : str, UUID : int, dSet1=0, dSet2=0):
    return {
        "type": pType,
        "senderUsername": senderName,
        "senderUUID": UUID,
        "dataSet1": dSet1,
        "dataSet2": dSet2
    }
def createNetworkPacket(pType : str, senderName : str, UUID : int, disconnect : bool, connect : bool):
    return {
        "type": pType,
        "senderUsername": senderName,
        "senderUUID": UUID,
        "disconnect": disconnect,
        "connect": connect
    }
def createWorldPacket(pType : str, senderName : str, UUID : int, dSet1=0, dSet2=0):
    return {
        "type": pType,
        "senderUsername": senderName,
        "senderUUID": UUID,
        "dataSet1": dSet1,
        "dataSet2": dSet2
    }
def createCombatPacket(pType : str, senderName : str, UUID : int, hit : bool, damage : int):
    return  {
        "type": pType,
        "senderUsername": senderName,
        "senderUUID": UUID,
        "hit": hit,
        "damage": damage
    }

packet = createMovementPacket("movement", "benji", 100000, 15, 15)