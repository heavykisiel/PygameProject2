import pygame


class Camera(pygame.sprite.Group):

    def __init__(self):
        super().__init__()
        self.screen = pygame.display.get_surface()
        self.zoom_scale = 1
        self.camera_borders = {'left': 200, 'right': 200, 'top': 100, 'bottom': 100}
        self.offset = pygame.math.Vector2()
        l = self.camera_borders['left']
        t = self.camera_borders['top']
        w = self.screen.get_size()[0] - (self.camera_borders['left'] + self.camera_borders['right'])
        h = self.screen.get_size()[1] - (self.camera_borders['top'] + self.camera_borders['bottom'])
        self.keyboard_speed = 16
        self.camera_rect = pygame.Rect(l, t, w, h)

    def draw(self, player):
        self.keyboard_control()

    def keyboard_control(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.camera_rect.x -= self.keyboard_speed
        if keys[pygame.K_d]:
            self.camera_rect.x += self.keyboard_speed
        if keys[pygame.K_w]:
            self.camera_rect.y -= self.keyboard_speed
        if keys[pygame.K_s]:
            self.camera_rect.y += self.keyboard_speed

        self.offset.x = self.camera_rect.left - self.camera_borders['left']
        self.offset.y = self.camera_rect.top - self.camera_borders['top']
