import pygame
from textures import TextureLoader
import math
class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, speed,surface_size,targetx,targety):
        pygame.sprite.Sprite.__init__(self)
        image = TextureLoader.Load_Bullet_test_Texture()
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.surface_size = surface_size
        self.speed = speed
        self.speedBullet = 2
        self.shoot = 0
        self.targetx = targetx
        self.targety = targety
        
        angle = math.atan2(self.targetx-self.rect.y,self.targety-self.rect.x)
        self.dx = math.cos(angle)*speed
        self.dy = math.sin(angle)*speed
        
    def move(self):
        self.rect.x += int(self.dx)
        self.rect.y += int(self.dy)
        
        
    def update(self):
        self.move()
        
        if self.rect.left<15 or self.rect.right > self.surface_size[0]-15: #DO ZROBIENIA PO PRZENIESIU NA LABIRYNT W WYKONANIU NIKODEMA
            self.kill()
    
            