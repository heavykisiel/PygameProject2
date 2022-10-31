import pygame

from textures import TextureLoader
from Bullets import Bullets
red = (255,0,0)
green = (0,255,0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group,screen):
        super().__init__(group)
        self.image = TextureLoader.Load_Enemy_Texture()
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.direction = pygame.math.Vector2()
        self.enemy_position = pos
        self.alive = True
        # spawn
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        self.speed = 16
        self.speedBullet = 32
        self.shootCooldown = 0
        self.lastShot = pygame.time.get_ticks()
        self.bulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.enemyDirection = 1
        
    def draw(self):
        self.screen.blit(self.image, self.rect)
    
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.kill()
    
    def update(self):
        self.check_alive()
        