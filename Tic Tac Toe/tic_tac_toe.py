import pygame
import random
import time

# Common settings
WIDTH = 400
HEIGHT = 500
FPS = 30

# some more Global variables
XO = 'x'  # This will store the current player's symbol, initialized with x because that will be our first player.
winner = None  # Storing the winner's value
draw = None  # To check if the game is a draw
board = [[None] * 3, [None] * 3, [None] * 3]  # Setting up a 3x3 board

# COLOURS
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)
BOARD = (0, 33, 2)

# initialize pygame window and sound
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")
clock = pygame.time.Clock()

# Loading Graphics
initiating_window = pygame.image.load("Cover.png")
x_img = pygame.image.load("x.png")
o_img = pygame.image.load("o.png")

# Rescaling Graphics
initiating_window = pygame.transform.scale(initiating_window, (WIDTH, HEIGHT))
x_img = pygame.transform.scale(x_img, (80, 80))
o_img = pygame.transform.scale(o_img, (80, 80))


def game_initiating_window():
    # displaying over the screen
    screen.blit(initiating_window, (0, 0))
    # updating the display
    pygame.display.update()
    time.sleep(3)
    screen.fill(BOARD)

    # Drawing vertical lines
    pygame.draw.line(screen, WHITE, (WIDTH // 3, 50), (WIDTH // 3, HEIGHT - 50), 7)
    pygame.draw.line(screen, WHITE, ((WIDTH // 3) * 2, 50), ((WIDTH // 3) * 2, HEIGHT - 50), 7)

    # drawing horizontal lines
    pygame.draw.line(screen, WHITE, (10, HEIGHT//3), (WIDTH-10,  HEIGHT//3), 7)
    pygame.draw.line(screen, WHITE, (10, (HEIGHT//3) * 2), (WIDTH-10, (HEIGHT//3) * 2), 7)
    draw_status()


def draw_status():
    # getting the global variable draw
    # into action
    global draw

    if winner is None:
        message = XO.upper() + "'s Turn"
    else:
        message = winner.upper() + " won !"

    if draw:
        message = "Game Draw!!"

    # setting a font object
    font = pygame.font.Font(None, 25)

    # setting the font properties like
    # color and width of the text
    text = font.render(message, 1, RED)

    # copy the rendered message onto the board
    # creating a small block at the bottom of the main display
    screen.fill(BOARD, (0, 500-30, WIDTH, 100))
    text_rect = text.get_rect(center=(WIDTH // 2, 500-20))
    screen.blit(text, text_rect)
    pygame.display.update()


def check_win():
    global board, winner, draw

    # checking for winning rows
    for row in range(0, 3):
        if (board[row][0] == board[row][1] == board[row][2]) and (board[row][0] is not None):
            winner = board[row][0]
            pygame.draw.line(screen, RED, (10, (row+1)*(HEIGHT//3)-HEIGHT//6 + 10), (WIDTH-10, (row+1)*(HEIGHT//3)-HEIGHT//6 + 10), 4)
            break

    # checking for winning columns
    for col in range(0, 3):
        if (board[0][col] == board[1][col] == board[2][col]) and (board[0][col] is not None):
            winner = board[0][col]
            pygame.draw.line(screen, RED, ((col+1)*(WIDTH//3)- WIDTH//6 , 50), ((col+1)*(WIDTH//3) -WIDTH//6 , HEIGHT-50),4)
            break

    # check for diagonal winners
    if (board[0][0] == board[1][1] == board[2][2]) and (board[0][0] is not None):
        # game won diagonally left to right
        winner = board[0][0]
        pygame.draw.line(screen, RED, (40, 50), (400, 500), 4)

    if (board[0][2] == board[1][1] == board[2][0]) and (board[0][2] is not None):
        # game won diagonally right to left
        winner = board[0][2]
        pygame.draw.line(screen, RED, (350, 50), (50, 450), 4)

    if (all([all(row) for row in board]) and winner is None):
        draw = True

    draw_status()


def drawXO(row, col):
    global board, XO

    # For 1st column
    if row == 1 and col ==1 :
        posx = 25
        posy = 55
    elif row == 2 and col == 1:
        posx = 25
        posy = HEIGHT//3 + 55
    elif row == 3 and col == 1:
        posx = 25
        posy = (HEIGHT//3)*2 +40

    # For second Column
    elif row == 1 and col == 2:
        posx = WIDTH//3+25
        posy = 55
    elif row == 2 and col == 2:
        posx = WIDTH//3+25
        posy = HEIGHT//3 + 55
    elif row == 3 and col == 2:
        posx= WIDTH//3+25
        posy= (HEIGHT//3)*2 +40

    # For third column
    elif row == 1 and col == 3:
        posx = (WIDTH//3)*2+25
        posy = 55
    elif row == 2 and col == 3:
        posx = (WIDTH//3)*2+25
        posy = HEIGHT//3 + 55
    elif row == 3 and col == 3:
        posx = (WIDTH//3)*2+25
        posy = (HEIGHT//3)*2 +40

    # setting up the required board
    # value to display
    board[row - 1][col - 1] = XO

    if XO == 'x':
        screen.blit(x_img, (posx, posy))
        XO = 'o'
    else:
        screen.blit(o_img, (posx, posy))
        XO = 'x'
    pygame.display.update()


def user_click():
    # get coordinates of mouse click
    x, y = pygame.mouse.get_pos()

    # get column of mouse click (1-3)
    if x < WIDTH//3:
        col = 1
    elif x < (WIDTH//3)*2:
        col = 2
    elif x < WIDTH:
        col = 3
    else:
        col = None

    # get row of mouse click (1-3)
    if y < HEIGHT//3:
        row = 1
    elif y < (HEIGHT//3)*2:
        row = 2
    elif y < HEIGHT:
        row = 3
    else:
        row = None

    # after getting the row and col,
    # we need to draw the images at
    # the desired positions
    if row and col and board[row - 1][col - 1] is None:
        drawXO(row, col)
        check_win()

def reset_game():
    global board, winner, XO, draw
    time.sleep(3)
    XO = 'x'
    draw = False
    game_initiating_window()
    winner = None
    board = [[None]*3, [None]*3, [None]*3]

# Game loop
game_initiating_window()

running = True
while running:

    clock.tick(FPS)
    x_change = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type is pygame.MOUSEBUTTONDOWN:
            user_click()
            if winner or draw:
                reset_game()
    # Update
    pygame.display.update()

pygame.quit()
