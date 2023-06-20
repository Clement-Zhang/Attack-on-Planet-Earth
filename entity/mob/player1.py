import pygame
import math
from entity.mob.mob import Mob
import data.constant
import data.var
import os
from entity.projectile.regular_bullet import RegBullet
from collection import Collection


class Player1(Mob):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(os.path.join(
            data.var.player_folder, "fly straight.png")).convert(), data.constant.PLAYER_ENEMY_SIZE)
        self.rect = self.image.get_rect()
        self.rect.center = (data.constant.WIDTH / 2,
                            data.constant.HEIGHT - self.rect.height)

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
            dist_x = data.constant.SMALL_NONZERO_VALUE
        hypot = math.hypot(dist_x, dist_y)
        angle = math.atan2(dist_y, dist_x)
        x = math.cos(angle) * (hypot * data.constant.SPEED_SENSITIVITY)
        y = -math.sin(angle) * (hypot * data.constant.SPEED_SENSITIVITY)
        if x > data.constant.PLAYER_MAX_SPEED and angle < (.5 * pi) and angle > (-.5 * pi):
            x = data.constant.PLAYER_MAX_SPEED  # right
        if x < -data.constant.PLAYER_MAX_SPEED and angle < (-.5 * pi) or angle > (.5 * pi):
            x = -data.constant.PLAYER_MAX_SPEED  # left
        if y > data.constant.PLAYER_MAX_SPEED and angle < 0:
            y = data.constant.PLAYER_MAX_SPEED  # down
        if y < -data.constant.PLAYER_MAX_SPEED and angle > 0:
            y = -data.constant.PLAYER_MAX_SPEED  # up
        if y < 0 and self.rect.top <= data.var.player_max_height:
            y = 0
        if hypot < data.constant.PLAYER_CENTER_AREA:
            x = 0
            y = 0
        self.rect.centerx += x
        self.rect.centery += y

    def shoot(self):
        """Spawn a bullet for event handler to pass to collection"""
        Collection.add_player_bullet(RegBullet(-data.constant.REGULAR_BULLET_SPEED, (self.rect.centerx,
                                                                                     self.rect.top - data.constant.REGULAR_BULLET_SIZE[1] / 2)))

    def update(self):
        """Perform all the actions necessary in one frame"""
        self.move()
