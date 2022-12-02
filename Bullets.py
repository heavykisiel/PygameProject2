import pygame
from textures import TextureLoader
import math


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, bulletSpeed, surface_size, targetx, targety,charName, bulletAngle = 0):
        pygame.sprite.Sprite.__init__(self)

        self.animationIndex = 0
        self.loop_list = []
        for i in range(3):
            image = TextureLoader.Load_Bullet_test_Texture(i)
            self.loop_list.append(image)
        self.image = self.loop_list[self.animationIndex]
        self.charName = charName
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        
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
        self.image = self.loop_list[self.animationIndex]
        cooldown = 50
        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            if self.animationIndex < 1:
                self.animationIndex += 1
            else:
                self.animationIndex == 1
                
    def mapCollide(self, chunk):
        if self.rect.x < chunk[0] * 1080 + 40:
            self.kill()
        if self.rect.x > chunk[0] * 1080 + 1020:
            self.kill()
        if self.rect.y < chunk[1]*720+135:
            self.kill()
        if self.rect.y > chunk[1]*720+555:
            self.kill()

    def bossShooting(self,xy, speed, bulletAngle):
        newVec = pygame.math.Vector2()
        newVec.from_polar((speed, bulletAngle))
        return xy + newVec

    def bulletKill(self):
        cooldown = 5
        self.animationIndex = 2
        self.image = self.loop_list[self.animationIndex]

        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.kill()

    def move(self):
        if self.charName == 'boss':
            position = self.bossShooting(self.rect.center, self.speed, -self.bulletAngle)
            self.rect.center = position
        else:
            self.rect.x += int(self.dx)
            self.rect.y += int(self.dy)

    # def actionMetod(self,newIndex):
    #    if newIndex != self.animationIndex:
    #        self.animationIndex = newIndex
    #       self.index = 0
    #       self.time = pygame.time.get_ticks()

    def update(self):
        self.move()
        self.animation()
        # if self.rect.left<15 or self.rect.right > self.surface_size[0]-15: #DO ZROBIENIA PO PRZENIESIU NA LABIRYNT W WYKONANIU NIKODEMA