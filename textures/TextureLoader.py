import pygame
from textures.colors import Colors

Color = Colors()


def LoadingScreenLoadTexture(screen_size):
    bg = pygame.image.load("textures/background_menu.jpg")
    bg = pygame.transform.scale(bg, screen_size)
    return bg


def Load_Front_Player_Texture(side, i):
    player_img = pygame.image.load(f'textures/player/{side}/{i}.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (36, 56))

    player_img.set_colorkey((246, 246, 246))
    return player_img


def Load_Bullet_test_Texture(i):
    player_img = pygame.image.load(f'textures/bullet/{i}.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (20, 20))
    player_img.set_colorkey((246, 246, 246))

    return player_img


def Load_Enemy_Texture(name,side,i):
    enemy_img = pygame.image.load(f'textures/enemies/{name}/{side}/{i}.png').convert_alpha()
    enemy_img = pygame.transform.scale(enemy_img, (64, 64))
    enemy_img.set_colorkey((246, 246, 246))

    return enemy_img


def Load_Block_Textures(block_pixels_x, block_pixels_y, id_block):
    if id_block == 0:
        floor_block = pygame.image.load('textures/maptex/floor.png').convert()
        floor_block = pygame.transform.scale(floor_block, (block_pixels_x, block_pixels_y))
        floor_block.set_colorkey((0, 0, 0))
        return floor_block
    elif id_block == 1:
        wall_e_block = pygame.image.load('textures/maptex/E.png').convert()
        wall_e_block = pygame.transform.scale(wall_e_block, (block_pixels_x, block_pixels_y))
        wall_e_block.set_colorkey((0, 0, 0))
        return wall_e_block
    elif id_block == 2:
        wall_n_block = pygame.image.load('textures/maptex/N.png').convert()
        wall_n_block = pygame.transform.scale(wall_n_block, (block_pixels_x, block_pixels_y))
        wall_n_block.set_colorkey((0, 0, 0))
        return wall_n_block
    elif id_block == 3:
        wall_s_block = pygame.image.load('textures/maptex/S.png').convert()
        wall_s_block = pygame.transform.scale(wall_s_block, (block_pixels_x, block_pixels_y))
        wall_s_block.set_colorkey((0, 0, 0))
        return wall_s_block
    elif id_block == 4:
        wall_w_block = pygame.image.load('textures/maptex/W.png').convert()
        wall_w_block = pygame.transform.scale(wall_w_block, (block_pixels_x, block_pixels_y))
        wall_w_block.set_colorkey((0, 0, 0))
        return wall_w_block
    elif id_block == 5:
        wall_ne_block = pygame.image.load('textures/maptex/NE.png').convert()
        wall_ne_block = pygame.transform.scale(wall_ne_block, (block_pixels_x, block_pixels_y))
        wall_ne_block.set_colorkey((0, 0, 0))
        return wall_ne_block
    elif id_block == 6:
        wall_we_block = pygame.image.load('textures/maptex/NW.png').convert()
        wall_we_block = pygame.transform.scale(wall_we_block, (block_pixels_x, block_pixels_y))
        wall_we_block.set_colorkey((0, 0, 0))
        return wall_we_block
    elif id_block == 7:
        wall_se_block = pygame.image.load('textures/maptex/SE.png').convert()
        wall_se_block = pygame.transform.scale(wall_se_block, (block_pixels_x, block_pixels_y))
        wall_se_block.set_colorkey((0, 0, 0))
        return wall_se_block
    elif id_block == 8:
        wall_sw_block = pygame.image.load('textures/maptex/SW.png').convert()
        wall_sw_block = pygame.transform.scale(wall_sw_block, (block_pixels_x, block_pixels_y))
        wall_sw_block.set_colorkey((0, 0, 0))
        return wall_sw_block
    elif id_block == 9:
        wall_block_block = pygame.image.load('textures/maptex/MID.png').convert()
        wall_block_block = pygame.transform.scale(wall_block_block, (block_pixels_x, block_pixels_y))
        return wall_block_block
    elif id_block == 10:
        grass_block = pygame.image.load('textures/grass.jpg').convert()
        grass_block = pygame.transform.scale(grass_block, (block_pixels_x, block_pixels_y))
        return grass_block


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
