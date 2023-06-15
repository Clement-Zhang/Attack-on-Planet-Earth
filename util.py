from setup import *
from mechanics.events import Events
from collection import Collection
import pygame
import data.constant
import data.var
import random
from entity.mob.enemy import Enemy


class Util():
    """Utility functions"""

    def blink():
        # blink signals the start of a new wave
        for _ in range(data.constant.BLINK_TIMES):
            screen.fill(data.constant.BACKGROUND)
            pygame.display.flip()
            pygame.time.wait(data.constant.BLINK_DURATION)
            Collection.get_all().draw(screen)
            pygame.display.flip()
            pygame.time.wait(data.constant.BLINK_DURATION)
            Events.alternating(pygame.event.get(pygame.QUIT))

    def flash():
        # flash signals the player's death
        for _ in range(data.constant.FLASH_TIMES):
            screen.fill(data.constant.BACKGROUND)
            pygame.display.flip()
            pygame.time.wait(data.constant.FLASH_DURATION)
            Collection.get_all().draw(screen)
            pygame.display.flip()
            pygame.time.wait(data.constant.FLASH_DURATION)
            Events.alternating(pygame.event.get(pygame.QUIT))

    def new_wave():
        grid = random.choice(data.var.placement_matrices)
        # create each enemy and send it to its assigned position
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j]:
                    Collection.add_enemy(Enemy(
                        ((j+1)*data.constant.ENEMY_POS_DISPLACEMENT, (i+1)*data.constant.ENEMY_POS_DISPLACEMENT)))
        # blink to signal the start of a new wave
        Util.blink()
