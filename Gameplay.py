import sys

import pygame.math
from pygame.locals import *

import Camera
from Camera import *
from map import Map
from textures.TextureLoader import Load_Block_Textures
from Player import Player


class Gameplay(pygame.sprite.Group):

    def __init__(self, screen):
        super().__init__()
        self.screen = screen  # 1080x720
        self.surface_size = pygame.Surface.get_size(self.screen)
        self.half_screen_w = self.surface_size[0] / 2
        self.half_screen_h = self.surface_size[1] / 2
        self.surface_size_vector = pygame.math.Vector2(self.surface_size)
        self.screen.fill((0, 0, 0))
        self.camera_group = Camera()
        self.display = pygame.Surface((300, 300))
        self.player = Player((540, 360), self.camera_group)
        self.block_pixelsx = 30
        self.block_pixelsy = 30
        self.texture_count_per_tilex = 36
        self.texture_count_per_tiley = 24
        # mnożnik block_pixels i texture count per title musi byc równe rectSize
        self.rectSizex = self.surface_size[0]  # 1080
        self.rectSizey = self.surface_size[1]  # 720

        self.grass_block = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 0)
        self.sand_block = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 1)
        self.door_texture = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 2)
        self.map_Data = Map.Map()
        self.player_pos = self.player.player_position

    def LoadNewFrame(self, player):

        # Validate player_pos
        self.player_pos += player.direction * self.player.speed

        # if self.player_pos[0] < 0:
        #     self.player_pos[0] = 0
        # if self.player_pos[1] < 0:
        #     self.player_pos[1] = 0
        # if self.player_pos[0] > (self.map_Data.ChunksX - 1) * self.rectSizex:
        #     self.player_pos[0] = (self.map_Data.ChunksX - 1) * self.rectSizex
        # if self.player_pos[1] > (self.map_Data.ChunksY - 1) * self.rectSizey:
        #     self.player_pos[1] = (self.map_Data.ChunksY - 1) * self.rectSizey

        print("{0}, {1}".format(self.player_pos, (self.map_Data.ChunksY - 1) * self.rectSizex))

        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    pygame.draw.rect(self.screen, (255, 255, 255),
                                     pygame.Rect(x * self.rectSizex, y * self.rectSizey,
                                                 self.rectSizex,
                                                 self.rectSizey), 1)
                    # pomocniczy rectangle można wykomentować
                    for rowC in range(self.texture_count_per_tilex):
                        for tileC in range(self.texture_count_per_tiley):
                            offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
                                         tile[1] * self.rectSizey + tileC * self.block_pixelsy
                            self.screen.blit(self.grass_block, offset_pos)
                            if rowC == self.texture_count_per_tilex - 1 or rowC == 0 or tileC == self.texture_count_per_tiley - 1 or tileC == 0:
                                border_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, tile[
                                    1] * self.rectSizey + tileC * self.block_pixelsy
                                self.screen.blit(self.sand_block, border_pos)
                            if (rowC == self.texture_count_per_tilex / 2 and (tileC == self.texture_count_per_tiley -1 or tileC == 0)) or \
                                    (tileC == self.texture_count_per_tiley / 2 and (rowC == self.texture_count_per_tilex -1 or rowC == 0)):
                                door_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, tile[
                                    1] * self.rectSizey + tileC * self.block_pixelsy
                                self.screen.blit(self.door_texture, door_pos)
                            # biom render
                            if tile[2] == 1:
                                offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
                                             tile[1] * self.rectSizey + tileC * self.block_pixelsy
                                self.screen.blit(self.sand_block, offset_pos)


            self.screen.blit(player.image, self.player_pos)
            # scaled_surface = pygame.transform.scale(self.screen,
            #                                         self.surface_size_vector * self.camera_group.zoom_scale)
            #
            # scaled_rect = scaled_surface.get_rect(center=(self.half_screen_w, self.half_screen_h))
            # self.screen.blit(scaled_surface, scaled_rect)

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
            self.LoadNewFrame(self.player)
            self.camera_group.draw(self.player)
            self.player.bulletGroup.update()
            self.player.bulletGroup.draw(self.screen)
            if self.player.shooting:
                self.player.shoot()

            pygame.display.update()
            pygame.time.Clock().tick(60)

            i = i + 1
            # print(i)
