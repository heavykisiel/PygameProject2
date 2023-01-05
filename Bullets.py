import pygame
from textures import TextureLoader
import math
import os

class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, bulletSpeed, surface_size, targetx, targety,charName,bulletType, bulletAngle = 0):
        pygame.sprite.Sprite.__init__(self)

        self.animationStopped = True
        self.index = 0
        self.action = 0
        self.bulletType = bulletType
        self.imageList = TextureLoader.Load_Bullet_Texture(self.bulletType)
        self.image = self.imageList[self.action][self.index]
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.charName = charName
        self.speed = bulletSpeed
        self.surface_size = surface_size
        self.shoot = 0
        self.targetx = targetx
        self.targety = targety
        self.time = pygame.time.get_ticks()
        self.angle = math.atan2(self.targetx - self.rect.y, self.targety - self.rect.x)
        self.dx = math.cos(self.angle) * bulletSpeed
        self.dy = math.sin(self.angle) * bulletSpeed
        self.bulletAngle = bulletAngle
        
    def animation(self):
        cooldown = 50
        self.image = self.imageList[self.action][self.index]
        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.imageList[self.action]):
            self.index = 0
                
                
    def mapCollide(self, chunk):
        if self.rect.x < chunk[0] * 1080 + 40:
            self.kill()
        if self.rect.x > chunk[0] * 1080 + 1020:
            self.kill()
        if self.rect.y < chunk[1]*720+125:
            self.kill()
        if self.rect.y > chunk[1]*720+585:
            self.kill()

    def bossShooting(self,xy, speed, bulletAngle):
        newVec = pygame.math.Vector2()
        newVec.from_polar((speed, bulletAngle))
        return xy + newVec

    def move(self):
        if self.charName == 'boss':
            position = self.bossShooting(self.rect.center, self.speed, -self.bulletAngle)
            self.rect.center = position
        else:
            self.rect.x += int(self.dx)
            self.rect.y += int(self.dy)

 
    def update(self):
        self.move()
        self.animation()