import math
from mob import Mob
from constants import static
from constants import dynamic
import random

class Enemy(Mob):
    def __init__(self, players, *sprite_groups):
        super().__init__()
        self.players = players
        self.image = dynamic.ENEMY_IMG
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randrange(25, static.WIDTH-25)
        self.rect.centery = random.randrange(25, static.HEIGHT-25)
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
            hypot = 10**-6
        unit_x = dist_x/hypot
        unit_y = dist_y/hypot
        self.rect.centerx += unit_x*4
        self.rect.centery += unit_y*4
        
    def update(self):
        self.move()