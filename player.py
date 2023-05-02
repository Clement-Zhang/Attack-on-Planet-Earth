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
        self.rect.center = (constants.static.WIDTH/2,
                            constants.static.HEIGHT-self.rect.height)
        for sprite_group in sprite_groups:
            sprite_group.add(self)

    def move(self):
        start = self.rect.center
        end = pygame.mouse.get_pos()
        dist_x = end[0]-start[0]
        dist_y = -(end[1]-start[1])
        pi = math.pi
        if dist_x == 0:
            dist_x = constants.static.SMALL_NONZERO_VALUE
        hypot = math.hypot(dist_x, dist_y)
        angle = math.atan2(dist_y, dist_x)
        x = math.cos(angle)*(hypot*constants.static.SPEED_SENSITIVITY)**.5
        y = -math.sin(angle)*(hypot*constants.static.SPEED_SENSITIVITY)**.5
        if abs(hypot*math.cos(angle)) < 5:
            x = 0  # center
        if x > 5 and angle < (.5*pi) and angle > (-.5*pi):
            x = constants.static.PLAYER_MAX_SPEED  # right
        if x < -5 and angle < (-.5*pi) or angle > (.5*pi):
            x = -constants.static.PLAYER_MAX_SPEED  # left
        if y > 5 and angle < 0:
            y = constants.static.PLAYER_MAX_SPEED  # down
        if y < -5 and angle > 0:
            y = -constants.static.PLAYER_MAX_SPEED  # up
        if abs(hypot*math.sin(angle)) < 5 or y<0 and self.rect.top<=constants.static.PLAYER_MAX_HEIGHT:
            y = 0  # center
        self.rect.centerx += x
        self.rect.centery += y

    def update(self):
        self.move()
