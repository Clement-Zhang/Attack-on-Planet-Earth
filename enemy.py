import math
from mob import Mob
import constants.static
import constants.dynamic
import random


class Enemy(Mob):
    def __init__(self, players, spot, *sprite_groups):
        super().__init__()
        self.players = players
        self.image = constants.dynamic.ENEMY_IMG
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(
            constants.static.ENEMY_SPAWN_X_RANGE, constants.static.WIDTH-constants.static.ENEMY_SPAWN_X_RANGE)
        self.rect.centery = random.randrange(
            constants.static.ENEMY_SPAWN_Y_MAX, constants.static.ENEMY_SPAWN_Y_MIN)
        for sprite_group in sprite_groups:
            sprite_group.add(self)
        self.spot = spot

    def move(self):
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
            travelx = dist_x
            travely = dist_y
        self.rect.centerx += travelx
        self.rect.centery += travely

    def update(self):
        self.move()
