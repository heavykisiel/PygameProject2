import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__(group)
        self.image = pygame.image.load('textures/player.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (20, 20))
        self.image.set_colorkey((246, 246, 246))
        self.rect = self.image.get_rect(center=pos)
        self.direction = pygame.math.Vector2()
        self.player_position = (0, 0)
        self.speed = 16
        # można zmieniać speed

    def input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def update(self):
        self.input()
