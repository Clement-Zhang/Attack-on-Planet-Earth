from setup import *
from mechanics.events import Events
import random
import copy
from collection import Collection
import pygame


class Util():
    """Utility functions"""

    def __init__(self):
        # set up placement matrices
        # each number in the matrix represents a position on the screen.
        # True means that position is to be occupied by an enemy, False means it is not to be occupied by an enemy.
        # The first matrix represents a full screen of enemies, the rest are randomized proportional to the difficulty.
        self.placement_matrices = []
        placement_matrix_template = [[False]*(constant.static.WIDTH//constant.static.ENEMY_POS_DISPLACEMENT-1)
                                     for _ in range(constant.static.PLAYER_MAX_HEIGHT//constant.static.ENEMY_POS_DISPLACEMENT)]
        placement_matrix = copy.deepcopy(placement_matrix_template)
        self.placement_matrices.append([[True]*(constant.static.WIDTH//constant.static.ENEMY_POS_DISPLACEMENT-1)
                                        for _ in range(constant.static.PLAYER_MAX_HEIGHT//constant.static.ENEMY_POS_DISPLACEMENT)])
        for _ in range(constant.static.RANDOMIZED_MATRIX_COUNT):
            placement_matrix = copy.deepcopy(placement_matrix_template)
            for i in range(len(placement_matrix)):
                for j in range(len(placement_matrix[i])):
                    if random.randrange(int(1 / constant.static.DIFFICULTY)) == 0:
                        placement_matrix[i][j] = True
            self.placement_matrices.append(placement_matrix)
        self.collection = Collection()
        self.events = Events()

    def blink(self):
        # blink signals the start of a new wave
        for _ in range(constant.static.BLINK_TIMES):
            screen.fill(constant.static.BACKGROUND)
            pygame.display.flip()
            pygame.time.wait(constant.static.BLINK_DURATION)
            self.collection.get_all().draw(screen)
            pygame.display.flip()
            pygame.time.wait(constant.static.BLINK_DURATION)
            self.events.alternating(pygame.event.get(pygame.QUIT))

    def flash(self):
        # flash signals the player's death
        for _ in range(constant.static.FLASH_TIMES):
            screen.fill(constant.static.BACKGROUND)
            pygame.display.flip()
            pygame.time.wait(constant.static.FLASH_DURATION)
            self.collection.get_all().draw(screen)
            pygame.display.flip()
            pygame.time.wait(constant.static.FLASH_DURATION)
            self.events.alternating(pygame.event.get(pygame.QUIT))

    def new_wave(self):
        grid = random.choice(self.placement_matrices)
        # create each enemy and send it to its assigned position
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    self.collection.add_enemy(
                        ((j+1)*constant.static.ENEMY_POS_DISPLACEMENT, (i+1)*constant.static.ENEMY_POS_DISPLACEMENT))
        # blink to signal the start of a new wave
        self.blink()
