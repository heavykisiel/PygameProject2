import pygame
import random

from textures import TextureLoader
from Bullets import Bullets
from Player import Player

red = (255,0,0)
green = (0,255,0)
class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group,screen,surface_size,player,enemyName):
        super().__init__(group)
        
        
        self.enemyName = enemyName 
        self.image = TextureLoader.Load_Enemy_Texture(self.enemyName)
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.direction = pygame.math.Vector2()
        self.alive = True
        self.surface_size=surface_size
        self.player = player
        self.health = 100
        self.healthMax = 100
        self.healthMin = self.health
        self.speed = 4
        self.speedBullet = 32
        self.shootCooldown = 0
        self.lastShot = pygame.time.get_ticks()
        self.enemybulletGroup = pygame.sprite.Group()
        self.shooting = False
        self.moving = False
        self.range = 200
        
        
        
        
    def move(self):
        print(self.rect.center)
        if self.enemyName == "bulbazaurus":
            if self.moving:
                
                if self.direction.magnitude() != 0:
                    self.direction = self.direction.normalize()
                if self.distance >= 100:
                    self.rect.x += self.direction[0] * self.speed
                    self.rect.y += self.direction[1] * self.speed
                    
                
        if self.enemyName == "ogier":
            if self.moving:
                if self.direction.magnitude() != 0:
                    self.direction = self.direction.normalize()
                if self.distance >= 100:
                    self.rect.x += self.direction[0] * self.speed
                    self.rect.y += self.direction[1] * self.speed
                    
    def ai(self):
        if self.moving == True:
            pass
        
                
    def direction_distance(self,player):
        player_vec = pygame.math.Vector2(player.rect.center)
        enemy_vec = pygame.math.Vector2(self.rect.center)
        distance = (player_vec - enemy_vec).magnitude()
        vecSum = player_vec - enemy_vec
        if vecSum.magnitude() != 0:
                self.direction = (player_vec - enemy_vec).normalize()
                
        return distance, self.direction
    
    def status(self,player):
        self.distance = self.direction_distance(player)[0]    
        if self.distance <=self.range:
            self.shoot()
            self.moving = True
        elif self.distance >= 2*self.range:
            self.moving = False
            self.ai()
            
    def draw(self,offset):
        self.offset = offset
        self.screen.blit(self.image, self.rect.topleft+offset)
        
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
            
        self.check_alive()
        self.move()
            
    def shoot(self):

        if self.shootCooldown == 0: 
            self.shootCooldown = 30 
            if self.direction[0] > 1 or self.direction[0] < -1:
                bullet = Bullets(self.rect.centerx(0.75 * self.rect.size[0]*self.direction[0]) + self.offset[0],
                                 self.rect.centery+ self.offset[1], 1, 1, self.speedBullet,self.surface_size,self.player.rect.centery,self.player.rect.centerx)
                self.enemybulletGroup.add(bullet)
                
                
            
            else:
                if self.direction[1]< 1:
                    bullet = Bullets(self.rect.centerx,
                                     self.rect.centery + (0.1 * self.rect.size[1] * self.direction[1]), 1,
                                      self.speedBullet,self.surface_size,self.player.rect.centery,self.player.rect.centerx)

                    self.enemybulletGroup.add(bullet)
                    
                    
                else:
                    bullet = Bullets(self.rect.centerx,
                                     self.rect.centery + (0.1 * self.rect.size[1] * self.direction[1]), 1,
                                     self.speedBullet,self.surface_size,self.player.rect.centery,self.player.rect.centerx)

                    self.enemybulletGroup.add(bullet)
                     
                    
              