import pygame
import random
import os
from enums import JSON
from textures import TextureLoader
from Bullets import Bullets
from Item import Item
from Player import Player

red = (255, 0, 0)
green = (0, 255, 0)


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen, surface_size, player, enemyName,bulletSpeed,currentChunk):
        super().__init__(group)
        self.enemyName = enemyName
        mobData = ''
        for i in JSON['mobs']:
            if i['name'] ==self.enemyName: 
                mobData = i     
        self.texSize =mobData['textureSize']
        self.type = mobData['type']
        self.index = 0
        self.action = 0
        self.imageList = TextureLoader.Load_Enemy_Texture(self.enemyName,self.texSize)
        self.image = self.imageList[self.action][self.index]
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.direction = pygame.math.Vector2()
        self.surface_size = surface_size
        self.player = player
        self.currentChunk= currentChunk
        self.time = pygame.time.get_ticks()
        self.range = 200
        #spawn
        self.alive = True
        self.health = int(mobData['hp'])
        self.healthMax = int(mobData['hp'])
        self.speed = int(mobData['moveSpeed'])
        
        #move
        self.moving = False
        self.aiMoving = True
        self.tempDirectionX = 1
        self.tempDirectionY = 1
        self.aiMovementSpeed =1
        self.flip= False
        
        #enemy bullets
        self.enemybulletGroup = pygame.sprite.Group()
        self.speedBullet = int(mobData['bulletSpeed'])
        self.bulletType = mobData['bulletType']
        self.shootCooldown = 0
        self.shootAnimationCooldown = 0
        self.shooting = False
        self.bulletAngle = 0
        
        
        self.killEvents = [] #profesor nakamichi 

    def animation(self):
        cooldown = 200
        self.image = self.imageList[self.action][self.index]
        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.imageList[self.action]):
            self.index = 0
            
    def actionMetod(self, newAction):
        if newAction != self.action:
            self.action = newAction
            self.index = 0
            self.time = pygame.time.get_ticks()

    def move(self):
        if self.type == "skeleton":
            if self.moving:
                if self.direction.magnitude() != 0:
                    self.direction = self.direction.normalize()
                self.rect.x += self.direction[0] * self.speed
                self.rect.y += self.direction[1] * self.speed
               
        if self.enemyName == "destroyer":
            if self.moving:
                if self.direction.magnitude() != 0:
                    
                    self.direction = self.direction.normalize() 
                self.rect.x += self.direction[0] * self.speed
                self.rect.y += self.direction[1] * self.speed
            
                
        if self.enemyName =="boss":
            if self.moving:
                if self.direction.magnitude() != 0:
                    self.direction = self.direction.normalize()
                self.rect.x += self.direction[0] * self.speed
                self.rect.y += self.direction[1] * self.speed
                
    def ai(self):
        if self.type == "skeleton":
           if self.aiMoving:
                self.moving = False
                if random.randint(1,50) == 1:
                    self.tempDirectionY *= -1
                if random.randint(1,50) == 2:
                    self.tempDirectionX *= -1
                    
                self.rect.x += self.tempDirectionX * self.aiMovementSpeed
                self.rect.y += self.tempDirectionY * self.aiMovementSpeed
        else:
            if self.aiMoving:
               
                 
                if random.randint(1,100) == 1:
                    self.tempDirectionY *= -1
                if random.randint(1,100) == 2:
                    self.tempDirectionX *= -1
                    
                self.rect.x += self.tempDirectionX * self.aiMovementSpeed
                self.rect.y += self.tempDirectionY * self.aiMovementSpeed
            if not self.aiMoving:
                self.tempDirectionX = 1    
                
    def direction_distance(self, player):
        playerVec = pygame.math.Vector2(player.rect.center)
        enemyVec = pygame.math.Vector2(self.rect.center)
        distance = (playerVec - enemyVec).magnitude()
        vecSum = playerVec - enemyVec
        if vecSum.magnitude() != 0:
            self.direction = (playerVec - enemyVec).normalize()

        return distance, self.direction
      
    def status(self, player):
        self.distance = self.direction_distance(player)[0]
        self.direction = self.direction_distance(player)[1]
        if self.type == "skeleton" and self.alive:
            if self.distance <= self.range:
                self.actionMetod(1)
                if self.action == 1 and self.index == 3:
                    self.shooting = True
                self.moving = False     
            elif self.distance >= self.range:
                self.moving = True
                self.actionMetod(0)  
                
        if self.type == "destroyer" and self.alive:
            if self.distance < 30:
                self.actionMetod(1)
                if self.action == 1 and self.index == 1:
                    self.shooting = True
                self.moving = False
                
            if self.distance > 50:
                self.aiMoving = False
                self.moving = True
                self.actionMetod(0)
                if self.direction[0] < 0:
                    self.flip = True
                if self.direction[0] >0:
                    self.flip = False 
                
            if self.distance > 200:
                if self.tempDirectionX >0:
                    self.flip = False
                
                if self.tempDirectionX <0:
                    self.flip = True 
                self.moving = False
                self.aiMoving = True
                self.ai()
                self.actionMetod(0)
                
        if self.type == "boss" and self.alive:
            if self.distance <= self.range*2:
                self.actionMetod(1)
                if self.action == 1:
                    self.shooting = True
                self.moving = False
            elif self.distance >= self.range:
                self.moving = True
                self.actionMetod(0)  
                
    def mapCollide(self, chunk):
        if self.rect.x < chunk[0] * 1080 + 30:
            self.tempDirectionX *= -1
        if self.rect.x > chunk[0] * 1080 + 990:
            self.tempDirectionX *= -1
        if self.rect.y < chunk[1]*720+125:
            self.tempDirectionY =1
        if self.rect.y > chunk[1]*720+535:
            self.tempDirectionY =-1

    def draw(self, offset):
        self.offset = offset
        self.screen.blit(pygame.transform.flip(self.image,self.flip,False), self.rect.topleft + self.offset)

    def checkAlive(self):
        if self.health <= 0:
            self.moving=False
            self.shooting=False
            self.speed = 0
            self.actionMetod(2)
            if self.type == "boss":
                self.alive = False
                self.kill()
            if self.action == 2 and self.index == 4:
                self.alive = False
                self.kill()
                for event in self.killEvents:
                    event()
            self.health = 0
            self.alive = False
        
    def timer(self):
        if self.shootAnimationCooldown > 0:
            self.shootAnimationCooldown -= 1
        if self.shootCooldown > 0:
            self.shootCooldown -= 1
            self.shooting = False

    def update(self):
        self.timer()
        self.animation()
        self.checkAlive()
        self.move()
        #self.checkDirection()
        
    def shoot(self):
        if self.shooting:
            if self.shootCooldown == 0:
                if self.type =='boss':
                        self.bulletAngle += 10
                        self.shootCooldown=15
                        
                        bullet0 = Bullets(self.rect.centerx,
                                    self.rect.centery, 1, self.speedBullet, self.surface_size,
                                    self.rect.centery + 1000, self.rect.centerx ,self.type,self.bulletType, self.bulletAngle)

                        bullet1 = Bullets(self.rect.centerx,
                                    self.rect.centery, 1, self.speedBullet, self.surface_size,
                                    self.rect.centery + 1000, self.rect.centerx ,self.type,self.bulletType, self.bulletAngle+90)

                        bullet2 = Bullets(self.rect.centerx,
                                    self.rect.centery, 1, self.speedBullet, self.surface_size,
                                    self.rect.centery + 1000, self.rect.centerx ,self.type,self.bulletType, self.bulletAngle+180)

                        bullet3 = Bullets(self.rect.centerx,
                                    self.rect.centery, 1, self.speedBullet, self.surface_size,
                                    self.rect.centery + 1000, self.rect.centerx ,self.type,self.bulletType, self.bulletAngle+270)

                        self.enemybulletGroup.add(bullet0)
                        self.enemybulletGroup.add(bullet1)
                        self.enemybulletGroup.add(bullet2)
                        self.enemybulletGroup.add(bullet3)
                else:
                    self.shootCooldown = 35
                    self.actionMetod(1)
                    if self.direction[0] > 1 or self.direction[0] < -1:
                        bullet = Bullets(self.rect.centerx,
                                        self.rect.centery, 1, 1,self.speedBullet , self.surface_size,
                                        self.player.rect.centery,
                                        self.player.rect.centerx,self.type,self.bulletType)
                        self.enemybulletGroup.add(bullet)
                        self.shooting=False

                    else:
                        if self.direction[1] < 1:
                            bullet = Bullets(self.rect.centerx,
                                            self.rect.centery, 1,
                                            self.speedBullet, self.surface_size, self.player.rect.centery,
                                            self.player.rect.centerx,self.type,self.bulletType)
                            self.enemybulletGroup.add(bullet)
                            self.shooting=False

                        else:
                            bullet = Bullets(self.rect.centerx,
                                            self.rect.centery, 1,
                                            self.speedBullet, self.surface_size, self.player.rect.centery,
                                            self.player.rect.centerx,self.type,self.bulletType)
                            self.enemybulletGroup.add(bullet)
                            self.shooting=False