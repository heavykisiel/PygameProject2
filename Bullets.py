import pygame
from textures import TextureLoader
import math


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed, surface_size, targetx, targety):
        pygame.sprite.Sprite.__init__(self)

        self.animationIndex = 0
        self.loop_list = []
        for i in range(3):
            image = TextureLoader.Load_Bullet_test_Texture(i)
            self.loop_list.append(image)
        self.image = self.loop_list[self.animationIndex]

        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        # self.surface_size = surface_size
        self.speed = speed
        self.surface_size = surface_size
        self.speedBullet = 2
        self.shoot = 0
        self.targetx = targetx
        self.targety = targety
        self.offset = 100
        self.time = pygame.time.get_ticks()
        self.angle = math.atan2(self.targetx - self.rect.y, self.targety - self.rect.x)
        self.dx = math.cos(self.angle) * speed
        self.dy = math.sin(self.angle) * speed

    def animation(self):
        self.image = self.loop_list[self.animationIndex]
        cooldown = 50
        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            if self.animationIndex < 1:
                self.animationIndex += 1
            else:
                self.animationIndex == 1

    def bulletKill(self):
        cooldown = 5
        self.animationIndex = 2
        self.image = self.loop_list[self.animationIndex]

        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.kill()

    def move(self):
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
