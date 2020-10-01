import pygame
import random

# Common settings
HEIGHT = 400
WIDTH = 600
FPS = 30


# COLOURS
BLACK = (72, 0, 72)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

# initialize pygame window and sound
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Classic Snake")
clock = pygame.time.Clock()

# Global variables



def Score(score):
    font = pygame.font.Font(None, 50)
    value = font.render("Score: " + str(score), True, GREEN)
    screen.blit(value, (0, 0))

def snake(snake_block, snake_list):
    for h in snake_list:
        pygame.draw.rect(screen, YELLOW, (h[0], h[1], snake_block, snake_block))


def message(msg):
    font = pygame.font.Font(None, 30)
    message = font.render(msg, True, RED)
    screen.blit(message, (WIDTH//6, HEIGHT//3))





# Game loop
def game_loop():
    x = WIDTH//2
    y = HEIGHT//2
    x_new = 0
    y_new = 0
    snake_block = 10
    snake_speed = 15
    snake_list = []
    length_snake = 1
    game_close = False
    foodx = random.randrange(0, (WIDTH-snake_block)//10)*10
    foody = random.randrange(0, (HEIGHT-snake_block)//10)*10

    # Game loop
    running = True
    while running:

        while game_close == True:
            screen.fill(BLACK)
            message("Game Over, Press Q-to quit or R-Play again")
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_close = False
                    if event.key == pygame.K_r:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_new = -snake_block
                    y_new = 0
                elif event.key == pygame.K_RIGHT:
                    x_new = snake_block
                    y_new = 0
                elif event.key == pygame.K_UP:
                    y_new = -snake_block
                    x_new = 0
                elif event.key == pygame.K_DOWN:
                    y_new = snake_block
                    x_new = 0

        if x >= WIDTH or x < 0 or y >= HEIGHT or y < 0:
            game_close = True

        x += x_new
        y += y_new
        snake_Head = []
        snake_Head.append(x)
        snake_Head.append(y)
        snake_list.append(snake_Head)
        if len(snake_list) > length_snake:
            del snake_list[0]

        for h in snake_list[:-1]:
            if h == snake_Head:
                game_close = True

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [foodx, foody, snake_block, snake_block])
        snake(snake_block, snake_list)
        Score(length_snake - 1)

        if x == foodx and y == foody:
            foodx = random.randrange(0, (WIDTH-snake_block)//10)*10
            foody = random.randrange(0, (HEIGHT-snake_block)//10)*10
            length_snake += 1

        clock.tick(snake_speed)
        pygame.display.update()



game_loop()
pygame.quit()














