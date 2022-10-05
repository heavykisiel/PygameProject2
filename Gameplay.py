import pygame


class Gameplay:

    def __init__(self, screen):
        self.screen = screen
        self.screen.fill((0, 0, 0))
        self.display = pygame.Surface((300, 300))

        self.block = pygame.image.load('textures/block.png').convert()
        self.block = pygame.transform.scale(self.block, (32, 32))
        self.block.set_colorkey((0, 0, 0))
        self.LoadNewGame()

    def LoadNewGame(self):
        f = open('map/map1.txt')
        map_data = [[int(c) for c in row] for row in f.read().split('\n')]
        f.close()
        print(map_data)
        for y, row in enumerate(map_data):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(self.screen, (255, 255, 255), pygame.Rect(x * 10, y * 10, 10, 10), 1)
                    self.screen.blit(self.block, (520 + x * 10, 360 + y * 10))
