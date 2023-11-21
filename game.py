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
first_guess_thing = 0
second_guess_thing = 0
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

letters = [a,b,c,d,e,f,g,h,i,j,k,l]
place = [(col1,row1),(col2, row1), (col3, row1), (col4, row1), (col1, row2), (col2, row2), (col3, row2),
         (col4, row2), (col1, row3), (col2, row3), (col3, row3), (col4, row3)]
turkey = [turkey, turkey, salt, salt, pepper, pepper, onion, onion, carrot, carrot, celery, celery]
random.shuffle(turkey)
correct = []




def draw_background():
    background.fill((250, 244, 167))
    # background.blit(a,place[0])
    # background.blit(b,place[1])
    # background.blit(c, place[2])
    # background.blit(d, place[3])
    # background.blit(e, place[4])
    # background.blit(f, place[5])
    # background.blit(g, place[6])
    # background.blit(h, place[7])
    # background.blit(i, place[8])
    # background.blit(j, place[9])
    # background.blit(k, place[10])
    # background.blit(l, place[11])
    text = game_font.render("Matching", True, (64, 44, 4))
    level_text = game_font.render(f"Level {level}", True, (64, 44, 4))
    # make level that will eventually change with each level
    background.blit(text, (TILE_SIZE * 2, TILE_SIZE // 2))
    background.blit(level_text, (SCREEN_WIDTH - TILE_SIZE * 2 - level_text.get_width(), TILE_SIZE // 2))

def draw_board():
    board_list = []
    for i in range(cols):
        for j in range(rows):
            piece = pygame.draw.rect(screen, (140, 109, 24), [i*(BRICK_SIZE+WSPACE)+WSPACE, j*(BRICK_SIZE+HSPACE) + HSPACE +100, BRICK_SIZE, BRICK_SIZE])
            board_list.append(piece)
    return board_list

# class Card:
#     def __init__(self, position):
#         self.position = position
#     def showfront(self):
#         background.blit(letters[self.position], place[self.position])
#     def showback(self):
#         background.blit(turkey[self.position], place[self.position])
#     def match(self):
#       if they both match keep them there and add 1 to the counter bc when counter hits 6 the round is done





# put this list then into a dictionary?



def flip_tile(pic, place):
    background.blit(pic, place)



#def match1():
   # holder = 0
    #if event.key == pygame.K_a:
     #   flip_tile(turkey[0], col1, row1)
      #  holder = turkey[0]
    #elif event.key == pygame.K_b:
     #   flip_tile(turkey[1], col2, row1)
      #  holder = turkey[1]
    #elif event.key == pygame.K_c:
     #   flip_tile(turkey[2], col3, row1)
      #  holder = turkey[2]
    #elif event.key == pygame.K_d:
     #   flip_tile(turkey[3], col4, row1)
      #  holder = turkey[3]
    #elif event.key == pygame.K_e:
     #   flip_tile(turkey[4], col1, row2)
      #  holder = turkey[4]
    #elif event.key == pygame.K_f:
     #   flip_tile(turkey[5], col2, row2)
      #  holder = turkey[5]
    #elif event.key == pygame.K_g:
     #   flip_tile(turkey[6], col3, row2)
      #  holder = turkey[6]
    #elif event.key == pygame.K_h:
     #   flip_tile(turkey[7], col4, row2)
      #  holder = turkey[7]
    #elif event.key == pygame.K_i:
     #   flip_tile(turkey[8], col1, row3)
      #  holder = turkey[8]
    #elif event.key == pygame.K_j:
     #   flip_tile(turkey[9], col2, row3)
      #  holder = turkey[9]
    #elif event.key == pygame.K_k:
     #   flip_tile(turkey[10], col3, row3)
      #  holder = turkey[10]
    #elif event.key == pygame.K_l:
      #  flip_tile(turkey[11], col4, row3)
     #   holder = turkey[11]
    #return holder
#holder1 = match1()
#def match2(hold):
  #  holder = 0
   # if event.key == pygame.K_a:
    #    flip_tile(turkey[0], col1, row1)
     #   holder = turkey[0]
    #elif event.key == pygame.K_b:
#         flip_tile(turkey[1], col2, row1)
#         holder = turkey[1]
#     elif event.key == pygame.K_c:
#         flip_tile(turkey[2], col3, row1)
#         holder = turkey[2]
#     elif event.key == pygame.K_d:
#         flip_tile(turkey[3], col4, row1)
#         holder = turkey[3]
#     elif event.key == pygame.K_e:
#         flip_tile(turkey[4], col1, row2)
#         holder = turkey[4]
#     elif event.key == pygame.K_f:
#         flip_tile(turkey[5], col2, row2)
#         holder = turkey[5]
#     elif event.key == pygame.K_g:
#         flip_tile(turkey[6], col3, row2)
#         holder = turkey[6]
#     elif event.key == pygame.K_h:
#         flip_tile(turkey[7], col4, row2)
#         holder = turkey[7]
#     elif event.key == pygame.K_i:
#         flip_tile(turkey[8], col1, row3)
#         holder = turkey[8]
#     elif event.key == pygame.K_j:
#         flip_tile(turkey[9], col2, row3)
#         holder = turkey[9]
#     elif event.key == pygame.K_k:
#         flip_tile(turkey[10], col3, row3)
#         holder = turkey[10]
#     elif event.key == pygame.K_l:
#         flip_tile(turkey[11], col4, row3)
#         holder = turkey[11]
#     if hold != holder:
#         background.blit(a, col1, row1)
#
#
draw_background()
# for event in pygame.event.get():
#     if event.type == pygame.KEYDOWN:
#         match1()

tilea = None
tileb = None
hold = None
while True:
    timer.tick(fps)
    # if tilea & tileb  == None:
    #     tilea = hold
    # elif tilea != None & tileb == None:
    #     tileb = hold
    # elif tilea & tileb != None:
    screen.blit(background, (0, 0))
    draw_board()


    for event in pygame.event.get():
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(turkey)):
                button = turkey[i]
                if button.collidepoint(event.pos) and not first_guess:
                    first_guess = True
                    first_guess_thing = i
                    print(i)
                if button.collidepoint(event.pos) and not second_guess and first_guess and i != first_guess_thing:
                    second_guess = True
                    second_guess_thing = i
                    print(i)
         if first_guess and second_guess:
            first_guess = False
            second_guess = False
         # if event.type == pygame.KEYDOWN:
         #    if event.key == pygame.K_a:
         #        flip_tile(turkey[0],place[0])
         #        hold = turkey[0]
         #    elif event.key == pygame.K_b:
         #        flip_tile(turkey[1], place[1])
         #    elif event.key == pygame.K_c:
         #        flip_tile(turkey[2], place[2])
         #    elif event.key == pygame.K_d:
         #        flip_tile(turkey[3], place[3])
         #    elif event.key == pygame.K_e:
         #        flip_tile(turkey[4], place[4])
         #    elif event.key == pygame.K_f:
         #        flip_tile(turkey[5], place[5])
         #    elif event.key == pygame.K_g:
         #        flip_tile(turkey[6], place[6])
         #    elif event.key == pygame.K_h:
         #        flip_tile(turkey[7], place[7])
         #    elif event.key == pygame.K_i:
         #        flip_tile(turkey[8], place[8])
         #    elif event.key == pygame.K_j:
         #        flip_tile(turkey[9], place[9])
         #    elif event.key == pygame.K_k:
         #        flip_tile(turkey[10], place[10])
         #    elif event.key == pygame.K_l:
         #        flip_tile(turkey[11], place[11])

    pygame.display.flip()
