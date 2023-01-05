import pygame
from textures.colors import Colors
import os

Color = Colors()


def LoadingScreenLoadTexture(screen_size):
    bg = pygame.image.load("textures/background_menu.jpg").convert()
    bg = pygame.transform.scale(bg, (bg.get_size()[0], screen_size[1]))
    return bg


def Load_Front_Player_Texture():
    animationList = []
    animationFolders = ['front', 'back', 'right', 'left']
    for animation in animationFolders:
        loopList = []
        filesNumber = len(os.listdir(f'textures/player/{animation}'))
        for i in range(filesNumber):
            img = pygame.image.load(f'textures/player/{animation}/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (46, 66))
            img.set_colorkey((246, 246, 246))
            loopList.append(img)
        animationList.append(loopList)
    return animationList


def Load_Bullet_Texture(bulletType):
    animationList = []
    animationFolders = ['attack']
    for animation in animationFolders:
        loopList = []
        filesNumber = len(os.listdir(f'textures/bullet/{bulletType}'))
        for i in range(filesNumber):
            img = pygame.image.load(f'textures/bullet/{bulletType}/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, (18, 18))
            img.set_colorkey((246, 246, 246))
            loopList.append(img)
        animationList.append(loopList)
    return animationList


def Load_Enemy_Texture(name, texSize):
    animationList = []
    animationFolders = ['idle', 'attack', 'death']
    for animation in animationFolders:
        loopList = []
        filesNumber = len(os.listdir(f'textures/enemies/{name}/{animation}'))
        for i in range(filesNumber):
            img = pygame.image.load(f'textures/enemies/{name}/{animation}/{i}.png').convert_alpha()
            img = pygame.transform.scale(img, texSize)
            img.set_colorkey((246, 246, 246))
            loopList.append(img)
        animationList.append(loopList)
    return animationList


def Load_Item_Texture(name):
    loop_list = []
    filesNumber = len(os.listdir(f'textures/items/{name}'))
    for i in range(filesNumber):
        item_img = pygame.image.load(f'textures/items/{name}/{i}.png').convert_alpha()
        item_img = pygame.transform.scale(item_img, (50, 50))
        item_img.set_colorkey((246, 246, 246))
        loop_list.append(item_img)

    return loop_list


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
    # elif id_block == 11:
    #     key_tex = pygame.image.load('textures/items/key_boss.png').convert()
    #     key_tex = pygame.transform.scale(key_tex, (block_pixels_x, block_pixels_y))
    #     key_tex.set_colorkey((255, 255, 255))
    #     return key_tex
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
    elif id_block == 18:  # =>28
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
    elif id_block == 28:  # =>18
        north_west_wall2_tex = pygame.image.load('textures/maptex/North West Corner/North West Bot Wall.png').convert()
        north_west_wall2_tex = pygame.transform.scale(north_west_wall2_tex, (block_pixels_x, block_pixels_y))
        north_west_wall2_tex.set_colorkey((255, 255, 255))
        return north_west_wall2_tex
    elif id_block == 29:
        southWest2_tex = pygame.image.load('textures/maptex/South West Corner/South West Bot Wall.png').convert()
        southWest2_tex = pygame.transform.scale(southWest2_tex, (block_pixels_x, block_pixels_y))
        southWest2_tex.set_colorkey((255, 255, 255))
        return southWest2_tex
    elif id_block == 30:
        southEast2_tex = pygame.image.load('textures/maptex/South East Corner/South East Bot Wall.png').convert()
        southEast2_tex = pygame.transform.scale(southEast2_tex, (block_pixels_x, block_pixels_y))
        southEast2_tex.set_colorkey((255, 255, 255))
        return southEast2_tex
    elif id_block == 31:
        northEastTop_tex = pygame.image.load('textures/maptex/North East Corner/North East Top Wall.png').convert()
        northEastTop_tex = pygame.transform.scale(northEastTop_tex, (block_pixels_x, block_pixels_y))
        northEastTop_tex.set_colorkey((255, 255, 255))
        return northEastTop_tex
    elif id_block == 32:
        southEast2_tex = pygame.image.load('textures/maptex/North East Corner/North East Bot Wall.png').convert()
        southEast2_tex = pygame.transform.scale(southEast2_tex, (block_pixels_x, block_pixels_y))
        southEast2_tex.set_colorkey((255, 255, 255))
        return southEast2_tex
    elif id_block == 33:
        north_wall1Bot_tex = pygame.image.load('textures/maptex/North Wall/v1 North Bot Wall v1.png').convert()
        north_wall1Bot_tex = pygame.transform.scale(north_wall1Bot_tex, (block_pixels_x, block_pixels_y))
        north_wall1Bot_tex.set_colorkey((255, 255, 255))
        return north_wall1Bot_tex
    elif id_block == 34:
        north_wall2Bot_tex = pygame.image.load('textures/maptex/North Wall/V2 North Bot Wall.png').convert()
        north_wall2Bot_tex = pygame.transform.scale(north_wall2Bot_tex, (block_pixels_x, block_pixels_y))
        north_wall2Bot_tex.set_colorkey((255, 255, 255))
        return north_wall2Bot_tex
    elif id_block == 35:
        north_wall3Bot_tex = pygame.image.load('textures/maptex/North Wall/V3 North Bot Wall.png').convert()
        north_wall3Bot_tex = pygame.transform.scale(north_wall3Bot_tex, (block_pixels_x, block_pixels_y))
        north_wall3Bot_tex.set_colorkey((255, 255, 255))
        return north_wall3Bot_tex
    elif id_block == 36:
        south_wall1Top_tex = pygame.image.load('textures/maptex/South Wall/v1 South Bot Wall v1.png').convert()
        south_wall1Top_tex = pygame.transform.scale(south_wall1Top_tex, (block_pixels_x, block_pixels_y))
        south_wall1Top_tex.set_colorkey((255, 255, 255))
        return south_wall1Top_tex
    elif id_block == 37:
        south_wall1Top_tex = pygame.image.load('textures/maptex/South Wall/V1 South Top Wall.png').convert()
        south_wall1Top_tex = pygame.transform.scale(south_wall1Top_tex, (block_pixels_x, block_pixels_y))
        south_wall1Top_tex.set_colorkey((255, 255, 255))
        return south_wall1Top_tex
    elif id_block == 38:
        north_wall2Top_tex = pygame.image.load('textures/maptex/South Wall/V2 South Top Wall.png').convert()
        north_wall2Top_tex = pygame.transform.scale(north_wall2Top_tex, (block_pixels_x, block_pixels_y))
        north_wall2Top_tex.set_colorkey((255, 255, 255))
        return north_wall2Top_tex
    elif id_block == 39:
        north_wall3Top_tex = pygame.image.load('textures/maptex/South Wall/V3 South Top Wall.png').convert()
        north_wall3Top_tex = pygame.transform.scale(north_wall3Top_tex, (block_pixels_x, block_pixels_y))
        north_wall3Top_tex.set_colorkey((255, 255, 255))
        return north_wall3Top_tex
    elif id_block == 40:
        north_wall2Bot_tex = pygame.image.load('textures/maptex/South Wall/V2 South  Bot Wall.png').convert()
        north_wall2Bot_tex = pygame.transform.scale(north_wall2Bot_tex, (block_pixels_x, block_pixels_y))
        north_wall2Bot_tex.set_colorkey((255, 255, 255))
        return north_wall2Bot_tex
    elif id_block == 41:
        north_wall3Bot_tex = pygame.image.load('textures/maptex/South Wall/V3 South  Bot Wall.png').convert()
        north_wall3Bot_tex = pygame.transform.scale(north_wall3Bot_tex, (block_pixels_x, block_pixels_y))
        north_wall3Bot_tex.set_colorkey((255, 255, 255))
        return north_wall3Bot_tex


def LoadingScreenAnimation(screen, screenSize, i, bg):
    screen.fill((0, 0, 0))
    screen.blit(bg, (i, 0))
    screen.blit(bg, (bg.get_size()[0] + i, 0))
    if i == -bg.get_size()[0]:
        screen.blit(bg, (bg.get_size()[0] + i, 0))
        i = 0
    i -= 1
    return i


def blit_text(surface, text, pos, font, color=pygame.Color('black')):

    words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.
def LoadAboutInfo(screen):
    rectText = [screen.get_size()[0] / 7,
                screen.get_size()[1] / 7,
                screen.get_size()[0],
                screen.get_size()[0]]
    font = pygame.font.SysFont('constantia', 64)
    AboutContent = '''
    Autors:
        Nikodem Luto 
        Filip Mielnik 
        Adam Lorek 
        Karol Madejski 
    '''
    label = []
    blit_text(screen, AboutContent, (rectText[0], rectText[1]), font)


def Load_Buttons(self):
    pygame.draw.rect(self.screen, (62, 57, 55), self.buttons[0])
    pygame.draw.rect(self.screen, (62, 57, 55), self.buttons[1])
    pygame.draw.rect(self.screen, (62, 57, 55), self.buttons[2])
    fontButton = pygame.font.SysFont('constantia', 64)
    fontTitle = pygame.font.SysFont('constantia', 72)
    fontTitle2 = pygame.font.SysFont('constantia', 74)
    img0 = fontButton.render('   Start', True, (236, 233, 232))
    img1 = fontButton.render('  About', True, (236, 233, 232))
    img2 = fontButton.render('   Quit', True, (236, 233, 232))
    img3 = fontTitle.render('Wizzard in Dungeon', True, (100, 100, 100))
    img4 = fontTitle2.render('Wizzard in Dungeon', True, (0, 0, 0))
    self.screen.blit(img0, self.buttons[0])
    self.screen.blit(img1, self.buttons[1])
    self.screen.blit(img2, self.buttons[2])
    self.screen.blit(img3, (self.screen_size[0] / 3 - 120, self.screen_size[1] / 3))
    self.screen.blit(img4, (self.screen_size[0] / 3 - 119, self.screen_size[1] / 3))


class TextureUnit:
    def __init__(self, block_pixelsx, block_pixelsy):
        self.Floor_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 0)
        self.floor1_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 12)
        self.floor2_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 13)
        self.floor3_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 14)
        self.eastWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 1)
        self.northWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 2)
        self.southWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 3)
        self.westWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 4)
        self.eastNorthWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 5)
        self.westNorthWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 6)
        self.eastSouthWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 7)
        self.westSouthWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 8)
        self.midWall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 9)
        self.grass_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 10)

        self.westWall1_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 15)
        self.westWall2_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 16)
        self.westWall3_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 17)
        self.northWestwallTop_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 18)
        self.eastWall1_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 19)
        self.eastWall2_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 20)
        self.eastWall3_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 21)
        self.northEastwall_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 22)
        self.northWall1Top_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 23)
        self.northWall2Top_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 24)
        self.northWall3Top_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 25)
        self.southEastTop_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 26)
        self.southWestTop_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 27)
        self.northWestwallBot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 28)
        self.southWestBot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 29)
        self.southEastBot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 30)
        self.northEastTop_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 31)
        self.northEastBot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 32)
        self.northWall1Bot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 33)
        self.northWall2Bot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 34)
        self.northWall3Bot_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 35)
        self.southWall1Bot = Load_Block_Textures(block_pixelsx, block_pixelsy, 36)
        self.south_wall1Top_tex = Load_Block_Textures(block_pixelsx, block_pixelsy, 37)
        self.southWall2Bot = Load_Block_Textures(block_pixelsx, block_pixelsy, 40)

        self.southWall3Bot = Load_Block_Textures(block_pixelsx, block_pixelsy, 41)

        self.key_tex = Load_Item_Texture('key')
        self.heartTex = Load_Item_Texture('heart')

        self.northWallList = list((self.northWall1Top_tex, self.northWall2Top_tex, self.northWall3Top_tex))
        self.westWallList = list((self.westWall1_tex, self.westWall2_tex, self.westWall3_tex))
        self.eastWallList = list((self.eastWall1_tex, self.eastWall2_tex, self.eastWall3_tex))
