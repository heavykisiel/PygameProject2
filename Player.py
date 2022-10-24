import pygame


from textures import TextureLoader
from Bullets import Bullets


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = TextureLoader.Load_Player_Texture()
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.player_position = (560, 360)
        # spawn
        self.speed = 16
        self.speedBullet = 2
        self.shootCooldown = 0
        self.lastShot = pygame.time.get_ticks()
        self.bulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.playerDirection = 1

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
            print("LOLOLO")
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
                bullet = Bullets(self.rect.centerx + (0.75 * self.rect.size[0] * (self.playerDirection / 2)),
                                 self.rect.centery, 2, self.playerDirection , self.speedBullet)

                self.bulletGroup.add(bullet)
                self.shooting = False
            else:
                if self.playerDirection == 1:
                    bullet = Bullets(self.rect.centerx,
                                     self.rect.centery + (0.5 * self.rect.size[0] * self.playerDirection), 1,
                                     self.playerDirection, self.speedBullet)

                    self.bulletGroup.add(bullet)
                    self.shooting = False
                else:
                    bullet = Bullets(self.rect.centerx,
                                     self.rect.centery + (0.5 * self.rect.size[0] * self.playerDirection), 1,
                                     self.playerDirection, self.speedBullet)
                    print(bullet)

                    self.bulletGroup.add(bullet)
                    self.shooting = False
