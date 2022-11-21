import random


class roomData:

    def __init__(self):
        self.mobsExist = bool(random.getrandbits(1))
        self.mobs_count = random.randint(1, 3) if self.mobsExist else 0

    def __repr__(self):
        return 'roomData(mobsExist=' + str(self.mobsExist) + ' ,mobs_count=' + str(self.mobs_count) + ')'