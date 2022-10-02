from pygame.locals import *
from textures.TextureLoader import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

key_dict = {K_k: BLACK, K_r: RED, K_g: GREEN, K_b: BLUE,
            K_y: YELLOW, K_c: CYAN, K_m: MAGENTA, K_w: WHITE}


class App:
    """Create App"""

    def __init__(self):
        pygame.init()
        self.screen_size = 1080, 720
        self.screen = pygame.display.set_mode(self.screen_size)

        caption = "Jarek Game"
        pygame.display.set_caption(caption)
        self.screen.fill(BLACK)
        self.width_b = 1 / 5 * self.screen_size[0]
        self.height_b = 1 / 8 * self.screen_size[1]
        self.buttons = [
            [self.screen_size[0] / 2 + self.width_b / 2 - self.width_b, self.screen_size[1] / 2 + self.height_b / 2,
             self.width_b,
             self.height_b],
            [self.screen_size[0] / 2 + self.width_b / 2 - self.width_b,
             self.screen_size[1] / 2 + self.height_b / 2 + 1.2 * self.height_b,
             self.width_b, self.height_b],
            [self.screen_size[0] / 2 + self.width_b / 2 - self.width_b,
             self.screen_size[1] / 2 + self.height_b / 2 + 2.4 * self.height_b,
             self.width_b, self.height_b]]

        # gameState = ["playing", "menu", "options", "quit"]
        self.bg = LoadingScreenLoadTexture(self.screen_size)

    def run(self):
        """run main event loop"""
        running = True
        i = 0
        while running:
            pygame.time.Clock().tick(60)  # tickrate
            i = LoadingScreenAnimation(self.screen, self.screen_size, i, self.bg)
            # https://www.askpython.com/python-modules/pygame-looping-background
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False

            pygame.draw.rect(self.screen, RED, self.buttons[0])
            pygame.draw.rect(self.screen, GREEN, self.buttons[1])
            pygame.draw.rect(self.screen, BLUE, self.buttons[2])

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    App().run()
