from gameplay import Gameplay

snake_game = Gameplay()


def play_snake():
    while True:
        snake_game.snake_movement()
        snake_game.fruit_interaction()
        snake_game.draw_snake_body()
        snake_game.set_game_over()
        snake_game.main_score()
        snake_game.update_display()
        snake_game.refresh_framerate()


if __name__ == "__main__":
    play_snake()
