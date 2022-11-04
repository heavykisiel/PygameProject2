import pygame

from textures import TextureLoader
from Bullets import Bullets

red = (255, 0, 0)
green = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen, surface_size):
        super().__init__(group)
        self.image = TextureLoader.Load_Player_Texture()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.playerDirection = 1
        self.player_position = pos
        self.screen = screen
        self.surface_size = surface_size
        # spawn
        self.speed = 16
        self.speedBullet = 32
        self.shootCooldown = 0
        self.alive = True
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        self.lastShot = pygame.time.get_ticks()
        self.bulletGroup = pygame.sprite.Group()
        self.shooting = False

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.playerDirection = -2
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.playerDirection = 2
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

            self.playerDirection = 1
        elif keys[pygame.K_LEFT]:
            self.playerDirection = -1
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
            print("1231231231231231223LOLOLO")
            self.shooting = True

    def update(self):
        if self.shootCooldown > 0:
            self.shootCooldown -= 1
        self.input()

    def shoot(self):

        if self.shootCooldown == 0:
            print("XDDDDD")
            self.shootCooldown = 20
            if self.playerDirection == 2 or self.playerDirection == -2:
                bullet = Bullets(self.player_position[0] + (0.1 * self.rect.size[0] * (self.playerDirection / 2)),
                                 self.player_position[1], 1, self.playerDirection, self.speedBullet, self.surface_size)

                self.bulletGroup.add(bullet)
                self.shooting = False
            else:
                if self.playerDirection == 1:
                    bullet = Bullets(self.player_position[0],
                                     self.player_position[1] + (0.1 * self.rect.size[0] * self.playerDirection), 1,
                                     self.playerDirection, self.speedBullet, self.surface_size)

                    self.bulletGroup.add(bullet)
                    self.shooting = False
                else:
                    bullet = Bullets(self.player_position[0],
                                     self.player_position[1] + (0.1 * self.rect.size[0] * self.playerDirection), 1,
                                     self.playerDirection, self.speedBullet, self.surface_size)
                    print(bullet)

                    self.bulletGroup.add(bullet)
                    self.shooting = False
