import pygame
import sys
from settings import *

print("hello world!")

pygame.init()

game_font = pygame.font.Font("assets/fonts/Queensides.ttf", 48)
level = 1
pygame.display.set_caption("Thanksgiving Dinner")
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(BACKGROUND_COLOR)
background = screen.copy()
clock = pygame.time.Clock()

butter = pygame.image.load("assets/images/butter.png").convert()


def draw_background(ing):
    background.fill((250, 244, 167))
    for x in range(2):
        for i in range(ingredients[ing]):
            if ingredients[ing] == 9:
                ring = (SPACE*2+ i*(SPACE+BRICK_SIZE),SCREEN_HEIGHT//2 + x*(SPACE+BRICK_SIZE))
            if ingredients[ing] == 7:
                ring = (2*BRICK_SIZE - BRICK_SIZE//2 + i*(SPACE+BRICK_SIZE),SCREEN_HEIGHT//2 + x*(SPACE+BRICK_SIZE))
            if ingredients[ing] == 5:
                ring = (3*BRICK_SIZE - BRICK_SIZE//2 + i * (SPACE + BRICK_SIZE), SCREEN_HEIGHT // 2 + x * (SPACE + BRICK_SIZE))
            if ingredients[ing] == 4:
                ring = (3*BRICK_SIZE + BRICK_SIZE//2 -SPACE + i * (SPACE + BRICK_SIZE), SCREEN_HEIGHT // 2 + x * (SPACE + BRICK_SIZE))
            background.blit(butter, ring)
    text = game_font.render("Matching", True, (64, 44, 4))
    level_text = game_font.render(f"Level {level}", True, (64, 44, 4))
    # make level that will eventually change with each level
    background.blit(text, (TILE_SIZE * 2, TILE_SIZE // 2))
    background.blit(level_text, (SCREEN_WIDTH - TILE_SIZE * 2 - level_text.get_width(), TILE_SIZE // 2))


draw_background(1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    pygame.display.flip()
