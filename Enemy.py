import pygame
import random
import os

from textures import TextureLoader
from Bullets import Bullets
from Player import Player

red = (255, 0, 0)
green = (0, 255, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen, surface_size, player, enemyName, speed):
        super().__init__(group)

        self.enemyName = enemyName

        self.index = 0
        self.animation_list = []
        self.action = 0
        animation_folders = ['idle', 'attack']
        for animation in animation_folders:
            loop_list = []
            self.filesNumber = len(os.listdir(f'textures/enemies/{self.enemyName}/{animation}'))
            for i in range(self.filesNumber):
                img = TextureLoader.Load_Enemy_Texture(self.enemyName, animation, i)
                loop_list.append(img)
            self.animation_list.append(loop_list)

        self.image = self.animation_list[self.action][self.index]
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.direction = pygame.math.Vector2()
        self.alive = True
        self.surface_size = surface_size
        self.player = player
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        self.speed = speed
        self.speedBullet = 32
        self.shootCooldown = 0
        self.enemybulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.moving = False
        self.range = 200
        self.time = pygame.time.get_ticks()
        self.shootAnimationCooldown = 0
        self.rangeTest = 20

    def animation(self):
        cooldown = 300
        self.image = self.animation_list[self.action][self.index]
        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.index += 1

        if self.index >= len(self.animation_list[self.action]):
            self.index = 0


    def actionMetod(self, newAction):
        if newAction != self.action:
            self.action = newAction
            self.index = 0
            self.time = pygame.time.get_ticks()

    def move(self):

        if self.enemyName == "skeleton":
            if self.moving:

                if self.direction.magnitude() != 0:
                    self.direction = self.direction.normalize()
                if self.distance >= 100:
                    self.rect.x += self.direction[0] * self.speed
                    self.rect.y += self.direction[1] * self.speed

        if self.enemyName == "destroyer":
            if self.moving:

                if self.direction.magnitude() != 0:
                    self.direction = self.direction.normalize()
                if self.distance >= 30:
                    self.rect.x += self.direction[0] * self.speed
                    self.rect.y += self.direction[1] * self.speed

    def ai(self):
        if self.moving:
            pass

    def direction_distance(self, player):
        player_vec = pygame.math.Vector2(player.rect.center)
        enemy_vec = pygame.math.Vector2(self.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        vecSum = player_vec - enemy_vec
        if vecSum.magnitude() != 0:
            self.direction = (player_vec - enemy_vec).normalize()

        return distance, self.direction

    def status(self, player):
        self.distance = self.direction_distance(player)[0]

        if self.enemyName == "skeleton":
            if self.distance <= self.range:
                self.actionMetod(1)
                if self.action == 1 and self.index == (self.filesNumber - 1):
                    self.shooting = True
                self.moving = False
            elif self.distance >= self.range:
                self.moving = True
                self.actionMetod(0)
                self.ai()
        if self.enemyName == "destroyer":
            if self.distance < 30:
                self.actionMetod(1)
                if self.action == 1 and self.index == (self.filesNumber - 2):
                    self.shooting = True
                self.moving = False
            if self.distance > 50:
                self.moving = True
                self.actionMetod(0)
            if self.distance > 200:
                self.moving = False
                self.actionMetod(0)

    def mapCollide(self, chunk):
        if self.rect.x < chunk[0] * 1080 + 30:
            self.rect.x += self.speed
        if self.rect.x > chunk[0] * 1080 + 990:
            self.rect.x -= self.speed

    def draw(self, offset):
        self.offset = offset
        self.screen.blit(self.image, self.rect.topleft + self.offset)

    def respawn(self):
        self.rect[0] = random.randrange(0, 600)
        self.rect[1] = random.randrange(0, 600)

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.kill()

    def timer(self):
        if self.shootAnimationCooldown > 0:
            self.shootAnimationCooldown -= 1
        if self.shootCooldown > 0:
            self.shootCooldown -= 1
            self.shooting = False

    def update(self):
        self.timer()
        self.animation()
        self.check_alive()
        self.move()

    def shoot(self):
        if self.shooting:
            if self.shootCooldown == 0:
                self.shootCooldown = 35
                self.actionMetod(1)
                if self.direction[0] > 1 or self.direction[0] < -1:
                    bullet = Bullets(self.rect.centerx(0.75 * self.rect.size[0] * self.direction[0]),
                                     self.rect.centery, 1, 1, self.speedBullet, self.surface_size,
                                     self.player.rect.centery,
                                     self.player.rect.centerx)
                    self.enemybulletGroup.add(bullet)
                    self.shooting = False

                else:
                    if self.direction[1] < 1:
                        bullet = Bullets(self.rect.centerx,
                                         self.rect.centery + (0.1 * self.rect.size[1] * self.direction[1]), 1,
                                         self.speedBullet, self.surface_size, self.player.rect.centery,
                                         self.player.rect.centerx)
                        self.enemybulletGroup.add(bullet)
                        self.shooting = False

                    else:
                        bullet = Bullets(self.rect.centerx,
                                         self.rect.centery + (0.1 * self.rect.size[1] * self.direction[1]), 1,
                                         self.speedBullet, self.surface_size, self.player.rect.centery,
                                         self.player.rect.centerx)
                        self.enemybulletGroup.add(bullet)
                        self.shooting = False
