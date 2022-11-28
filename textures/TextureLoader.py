import pygame
from textures.colors import Colors

Color = Colors()


def LoadingScreenLoadTexture(screen_size):
    bg = pygame.image.load("textures/background_menu.jpg")
    bg = pygame.transform.scale(bg, screen_size)
    return bg


def Load_Front_Player_Texture(side, i):
    player_img = pygame.image.load(f'textures/player/{side}/{i}.png').convert_alpha()
    player_img = pygame.transform.scale(player_img, (46, 66))

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
        floor_block = pygame.image.load('textures/maptex/Floor/floor.png').convert()
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
    elif id_block == 11:
        key_tex = pygame.image.load('textures/items/key_boss.png').convert()
        key_tex = pygame.transform.scale(key_tex, (block_pixels_x, block_pixels_y))
        key_tex.set_colorkey((255, 255, 255))
        return key_tex
    elif id_block == 12:
        floor1_tex = pygame.image.load('textures/maptex/Floor/v1.png').convert()
        floor1_tex = pygame.transform.scale(floor1_tex, (block_pixels_x, block_pixels_y))
        floor1_tex.set_colorkey((255, 255, 255))
        return floor1_tex
    elif id_block == 13:
        floor2_tex = pygame.image.load('textures/maptex/Floor/v2.png').convert()
        floor2_tex = pygame.transform.scale(floor2_tex, (block_pixels_x, block_pixels_y))
        floor2_tex.set_colorkey((255, 255, 255))
        return floor2_tex
    elif id_block == 14:
        floor3_tex = pygame.image.load('textures/maptex/Floor/v3.png').convert()
        floor3_tex = pygame.transform.scale(floor3_tex, (block_pixels_x, block_pixels_y))
        floor3_tex.set_colorkey((255, 255, 255))
        return floor3_tex
    elif id_block == 15:
        west_wall_1 = pygame.image.load('textures/maptex/WestWall/V1 West Wall.png').convert()
        west_wall_1 = pygame.transform.scale(west_wall_1, (block_pixels_x, block_pixels_y))
        west_wall_1.set_colorkey((255, 255, 255))
        return west_wall_1
    elif id_block == 16:
        west_wall_2 = pygame.image.load('textures/maptex/WestWall/V2 West Wall.png').convert()
        west_wall_2 = pygame.transform.scale(west_wall_2, (block_pixels_x, block_pixels_y))
        west_wall_2.set_colorkey((255, 255, 255))
        return west_wall_2
    elif id_block == 17:
        west_wall_3 = pygame.image.load('textures/maptex/WestWall/V3 West Wall.png').convert()
        west_wall_3 = pygame.transform.scale(west_wall_3, (block_pixels_x, block_pixels_y))
        west_wall_3.set_colorkey((255, 255, 255))
        return west_wall_3
    elif id_block == 18:
        north_west_wall_tex = pygame.image.load('textures/maptex/North West Corner/North West Top Wall.png').convert()
        north_west_wall_tex = pygame.transform.scale(north_west_wall_tex, (block_pixels_x, block_pixels_y))
        north_west_wall_tex.set_colorkey((255, 255, 255))
        return north_west_wall_tex
    elif id_block == 19:
        east_wall_1_tex = pygame.image.load('textures/maptex/East Wall/V1 East Wall.png').convert()
        east_wall_1_tex = pygame.transform.scale(east_wall_1_tex, (block_pixels_x, block_pixels_y))
        east_wall_1_tex.set_colorkey((255, 255, 255))
        return east_wall_1_tex
    elif id_block == 20:
        east_wall_2_tex = pygame.image.load('textures/maptex/East Wall/V2 East Wall.png').convert()
        east_wall_2_tex = pygame.transform.scale(east_wall_2_tex, (block_pixels_x, block_pixels_y))
        east_wall_2_tex.set_colorkey((255, 255, 255))
        return east_wall_2_tex
    elif id_block == 21:
        east_wall_3_tex = pygame.image.load('textures/maptex/East Wall/V3 East Wall.png').convert()
        east_wall_3_tex = pygame.transform.scale(east_wall_3_tex, (block_pixels_x, block_pixels_y))
        east_wall_3_tex.set_colorkey((255, 255, 255))
        return east_wall_3_tex
    elif id_block == 22:
        north_east_wall = pygame.image.load('textures/maptex/North East Corner/North East Top Wall.png').convert()
        north_east_wall = pygame.transform.scale(north_east_wall, (block_pixels_x, block_pixels_y))
        north_east_wall.set_colorkey((255, 255, 255))
        return north_east_wall
    elif id_block == 23:
        north_wall1_tex = pygame.image.load('textures/maptex/North Wall/v1 North Top Wall v1.png').convert()
        north_wall1_tex = pygame.transform.scale(north_wall1_tex, (block_pixels_x, block_pixels_y))
        north_wall1_tex.set_colorkey((255, 255, 255))
        return north_wall1_tex
    elif id_block == 24:
        north_wall2_tex = pygame.image.load('textures/maptex/North Wall/V2 North Top Wall.png').convert()
        north_wall2_tex = pygame.transform.scale(north_wall2_tex, (block_pixels_x, block_pixels_y))
        north_wall2_tex.set_colorkey((255, 255, 255))
        return north_wall2_tex
    elif id_block == 25:
        north_wall3_tex = pygame.image.load('textures/maptex/North Wall/V3 North Top Wall.png').convert()
        north_wall3_tex = pygame.transform.scale(north_wall3_tex, (block_pixels_x, block_pixels_y))
        north_wall3_tex.set_colorkey((255, 255, 255))
        return north_wall3_tex
    elif id_block == 26:
        southEast_tex = pygame.image.load('textures/maptex/South East Corner/South East Top Wall.png').convert()
        southEast_tex = pygame.transform.scale(southEast_tex, (block_pixels_x, block_pixels_y))
        southEast_tex.set_colorkey((255, 255, 255))
        return southEast_tex
    elif id_block == 27:
        southWest_tex = pygame.image.load('textures/maptex/South West Corner/South West Top Wall.png').convert()
        southWest_tex = pygame.transform.scale(southWest_tex, (block_pixels_x, block_pixels_y))
        southWest_tex.set_colorkey((255, 255, 255))
        return southWest_tex

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
