import random
import pygame
from pygame import Rect
from textures.TextureLoader import TextureUnit


class roomData:

    texture_count_per_tilex = 18
    texture_count_per_tiley = 12
    block_pixelsx = 60
    block_pixelsy = 60
    screenSizeX = 1080
    screenSizeY = 720
    mobsCount = 20

    def __init__(self, roomCode, chunk, colliders_list):
        self.Chunk = chunk
        self.mobsExist = None
        self.rectColliders = self.roomColidersdetection(colliders_list)
        self.roomCode = self.roomCodeConverter(roomCode)
        self.mobs_count = random.randint(2, 5) if self.mobsExist else 0
        self.tex_list = self.TexCoordsList()
        self.tex2_cracked_list, self.tex3_cracked_list = self.get_cracked_tex_pos()
        self.textureUnit = TextureUnit(self.block_pixelsx, self.block_pixelsy)
        print(len(self.rectColliders))

    def __repr__(self):
        return 'roomData(mobsExist=' + str(self.mobsExist) + ' ,mobs_count=' + str(self.mobs_count) + ')'

    def roomCodeConverter(self, roomCode):
        if roomCode == "Room":
            self.mobsExist = True if random.randint(0, 100) < 90 else False
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

    def roomColidersdetection(self, colliders_list):
        a = list()
        for x in colliders_list:
            if self.Chunk[0] * self.screenSizeX <= x.x < (self.Chunk[0] * self.screenSizeX) + self.screenSizeX and \
                    self.Chunk[1] * self.screenSizeY <= x.y < (self.Chunk[1] * self.screenSizeY) + self.screenSizeY:
                a.append(x)
        if len(a) == 73 or len(a) == 76 or len(a) == 79 or len(a) == 82 or len(a) == 85:

            return a
        else:
            raise Exception(f"on Chunk: {self.Chunk} len.colliderlist: {len(a)}, a: \t {a} , colliders: {colliders_list}")

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

    def draw_border(self, screen, ground_offset, test_tex):

        for x in self.rectColliders:
            if x.x % self.screenSizeX == 0:
                if x.y % self.screenSizeY == 0:
                    screen.blit(self.textureUnit.northWestwallTop_tex, (x.x, x.y) + ground_offset) # west north Top
                elif x.y % self.screenSizeY == 60:
                    screen.blit(self.textureUnit.northWestwallBot_tex, (x.x, x.y) + ground_offset) # west north Bot
                elif x.y % self.screenSizeY == 660:
                    screen.blit(self.textureUnit.southWestBot_tex, (x.x, x.y) + ground_offset) # south west Bot
                elif x.y % self.screenSizeY == 600:
                    screen.blit(self.textureUnit.southWestTop_tex, (x.x, x.y) + ground_offset)  # south west Top
                else:
                    screen.blit(self.textureUnit.westWall1_tex, (x.x, x.y) + ground_offset) # west
            elif x.x % self.screenSizeX == 1020:
                if x.y % self.screenSizeY == 0:
                    screen.blit(self.textureUnit.northEastTop_tex, (x.x, x.y) + ground_offset) # north east
                elif x.y % self.screenSizeY == 60:
                    screen.blit(self.textureUnit.northEastBot_tex, (x.x, x.y) + ground_offset) # north east
                elif x.y % self.screenSizeY == 660:
                    screen.blit(self.textureUnit.southEastBot_tex, (x.x, x.y) + ground_offset) # south east
                elif x.y % self.screenSizeY == 600:
                    screen.blit(self.textureUnit.southEastTop_tex, (x.x, x.y) + ground_offset) # south east
                else:
                    screen.blit(self.textureUnit.eastWall1_tex, (x.x, x.y) + ground_offset) # east
            elif x.y % self.screenSizeY == 0:
                screen.blit(self.textureUnit.northWall1Top_tex, (x.x, x.y) + ground_offset) # north Top
            elif x.y % self.screenSizeY == 60:
                screen.blit(self.textureUnit.northWall1Bot_tex, (x.x, x.y) + ground_offset) # north Bot
            elif x.y % self.screenSizeY == 660:
                screen.blit(self.textureUnit.southWall1Bot, (x.x, x.y) + ground_offset)  # south Bot
            elif x.y % self.screenSizeY == 600:
                screen.blit(self.textureUnit.south_wall1Top_tex, (x.x, x.y) + ground_offset)  # south Top
            else:
                screen.blit(self.textureUnit.midWall_tex, (x.x, x.y) + ground_offset)
