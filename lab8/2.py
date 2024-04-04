import pygame
import time
import random

pygame.init()

# Window dimensions
window_x = 720
window_y = 480
game_window = pygame.display.set_mode((window_x, window_y))
pygame.display.set_caption('Snake Game')

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
green = pygame.Color(0, 255, 0)
red = pygame.Color(255, 0, 0)

# Clock for controlling game speed
clock = pygame.time.Clock()

# Initial snake properties
snake_speed = 15
snake_block = 10
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Initial fruit properties
fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
fruit_spawn = True

# Initial snake direction
direction = 'RIGHT'
change_to = direction

# Initial score and font
score = 0
font = pygame.font.SysFont('comicsansms', 35)

# Function to display score
def show_score():
    score_text = font.render('Score: ' + str(score), True, white)
    game_window.blit(score_text, [0, 0])

# Function to display game over message and quit the game
def game_over():
    game_over_text = font.render('Game Over! Your Score: ' + str(score), True, red)
    game_window.blit(game_over_text, [window_x // 4, window_y // 2])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # Change direction if a valid key is pressed
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    elif change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    elif change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    elif change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Update snake position based on direction
    if direction == 'UP':
        snake_position[1] -= snake_block
    elif direction == 'DOWN':
        snake_position[1] += snake_block
    elif direction == 'LEFT':
        snake_position[0] -= snake_block
    elif direction == 'RIGHT':
        snake_position[0] += snake_block

    # Check if snake collides with window boundaries
    if snake_position[0] >= window_x or snake_position[0] < 0 or snake_position[1] >= window_y or snake_position[1] < 0:
        game_over()

    # Check if snake collides with itself
    for block in snake_body[1:]:
        if snake_position[0] == block[0] and snake_position[1] == block[1]:
            game_over()

    # Check if snake eats the fruit
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    # Spawn new fruit if eaten
    if not fruit_spawn:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruit_spawn = True

    # Update snake body
    snake_body.insert(0, list(snake_position))

    # Draw game elements
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_position[0], fruit_position[1], snake_block, snake_block))
    show_score()
    pygame.display.update()

    # Control game speed
    clock.tick(snake_speed)
