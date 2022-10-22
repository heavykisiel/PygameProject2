import pygame


class Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.zoom_scale = 1

    def draw(self, player):
        self.zoom_keyboard_control()
        for sprite in self.sprites():
            self.screen.blit(sprite.image, sprite.rect)

    def zoom_keyboard_control(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_q]:
            self.zoom_scale += 0.1
        if keys[pygame.K_e]:
            self.zoom_scale -= 0.1
