import pygame

from textures import TextureLoader
from Bullets import Bullets


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = TextureLoader.Load_Enemy_Texture()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.enemy_position = pos
        # spawn
        self.speed = 16
        self.speedBullet = 32
        self.shootCooldown = 0
        self.lastShot = pygame.time.get_ticks()
        self.bulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.enemyDirection = 1
