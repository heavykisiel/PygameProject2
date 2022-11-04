import pygame
from Gameplay import Gameplay


def button_trigger(buttons, mouse):
    # print(mouse) xy
    i = 0
    for x in buttons:
        if x[0] <= mouse[0] <= x[0] + x[2] and x[1] <= mouse[1] <= x[1] + x[3]:
            return i
        i += 1
    return 404


def button_handler(buttons, self):
    mouse = pygame.mouse.get_pos()
    selected_button_index = button_trigger(buttons, mouse)
    if selected_button_index == 0:
        print(selected_button_index)
    elif selected_button_index == 1:
        print(selected_button_index)
    elif selected_button_index == 2:
        print(selected_button_index)
    elif selected_button_index == 404:
        pass
    else:
        print(selected_button_index)
        raise Exception("index numer should be 0, 1 or 2")

    return selected_button_index

