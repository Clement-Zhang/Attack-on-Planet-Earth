import pygame
import math
from mobs.mob import Mob
import constants.dynamic
import constants.static
from sprite_groups import SpriteGroups


class Player1(Mob):
    def __init__(self, *sprite_groups):
        super().__init__()
        self.image = constants.dynamic.PLAYER_IMG
        self.rect = self.image.get_rect()
        self.rect.center = (constants.static.WIDTH/2,
                            constants.static.HEIGHT-self.rect.height)
        for sprite_group in sprite_groups:
            sprite_group.add(self)

    def move(self):
        """Move the player towards the mouse, agario style.
        Max speed is PLAYER_MAX_SPEED, the player moves proportionate to the distance from the mouse,
        and the player cannot move more than PLAYER_GAMEPLAY_AREA pixels from the bottom of the screen."""
        start = self.rect.center
        end = pygame.mouse.get_pos()
        dist_x = end[0]-start[0]
        # due to angle calculations this calculation must be negated
        dist_y = -(end[1]-start[1])
        pi = math.pi
        if dist_x == 0:
            dist_x = constants.static.SMALL_NONZERO_VALUE
        hypot = math.hypot(dist_x, dist_y)
        angle = math.atan2(dist_y, dist_x)
        x = math.cos(angle)*(hypot*constants.static.SPEED_SENSITIVITY)
        y = -math.sin(angle)*(hypot*constants.static.SPEED_SENSITIVITY)
        if x > constants.static.PLAYER_MAX_SPEED and angle < (.5*pi) and angle > (-.5*pi):
            x = constants.static.PLAYER_MAX_SPEED  # right
        if x < -constants.static.PLAYER_MAX_SPEED and angle < (-.5*pi) or angle > (.5*pi):
            x = -constants.static.PLAYER_MAX_SPEED  # left
        if y > constants.static.PLAYER_MAX_SPEED and angle < 0:
            y = constants.static.PLAYER_MAX_SPEED  # down
        if y < -constants.static.PLAYER_MAX_SPEED and angle > 0:
            y = -constants.static.PLAYER_MAX_SPEED  # up
        if y < 0 and self.rect.top <= constants.static.PLAYER_MAX_HEIGHT:
            y = 0
        if hypot < constants.static.PLAYER_CENTER_AREA:
            x = 0
            y = 0
        self.rect.centerx += x
        self.rect.centery += y

    def shoot(self, all, bullets):
        pass

    def update(self, control_args, sprite_group_args):
        """Perform all the actions necessary in one frame"""
        self.move()
        if "p1_shoot" in control_args:
            self.shoot(sprite_group_args[SpriteGroups.ALL.value],
                       sprite_group_args[SpriteGroups.BULLETS.value])
