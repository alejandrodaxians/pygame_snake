import pygame
import random

from initializer import SnakeInit
from hud import HUD
from score import Score

snake_hud = HUD()
snake_init = SnakeInit()
snake_score = Score()


def play_snake():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.type == pygame.K_UP:
                    snake_init.change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    snake_init.change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    snake_init.change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    snake_init.change_to = 'RIGHT'

        if snake_init.change_to == 'UP' and snake_init.direction != 'DOWN':
            snake_init.direction = 'UP'
        if snake_init.change_to == 'DOWN' and snake_init.direction != 'UP':
            snake_init.direction = 'DOWN'
        if snake_init.change_to == 'LEFT' and snake_init.direction != 'RIGHT':
            snake_init.direction = 'LEFT'
        if snake_init.change_to == 'RIGHT' and snake_init.direction != 'LEFT':
            snake_init.direction = 'RIGHT'

        if snake_init.direction == 'UP':
            snake_init.snake_position[1] -= 10
        if snake_init.direction == 'DOWN':
            snake_init.snake_position[1] += 10
        if snake_init.direction == 'LEFT':
            snake_init.snake_position[0] -= 10
        if snake_init.direction == 'RIGHT':
            snake_init.snake_position[0] += 10

        snake_init.snake_body.insert(0, list(snake_init.snake_position))
        if snake_init.snake_position[0] == snake_init.fruit_position[0] \
                and snake_init.snake_position[1] == snake_init.fruit_position[1]:
            snake_score.score += 10
            snake_init.fruit_spawn = False
        snake_init.snake_body.pop()

        if not snake_init.fruit_spawn:
            snake_init.fruit_position = [random.randrange(1, (snake_hud.window_x // 10)) * 10,
                                         random.randrange(1, (snake_hud.window_y // 10)) * 10]

        snake_init.fruit_spawn = True
        snake_init.game_window.fill(snake_hud.colors.get('black', ""))

        for pos in snake_init.snake_body:
            pygame.draw.rect(snake_init.game_window, snake_hud.colors.get("green", ""),
                             pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(snake_init.game_window, snake_hud.colors.get("white", ""),
                         pygame.Rect(snake_init.fruit_position[0], snake_init.fruit_position[1], 10, 10))

        if snake_init.snake_position[0] < 0 or snake_init.snake_position[0] > snake_hud.window_x - 10:
            snake_score.game_over()
        if snake_init.snake_position[0] < 0 or snake_init.snake_position[1] > snake_hud.window_y - 10:
            snake_score.game_over()

        for block in snake_init.snake_body[1:]:
            if snake_init.snake_position[0] == block[0] and snake_init.snake_position[1] == block[1]:
                snake_score.game_over()

        snake_score.show_score(1, snake_hud.colors.get("white", ""), 'times new roman', 20)

        pygame.display.update()
        snake_init.fps.tick(snake_hud.speed)


if __name__ == "__main__":
    play_snake()
