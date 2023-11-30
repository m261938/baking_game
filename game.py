import pygame
import sys
from settings import *
import random

pygame.init()

big_font = pygame.font.Font("assets/fonts/Queensides.ttf", 48)
lil_font = pygame.font.Font("assets/fonts/Queensides.ttf", 20)
level = 1
timer = pygame.time.Clock()
pygame.display.set_caption("Thanksgiving Match")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
background = screen.copy()
clock = pygame.time.Clock()
first_guess = False
second_guess = False
level1 = False
first_guess_word = 0
second_guess_word = 0
fps = 60
score = 0
match = 0
location1 = ""
location2 = ""
levels_won_counter = 0

turkey = pygame.image.load("assets/images/turkey.png").convert()
salt = pygame.image.load("assets/images/salt.png").convert()
pepper = pygame.image.load("assets/images/pepper.png").convert()
onion = pygame.image.load("assets/images/onion.png").convert()
carrot = pygame.image.load("assets/images/carrot.png").convert()
celery = pygame.image.load("assets/images/celery.png").convert()
potato = pygame.image.load("assets/images/potato.png").convert()
butter = pygame.image.load("assets/images/butter.png").convert()
cream_cheese = pygame.image.load("assets/images/cream_cheese.png").convert()
milk = pygame.image.load("assets/images/milk.png").convert()


turkey_num_foods = {1: turkey, 2: salt, 3: pepper, 4: onion, 5: carrot, 6: celery, 10: turkey, 20: salt, 30: pepper,
                    40: onion, 50: carrot, 60: celery}
mashed_potato_num_foods = {1: potato, 2: salt, 3: butter, 4: cream_cheese, 5: milk, 6: pepper, 10: potato, 20: salt,
                           30: butter, 40: cream_cheese, 50: milk, 60: pepper}
num_foods = [turkey_num_foods, mashed_potato_num_foods]
place = [(col1, row1), (col1, row2), (col1, row3), (col2, row1), (col2, row2), (col2, row3), (col3, row1), (col3, row2),
         (col3, row3), (col4, row1), (col4, row2), (col4, row3)]
turkey_level = ['turkey', 'turkey', 'salt', 'salt', 'pepper', 'pepper', 'onion', 'onion', 'carrot', 'carrot',
                'celery', 'celery']
mashed_potato_level = ['potato', 'potato', 'salt', 'salt', 'butter', 'butter', 'cream cheese', 'cream cheese', 'milk',
                       'milk', 'pepper', 'pepper']
nums = [1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50, 60]
random.shuffle(nums)
random.shuffle(turkey_level)
random.shuffle(mashed_potato_level)
places = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2, nums[7]: 2, nums[8]: 2,
            nums[9]: 3, nums[10]: 3, nums[11]: 3}
num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0, nums[7]: 1, nums[8]: 2,
            nums[9]: 0, nums[10]: 1, nums[11]: 2}


correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def draw_background():
    global level
    global background
    screen.fill((2, 244, 167))

    text = big_font.render("Matching game", True, (0, 44, 255))
    level_text = lil_font.render(f"Level {level}", True, (0, 44, 255))
    levels_won_text = lil_font.render(f"Levels won: {levels_won_counter}/6", True, (0, 44, 255))
    screen.blit(text, (30, 30))
    screen.blit(level_text, (400, 30 ))
    screen.blit(levels_won_text, (400, 70) )


def draw_homescreen():
    text = big_font.render("Matching game", True, (0, 44, 255))
    screen.blit(text, (100, 100))
    #quits = lil_font.render("Enter 'q' to return to homescreen at any point", True, BLACK)
    #screen.blit(quits, (100, 200))
    turkey_level_print = lil_font.render("Enter 't' for turkey level", True, BLACK)
    screen.blit(turkey_level_print, (100, 200))
    potato_level_print = lil_font.render("Enter 'p' for potato level", True, BLACK)
    screen.blit(potato_level_print, (100, 250))
    levels_won_text = lil_font.render(f"Levels won: {levels_won_counter}/6", True, (0, 44, 255))
    screen.blit(levels_won_text, (500, 125))

def draw_board():
    pieces = []
    # make dependent on which food num foods
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, (140, 109, 24), [i * (BRICK_SIZE + WSPACE) + WSPACE,
                                                              j * (BRICK_SIZE + HSPACE) + HSPACE + 100, BRICK_SIZE,
                                                              BRICK_SIZE])
            pieces.append(piece)
    for c in range(cols):
        for r in range(rows):
            if correct[r][c] == 1:
                screen.blit(num_foods[level][nums[c * rows + r]], place[c * rows + r])

    return pieces


def check_guesses(first, second):
    global correct
    global score
    global match
    global location1
    global location2
    if (first // 10) == second or first == (second // 10):
        coll1 = num_cols[first]
        coll2 = num_cols[second]
        roww1 = num_rows[first]
        roww2 = num_rows[second]
        if correct[roww1][coll1] == 0 and correct[roww2][coll2] == 0:
            correct[roww1][coll1] = 1
            correct[roww2][coll2] = 1
            score += 1
            match += 1

    else:
        score += 1


start = True
while start:
    screen.blit(background, (0, 0))
    draw_homescreen()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        else:
            start = False

while True:
    timer.tick(fps)

    if first_guess and second_guess:
        first_guess = False
        second_guess = False
        check_guesses(first_guess_word, second_guess_word)
        pygame.time.delay(1000)
        piecey = draw_board()
    if match == 6:
        screen.blit(background, (0, 0))
        draw_homescreen()
        match = 0
        correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        levels_won_counter += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                level = 0
                draw_background()
                piecey = draw_board()
            if event.key == pygame.K_p:
                level = 1
                draw_background()
                piecey = draw_board()
        if event.type == pygame.MOUSEBUTTONDOWN:
            piecey = draw_board()
            for i in range(len(piecey)):
                button = piecey[i]
                if button.collidepoint(event.pos) and not first_guess:
                    first_guess = True
                    first_guess_word = nums[i]
                    location1 = place[i]
                elif button.collidepoint(event.pos) and not second_guess and first_guess and (
                        ((nums[i] // 10) != first_guess_word) or (nums[i] != (first_guess_word // 10))):
                    second_guess = True
                    second_guess_word = nums[i]
                    location2 = place[i]

        if first_guess:
            screen.blit(num_foods[level][first_guess_word], location1)
        if second_guess:
            screen.blit(num_foods[level][second_guess_word], location2)

    pygame.display.flip()
