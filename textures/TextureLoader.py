import pygame


def LoadingScreenLoadTexture(screen_size):
    bg = pygame.image.load("textures/background_menu.jpg")
    bg = pygame.transform.scale(bg, screen_size)
    return bg


def LoadingScreenAnimation(screen, screenSize, i, bg):
    screen.fill((0, 0, 0))
    screen.blit(bg, (i, 0))
    screen.blit(bg, (screenSize[0] + i, 0))
    if i == -screenSize[0]:
        screen.blit(bg, (screenSize[0] + i, 0))
        print(pygame.mouse.get_pos(), bg.get_width(), bg.get_height())
        i = 0
    i -= 1
    return i
