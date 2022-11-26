import random


class roomData:

    def __init__(self, roomCode):
        self.mobsExist = None
        self.roomCode = self.roomCodeConerter(roomCode)
        self.mobs_count = random.randint(1, 3) if self.mobsExist else 0

    def __repr__(self):
        return 'roomData(mobsExist=' + str(self.mobsExist) + ' ,mobs_count=' + str(self.mobs_count) + ')'

    def roomCodeConerter(self, roomCode):
        if roomCode == "Room":
            self.mobsExist = bool(random.getrandbits(1))
            return "Room"
        elif roomCode == "Boss":
            self.mobsExist = False
            return "Boss"
        elif roomCode == "Key":
            self.mobsExist = False
            return "Key"
        elif roomCode == "Bonus":
            self.mobsExist = False
            return "Bonus"
        elif roomCode == "Spawn":
            self.mobsExist = False
            return "Spawn"
        else:
            raise Exception(f"Invalid RoomCode: {roomCode} in roomData.roomCodeConverter")

