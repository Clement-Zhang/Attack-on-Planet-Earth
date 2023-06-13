import math
from mobs.mob import Mob
import constants.static
import constants.dynamic
import random
import os
import pygame
import projectiles.regular_bullet


class Enemy(Mob):
    def __init__(self, bullet_group, spot, *sprite_groups):
        super().__init__(*sprite_groups)
        self.bullet_group = bullet_group
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            constants.dynamic.ENEMY_FOLDER, "fly straight.png")).convert(), constants.static.PLAYER_ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(
            constants.static.ENEMY_SPAWN_X_RANGE, constants.static.WIDTH-constants.static.ENEMY_SPAWN_X_RANGE)
        self.rect.centery = random.randrange(
            constants.static.ENEMY_SPAWN_Y_MAX, constants.static.ENEMY_SPAWN_Y_MIN)
        self.spot = spot  # final destination, corresponds to its spot in the placement matrix

    def move(self):
        """Move the enemy towards its final spot at the speed of ENEMY_SPEED"""
        start = self.rect.center
        dist_x = self.spot[0]-start[0]
        dist_y = self.spot[1]-start[1]
        hypot = math.hypot(dist_x, dist_y)
        if hypot == 0:
            hypot = constants.static.SMALL_NONZERO_VALUE
        unit_x = dist_x/hypot
        unit_y = dist_y/hypot
        travelx = unit_x*constants.static.ENEMY_SPEED
        travely = unit_y*constants.static.ENEMY_SPEED
        if hypot <= constants.static.ENEMY_SPEED:
            # if the enemy is close enough to its final spot, just move it there to avoid jittering
            travelx = dist_x
            travely = dist_y
        self.rect.centerx += travelx
        self.rect.centery += travely

    def shoot(self):
        """Enemy shooting is to be done in a centralized manner"""
        projectiles.regular_bullet.RegBullet(
            constants.static.REGULAR_BULLET_SPEED,
            (self.rect.centerx, self.rect.bottom + constants.static.REGULAR_BULLET_SIZE[1] / 2), self.bullet_group)

    def update(self, control_args, sprite_group_args):
        """Perform all the actions necessary in one frame"""
        self.move()
