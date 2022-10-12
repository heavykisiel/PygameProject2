import pygame
from map import Map


class Gameplay:

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.display = pygame.Surface((300, 300))

        self.block = pygame.image.load('textures/grass.jpg').convert()
        self.block = pygame.transform.scale(self.block, (16, 16))
        self.block.set_colorkey((0, 0, 0))
        self.map_Data = Map.Map()
        self.LoadNewGame()

    def LoadNewGame(self):
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 128, y * 128, 128, 128), 1)
                    for rowC in range(8):
                        for tileC in range(8):
                            self.screen.blit(self.block, (rowC * 16, tileC * 16))
