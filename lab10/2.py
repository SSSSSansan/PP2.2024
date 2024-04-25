import psycopg2
import pygame
import time
import random

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="phonebook",
    user="postgres",
    password="sanman8070",
    host="localhost",
    port=5433
)
cur = conn.cursor()

# Create user and user_score tables if not exists
cur.execute('''CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE
            )''')
cur.execute('''CREATE TABLE IF NOT EXISTS user_score (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id),
                level INTEGER,
                score INTEGER
            )''')
conn.commit()

# Function to insert user if not exists
def insert_user(username):
    try:
        cur.execute("INSERT INTO users (username) VALUES (%s)", (username,))
        conn.commit()
        print("User created successfully.")
    except psycopg2.IntegrityError:
        print("User already exists.")

# Function to get user ID
def get_user_id(username):
    cur.execute("SELECT id FROM users WHERE username = %s", (username,))
    row = cur.fetchone()
    return row[0] if row else None

# Function to check if user exists and get current level
def get_user_level(username):
    user_id = get_user_id(username)
    if user_id:
        cur.execute("SELECT level FROM user_score WHERE user_id = %s", (user_id,))
        row = cur.fetchone()
        return row[0] if row else 1  # Default level is 1
    else:
        return None

# Function to save score
def save_score(username, level, score):
    user_id = get_user_id(username)
    if user_id:
        cur.execute("INSERT INTO user_score (user_id, level, score) VALUES (%s, %s, %s)", (user_id, level, score))
        conn.commit()

# Function to display score
def show_score(username, level, score):
    level_text = font.render('Level: ' + str(level), True, white)
    score_text = font.render('Score: ' + str(score), True, white)
    user_text = font.render('User: ' + username, True, white)
    
    game_window.blit(score_text, [0, 0])
    game_window.blit(level_text, [0, 30])
    game_window.blit(user_text, [0, 60])

# Prompt user for username
username = input("Enter your username: ")

# Create user if not exists
insert_user(username)

# Get user's current level
current_level = get_user_level(username)

# Initialize game with user's current level
level = current_level if current_level else 1

# Initialize pygame
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
fruits = [{'color': red, 'value': 10, 'weight': 70},  # Normal fruit
          {'color': green, 'value': 20, 'weight': 20},  # High-value fruit
          {'color': white, 'value': 30, 'weight': 10}]  # Super high-value fruit
fruit_spawn = True
current_fruit = None

# Timer for fruit disappearance
fruit_timer = pygame.time.get_ticks()

# Initial snake direction
direction = 'RIGHT'
change_to = direction

# Initial score and font
score = 0
font = pygame.font.SysFont('comicsansms', 35)

# Function to display game over message and quit the game
def game_over():
    game_over_text = font.render('Game Over! Your Score: ' + str(score), True, red)
    game_window.blit(game_over_text, [window_x // 5, window_y // 2.5])
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Function to generate a random fruit based on weights
def generate_fruit():
    global current_fruit
    rand_num = random.randint(1, 100)
    cumulative_weight = 0
    for fruit in fruits:
        cumulative_weight += fruit['weight']
        if rand_num <= cumulative_weight:
            current_fruit = fruit
            break

# Main game loop
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
    if current_fruit and snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += current_fruit['value']
        level += 1
        fruit_spawn = False
    else:
        snake_body.pop()
    
    # Spawn new fruit if eaten or timer expired
    if not fruit_spawn or pygame.time.get_ticks() - fruit_timer > 5000:  # 5 seconds
        generate_fruit()
        fruit_position = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
        fruit_timer = pygame.time.get_ticks()
        fruit_spawn = True

    # Update snake body
    snake_body.insert(0, list(snake_position))

    # Draw game elements
    game_window.fill(black)
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], snake_block, snake_block))
    if current_fruit:
        pygame.draw.rect(game_window, current_fruit['color'], pygame.Rect(fruit_position[0], fruit_position[1], snake_block, snake_block))
    show_score(username, level, score)
    pygame.display.update()

    # Control game speed
    clock.tick(snake_speed)
