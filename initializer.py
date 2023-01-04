import pygame
import random

from hud import HUD

snake_hud = HUD()


class SnakeInit:
    def __init__(self):
        self.init = pygame.init()
        self.caption = pygame.display.set_caption('Snake')
        self.game_window = pygame.display.set_mode([snake_hud.window_x, snake_hud.window_y])
        self.fps = pygame.time.Clock()
        self.snake_position = [100, 50]
        self.snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]
        self.fruit_position = [random.randrange(1, (snake_hud.window_x // 10)) * 10,
                               random.randrange(1, (snake_hud.window_y // 10)) * 10]
        self.fruit_spawn = True
        self.direction = 'RIGHT'
        self.change_to = self.direction
