import pygame

TILE_SIZE = 60
SCREEN_WIDTH = 725
SCREEN_HEIGHT = 650
BRICK_SIZE = 150
WSPACE = 25
HEADER = 130
HSPACE = 25
rows = 3
cols = 4
ingredients = (6, 9, 5, 7, 4, 4, 7, 5, 7, 7)
row1 = HEADER
row2 = HEADER+BRICK_SIZE+HSPACE
row3 = HEADER+2*BRICK_SIZE+2*HSPACE
col1 = WSPACE
col2 = 2*WSPACE+BRICK_SIZE
col3 = 3*WSPACE+2*BRICK_SIZE
col4 = 4*WSPACE+3*BRICK_SIZE



real_overall_score = 0
level = 1
first_guess = False
second_guess = False
level1 = False
first_guess_word = 0
second_guess_word = 0
fps = 60
score = 0
match = 0
overall_score = 0

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

place = [(col1, row1), (col1, row2), (col1, row3), (col2, row1), (col2, row2), (col2, row3), (col3, row1), (col3, row2),
         (col3, row3), (col4, row1), (col4, row2), (col4, row3)]
places = [[0, 1, 2, 3], [0, 1, 2, 3], [0, 1, 2, 3]]
correct = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


BACKGROUND_COLOR = (250, 244, 167)
HSCOLOR = (92, 66, 28)
BLACK = (0,0,0)
