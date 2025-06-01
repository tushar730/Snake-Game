import pygame
import random
import sys

# Initialize
pygame.init()

# Screen
WIDTH, HEIGHT = 600, 400
CELL_SIZE = 20
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('🐍 Snake Game')

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Clock
clock = pygame.time.Clock()
FPS = 10

font = pygame.font.SysFont('arial', 24)

def draw_snake(snake):
    for block in snake:
        pygame.draw.rect(screen, GREEN, pygame.Rect(block[0], block[1], CELL_SIZE, CELL_SIZE))

def draw_food(pos):
    pygame.draw.rect(screen, RED, pygame.Rect(pos[0], pos[1], CELL_SIZE, CELL_SIZE))

def game_over(score):
    screen.fill(BLACK)
    text = font.render(f'Game Over! Score: {score}', True, WHITE)
    screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2))
    pygame.display.flip()
    pygame.time.wait(3000)
    pygame.quit()
    sys.exit()

def main():
    snake = [[100, 50], [80, 50], [60, 50]]
    direction = 'RIGHT'
    food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != 'DOWN':
                    direction = 'UP'
                elif event.key == pygame.K_DOWN and direction != 'UP':
                    direction = 'DOWN'
                elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                    direction = 'LEFT'
                elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                    direction = 'RIGHT'

        # Move snake
        x, y = snake[0]
        if direction == 'UP':
            y -= CELL_SIZE
        elif direction == 'DOWN':
            y += CELL_SIZE
        elif direction == 'LEFT':
            x -= CELL_SIZE
        elif direction == 'RIGHT':
            x += CELL_SIZE
        new_head = [x, y]

        # Game over conditions
        if (
            x < 0 or x >= WIDTH or
            y < 0 or y >= HEIGHT or
            new_head in snake
        ):
            game_over(len(snake) - 3)

        snake.insert(0, new_head)

        if new_head == food:
            food = [random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE)]
        else:
            snake.pop()

        # Draw everything
        screen.fill(BLACK)
        draw_snake(snake)
        draw_food(food)

        score = font.render(f'Score: {len(snake) - 3}', True, WHITE)
        screen.blit(score, (10, 10))

        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
