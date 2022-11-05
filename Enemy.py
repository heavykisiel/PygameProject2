import pygame
import random

from textures import TextureLoader
from Bullets import Bullets
from Player import Player

red = (255,0,0)
green = (0,255,0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group,screen,surface_size,player):
        super().__init__(group)
        self.image = TextureLoader.Load_Enemy_Texture()
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.direction = pygame.math.Vector2()
        self.enemy_position = pos
        self.alive = True
        self.attackRadius = 50
        self.noticeRadius = 250
        self.surface_size=surface_size
        self.player = player
        # spawn
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        self.speed = 16
        self.speedBullet = 32
        self.shootCooldown = 0
        self.lastShot = pygame.time.get_ticks()
        self.enemybulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.enemyDirection = 1
        
        #range
        self.range = 200
    def move(self):
        pass     
        
    def direction_distance(self,player):
        player_vec = pygame.math.Vector2(player.player_position)
        enemy_vec = pygame.math.Vector2(self.enemy_position)
        distance = (player_vec - enemy_vec).magnitude()
        self.direction = (player_vec - enemy_vec).normalize()
        
        #if distance >0:
        #    direction = (player_vec - enemy_vec).normalize()
        #else:
        #    direction = pygame.math.Vector2()
        #print(player_vec)
        #print(enemy_vec)
        #print(distance)
        #print(self.direction)
        return distance, self.direction
    
    def status(self,player):
        distance = self.direction_distance(player)[0]    
        if distance <=self.range:
            self.shoot()
            pass
            
    def draw(self):
        
        self.screen.blit(self.image, self.rect)
        
    def respawn(self):
        self.rect[0]= random.randrange(0,600)
        self.rect [1]= random.randrange(0,600)

    
    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
            self.kill()
    
    def update(self):
        if self.shootCooldown > 0:
            self.shootCooldown -= 1
            self.shooting = False
            print(self.shootCooldown)
        self.check_alive()
        
        
    # def rangeCollide(self,player):
    #     if self.alive:
    #         if self.direction_distance(player)[0] < self.range:
    #             self.shooting = True
    #             self.shoot()
                
                
            
    def shoot(self):

        if self.shootCooldown == 0: 
            self.shootCooldown = 30 
            if self.direction[0] > 1 or self.direction[0] < -1:
                bullet = Bullets(self.enemy_position[0],
                                 self.enemy_position[1], 1, 1, self.speedBullet,self.surface_size,self.player.player_position[1],self.player.player_position[0])
                self.enemybulletGroup.add(bullet)
                
                
            
            else:
                if self.direction[1]< 1:
                    bullet = Bullets(self.enemy_position[0],
                                     self.enemy_position[1] + (0.1 * self.rect.size[0] * self.direction[0]), 1,
                                      self.speedBullet,self.surface_size,self.player.player_position[1],self.player.player_position[0])

                    self.enemybulletGroup.add(bullet)
                    
                    
                else:
                    bullet = Bullets(self.enemy_position[0],
                                     self.enemy_position[1] + (0.1 * self.rect.size[0] * self.direction[0]), 1,
                                     self.speedBullet,self.surface_size,self.player.player_postiion[1],self.player.player_position[0])

                    self.enemybulletGroup.add(bullet)
                     
                    
              