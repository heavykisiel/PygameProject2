import sys

import pygame.math
from pygame.locals import *

import Camera
from Camera import *
from map import Map
from textures.TextureLoader import Load_Block_Textures
from Player import Player
from Enemy import Enemy
from .Utilities.GameplayUtilities import OptedWalls
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
        self.grass_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 10)
        self.key_tex = Load_Block_Textures(self.block_pixelsx, self.block_pixelsy, 11)

        self.doorlistv2 = doors(self)
        self.wall_collider_rect = detect_rect_colliders(self)
        self.walls_opti = OptedWalls(self)
        self.OneDoorRooms = one_door_rooms(self)
        self.isOneDoorRoomsvalidData = one_door_rooms_validation(self)
        self.Room_Function_setter = room_function_setter(self)
        self.map_Data = self.Room_Function_setter
        for z in self.map_Data.ChunkMap:
            print(z)

        self.MapRect = Rect(0, 0, self.map_Data.ChunksX * self.rectSizex, self.map_Data.ChunksY * self.rectSizey)
        self.ground_offset = self.MapRect.topleft - self.camera_group.offset - pygame.math.Vector2(
            self.currentChunk[0] * self.rectSizex, self.currentChunk[1] * self.rectSizey)

        self.player = Player(
            (540 + (self.currentChunk[0] * self.rectSizex),
             360 + (self.currentChunk[1] * self.rectSizey)),
            self.camera_group, self.screen, self.surface_size)
        self.enemy = Enemy((560 - self.ground_offset[0], 300 - self.ground_offset[1]), self.camera_group, self.screen,
                           self.surface_size, self.player, "skeleton", 6)
        self.enemy1 = Enemy((210 - self.ground_offset[0], 200 - self.ground_offset[1]), self.camera_group, self.screen,
                            self.surface_size, self.player, "destroyer", 4)
        self.enemyGroup = pygame.sprite.Group()
        self.enemyGroup.add(self.enemy)
        self.enemyGroup.add(self.enemy1)

    def drawMap(self, player):
        # player interaction with map elements
        self.GamePlay_Logic(player)
        # fill screen with floor
        self.Draw_Floor()
        # fill screen with borders
        self.draw_Borders()
        # draw player
        self.screen.blit(player.image, self.player.rect.topleft + self.ground_offset)

        # enemy ( powinno być rozdzielone na logikę i render #TODO
        # Do it filip bo nie chce nic zjebać) #TODO

        for enemy in self.enemyGroup:
            enemy.direction_distance(self.player)
            enemy.draw(self.ground_offset)
            enemy.status(self.player)
            enemy.mapCollide(self.currentChunk)
            enemy.enemybulletGroup.update()
            for bullets in enemy.enemybulletGroup:
                self.screen.blit(bullets.image, bullets.rect.topleft + self.ground_offset)
            if enemy.shooting:
                enemy.shoot()

        # self.return_gamedata()
        self.screen.blit(player.image, self.player.rect.topleft + self.ground_offset)
        # pygame.draw.rect(self.screen, (255, 255, 0), self.player.rect)
        if self.player.shooting:
            self.player.shoot()

        self.player.bulletGroup.update()
        for bullets in self.player.bulletGroup:
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
                    for rowC in range(self.texture_count_per_tilex):
                        for tileC in range(self.texture_count_per_tiley):
                            offset_pos = tile[0] * self.rectSizex + rowC * self.block_pixelsx, \
                                         tile[1] * self.rectSizey + tileC * self.block_pixelsy
                            self.screen.blit(self.floor_tex, offset_pos + self.ground_offset)
        for x in self.OneDoorRooms:
            if x[4] == 'Key':
                # render key
                offset_pos = x[0] * self.rectSizex + 16 * self.block_pixelsx, \
                             x[1] * self.rectSizey + 12 * self.block_pixelsy
                self.screen.blit(self.key_tex, offset_pos + self.ground_offset)
            else:
                offset_pos = x[0] * self.rectSizex + 16 * self.block_pixelsx, \
                         x[1] * self.rectSizey + 12 * self.block_pixelsy
                self.screen.blit(self.grass_tex, offset_pos + self.ground_offset)

    def OnNewRoom(self):
        # Battle Mode Update
        if self.player.BattleMode:
            print("true 1")
        else:
            print("false 0")

    def draw_Borders(self):
        for x in self.wall_collider_rect:
            self.screen.blit(self.midWall_tex, (x.x, x.y) + self.ground_offset)

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
                if pygame.sprite.spritecollide(enemy, self.player.bulletGroup, False):
                    if enemy.alive:
                        enemy.healthMin -= 20
                        enemy.health -= 20

                        for bullets in self.player.bulletGroup:
                            bullets.kill()

                if pygame.sprite.spritecollide(self.player, enemy.enemybulletGroup, False):
                    if enemy.alive:
                        self.player.health -= 20
                        print(self.player.health)
                        for bullets in enemy.enemybulletGroup:
                            bullets.kill()

            pygame.display.update()
            pygame.time.Clock().tick(60)

            i = i + 1
            # print(i)
