import sys
import pygame

import pickle
from settings import *
import random



try:
    with open('highscore.dat', 'rb') as file:
        highscore = pickle.load(file)
except:
    highscore = 0

pygame.init()

real_overall_score = 0
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
overall_score = 0

pygame.mixer_music.load('assets/sounds/background_music.wav')
pygame.mixer_music.play(-1)
win_sound = pygame.mixer.Sound('assets/sounds/Won!.wav')

#pygame.mixer_music.load('assets/sounds/Won!.wav')
location1 = ""
location2 = ""
levels_won_counter = 0
before_played_color = (133, 12, 34)
turkey_color = before_played_color
potato_color = before_played_color
cranberry_color = before_played_color
pumpkin_pie_color = before_played_color
cornbread_color = before_played_color
roll_color = before_played_color
pecan_pie_color = before_played_color
played_color = (19, 94, 45)
levels_won_text = lil_font.render(f"Levels won: {levels_won_counter}/7", True, (0, 44, 255))
score_text = lil_font.render(f'Score: {score}', True, (0,44,255))

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
cranberry_cocktail = pygame.image.load("assets/images/cranberry_cocktail.png").convert()
cranberries = pygame.image.load("assets/images/cranberries.png").convert()
lemon_juice = pygame.image.load("assets/images/lemon_juice.png").convert()
gelatin = pygame.image.load("assets/images/gelatin.png").convert()
sugar = pygame.image.load("assets/images/sugar.png").convert()
pumpkin = pygame.image.load("assets/images/pumpkin.png").convert()
eggs = pygame.image.load("assets/images/eggs.png").convert()
cream = pygame.image.load("assets/images/cream.png").convert()
spices = pygame.image.load("assets/images/spices.png").convert()
pie_crust = pygame.image.load("assets/images/pie_crust.png").convert()
cornbread = pygame.image.load("assets/images/cornbread.png").convert()
thyme = pygame.image.load("assets/images/thyme.png").convert()
mushrooms = pygame.image.load("assets/images/mushrooms.png").convert()
flour = pygame.image.load("assets/images/flour.png").convert()
yeast = pygame.image.load("assets/images/yeast.png").convert()
pecans = pygame.image.load("assets/images/pecans.png").convert()
brown_sugar = pygame.image.load("assets/images/brown_sugar.png").convert()
vanilla = pygame.image.load("assets/images/vanilla.png").convert()
tree = pygame.image.load("assets/images/treee.png").convert()
end_screen = pygame.image.load("assets/images/thanksgiving_dinner.png").convert()
tree.set_colorkey((0, 0, 0))

turkey_foods = {1: turkey, 2: salt, 3: pepper, 4: onion, 5: carrot, 6: celery, 10: turkey, 20: salt, 30: pepper,
                40: onion, 50: carrot, 60: celery}
mashed_potato_foods = {1: potato, 2: salt, 3: butter, 4: cream_cheese, 5: milk, 6: pepper, 10: potato, 20: salt,
                       30: butter, 40: cream_cheese, 50: milk, 60: pepper}
cranberry_foods = {1: cranberry_cocktail, 2: cranberries, 3: celery, 4: lemon_juice, 5: gelatin, 6: sugar,
                   10: cranberry_cocktail, 20: cranberries, 30: celery, 40: lemon_juice, 50: gelatin, 60: sugar}
pumpkin_pie_foods = {1: pumpkin, 2: sugar, 3: eggs, 4: cream, 5: spices, 6: pie_crust, 10: pumpkin, 20: sugar,
                     30: eggs, 40: cream, 50: spices, 60: pie_crust}
cornbread_foods = {1: cornbread, 2: thyme, 3: eggs, 4: mushrooms, 5: celery, 6: onion, 10: cornbread, 20: thyme,
                   30: eggs, 40: mushrooms, 50: celery, 60: onion}
roll_foods = {1: flour, 2: yeast, 3: sugar, 4: milk, 5: salt, 6: butter, 10: flour, 20: yeast,
              30: sugar, 40: milk, 50: salt, 60: butter}
pecan_pie_foods = {1: pie_crust, 2: pecans, 3: brown_sugar, 4: butter, 5: eggs, 6: vanilla, 10: pie_crust, 20: pecans,
                   30: brown_sugar, 40: butter, 50: eggs, 60: vanilla}

num_foods = [turkey_foods, mashed_potato_foods, cranberry_foods, pumpkin_pie_foods, cornbread_foods, roll_foods,
             pecan_pie_foods]
place = [(col1, row1), (col1, row2), (col1, row3), (col2, row1), (col2, row2), (col2, row3), (col3, row1), (col3, row2),
         (col3, row3), (col4, row1), (col4, row2), (col4, row3)]
nums = [1, 2, 3, 4, 5, 6, 10, 20, 30, 40, 50, 60]
random.shuffle(nums)
places = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2, nums[7]: 2, nums[8]: 2,
            nums[9]: 3, nums[10]: 3, nums[11]: 3}
num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0, nums[7]: 1, nums[8]: 2,
            nums[9]: 0, nums[10]: 1, nums[11]: 2}
correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

restart_button = pygame.draw.rect(screen, (255, 255, 255), [525, 10, 180, 80], 0, 5)
restart_text = big_font.render("restart", True, (0, 0, 0))
screen.blit(restart_text, (550, 10))

