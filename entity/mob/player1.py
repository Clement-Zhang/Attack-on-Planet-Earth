import pygame
import math
from entity.mob.mob import Mob
import constant.dynamic
import constant.static
import os


class Player1(Mob):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            constant.dynamic.PLAYER_FOLDER, "fly straight.png")).convert(), constant.static.PLAYER_ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (constant.static.WIDTH / 2,
                            constant.static.HEIGHT - self.rect.height)

    def move(self):
        """Move the player towards the mouse, agario style.
        Max speed is PLAYER_MAX_SPEED, the player moves proportionate to the distance from the mouse,
        and the player cannot move more than PLAYER_GAMEPLAY_AREA pixels from the bottom of the screen."""
        start = self.rect.center
        end = pygame.mouse.get_pos()
        dist_x = end[0] - start[0]
        # due to angle calculations this calculation must be negated
        dist_y = -(end[1] - start[1])
        pi = math.pi
        if dist_x == 0:
            dist_x = constant.static.SMALL_NONZERO_VALUE
        hypot = math.hypot(dist_x, dist_y)
        angle = math.atan2(dist_y, dist_x)
        x = math.cos(angle) * (hypot * constant.static.SPEED_SENSITIVITY)
        y = -math.sin(angle) * (hypot * constant.static.SPEED_SENSITIVITY)
        if x > constant.static.PLAYER_MAX_SPEED and angle < (.5 * pi) and angle > (-.5 * pi):
            x = constant.static.PLAYER_MAX_SPEED  # right
        if x < -constant.static.PLAYER_MAX_SPEED and angle < (-.5 * pi) or angle > (.5 * pi):
            x = -constant.static.PLAYER_MAX_SPEED  # left
        if y > constant.static.PLAYER_MAX_SPEED and angle < 0:
            y = constant.static.PLAYER_MAX_SPEED  # down
        if y < -constant.static.PLAYER_MAX_SPEED and angle > 0:
            y = -constant.static.PLAYER_MAX_SPEED  # up
        if y < 0 and self.rect.top <= constant.static.PLAYER_MAX_HEIGHT:
            y = 0
        if hypot < constant.static.PLAYER_CENTER_AREA:
            x = 0
            y = 0
        self.rect.centerx += x
        self.rect.centery += y

    def shoot(self,collection):
        collection.add_player_bullet(
            (self.rect.centerx, self.rect.top - constant.static.REGULAR_BULLET_SIZE[1] / 2))

    def update(self):
        """Perform all the actions necessary in one frame"""
        self.move()
