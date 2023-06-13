import pygame
import random
import constants.static
import time
from setup import *
import constants.dynamic
from mobs.player1 import Player1
from mobs.enemy import Enemy
import copy


def flash():
    for _ in range(constants.static.FLASH_TIMES):
        screen.fill(constants.static.BACKGROUND)
        pygame.display.flip()
        time.sleep(constants.static.FLASH_DURATION)
        all.draw(screen)
        pygame.display.flip()
        time.sleep(constants.static.FLASH_DURATION)


# set up sprite groups
all = pygame.sprite.Group()
players = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
sprite_group_args = (all, players, enemies, bullets)

Player1(players, all)

# set up placement matrices
# each number in the matrix represents a position on the screen.
# True means that position is to be occupied by an enemy, False means it is not to be occupied by an enemy.
# The first matrix represents a full screen of enemies, the rest are randomized proportional to the difficulty.
placement_matrices = []
placement_matrix_template = []
for _ in range(constants.static.PLAYER_MAX_HEIGHT//constants.static.ENEMY_POS_DISPLACEMENT):
    placement_matrix_template.append(
        [False]*(constants.static.WIDTH//constants.static.ENEMY_POS_DISPLACEMENT-1))
placement_matrix = copy.deepcopy(placement_matrix_template)
for i in range(len(placement_matrix)):
    for j in range(len(placement_matrix[i])):
        placement_matrix[i][j] = True
placement_matrices.append(placement_matrix)
for _ in range(constants.static.RANDOMIZED_MATRIX_COUNT):
    placement_matrix = copy.deepcopy(placement_matrix_template)
    for i in range(len(placement_matrix)):
        for j in range(len(placement_matrix[i])):
            if random.randrange(int(1/constants.static.DIFFICULTY)) == 0:
                placement_matrix[i][j] = True
    placement_matrices.append(placement_matrix)

while running:
    screen.fill(constants.static.BACKGROUND)
    control_args = []  # list of commands to be passed to the entities
    # spawn new wave of enemies at start of game and when player beats a wave
    if len(enemies.sprites()) == 0:
        grid = placement_matrices[random.randrange(len(placement_matrices))]
        # create each enemy and send it to its assigned position
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    Enemy(players, ((j+1)*constants.static.ENEMY_POS_DISPLACEMENT,
                          (i+1)*constants.static.ENEMY_POS_DISPLACEMENT), enemies, all)
        # blink to signal the start of a new wave
        for _ in range(constants.static.BLINK_TIMES):
            screen.fill(constants.static.BACKGROUND)
            pygame.display.flip()
            time.sleep(constants.static.BLINK_DURATION)
            all.draw(screen)
            pygame.display.flip()
            time.sleep(constants.static.BLINK_DURATION)
        time.sleep(constants.static.BLINK_DURATION)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            control_args.append("p1_shoot")
    all.update(control_args, sprite_group_args)
    all.draw(screen)
    pygame.display.flip()
    clock.tick(constants.static.FPS)
pygame.quit
