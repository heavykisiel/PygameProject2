import pygame
import os

from textures import TextureLoader
from Bullets import Bullets

red = (255, 0, 0)
green = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self,pos, group, screen, surface_size):
        super().__init__(group)
        
       
        
        
        self.index = 0
        self.animation_list = []
        self.action = 0
        animation_folders = ['front', 'back', 'right', 'left']

        for animation in animation_folders:
            loop_list = []
            filesNumber = len(os.listdir(f'textures/player/{animation}'))
            for i in range(filesNumber):
                img = TextureLoader.Load_Front_Player_Texture(animation, i)
                loop_list.append(img)
            self.animation_list.append(loop_list)

        self.image = self.animation_list[self.action][self.index]
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.playerDirection = 1
        self.screen = screen
        self.surface_size = surface_size
        
        # spawn
        self.speed = 16
        self.speedBullet = 32
        self.shootCooldown = 0
        self.shootSpaceCooldown=0
        self.alive = True
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        self.lastShot = pygame.time.get_ticks()
        self.bulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.time = pygame.time.get_ticks()

    def animation(self):
        cooldown = 100
        self.image = self.animation_list[self.action][self.index]

        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.index += 1
            self.side = 2
        if self.index >= len(self.animation_list[self.action]):
            self.index = 0

    def actionMetod(self, newAction):
        if newAction != self.action:
            self.action = newAction
            self.index = 0
            self.time = pygame.time.get_ticks()

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
            self.playerDirection = -2
            self.actionMetod(1)
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
            self.playerDirection = 2
            self.actionMetod(0)
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.playerDirection = 1
            self.actionMetod(2)
        elif keys[pygame.K_LEFT]:
            self.playerDirection = -1
            self.direction.x = -1
            self.actionMetod(3)
        else:
            self.direction.x = 0
        if keys[pygame.K_SPACE]:
           if self.shootCooldown == 0:
                self.shootCooldown = 1
                self.shooting = True

    def update(self):
        if self.shootCooldown > 0:
            self.shootCooldown -= 1
        if self.shootSpaceCooldown >0:
            self.shootSpaceCooldown -=1
        # print(self.player_position)
        self.input()
        self.animation()

    def shoot(self,offset):

        if self.shootCooldown == 0:
            
            self.shootCooldown = 20

            if self.playerDirection == 2:
                print("TEEEEEEEEEEEEEEEEST")
                bullet = Bullets(self.rect.centerx+offset[0] + (0.1 * self.rect.size[0] * self.playerDirection / 2),
                                 self.rect.centery+offset[1], 1, self.speedBullet,self.surface_size,
                                 self.rect.centery + 10000+offset[1], self.rect.centerx+offset[0])
                print("test")
                self.bulletGroup.add(bullet)
                self.shooting = False
            elif self.playerDirection == -2:
                print("TEEEEEEEEEEEEEEEEST")
                bullet = Bullets(self.rect.x + (0.1 * self.rect.size[0] * self.playerDirection / 2)+offset[0],
                                 self.rect.y+offset[1], 1, self.speedBullet, self.surface_size,
                                 self.rect.y - 10000+offset[1], self.rect.x+offset[0])

                self.bulletGroup.add(bullet)
                self.shooting = False
                print(self.bulletGroup)
            elif self.playerDirection == 1:
                
                bullet = Bullets(self.rect.centerx+offset[0],
                                 self.rect.centery + (0.1 * self.rect.size[0] * self.playerDirection)+offset[1], 1,
                                 self.speedBullet, self.surface_size, self.rect.centery+offset[1],
                                 self.rect.centerx + 1000+offset[0])

                self.bulletGroup.add(bullet)
                self.shooting = False
                print(self.bulletGroup)
            else:
                bullet = Bullets(self.rect.centerx+offset[0],
                                 
                                 self.rect.centery + (0.3 * self.rect.size[0] * self.playerDirection)+offset[1], 1,
                                 self.speedBullet, self.surface_size, self.rect.centery+offset[1],
                                 self.rect.centerx - 1000+offset[0])
                
                print(self.bulletGroup)

                self.bulletGroup.add(bullet)
                self.shooting = False
