import pygame
import sys
from settings import *
import random

pygame.init()

game_font = pygame.font.Font("assets/fonts/Queensides.ttf", 48)
level = 1
timer = pygame.time.Clock()
pygame.display.set_caption("Thanksgiving Match")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
background = screen.copy()
clock = pygame.time.Clock()
first_guess = False
second_guess = False
first_guess_word = 0
second_guess_word = 0
fps = 60
score = 0
match = 0
location1 = ""
location2 = ""
turkey = pygame.image.load("assets/images/turkey.png").convert()
salt = pygame.image.load("assets/images/salt.png").convert()
pepper = pygame.image.load("assets/images/pepper.png").convert()
onion = pygame.image.load("assets/images/onion.png").convert()
carrot = pygame.image.load("assets/images/carrot.png").convert()
celery = pygame.image.load("assets/images/celery.png").convert()

turkey_foods = {"turkey": turkey, "salt": salt, "pepper": pepper, "onion": onion, "carrot": carrot, "celery": celery}
num_foods = {1: turkey, 2: salt, 3: pepper, 4: onion, 5: carrot, 6: celery, 10: turkey, 20: salt, 30: pepper, 40: onion,
             50: carrot, 60: celery}
place = [(col1, row1), (col1, row2), (col1, row3), (col2, row1), (col2, row2),
         (col2, row3), (col3, row1), (col3, row2),
         (col3, row3), (col4, row1), (col4, row2), (col4, row3)]
foods = ['turkey', 'turkey', 'salt', 'salt', 'pepper', 'pepper', 'onion', 'onion', 'carrot', 'carrot',
         'celery', 'celery']
nums = [1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50, 60]
random.shuffle(nums)
random.shuffle(foods)
print(foods)
places = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2, nums[7]: 2, nums[8]: 2,
            nums[9]: 3, nums[10]: 3, nums[11]: 3}
num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0, nums[7]: 1, nums[8]: 2,
            nums[9]: 0, nums[10]: 1, nums[11]: 2}
food_cols = {foods[0]: 0, foods[1]: 0, foods[2]: 0, foods[3]: 1, foods[4]: 1, foods[5]: 1, foods[6]: 2, foods[7]: 2,
             foods[8]: 2, foods[9]: 3, foods[10]: 3, foods[11]: 3}
food_rows = {foods[0]: 0, foods[1]: 1, foods[2]: 2, foods[3]: 0, foods[4]: 1, foods[5]: 2, foods[6]: 0, foods[7]: 1,
             foods[8]: 2, foods[9]: 0, foods[10]: 1, foods[11]: 2}

correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


def draw_background():
    background.fill((250, 244, 167))

    text = game_font.render("Matching", True, (64, 44, 4))
    level_text = game_font.render(f"Level {level}", True, (64, 44, 4))
    # make level that will eventually change with each level
    background.blit(text, (TILE_SIZE * 2, TILE_SIZE // 2))
    background.blit(level_text, (SCREEN_WIDTH - TILE_SIZE * 2 - level_text.get_width(), TILE_SIZE // 2))


def draw_board():
    pieces = []
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, (140, 109, 24), [i * (BRICK_SIZE + WSPACE) + WSPACE,
                                                              j * (BRICK_SIZE + HSPACE) + HSPACE + 100, BRICK_SIZE,
                                                              BRICK_SIZE])
            pieces.append(piece)
    for c in range(cols):
        for r in range(rows):
            if correct[r][c] == 1:
                screen.blit(num_foods[nums[c*rows+r]], place[c*rows+r])


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
        print(roww2)
        if correct[roww1][coll1] == 0 and correct[roww2][coll2] == 0:
            correct[roww1][coll1] = 1
            correct[roww2][coll2] = 1
            score += 1
            match += 1

    else:
        score += 1


piecey = draw_board()

while True:
    timer.tick(fps)
    draw_background()

    if first_guess and second_guess:
        first_guess = False
        second_guess = False
        check_guesses(first_guess_word, second_guess_word)
        pygame.time.delay(1000)
        piecey = draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(piecey)):
                button = piecey[i]
                if button.collidepoint(event.pos) and not first_guess:
                    first_guess = True
                    first_guess_word = nums[i]
                    location1 = place[i]
                    print(first_guess_word)
                    print(location1)
                elif button.collidepoint(event.pos) and not second_guess and first_guess and (((nums[i] // 10) != first_guess_word) or (nums[i] != (first_guess_word // 10))):
                    second_guess = True
                    second_guess_word = nums[i]
                    location2 = place[i]
                    print(second_guess_word)
                    print(location2)

        if first_guess:
            screen.blit(num_foods[first_guess_word], location1)
        if second_guess:
            screen.blit(num_foods[second_guess_word], location2)

    pygame.display.flip()
