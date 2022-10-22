import pygame
from textures.colors import Colors

Color = Colors()


def LoadingScreenLoadTexture(screen_size):
    bg = pygame.image.load("textures/background_menu.jpg")
    bg = pygame.transform.scale(bg, screen_size)
    return bg


def Load_Block_Textures(block_pixels, id_block):
    if id_block == 0:
        grass_block = pygame.image.load('textures/grass.jpg').convert()
        grass_block = pygame.transform.scale(grass_block, (block_pixels, block_pixels))
        grass_block.set_colorkey((0, 0, 0))
        return grass_block
    elif id_block == 1:
        sand_block = pygame.image.load('textures/sand.jpg').convert()
        sand_block = pygame.transform.scale(sand_block, (block_pixels, block_pixels))
        sand_block.set_colorkey((0, 0, 0))
        return sand_block


def LoadingScreenAnimation(screen, screenSize, i, bg):
    screen.fill((0, 0, 0))
    screen.blit(bg, (i, 0))
    screen.blit(bg, (screenSize[0] + i, 0))
    if i == -screenSize[0]:
        screen.blit(bg, (screenSize[0] + i, 0))
        i = 0
    i -= 1
    return i


def Load_Buttons(self):
    pygame.draw.rect(self.screen, Color.RED, self.buttons[0])
    pygame.draw.rect(self.screen, Color.GREEN, self.buttons[1])
    pygame.draw.rect(self.screen, Color.BLUE, self.buttons[2])
    font = pygame.font.SysFont(None, 64)
    img0 = font.render('   START', True, Color.BLACK)
    img1 = font.render('OPTIONS', True, Color.BLACK)
    img2 = font.render('    QUIT', True, Color.BLACK)
    img3 = font.render('JAREK GAME ', True, Color.GREEN)
    self.screen.blit(img0, self.buttons[0])
    self.screen.blit(img1, self.buttons[1])
    self.screen.blit(img2, self.buttons[2])
    self.screen.blit(img3, (self.screen_size[0] / 3 + 40, self.screen_size[1] / 3))
