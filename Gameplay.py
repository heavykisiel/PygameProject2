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
        self.map_Data = Map.Map()
        self.mapSurfSize = self.surface_size[0] * self.map_Data.ChunksX, self.surface_size[1] * self.map_Data.ChunksY
        self.mapSurf = pygame.Surface(self.mapSurfSize, pygame.SRCALPHA)
        self.half_screen_w = self.surface_size[0] / 2
        self.half_screen_h = self.surface_size[1] / 2
        self.surface_size_vector = pygame.math.Vector2(self.surface_size)
        self.screen.fill((0, 0, 0))
        self.camera_group = Camera()
        self.display = pygame.Surface((300, 300))
        self.rectSizex = self.surface_size[0]  # 1080
        self.rectSizey = self.surface_size[1]  # 720
        self.spawn = [self.map_Data.maze_start_x, self.map_Data.maze_start_y]
        self.currentChunk = self.spawn
        self.player = Player(
            (540 + (self.currentChunk[0] * self.rectSizex),
             360 + (self.currentChunk[1] * self.rectSizey)),
            self.camera_group, self.screen, self.surface_size)
        self.enemy=Enemy((560,300),self.camera_group,self.screen,self.surface_size,self.player,"bulbazaurus")
        self.enemy1=Enemy((210,200),self.camera_group,self.screen,self.surface_size,self.player,"ogier")
        self.enemyGroup = pygame.sprite.Group()
        self.enemyGroup.add(self.enemy)
        self.enemyGroup.add(self.enemy1)
        self.block_pixelsx = 30
        self.block_pixelsy = 30
        self.texture_count_per_tilex = 36
        self.texture_count_per_tiley = 24
        # mnożenie block_pixels i texture count per title musi byc równe rectSize


        self.floor_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 0)
        self.eastWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 1)
        self.northWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 2)
        self.southWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 3)
        self.westWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 4)
        self.eastNorthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 5)
        self.westNorthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 6)
        self.eastSouthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 7)
        self.westSouthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 8)
        self.midWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 9)

        self.player_pos = self.player.player_position
        self.doorlistv2 = self.doors()
        self.wall_collider_rect = self.detect_rect_colliders()
        self.doorlist = None
        self.walls_opti = self.OptedWalls()

    def detect_rect_colliders(self):
        lista = list()
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
                                # if (rowC == self.texture_count_per_tilex / 2 and (
                                #         tileC == self.texture_count_per_tiley - 1 or tileC == 0)) or \
                                #         (tileC == self.texture_count_per_tiley / 2 and (
                                #                 rowC == self.texture_count_per_tilex - 1 or rowC == 0)):
                                #     door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                #                     tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                #                     self.block_pixelsx, self.block_pixelsy)
                                #     listb.append(door_pos)
        print(f"lista len before: {len(lista)}")
        for door in self.doorlistv2:
            for xx in lista:
                if xx.contains(door):
                    print(f"{door}")
                    lista.remove(xx)
        print(f"door length: {len(self.doorlistv2)}  |  lista length after: {len(lista)} ")
        return lista

    def OptedWalls(self):
        a = list()
        for x in self.wall_collider_rect:
            if x.x < 1100:
                a.append(x)
            elif x.y < 800:
                a.append(x)
        for x in a:
            print(f"{x}")
        return a

    def doors(self):
        listC = list()
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    doorStr = "wnse"
                    print(f"{tile[2]}")
                    if str(tile[2]).__contains__('w'):
                        doorStr = doorStr.replace('w', '')
                    if str(tile[2]).__contains__('n'):
                        doorStr = doorStr.replace('n', '')
                    if str(tile[2]).__contains__('s'):
                        doorStr = doorStr.replace('s', '')
                    if str(tile[2]).__contains__('e'):
                        doorStr = doorStr.replace('e', '')
                    print(f"kierunek drzwii {doorStr} w chunku x:{tile[0]} y:{tile[1]}")
                    for rowC in range(self.texture_count_per_tilex):
                        for tileC in range(self.texture_count_per_tiley):
                            if doorStr.__contains__('n') and (rowC == 0 and
                                                              tileC == self.texture_count_per_tiley / 2):
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + (tileC - 1) * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + (tileC + 1) * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                            if doorStr.__contains__('w') and (
                                    rowC == self.texture_count_per_tilex / 2 and
                                    tileC == 0):
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + (rowC + 1) * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + (rowC - 1) * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)

                            if doorStr.__contains__('s') and (tileC == self.texture_count_per_tiley / 2 and
                                                              rowC == self.texture_count_per_tilex - 1):
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + (tileC - 1) * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + (tileC + 1) * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)

                            if doorStr.__contains__('e') and (tileC == self.texture_count_per_tiley - 1 and
                                                              rowC == self.texture_count_per_tilex / 2):
                                door_pos = Rect(tile[0] * self.rectSizex + rowC * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + (rowC + 1) * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)
                                door_pos = Rect(tile[0] * self.rectSizex + (rowC - 1) * self.block_pixelsx,
                                                tile[1] * self.rectSizey + tileC * self.block_pixelsy,
                                                self.block_pixelsx, self.block_pixelsy)
                                listC.append(door_pos)

        return listC

    def drawMap(self, player):

        MapRect = Rect(0, 0, self.map_Data.ChunksX * self.rectSizex, self.map_Data.ChunksY * self.rectSizey)
        ground_offset = MapRect.topleft - self.camera_group.offset - pygame.math.Vector2(
            self.currentChunk[0] * self.rectSizex, self.currentChunk[1] * self.rectSizey)
        self.screen.fill((0, 0, 0))
        if player.direction.magnitude() != 0:
            player.direction = player.direction.normalize()
        # Validate player_pos
        print(f"{self.player_pos}  {self.player.rect}")

        self.player_pos += player.direction * self.player.speed
        self.player.rect.x += player.direction.x * self.player.speed
        self.player.rect.y += player.direction.y * self.player.speed

        for x in self.wall_collider_rect:
            if player.rect.colliderect(x):
                print(f"collided with wall")
                print(f"player.rect.left: {self.player.rect.left}    |   x.right: {x.right}")
                if abs(player.rect.top - x.bottom) < 20:
                    print(f"player hit top")
                    self.player_pos[1] = self.block_pixelsy + 20
                    self.player.rect.y = self.block_pixelsy + 20
                    break
                if abs(player.rect.left - x.right) < 20:
                    print(f"player hit left")
                    self.player_pos[0] = self.block_pixelsx + 20
                    self.player.rect.x = self.block_pixelsx + 20
                    break
                if abs(player.rect.right - x.left) < 20:
                    print(f"player hit right")
                    self.player_pos[0] = self.rectSizex - self.block_pixelsx - 20
                    self.player.rect.x = self.rectSizex - self.block_pixelsx - 20
                    break
                if abs(player.rect.bottom - x.top) < 20:
                    print(f"player hit bottom")
                    self.player_pos[1] = self.rectSizey - self.block_pixelsy - 20
                    self.player.rect.y = self.rectSizey - self.block_pixelsy - 20
                    break

        # for i in self.wall_collider_rect:
        #     if self.player.rect.colliderect(i):
        #         print(f"collision occured on {i}")
        #         self.player.rect.x += player.direction.x * self.player.speed
        #         self.player.rect.y = self.rectSizex - self.block_pixelsx
        #         self.player_pos = self.rectSizex - self.block_pixelsx
        #     else:
        #         self.player_pos += player.direction * self.player.speed
        #         self.player.rect.x += player.direction.x * self.player.speed
        #         self.player.rect.y += player.direction.y * self.player.speed
        if self.player_pos[0] < 0 + (self.currentChunk[0] * self.rectSizex):
            self.currentChunk[0] -= 1
        if self.player_pos[1] < 0 + (self.currentChunk[1] * self.rectSizey):
            self.currentChunk[1] -= 1
        if self.player_pos[0] > self.rectSizex + (self.currentChunk[0] * self.rectSizex):
            self.currentChunk[0] += 1
        if self.player_pos[1] > self.rectSizey + (self.currentChunk[1] * self.rectSizey):
            self.currentChunk[1] += 1

        # print("{0}".format(self.player_pos,))

        # fill screen with floor
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    for rowC in range(self.texture_count_per_tilex):
                        for tileC in range(self.texture_count_per_tiley):
                            offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
                                         tile[1] * self.rectSizey + tileC * self.block_pixelsy
                            self.screen.blit(self.floor_tex, offset_pos + ground_offset)
        # fill screen with borders
        for x in self.wall_collider_rect:
            self.screen.blit(self.midWall_tex, (x.x, x.y) + ground_offset)
            # if x.top == 0 :
            #     self.screen.blit(self.northWall_tex, (x.x, x.y) + ground_offset)
            #     if x.x == 0 and x.y == 0:
            #         self.screen.blit(self.westNorthWall_tex, (x.x, x.y) + ground_offset)
            #     if x.x == 1050 and x.y == 0:
            #         self.screen.blit(self.eastNorthWall_tex, (x.x, x.y) + ground_offset)
            # if x.left == 0 and x.top != 0:
            #     self.screen.blit(self.westWall_tex, (x.x, x.y) + ground_offset)
            # if x.right == 1080 and x.y != 0:
            #     self.screen.blit(self.eastWall_tex, (x.x, x.y) + ground_offset)
            # if x.bottom == 720:
            #     self.screen.blit(self.southWall_tex, (x.x, x.y) + ground_offset)
            #     if x.x == 1050  and x.y == 690:
            #         self.screen.blit(self.eastSouthWall_tex, (x.x, x.y) + ground_offset)
            #     if x.x == 0 and x.y == 690:
            #         self.screen.blit(self.westSouthWall_tex, (x.x, x.y) + ground_offset)

        for x in self.doorlistv2:
            self.screen.blit(self.floor_tex, (x.x, x.y) + ground_offset)

        # self.detect_rect_colliders()
        self.screen.blit(player.image, self.player_pos + ground_offset)

        


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

            # self.enemy.rangeCollide(self.player)

            self.camera_group.draw(self.player)
            self.player.bulletGroup.update()
            self.player.bulletGroup.draw(self.screen)
           

            if self.player.shooting:
                self.player.shoot()
                
            for enemy in self.enemyGroup: 
                enemy.direction_distance(self.player)   
                enemy.draw()
                enemy.status(self.player)
                enemy.enemybulletGroup.update()
                enemy.enemybulletGroup.draw(self.screen)
                
                
            for enemies in self.enemyGroup.sprites():
                test1=[x for x in self.enemyGroup if x != enemies]
                collide = pygame.sprite.spritecollide(enemies, test1, False)     
                if not collide:
                    pass   
                else: 
                    for a in collide:
                        print(a)
                        
            if pygame.sprite.spritecollide(self.enemy, self.player.bulletGroup, False):
                if self.enemy.alive:
                    self.enemy.healthMin -= 20
                    self.enemy.health -= 20
                    for bullets in self.player.bulletGroup:
                        bullets.kill()
                    

            pygame.display.update()
            pygame.time.Clock().tick(60)

            i = i + 1
            # print(i)
