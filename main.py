"""Snake game with restart functionality."""

import os
import time
import sys
import random
from snake import Snake

try:
    import msvcrt
    def get_key():
        if msvcrt.kbhit():
            return msvcrt.getch().decode('utf-8', errors='ignore')
        return None
except ImportError:
    import termios, tty, select
    def get_key():
        if select.select([sys.stdin], [], [], 0)[0]:
            return sys.stdin.read(1)
        return None

def draw(board_width, board_height, snake, food):
    """Clear screen and draw the game board."""
    os.system('cls' if os.name == 'nt' else 'clear')
    board = [[' ' for _ in range(board_width)] for _ in range(board_height)]
    for seg in snake.get_body():
        x, y = seg
        if 0 <= x < board_width and 0 <= y < board_height:
            board[y][x] = 'O' if seg == snake.get_head() else 'o'
    fx, fy = food
    if 0 <= fx < board_width and 0 <= fy < board_height:
        board[fy][fx] = '*'
    for row in board:
        print(''.join(row))
    print(f"Score: {len(snake.get_body()) - snake.length}")

def main():
    board_width = 20
    board_height = 15
    snake = Snake(board_width // 2, board_height // 2, length=3)
    score = 0
    food = (random.randint(0, board_width-1), random.randint(0, board_height-1))
    while food in snake.get_body():
        food = (random.randint(0, board_width-1), random.randint(0, board_height-1))

    while True:
        key = get_key()
        if key:
            if key.lower() == 'q':
                break
            elif key == 'w':
                snake.change_direction((0, -1))
            elif key == 's':
                snake.change_direction((0, 1))
            elif key == 'a':
                snake.change_direction((-1, 0))
            elif key == 'd':
                snake.change_direction((1, 0))
        snake.move()
        if snake.get_head() == food:
            snake.grow()
            score += 1
            food = (random.randint(0, board_width-1), random.randint(0, board_height-1))
            while food in snake.get_body():
                food = (random.randint(0, board_width-1), random.randint(0, board_height-1))
        if snake.check_collision(board_width, board_height):
            draw(board_width, board_height, snake, food)
            print("Game Over! Press 'r' to restart or 'q' to quit.")
            while True:
                key2 = get_key()
                if key2:
                    if key2.lower() == 'r':
                        snake.reset()
                        score = 0
                        food = (random.randint(0, board_width-1), random.randint(0, board_height-1))
                        while food in snake.get_body():
                            food = (random.randint(0, board_width-1), random.randint(0, board_height-1))
                        break
                    elif key2.lower() == 'q':
                        return
            continue
        draw(board_width, board_height, snake, food)
        time.sleep(0.2)

if __name__ == '__main__':
    main()


