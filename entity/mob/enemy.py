import math
from entity.mob.mob import Mob
import data.constant
import data.var
import random
import os
import pygame
from entity.projectile.regular_bullet import RegBullet
from collection import Collection


class Enemy(Mob):
    def __init__(self, spot):
        super().__init__()
        self.image = pygame.transform.flip(pygame.transform.scale(pygame.image.load(os.path.join(
            data.var.plane_folder, "fly straight.png")).convert(), data.constant.PLAYER_ENEMY_SIZE), False, True)
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(
            data.constant.ENEMY_SPAWN_X_RANGE, data.constant.WIDTH-data.constant.ENEMY_SPAWN_X_RANGE)
        self.rect.centery = random.randrange(
            data.var.enemy_spawn_y_max, data.var.enemy_spawn_y_min)
        self.spot = spot  # final destination, corresponds to its spot in the placement matrix

    def move(self):
        """Move the enemy towards its final spot at the speed of ENEMY_SPEED"""
        start = self.rect.center
        dist_x = self.spot[0] - start[0]
        dist_y = self.spot[1] - start[1]
        hypot = math.hypot(dist_x, dist_y)
        if hypot == 0:
            hypot = data.constant.SMALL_NONZERO_VALUE
        unit_x = dist_x / hypot
        unit_y = dist_y / hypot
        travelx = unit_x * data.constant.ENEMY_SPEED
        travely = unit_y * data.constant.ENEMY_SPEED
        if hypot <= data.constant.ENEMY_SPEED:
            # if the enemy is close enough to its final spot, just move it there to avoid jittering
            travelx = dist_x
            travely = dist_y
        self.rect.centerx += travelx
        self.rect.centery += travely

    def shoot(self):
        """Spawn a bullet for event handler to pass to collection"""
        Collection.add_enemy_bullet(RegBullet(data.constant.REGULAR_BULLET_SPEED, (self.rect.centerx,
                                                                                   self.rect.bottom + data.constant.REGULAR_BULLET_SIZE[1] / 2)))

    def update(self):
        """Perform all the actions necessary in one frame"""
        self.move()
