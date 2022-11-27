import random


class roomData:
    texture_count_per_tilex = 18
    texture_count_per_tiley = 12
    block_pixelsx = 60
    block_pixelsy = 60
    screenSizeX = 1080
    screenSizeY = 720

    def __init__(self, roomCode, chunk):
        self.Chunk = chunk
        self.mobsExist = None
        self.roomCode = self.roomCodeConverter(roomCode)
        self.mobs_count = random.randint(1, 3) if self.mobsExist else 0
        self.tex_list = self.TexCoordsList()
        self.tex2_cracked_list, self.tex3_cracked_list = self.get_cracked_tex_pos()

    def __repr__(self):
        return 'roomData(mobsExist=' + str(self.mobsExist) + ' ,mobs_count=' + str(self.mobs_count) + ')'

    def roomCodeConverter(self, roomCode):
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

    def TexCoordsList(self):
        a = list()
        for rowC in range(self.texture_count_per_tilex):
            for tileC in range(self.texture_count_per_tiley):
                a.append((self.Chunk[0] * self.screenSizeX + rowC * self.block_pixelsx,
                          self.Chunk[1] * self.screenSizeY + tileC * self.block_pixelsy))
        return a

    def get_cracked_tex_pos(self):
        a = self.tex_list
        b = list()
        c = list()
        for _ in range(40):
            b.append(random.choice(a))
        for _ in range(40):
            c.append(random.choice(a))
        return b, c

    def draw_floor(self, tex, screen, ground_offset, tex2, tex3):
        for rowC in range(self.texture_count_per_tilex):
            for tileC in range(self.texture_count_per_tiley):
                offset_pos = self.Chunk[0] * self.screenSizeX + rowC * self.block_pixelsx, \
                             self.Chunk[1] * self.screenSizeY + tileC * self.block_pixelsy
                screen.blit(tex, offset_pos + ground_offset)
        for a in self.tex2_cracked_list:
            screen.blit(tex2, a + ground_offset)
        for b in self.tex3_cracked_list:
            screen.blit(tex3, b + ground_offset)


