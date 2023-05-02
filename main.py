import pygame
import random
import constants.static
import time
from setup import *
import constants.dynamic
from player import Player
from enemy import Enemy
import copy

all = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()

Player(players, all)
placement_matrices = []
placement_matrix_template = []
for _ in range(constants.static.HEIGHT//constants.static.ENEMY_POS_DISPLACEMENT):
    placement_matrix_template.append(
        [1]*(constants.static.WIDTH//constants.static.ENEMY_POS_DISPLACEMENT))
placement_matrices.append(copy.deepcopy(placement_matrix_template))
for _ in range(constants.static.RANDOMIZED_MATRIX_COUNT):
    placement_matrix = copy.deepcopy(placement_matrix_template)
    for i in range(constants.static.HEIGHT//constants.static.ENEMY_POS_DISPLACEMENT):
        for j in range(constants.static.WIDTH//constants.static.ENEMY_POS_DISPLACEMENT):
            if random.randrange(0, 2):
                placement_matrix[i][j] = 0
    placement_matrices.append(placement_matrix)

all.draw(screen)
pygame.display.flip()
time.sleep(1.5)

while running:
    clock.tick(constants.static.FPS)
    # process inputs
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = 0
    # update
    all.update()
    # draw screen
    screen.fill(constants.static.BACKGROUND)
    all.draw(screen)
    pygame.display.flip()
pygame.quit
