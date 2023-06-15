import math
from entity.mob.mob import Mob
import constant.static
import constant.dynamic
import random
import os
import pygame


class Enemy(Mob):
    def __init__(self, spot):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            constant.dynamic.ENEMY_FOLDER, "fly straight.png")).convert(), constant.static.PLAYER_ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(
            constant.static.ENEMY_SPAWN_X_RANGE, constant.static.WIDTH-constant.static.ENEMY_SPAWN_X_RANGE)
        self.rect.centery = random.randrange(
            constant.static.ENEMY_SPAWN_Y_MAX, constant.static.ENEMY_SPAWN_Y_MIN)
        self.spot = spot  # final destination, corresponds to its spot in the placement matrix

    def move(self):
        """Move the enemy towards its final spot at the speed of ENEMY_SPEED"""
        start = self.rect.center
        dist_x = self.spot[0] - start[0]
        dist_y = self.spot[1] - start[1]
        hypot = math.hypot(dist_x, dist_y)
        if hypot == 0:
            hypot = constant.static.SMALL_NONZERO_VALUE
        unit_x = dist_x / hypot
        unit_y = dist_y / hypot
        travelx = unit_x * constant.static.ENEMY_SPEED
        travely = unit_y * constant.static.ENEMY_SPEED
        if hypot <= constant.static.ENEMY_SPEED:
            # if the enemy is close enough to its final spot, just move it there to avoid jittering
            travelx = dist_x
            travely = dist_y
        self.rect.centerx += travelx
        self.rect.centery += travely

    def shoot(self, collection):
        """Enemy shooting is to be done in a centralized manner"""
        collection.add_enemy_bullet(
            (self.rect.centerx, self.rect.bottom + constant.static.REGULAR_BULLET_SIZE[1] / 2))

    def update(self):
        """Perform all the actions necessary in one frame"""
        self.move()
