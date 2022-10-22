import sys

import pygame.math
from pygame.locals import *

import Camera
from Camera import *
from map import Map
from textures.TextureLoader import Load_Block_Textures
from Player import Player


class Gameplay:

    def __init__(self, screen):
        self.screen = screen  # 1080x720
        self.surface_size = pygame.Surface.get_size(self.screen)
        self.half_screen_w = self.surface_size[0] / 2
        self.half_screen_h = self.surface_size[1] / 2
        self.surface_size_vector = pygame.math.Vector2(self.surface_size)
        self.screen.fill((0, 0, 0))
        self.camera_group = Camera()
        self.display = pygame.Surface((300, 300))
        self.player = Player((540, 360), self.camera_group)
        self.block_pixels = 64
        self.texture_count_per_tile = 16
        # mnożnik block_pixels i texture count per title musi byc równe rectSize
        self.rectSize = 1024
        self.grass_block = Load_Block_Textures(self.block_pixels, 0)
        self.sand_block = Load_Block_Textures(self.block_pixels, 1)
        self.map_Data = Map.Map()
        self.player_pos = (0, 0)

    def LoadNewGame(self, player):
        self.player_pos += player.direction * self.player.speed
        print(self.player_pos)
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     pygame.Rect(x * self.rectSize, y * self.rectSize, self.rectSize, self.rectSize), 1)
                    # pomocniczy rectangle można wykomentować
                    for rowC in range(self.texture_count_per_tile):
                        for tileC in range(self.texture_count_per_tile):
                            offset_pos = tile[0] * self.rectSize + rowC * self.block_pixels - self.player_pos[0], \
                                         tile[1] * self.rectSize + tileC * self.block_pixels - self.player_pos[1]
                            self.screen.blit(self.grass_block, offset_pos)
                            # biom render
                            if tile[2] == 1:
                                offset_pos = tile[0] * self.rectSize + rowC * self.block_pixels - self.player_pos[0], \
                                             tile[1] * self.rectSize + tileC * self.block_pixels - self.player_pos[1]
                                self.screen.blit(self.sand_block, offset_pos)
            scaled_surface = pygame.transform.scale(self.screen,
                                                    self.surface_size_vector * self.camera_group.zoom_scale)

            scaled_rect = scaled_surface.get_rect(center=(self.half_screen_w, self.half_screen_h))
            self.screen.blit(scaled_surface, scaled_rect)
            # tile[0] == x
            # tile[1] == y
            # tile[2] == biom_id

    def run(self):

        running = True
        i = 0
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEWHEEL:
                    self.camera_group.zoom_scale += event.y * 0.03
                    # zoom jest ale są cyrki, ale można się pobawić
            self.screen.fill((0, 0, 0))
            self.camera_group.update()
            self.LoadNewGame(self.player)
            self.camera_group.draw(self.player)

            pygame.display.update()
            pygame.time.Clock().tick(20)
            # można zmieniać, ale do testowania dałem 20

            i = i + 1
            # print(i)
