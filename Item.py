import pygame


class Item(pygame.sprite.Sprite):
    def __init__(self, pos, group, screen, name, texture):
        super().__init__(group)

        self.image = texture
        self.position = pos
        self.rect = self.image.get_rect(center=pos)
        self.screen = screen
        self.taken = False
        self.name = name

    def draw(self, ground_offset):
        if not self.taken:
            self.screen.blit(self.image, (self.rect.x, self.rect.y) + ground_offset)

    # def pickup(self):
    #     self.taken = True

    def __str__(self) -> str:
        return self.name
