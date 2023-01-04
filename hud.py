import pygame


class HUD:
    def __init__(self):
        self.speed = 15
        self.window_x = 720
        self.window_y = 480
        self.colors = {'black': pygame.Color(0, 0, 0),
                       'white': pygame.Color(255, 255, 255),
                       'red': pygame.Color(255, 0, 0),
                       'green': pygame.Color(0, 255, 0),
                       'blue': pygame.Color(0, 0, 255)}
