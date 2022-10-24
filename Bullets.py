import pygame
from textures import TextureLoader


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y, scale, direction, speed):
        pygame.sprite.Sprite.__init__(self)
        image = TextureLoader.Load_Bullet_test_Texture()
        self.image = pygame.transform.scale(image, (int(image.get_width() * scale), int(image.get_height() * scale)))
        self.rect = self.image.get_rect()
        self.rect.center = [x, y]
        self.speed = speed
        self.direction = direction
        self.speedBullet = 2
        self.shoot = 0

    def update(self):
        if self.direction == 1 or self.direction == -1:
            self.rect.x += (self.direction * self.speed)
        if self.direction == 2 or self.direction == -2:
            self.rect.y += ((self.direction / 2) * self.speed)
