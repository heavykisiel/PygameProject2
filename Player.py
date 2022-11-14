import pygame
import os 

from textures import TextureLoader
from Bullets import Bullets

red = (255, 0, 0)
green = (0, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen, surface_size):
        super().__init__(group)
        self.index = 0
        self.animation_list=[]
        self.action = 0
        animation_folders = ['front','back','right','left']
        
        
        for animation in animation_folders:
            loop_list = []
            filesNumber = len(os.listdir(f'textures/player/{animation}'))
            for i in range (filesNumber):
                img = TextureLoader.Load_Front_Player_Texture(animation,i)
                loop_list.append(img)
            self.animation_list.append(loop_list)  
        
        
        self.image = self.animation_list[self.action][self.index]
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
        # print(self.player_position)
        self.input()
        self.animation()

    def shoot(self):

        if self.shootCooldown == 0:

            self.shootCooldown = 20

            if self.playerDirection == 2:
                bullet = Bullets(self.player_position[0] + (0.1 * self.rect.size[0] * self.playerDirection / 2),
                                 self.player_position[1], 1, self.speedBullet, self.surface_size,
                                 self.player_position[1] + 10000, self.player_position[0])
                print("test")
                self.bulletGroup.add(bullet)
                self.shooting = False
            elif self.playerDirection == -2:
                bullet = Bullets(self.player_position[0] + (0.1 * self.rect.size[0] * self.playerDirection / 2),
                                 self.player_position[1], 1, self.speedBullet, self.surface_size,
                                 self.player_position[1] - 10000, self.player_position[0])

                self.bulletGroup.add(bullet)
                self.shooting = False

            elif self.playerDirection == 1:
                bullet = Bullets(self.player_position[0],
                                 self.player_position[1] + (0.1 * self.rect.size[0] * self.playerDirection), 1,
                                 self.speedBullet, self.surface_size, self.player_position[1],
                                 self.player_position[0] + 1000)

                self.bulletGroup.add(bullet)
                self.shooting = False
            else:
                bullet = Bullets(self.player_position[0],
                                 self.player_position[1] + (0.3 * self.rect.size[0] * self.playerDirection), 1,
                                 self.speedBullet, self.surface_size, self.player_position[1],
                                 self.player_position[0] - 1000)
                print(bullet)

                self.bulletGroup.add(bullet)
                self.shooting = False
