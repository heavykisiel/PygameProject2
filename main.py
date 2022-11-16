from pygame.locals import *

from Gameplay.Gameplay import Gameplay
from buttonHandler import button_handler
from textures.TextureLoader import *
from textures.colors import Colors
from sys import exit


class App:
    """Create App"""

    def __init__(self):
        pygame.init()
        self.screen_size = 1080, 720
        self.screen = pygame.display.set_mode(self.screen_size)
        self.Colors = Colors()

        caption = "Jarek Game"
        pygame.display.set_caption(caption)
        self.screen.fill(Colors.BLACK)
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

        self.gameState = {
            0: "playing",
            1: "options",
            2: "quit",
            3: "menu"
        }

        self.current_Game_State = self.gameState[3]
        self.bg = LoadingScreenLoadTexture(self.screen_size)

    def run(self):
        """run main event loop"""
        running = True
        i = 0
        gameplay_instance = None
        while running:
            pygame.time.Clock().tick(60)  # tickrate
            if self.current_Game_State == "playing":
                if gameplay_instance is not None:
                    gameplay_instance.run()
                    running = False
            if self.current_Game_State == "menu":
                i = LoadingScreenAnimation(self.screen, self.screen_size, i, self.bg)
                Load_Buttons(self)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        selected_button_index = button_handler(self.buttons)
                        if selected_button_index == 404:
                            pass
                        else:
                            self.current_Game_State = self.gameState[selected_button_index]
            elif self.current_Game_State == "playing" and gameplay_instance is None:
                gameplay_instance = Gameplay(self.screen)
            elif self.current_Game_State == "quit":
                running = False
                pygame.display.quit()
                pygame.quit()
                exit()
            elif self.current_Game_State == "options":
                for event in pygame.event.get():
                    if event.type == QUIT:
                        running = False
                    print("options")

            pygame.display.update()

        pygame.quit()


if __name__ == '__main__':
    App().run()
