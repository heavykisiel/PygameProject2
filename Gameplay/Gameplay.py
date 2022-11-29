import sys
import random
import pygame.math
from pygame.locals import *

import Camera
from Camera import *
from map import Map
from textures.TextureLoader import Load_Block_Textures
from Player import Player
from Enemy import Enemy
from enums import MOBS
from .Utilities.GameplayUtilities import add_mob_chunks
from .Utilities.GameplayUtilities import detect_rect_colliders
from .Utilities.GameplayUtilities import doors
from .Utilities.GameplayUtilities import one_door_rooms
from .Utilities.GameplayUtilities import one_door_rooms_validation
from .Utilities.GameplayUtilities import room_function_setter


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
        self.block_pixelsx = 60
        self.block_pixelsy = 60
        self.texture_count_per_tilex = 18
        self.texture_count_per_tiley = 12

        # mnożenie block_pixels i texture count per title musi byc równe rectSize

        self.floor_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 0)
        self.floor1_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 12)
        self.floor2_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 13)
        self.floor3_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 14)
        self.eastWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 1)
        self.northWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 2)
        self.southWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 3)
        self.westWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 4)
        self.eastNorthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 5)
        self.westNorthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 6)
        self.eastSouthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 7)
        self.westSouthWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 8)
        self.midWall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 9)
        self.grass_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 10)
        self.key_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 11)
        self.westWall1_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 15)
        self.westWall2_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 16)
        self.westWall3_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 17)
        self.northWestwall_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 18)
        self.eastWall1_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 19)
        self.eastWall2_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 20)
        self.eastWall3_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 21)
        self.northEastwall_tex = Load_Block_Textures(self.block_pixelsx,self.block_pixelsy, 22)
        self.northWall1_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 23)
        self.northWall2_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 24)
        self.northWall3_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 25)
        self.southEast_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 26)
        self.southWest_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 27)
        self.northWallList = list((self.northWall1_tex, self.northWall2_tex, self.northWall3_tex))
        self.westWallList = list((self.westWall1_tex, self.westWall2_tex, self.westWall3_tex))
        self.eastWallList = list((self.eastWall1_tex, self.eastWall2_tex, self.eastWall3_tex))
        self.doorlistv2 = doors(self)
        self.wall_collider_rect = detect_rect_colliders(self)
        self.OneDoorRooms = one_door_rooms(self)
        self.isOneDoorRoomsvalidData = one_door_rooms_validation(self)
        self.Room_Function_setter = room_function_setter(self)
        self.map_Data = self.Room_Function_setter
        self.map_Data = add_mob_chunks(self)
        for z in self.map_Data.ChunkMap:
            print(z)

        self.MapRect = Rect(0, 0, self.map_Data.ChunksX * self.rectSizex, self.map_Data.ChunksY * self.rectSizey)
        self.ground_offset = self.MapRect.topleft - self.camera_group.offset - pygame.math.Vector2(
            self.currentChunk[0] * self.rectSizex, self.currentChunk[1] * self.rectSizey)

        self.player = Player(
            (540 + (self.currentChunk[0] * self.rectSizex),
             360 + (self.currentChunk[1] * self.rectSizey)),
            self.camera_group, self.screen, self.surface_size)

        self.enemyGroup = pygame.sprite.Group()

    def drawMap(self, player):
        # player interaction with map elements
        self.GamePlay_Logic(player)
        # fill screen with floor
        self.Draw_Floor()
        # fill screen with borders
        self.draw_borders()
        # draw player
        self.screen.blit(player.image, self.player.rect.topleft + self.ground_offset)

        # enemy ( powinno być rozdzielone na logikę i render #TODO
        # Do it filip bo nie chce nic zjebać) #TODO

        for enemy in self.enemyGroup:
            enemy.direction_distance(self.player)
            enemy.draw(self.ground_offset)
            if self.currentChunk == enemy.currentChunk:
                enemy.status(self.player)
            enemy.mapCollide(self.currentChunk)
            enemy.enemybulletGroup.update()
            for bullets in enemy.enemybulletGroup:
                bullets.mapCollide(self.currentChunk)
                self.screen.blit(bullets.image, bullets.rect.topleft + self.ground_offset)
            if enemy.shooting:
                enemy.shoot()
        pygame.draw.rect(self.screen, (0,0,0), (48,8,204,14))
        pygame.draw.rect(self.screen, (255,0,0), (50,10,200, 10))
        if self.player.health >0:    
            pygame.draw.rect(self.screen, (0,255,0), (50,10, 200 * (self.player.healthMin / self.player.healthMax),10))
        if self.player.shooting:
            self.player.shoot()

        self.player.bulletGroup.update()
        for bullets in self.player.bulletGroup:
            bullets.mapCollide(self.currentChunk)
            self.screen.blit(bullets.image, bullets.rect.topleft + self.ground_offset)

    def GamePlay_Logic(self, player):
        # normalize movement player
        if player.direction.magnitude() != 0:
            player.direction = player.direction.normalize()

        # player movement
        self.player.rect.x += player.direction.x * self.player.speed
        self.player.rect.y += player.direction.y * self.player.speed

        # wall interaction
        for x in self.wall_collider_rect:
            if player.rect.colliderect(x):
                if abs(player.rect.top - x.bottom) < 20:
                    self.player.rect.y = x.bottom
                if abs(player.rect.left - x.right) < 20:
                    self.player.rect.x = x.right
                if abs(player.rect.right - x.left) < 20:
                    self.player.rect.x = x.left - self.player.rect.width
                if abs(player.rect.bottom - 30 - x.top) < 20:
                    self.player.rect.y = x.top - self.player.rect.height
        # current chunk update
        if self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].mobsExist:

            # nie można wyjśc dopuki się wszystkich mobów nie pokona
            ax = self.currentChunk[0] * self.rectSizex
            ay = self.currentChunk[1] * self.rectSizey
            if abs(player.rect.top - ay) < 17:
                self.player.rect.y = ay + 17
            if abs(player.rect.left - ax) < 17:
                self.player.rect.x = ax + 17
            if abs(player.rect.right - (ax + self.rectSizex - 10)) < 17:
                self.player.rect.x = ax + self.rectSizex - 60
            if abs(player.rect.bottom - (ay + self.rectSizey - 10)) < 17:
                self.player.rect.y = ay + self.rectSizey - 80
            if len(self.enemyGroup) == 0:
                self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].mobsExist = False

        else:
            if self.player.rect.centerx < 0 + (self.currentChunk[0] * self.rectSizex):
                self.currentChunk[0] -= 1
                self.OnNewRoom()
            if self.player.rect.centery < 0 + (self.currentChunk[1] * self.rectSizey):
                self.currentChunk[1] -= 1
                self.OnNewRoom()
            if self.player.rect.centerx > self.rectSizex + (self.currentChunk[0] * self.rectSizex):
                self.currentChunk[0] += 1
                self.OnNewRoom()
            if self.player.rect.centery > self.rectSizey + (self.currentChunk[1] * self.rectSizey):
                self.currentChunk[1] += 1
                self.OnNewRoom()
        # Update offset
        self.ground_offset = self.MapRect.topleft - self.camera_group.offset - pygame.math.Vector2(
            self.currentChunk[0] * self.rectSizex, self.currentChunk[1] * self.rectSizey)

    def Draw_Floor(self):
        # fill screen with floor
        for y, row in enumerate(self.map_Data.ChunkMap):
            for x, tile in enumerate(row):
                if tile:
                    tile[4].draw_floor(self.floor1_tex, self.screen, self.ground_offset, self.floor2_tex, self.floor3_tex)

        for x in self.OneDoorRooms:
            if x[4].roomCode == 'Key':
                # render key
                offset_pos = x[0] * self.rectSizex + 9 * self.block_pixelsx, \
                             x[1] * self.rectSizey + 6 * self.block_pixelsy
                self.screen.blit(self.key_tex, offset_pos + self.ground_offset)
            else:
                offset_pos = x[0] * self.rectSizex + 9 * self.block_pixelsx, \
                             x[1] * self.rectSizey + 6 * self.block_pixelsy
                self.screen.blit(self.grass_tex, offset_pos + self.ground_offset)

    def OnNewRoom(self):

        if self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].roomCode == "Spawn":
            print("spawn")
        elif self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].roomCode == "Key":
            print("key")
        elif self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].roomCode == "Boss":
            print("boss")
        elif self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].roomCode == "Bonus":
            print("bonus")
        elif self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].mobsExist:
            mobsCount = self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].mobs_count

            for newEnemy in range(0, mobsCount):
                mobsType = MOBS[random.randint(0, len(MOBS) - 1)]
                tempCurrentChunk = self.currentChunk
                enemy1 = Enemy(((self.currentChunk[0] * self.rectSizex) + random.randrange(100, 600),
                                (self.currentChunk[1] * self.rectSizey) + random.randrange(100, 600)),
                               self.camera_group, self.screen,
                               self.surface_size, self.player, mobsType, 4, tempCurrentChunk)

                self.enemyGroup.add(enemy1)

            print(
                f"there should be {self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].mobs_count} mobs")
        elif not self.map_Data.ChunkMap[self.currentChunk[0]][self.currentChunk[1]][4].mobsExist:
            print("there shouldnt be any mobs")

    def draw_borders(self):
        for x in self.wall_collider_rect:
            if x.x == 0 or x.x == 1080 or x.x == 2160 or x.x == 3240:
                if x.y == 0 or x.y == 720 or x.y == 1440 or x.y == 2160:
                    self.screen.blit(self.northWestwall_tex, (x.x, x.y) + self.ground_offset) # west north
                elif x.y == 660 or x.y == 1380 or x.y == 2100 or x.y == 2820:
                    self.screen.blit(self.southWest_tex, (x.x, x.y) + self.ground_offset)
                else:
                    self.screen.blit(random.choice(self.westWallList), (x.x, x.y) + self.ground_offset) # west
            elif x.x == 1020 or x.x == 2100 or x.x == 3180 or x.x == 4260:
                if x.y == 0 or x.y == 720 or x.y == 1440 or x.y == 2160:
                    self.screen.blit(self.northEastwall_tex, (x.x, x.y) + self.ground_offset) # north east
                elif x.y == 660 or x.y == 1380 or x.y == 2100 or x.y == 2820:
                    self.screen.blit(self.southEast_tex , (x.x, x.y) + self.ground_offset)
                else:
                    self.screen.blit(random.choice(self.eastWallList), (x.x, x.y) + self.ground_offset) # east
            elif x.y == 0 or x.y == 720 or x.y == 1440 or x.y == 2160:
                self.screen.blit(random.choice(self.northWallList), (x.x, x.y) + self.ground_offset) # north
            elif x.y == 660 or x.y == 1380 or x.y == 2100 or x.y == 2820:
                    self.screen.blit(random.choice(self.northWallList), (x.x, x.y) + self.ground_offset)  # south
            else:
                self.screen.blit(self.midWall_tex, (x.x, x.y) + self.ground_offset)

            #Jak chcecie naprawić to to dajcie jakaś teksturkę z tej listy[0]np a nie random.choice
    def run(self):

        running = True
        i = 0
        while running:

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
            self.screen.fill((0, 0, 0))
            self.camera_group.update()
            self.drawMap(self.player)
            self.camera_group.draw(self.player)

            for enemies in self.enemyGroup.sprites():
                test1 = [x for x in self.enemyGroup if x != enemies]
                collide = pygame.sprite.spritecollide(enemies, test1, False)
                if not collide:
                    pass
                else:
                    for a in collide:
                        # a.rect.x -=a.speed
                        # a.rect.y -=a.speed
                        pass

            for enemy in self.enemyGroup:
                if pygame.sprite.spritecollide(enemy, self.player.bulletGroup, True):
                    if enemy.alive:
                        enemy.healthMin -= 20
                        enemy.health -= 20

                if pygame.sprite.spritecollide(self.player, enemy.enemybulletGroup, True):
                    if enemy.alive:
                        self.player.health -= 5
                        self.player.healthMin -= 5

            pygame.display.update()
            pygame.time.Clock().tick(60)

            i = i + 1
            # print(i)
