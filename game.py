import pygame
import sys
from settings import *
import random

print("hello world!")

pygame.init()

game_font = pygame.font.Font("assets/fonts/Queensides.ttf", 48)
level = 1
pygame.display.set_caption("Thanksgiving Dinner")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
background = screen.copy()
clock = pygame.time.Clock()
a = pygame.image.load("assets/images/a.png").convert()
b = pygame.image.load("assets/images/b.png").convert()
c = pygame.image.load("assets/images/c.png").convert()
d = pygame.image.load("assets/images/d.png").convert()
e = pygame.image.load("assets/images/e.png").convert()
f = pygame.image.load("assets/images/f.png").convert()
g = pygame.image.load("assets/images/g.png").convert()
h = pygame.image.load("assets/images/h.png").convert()
i = pygame.image.load("assets/images/i.png").convert()
j = pygame.image.load("assets/images/j.png").convert()
k = pygame.image.load("assets/images/k.png").convert()
l = pygame.image.load("assets/images/l.png").convert()

turkey = pygame.image.load("assets/images/turkey.png").convert()
salt = pygame.image.load("assets/images/salt.png").convert()
pepper = pygame.image.load("assets/images/pepper.png").convert()
onion = pygame.image.load("assets/images/onion.png").convert()
carrot = pygame.image.load("assets/images/carrot.png").convert()
celery = pygame.image.load("assets/images/celery.png").convert()


def draw_background():
    background.fill((250, 244, 167))
    background.blit(a,(col1, row1))
    background.blit(b,(col2, row1))
    background.blit(c, (col3, row1))
    background.blit(d, (col4, row1))
    background.blit(e, (col1, row2))
    background.blit(f, (col2, row2))
    background.blit(g, (col3, row2))
    background.blit(h, (col4, row2))
    background.blit(i, (col1, row3))
    background.blit(j, (col2, row3))
    background.blit(k, (col3, row3))
    background.blit(l, (col4, row3))





    text = game_font.render("Matching", True, (64, 44, 4))
    level_text = game_font.render(f"Level {level}", True, (64, 44, 4))
    # make level that will eventually change with each level
    background.blit(text, (TILE_SIZE * 2, TILE_SIZE // 2))
    background.blit(level_text, (SCREEN_WIDTH - TILE_SIZE * 2 - level_text.get_width(), TILE_SIZE // 2))


turkey = [turkey, turkey, salt, salt, pepper, pepper, onion, onion, carrot, carrot, celery, celery]
random.shuffle(turkey)

def flip_tile(pic, col, row):
    background.blit(pic, (col, row))



draw_background()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                flip_tile(turkey[0], col1, row1)
            if event.key == pygame.K_b:
                flip_tile(turkey[1], col2, row1)
            if event.key == pygame.K_c:
                    flip_tile(turkey[2], col3, row1)
            if event.key == pygame.K_d:
                flip_tile(turkey[3], col4, row1)
            if event.key == pygame.K_e:
                flip_tile(turkey[4], col1, row2)
            if event.key == pygame.K_f:
                flip_tile(turkey[5], col2, row2)
            if event.key == pygame.K_g:
                flip_tile(turkey[6], col3, row2)
            if event.key == pygame.K_h:
                flip_tile(turkey[7], col4, row2)
            if event.key == pygame.K_i:
                flip_tile(turkey[8], col1, row3)
            if event.key == pygame.K_j:
                flip_tile(turkey[9], col2, row3)
            if event.key == pygame.K_k:
                flip_tile(turkey[10], col3, row3)
            if event.key == pygame.K_l:
                flip_tile(turkey[11], col4, row3)
    screen.blit(background, (0, 0))
    pygame.display.flip()
