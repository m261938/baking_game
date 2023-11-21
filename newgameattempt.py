import pygame
import random
from settings import *

pygame.init()

timer = pygame.time.Clock()
correct = []
options = []
pieces = []
used = []
new_board = True
first_guess = False
second_guess = False
first_guess_num = 0
