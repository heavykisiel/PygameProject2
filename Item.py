import pygame
import os
import math

class Item(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen, name, texture):
        super().__init__(group)
        
        self.textureList = texture
        self.index = 0
        self.image = self.textureList[self.index]
        self.position = pos
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.taken = False
        self.name = name
        self.time = pygame.time.get_ticks()
        
    def animation(self):
        cooldown = 200
        self.image = self.textureList[self.index]
        if pygame.time.get_ticks() - self.time > cooldown:
            self.time = pygame.time.get_ticks()
            self.index += 1
        if self.index >= len(self.textureList):
            self.index = 0
    
    
    def following(self,player):
        if player.health <=175:
            vector = pygame.math.Vector2(player.rect.x - self.rect.x,
                                            player.rect.y - self.rect.y)
            if 0 < vector.length() < 200:
                speed = 1 / vector.length() * 250
                vector.normalize_ip() #normalize to its 1 lenght
                vector.scale_to_length(speed) 
                if vector[0] < 1:
                    vector[0] = math.ceil(vector[0]) #Round a number upward to its nearest integer
                if vector[1] < 1:
                    vector[1] = math.ceil(vector[1])
                self.rect.move_ip(*vector)  #changes the pygame.Rect object
            
                  
    def draw(self, ground_offset):
        if not self.taken:
            self.screen.blit(self.image, (self.rect.x, self.rect.y) + ground_offset)

    def __str__(self) -> str:
        return self.name
