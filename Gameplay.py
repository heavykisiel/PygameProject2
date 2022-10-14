import pygame
from pygame.locals import *
from map import Map


class Gameplay:

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.display = pygame.Surface((300, 300))

        # self.camera = Camera.Camera()
        self.block = pygame.image.load('textures/grass.jpg').convert()
        self.block = pygame.transform.scale(self.block, (16, 16))
        self.block.set_colorkey((0, 0, 0))
        self.block1 = pygame.image.load('textures/sand.jpg').convert()
        self.block1 = pygame.transform.scale(self.block1, (16, 16))
        self.block1.set_colorkey((0, 0, 0))
        self.map_Data = Map.Map()
        self.LoadNewGame()

    def LoadNewGame(self):
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 128, y * 128, 128, 128), 1)
                    # print(tile)
                    for rowC in range(8):
                        for tileC in range(8):
                            self.screen.blit(self.block, (tile[0] * 128 + rowC * 16, tile[1] * 128 + tileC * 16))
                            if tile[2] == 1:
                                self.screen.blit(self.block1, (tile[0] * 128 + rowC * 16, tile[1] * 128 + tileC * 16))

            # tile[0] == x
            # tile[1] == y
            # tile[2] == biom_id

    def run(self):

        running = True
        i = 0
        while running:
            pygame.time.Clock().tick(60)
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            i = i+1
            print(i)
