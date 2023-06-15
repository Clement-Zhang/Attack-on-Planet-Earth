from data.constant import *
import os
import pygame
from enums.sprite_group import SpriteGroup
import copy
import random

game_folder = os.path.join(os.path.dirname(__file__), '..')
player_folder = os.path.join(
    game_folder, "art/player")
enemy_folder = os.path.join(
    game_folder, "art/enemy")
projectile_folder = os.path.join(game_folder, "art/projectile")
# how far from the top of the screen the enemy must spawn
enemy_spawn_y_min = -PLAYER_ENEMY_SIZE[1]
# how far from the top of the screen the enemy can spawn
enemy_spawn_y_max = -PLAYER_ENEMY_SIZE[1] * ENEMY_SPAWN_AREA
player_max_height = HEIGHT-PLAYER_GAMEPLAY_AREA
enemy_shoot = pygame.event.custom_type()
sprite_groups = [pygame.sprite.Group() for _ in range(len(SpriteGroup))]
# set up placement matrices
# each number in the matrix represents a position on the screen.
# True means that position is to be occupied by an enemy, False means it is not to be occupied by an enemy.
# The first matrix represents a full screen of enemies, the rest are randomized proportional to the difficulty.
placement_matrices = []
placement_matrix_template = [[False]*(WIDTH//ENEMY_POS_DISPLACEMENT-1)
                             for _ in range(player_max_height//ENEMY_POS_DISPLACEMENT)]
placement_matrix = copy.deepcopy(placement_matrix_template)
placement_matrices.append([[True]*(WIDTH//ENEMY_POS_DISPLACEMENT-1)
                           for _ in range(player_max_height//ENEMY_POS_DISPLACEMENT)])
for _ in range(RANDOMIZED_MATRIX_COUNT):
    placement_matrix = copy.deepcopy(placement_matrix_template)
    for i in range(len(placement_matrix)):
        for j in range(len(placement_matrix[i])):
            if random.randrange(int(1 / DIFFICULTY)) == 0:
                placement_matrix[i][j] = True
    placement_matrices.append(placement_matrix)
