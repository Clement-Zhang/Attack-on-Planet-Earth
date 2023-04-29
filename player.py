import pygame
import math
from mob import Mob
import constants.dynamic
import constants.static

class Player(Mob):
    def __init__(self, *sprite_groups):
        super().__init__()
        self.image = constants.dynamic.PLAYER_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (constants.static.WIDTH/2, constants.static.HEIGHT/2)
        for sprite_group in sprite_groups:
            sprite_group.add(self)

    def move(self):
        start = self.rect.center
        end = pygame.mouse.get_pos()
        dist_x = end[0]-start[0]
        dist_y = -(end[1]-start[1])
        pi = math.pi
        if dist_x == 0:
            dist_x = 10 ** -6
        hypot = math.hypot(dist_x, dist_y)
        angle = math.atan2(dist_y, dist_x)
        x = math.cos(angle)*(hypot/2)**.5
        y = -math.sin(angle)*(hypot/2)**.5
        if abs(hypot*math.cos(angle)) < 5:
            x = 0  # center
        if x > 5 and angle < (.5*pi) and angle > (-.5*pi):
            x = 5  # right
        if x < -5 and angle < (-.5*pi) or angle > (.5*pi):
            x = -5  # left
        if abs(hypot*math.sin(angle)) < 5:
            y = 0  # center
        if y > 5 and angle < 0:
            y = 5  # down
        if y < -5 and angle > 0:
            y = -5  # up
        self.rect.centerx += x
        self.rect.centery += y

    def update(self):
        self.move()