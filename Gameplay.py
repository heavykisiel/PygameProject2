import sys

import pygame.math
from pygame.locals import *

import Camera
from Camera import *
from map import Map
from textures.TextureLoader import Load_Block_Textures
from Player import Player
from Enemy import Enemy
from Bullets import Bullets



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
        self.player = Player((540, 360), self.camera_group,self.screen,self.surface_size)
        self.enemy=Enemy((560,300),self.camera_group,self.screen,self.surface_size,self.player)
        self.enemyGroup = pygame.sprite.Group()
        self.enemyGroup.add(self.enemy)
        self.block_pixelsx = 30
        self.block_pixelsy = 30
        self.texture_count_per_tilex = 36
        self.texture_count_per_tiley = 24
        # mnożnik block_pixels i texture count per title musi byc równe rectSize
        self.rectSizex = self.surface_size[0]  # 1080
        self.rectSizey = self.surface_size[1]  # 720

        self.floor_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 0)
        self.eastWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 1)
        self.northWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 2)
        self.southWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 3)
        self.westWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 4)
        self.eastNorthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 5)
        self.westNorthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 6)
        self.eastSouthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 7)
        self.westSouthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 8)
        self.map_Data = Map.Map()
        self.player_pos = self.player.player_position
        self.wall_collider_rect = self.detect_rect_colliders()
        self.doorlist = None

    def detect_rect_colliders(self):
        lista = list()
        listb = list()
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    for rowC in range(self.texture_count_per_tilex):
                        for tileC in range(self.texture_count_per_tiley):
                            if rowC == self.texture_count_per_tilex - 1 or rowC == 0 or \
                                    tileC == self.texture_count_per_tiley - 1 or tileC == 0:
                                border_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                  tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                  self.block_pixelsx, self.block_pixelsy)
                                lista.append(border_pos)
                                if (rowC == self.texture_count_per_tilex / 2 and (
                                        tileC == self.texture_count_per_tiley - 1 or tileC == 0)) or \
                                        (tileC == self.texture_count_per_tiley / 2 and (
                                                rowC == self.texture_count_per_tilex - 1 or rowC == 0)):
                                    door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                    tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                    self.block_pixelsx, self.block_pixelsy)
                                    listb.append(door_pos)
        self.doorlist = listb
        return lista

    def drawMap(self, player):
        if player.direction.magnitude() != 0:
            player.direction = player.direction.normalize()
        # Validate player_pos
        self.player_pos += player.direction * self.player.speed
        if self.doorlist is not None:
            for door in self.doorlist:
                if self.player.rect.colliderect(door):
                    self.renderNewRoom()
        if self.player_pos[0] < self.block_pixelsx / 2:
            self.player_pos[0] = self.block_pixelsx / 2
        if self.player_pos[1] < self.block_pixelsy / 2:
            self.player_pos[1] = self.block_pixelsy / 2
        if self.player_pos[0] > self.rectSizex - self.block_pixelsx:
            self.player_pos[0] = self.rectSizex - self.block_pixelsx
        if self.player_pos[1] > self.rectSizey - self.block_pixelsy:
            self.player_pos[1] = self.rectSizey - self.block_pixelsy

       # print("{0}, {1}".format(self.player_pos, self.player.rect.left))

        # fill screen with floor
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    for rowC in range(self.texture_count_per_tilex):
                        for tileC in range(self.texture_count_per_tiley):
                            offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
                                         tile[1] * self.rectSizey + tileC * self.block_pixelsy
                            self.screen.blit(self.floor_tex, offset_pos)
        # fill screen with borders
        for x in self.wall_collider_rect:
            if x.top == 0:
                self.screen.blit(self.northWall_tex, (x.x, x.y))
                if x.x == 0 and x.y == 0:
                    self.screen.blit(self.westNorthWall_tex, (x.x, x.y))
                if x.x == 1050 and x.y == 0:
                    self.screen.blit(self.eastNorthWall_tex, (x.x, x.y))
            if x.left == 0 and x.top != 0:
                self.screen.blit(self.westWall_tex, (x.x, x.y))
            if x.right == 1080 and x.y != 0:
                self.screen.blit(self.eastWall_tex, (x.x, x.y))
            if x.bottom == 720:
                self.screen.blit(self.southWall_tex, (x.x, x.y))
                if x.x == 1050 and x.y == 690:
                    self.screen.blit(self.eastSouthWall_tex, (x.x, x.y))
                if x.x == 0 and x.y == 690:
                    self.screen.blit(self.westSouthWall_tex, (x.x, x.y))
        self.detect_rect_colliders()
        self.screen.blit(player.image, self.player_pos)
        # print(listb.__len__())
        # for x in listb:
        #     pygame.draw.rect(self.screen, (0, 0, 200), x, 1)

        # for y, row in enumerate(self.map_Data.ChunkMap):
        #     for x, tile in enumerate(row):
        #         if tile:
        #             pygame.draw.rect(self.screen, (255, 255, 255),
        #                              pygame.Rect(x * self.rectSizex, y * self.rectSizey,
        #                                          self.rectSizex,
        #                                          self.rectSizey), 1)
        #             # pomocniczy rectangle można wykomentować
        #             for rowC in range(self.texture_count_per_tilex):
        #                 for tileC in range(self.texture_count_per_tiley):
        #                     offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
        #                                  tile[1] * self.rectSizey + tileC * self.block_pixelsy
        #                     self.screen.blit(self.grass_block, offset_pos)
        #                     if rowC == self.texture_count_per_tilex - 1 or rowC == 0 or tileC == self.texture_count_per_tiley - 1 or tileC == 0:
        #                         border_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
        #                                      tile[1] * self.rectSizey + tileC * self.block_pixelsy
        #
        #                         self.screen.blit(self.sand_block, border_pos)
        #                     if (rowC == self.texture_count_per_tilex / 2 and (
        #                             tileC == self.texture_count_per_tiley - 1 or tileC == 0)) or \
        #                             (tileC == self.texture_count_per_tiley / 2 and (
        #                                     rowC == self.texture_count_per_tilex - 1 or rowC == 0)):
        #                         door_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, tile[
        #                             1] * self.rectSizey + tileC * self.block_pixelsy
        #                         self.screen.blit(self.door_texture, door_pos)
        #                     # biom render
        #                     if tile[2] == 1:
        #                         offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
        #                                      tile[1] * self.rectSizey + tileC * self.block_pixelsy
        #                         self.screen.blit(self.sand_block, offset_pos)

        # if self.player.rect.colli

        # scaled_surface = pygame.transform.scale(self.screen,
        #                                         self.surface_size_vector * self.camera_group.zoom_scale)
        #
        # scaled_rect = scaled_surface.get_rect(center=(self.half_screen_w, self.half_screen_h))
        # self.screen.blit(scaled_surface, scaled_rect)

        # tile[0] == x
        # tile[1] == y
        # tile[2] == biom_id

        self.return_gamedata()

    def return_gamedata(self):
        self.player.player_position = self.player_pos

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
            self.drawMap(self.player)
            
            for self.enemy in self.enemyGroup: 
                self.enemy.direction_distance(self.player)   
                self.enemy.draw()
                self.enemy.status(self.player)
                #self.enemy.rangeCollide(self.player)
            
            
            self.camera_group.draw(self.player)
            self.player.bulletGroup.update()
            self.player.bulletGroup.draw(self.screen)
            self.enemy.enemybulletGroup.update()
            self.enemy.enemybulletGroup.draw(self.screen)
            
            
            if self.player.shooting:
                self.player.shoot()
                
                
            if pygame.sprite.spritecollide(self.enemy, self.player.bulletGroup, False):
                if self.enemy.alive:
                    print("ZYCIEZYCIEZYCIEZYCIE")
                    self.enemy.healthMin -=20
                    self.enemy.health -= 20
                    for bullets in self.player.bulletGroup:
                        bullets.kill()
                    print(self.enemy.health)
                    
            pygame.display.update()
            pygame.time.Clock().tick(60)

            i = i + 1
            # print(i)
