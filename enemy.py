import math
from mob import Mob
import constants.static
import constants.dynamic
import random


class Enemy(Mob):
    def __init__(self, players, *sprite_groups):
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

    def move(self):
        possible_targets = self.players.sprites()
        target = possible_targets[0]
        target_dist = math.hypot(
            target.rect.centerx-self.rect.centerx, target.rect.centery-self.rect.centery)
        for i in range(1, len(possible_targets)):
            dist = math.hypot(possible_targets[i].rect.centerx-self.rect.centerx,
                              possible_targets[i].rect.centery-self.rect.centery)
            if dist < target_dist:
                target_dist = dist
                target = possible_targets[i]
        start = self.rect.center
        end = target.rect.center
        dist_x = end[0]-start[0]
        dist_y = end[1]-start[1]
        hypot = math.hypot(dist_x, dist_y)
        if hypot == 0:
            hypot = constants.static.SMALL_NONZERO_VALUE
        unit_x = dist_x/hypot
        unit_y = dist_y/hypot
        self.rect.centerx += unit_x*constants.static.ENEMY_MAX_SPEED
        self.rect.centery += unit_y*constants.static.ENEMY_MAX_SPEED

    def update(self):
        self.move()
