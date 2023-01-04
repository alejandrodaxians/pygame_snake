import time
import pygame

from initializer import SnakeInit
from hud import HUD

snake_hud = HUD()
snake_init = SnakeInit()


class Score:
    def __init__(self):
        self.score = 0

    def show_score(self, choice, color, font, size):
        score_font = pygame.font.SysFont(font, size)
        score_surface = score_font.render('Score : ' + str(self.score), True, color)
        score_rect = score_surface.get_rect()
        snake_init.game_window.blit(score_surface, score_rect)

    def game_over(self):
        my_font = pygame.font.SysFont('times new roman', 50)
        game_over_surface = my_font.render('Your score is : ' + str(self.score), True, snake_hud.colors.get('red', ""))
        game_over_rect = game_over_surface.get_rect()
        game_over_rect.midtop = (snake_hud.window_x / 2, snake_hud.window_y / 4)
        snake_init.game_window.blit(game_over_surface, game_over_rect)

        pygame.display.flip()
        time.sleep(2.0)
        pygame.quit()
        quit()
