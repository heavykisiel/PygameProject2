import pygame
import os

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
            
    def draw(self, ground_offset):
        if not self.taken:
            self.screen.blit(self.image, (self.rect.x, self.rect.y) + ground_offset)

    # def pickup(self):
    #     self.taken = True

    def __str__(self) -> str:
        return self.name
