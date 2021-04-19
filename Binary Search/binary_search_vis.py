import pygame
import random

#  Globals
WIDTH = 900
HEIGHT = 650
run = True
nums = [0] * 151
key = 0
foundkey = False
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
color1 = (72, 0, 72)
color2 = (255, 193, 7)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Initialization
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("BINARY SEARCH VISUALISER")

bar_colours = [color1] * 151
bigfont = pygame.font.SysFont("comicsans", 70)
fnt = pygame.font.SysFont("comicsans", 30)
fnt1 = pygame.font.SysFont("comicsans", 20)


def generate_list():
    for i in range(1, 151):
        nums[i] = random.randrange(1, 100)
    nums.sort()


# Initially generate a array
generate_list()


# Function to refill the
# updates on the window
def refill():
    screen.fill(color2)
    draw()
    pygame.display.update()
    pygame.time.delay(400)


def binarySearch(nums, key):
    left = 0
    right = len(nums) - 1

    while left < right:
        bar_colours[left] = RED
        bar_colours[right] = RED
        refill()
        mid = left + (right - left) // 2

        if nums[mid] == key:
            bar_colours[left] = color1
            bar_colours[right] = color1
            bar_colours[mid] = GREEN
            return 1

        elif nums[mid] < key:
            bar_colours[left] = color1
            left = mid + 1

        else:
            bar_colours[right] = color1
            right = mid - 1
        refill()
    bar_colours[left] = color1
    bar_colours[right] = color1
    refill()
    return -1


# Function to Draw the list values
def draw():
    txt = fnt.render("SEARCH: PRESS 'ENTER'", 1, BLACK)
    screen.blit(txt, (20, 20))
    txt1 = fnt.render("NEW ARRAY: PRESS 'R'", 1, BLACK)
    screen.blit(txt1, (20, 40))
    txt2 = fnt1.render("ENTER NUMBER TO SEARCH:" + str(key), 1, BLACK)
    screen.blit(txt2, (600, 60))
    element_width = (WIDTH - 150) // 150
    boundry_arr = 900 / 150
    boundry_grp = 550 / 100
    pygame.draw.line(screen, (0, 0, 0), (0, 95),
                     (900, 95), 6)

    # Drawing the array values as lines
    for i in range(1, 151):
        pygame.draw.line(screen, bar_colours[i],
                         (boundry_arr * i - 3, 100),
                         (boundry_arr * i - 3,
                          nums[i] * boundry_grp + 100), element_width)
    if foundkey == 1:
        text4 = bigfont.render("Key Found. Press N to Reset Key", 1, BLACK)
        screen.blit(text4, (100, 300))

    elif foundkey == -1:
        text4 = bigfont.render("Key Not Found. Press N to Reset Key", 1, BLACK)
        screen.blit(text4, (30, 300))


# Game Loop
while run:
    # background
    screen.fill(color2)
    # Event handler stores all event
    for event in pygame.event.get():

        # If we click Close button in window
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                key = 0
                foundkey = 0
                generate_list()
            if event.key == pygame.K_n:
                foundkey = 0
                key = 0
                for i in range(0, len(nums)):
                    bar_colours[i] = color1
            if event.key == pygame.K_RETURN and key != 0:
                foundkey = binarySearch(nums, key)
            if event.key == pygame.K_0:
                key = key * 10
            if event.key == pygame.K_1:
                key = key * 10 + 1
            if event.key == pygame.K_2:
                key = key * 10 + 2
            if event.key == pygame.K_3:
                key = key * 10 + 3
            if event.key == pygame.K_4:
                key = key * 10 + 4
            if event.key == pygame.K_5:
                key = key * 10 + 5
            if event.key == pygame.K_6:
                key = key * 10 + 6
            if event.key == pygame.K_7:
                key = key * 10 + 7
            if event.key == pygame.K_8:
                key = key * 10 + 8
            if event.key == pygame.K_9:
                key = key * 10 + 9
    draw()
    pygame.display.update()

pygame.quit()