def draw_background():
    global level
    global background
    screen.fill(BACKGROUND_COLOR)

    text = big_font.render("Matching game", True, (0, 44, 255))
    level_text = lil_font.render(f"Level {level}", True, (0, 44, 255))
    screen.blit(text, (30, 30))
    screen.blit(level_text, (400, 30))
    screen.blit(levels_won_text, (400, 70))


def draw_homescreen():
    text = big_font.render("Matching game", True, (0, 44, 255))
    screen.blit(text, (100, 100))
    #quits = lil_font.render("Enter 'q' to return to homescreen at any point", True, BLACK)
    #screen.blit(quits, (100, 200))
    turkey_level_print = lil_font.render("Enter 't' for turkey level", True, turkey_color)
    screen.blit(turkey_level_print, (100, 200))
    potato_level_print = lil_font.render("Enter 'p' for potato level", True, potato_color)
    screen.blit(potato_level_print, (100, 250))
    cranberry_level_print = lil_font.render("Enter 'c' for cranberry level", True, cranberry_color)
    screen.blit(cranberry_level_print, (100, 300))
    pumpkin_pie_level_print = lil_font.render("Enter 'i' for pumpkin pie level", True, pumpkin_pie_color)
    screen.blit(pumpkin_pie_level_print, (100, 350))
    cornbread_level_print = lil_font.render("Enter 'o' for cornbread level", True, cornbread_color)
    screen.blit(cornbread_level_print, (100, 400))
    roll_level_print = lil_font.render("Enter 'r' for roll level", True, roll_color)
    screen.blit(roll_level_print, (100, 450))
    pecan_pie_level_print = lil_font.render("Enter 'e' for pecan pie level", True, pecan_pie_color)
    screen.blit(pecan_pie_level_print, (100, 500))
    screen.blit(levels_won_text, (500, 125))
    screen.blit(score_text, (500, 200))
    screen.blit(tree, (500, 430))
    highscore_text = lil_font.render(f"Highscore: {highscore}", True, BLACK)
    screen.blit(highscore_text, (500, 250))

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
        win_sound.play()
        screen.blit(background, (0, 0))
        match = 0
        correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        levels_won_counter += 1
        score_text = lil_font.render(f'Score:{score}', True, (0,44,255))
        levels_won_text = lil_font.render(f"Levels won: {levels_won_counter}/7", True, (0, 44, 255))
        draw_homescreen()
    if levels_won_counter == 7:
        overall_score = score
        score = 0
        screen.blit(end_screen, (0, 0))
        end_text1 = big_font.render("Good job!", True, (255, 255, 255))
        end_text2 = big_font.render("You made thanksgiving dinner!", True, (255, 255, 255))
        screen.blit(end_text1, (250, 150))
        screen.blit(end_text2, (30, 500))
        restart_button = pygame.draw.rect(screen, (255, 255, 255), [525, 10, 180, 80], 0, 5)
        restart_text = big_font.render("restart", True, (0, 0, 0))
        screen.blit(restart_text, (550, 10))
        levels_won_counter= 0
        cranberry_color = before_played_color
        pumpkin_pie_color = before_played_color
        cornbread_color = before_played_color
        turkey_color = before_played_color
        pecan_pie_color = before_played_color
        roll_color = before_played_color
        potato_color = before_played_color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_t:
                level = 0
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                turkey_color = played_color
            if event.key == pygame.K_p:
                level = 1
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                potato_color = played_color
            if event.key == pygame.K_c:
                level = 2
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                cranberry_color = played_color
            if event.key == pygame.K_i:
                level = 3
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                pumpkin_pie_color = played_color
            if event.key == pygame.K_o:
                level = 4
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                cornbread_color = played_color
            if event.key == pygame.K_r:
                level = 5
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                roll_color = played_color
            if event.key == pygame.K_e:
                level = 6
                draw_background()
                random.shuffle(nums)
                num_cols = {nums[0]: 0, nums[1]: 0, nums[2]: 0, nums[3]: 1, nums[4]: 1, nums[5]: 1, nums[6]: 2,
                            nums[7]: 2, nums[8]: 2,
                            nums[9]: 3, nums[10]: 3, nums[11]: 3}
                num_rows = {nums[0]: 0, nums[1]: 1, nums[2]: 2, nums[3]: 0, nums[4]: 1, nums[5]: 2, nums[6]: 0,
                            nums[7]: 1, nums[8]: 2,
                            nums[9]: 0, nums[10]: 1, nums[11]: 2}
                piecey = draw_board()
                pecan_pie_color = played_color
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
            if restart_button.collidepoint(event.pos):
                screen.blit(background, (0, 0))
                match = 0
                score = 0
                correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                score_text = lil_font.render(f'Score:{score}', True, (0, 44, 255))
                levels_won_text = lil_font.render(f"Levels won: {levels_won_counter}/7", True, (0, 44, 255))
                draw_homescreen()


        if first_guess:
            screen.blit(num_foods[level][first_guess_word], location1)
        if second_guess:
            screen.blit(num_foods[level][second_guess_word], location2)


    if overall_score > highscore:
        highscore = overall_score
        with open('highscore.dat', 'wb') as file:
            pickle.dump(overall_score, file)




    pygame.display.flip()
