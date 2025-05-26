from entity.projectile.projectile import Projectile
import os
import pygame
import data.constant
import data.var


class RegBullet(Projectile):
    """Projectile fired by the default gun"""

    def __init__(self, start_speed, start_location):
        super().__init__()
        if start_speed < 0:
            self.image = data.var.bullet_up
        else:
            self.image = data.var.bullet_down
        self.rect = self.image.get_rect()
        self.speed = start_speed
        self.rect.center = start_location

    def animate(self):
        """Move the bullet at a constant speed"""
        self.rect.centery += self.speed

    def despawn(self):
        """Despawn the bullet if it's in a useless location"""
        if self.rect.bottom < data.var.enemy_spawn_y_max or self.rect.top > data.constant.HEIGHT:
            self.kill()

    def update(self):
        """Perform all the actions necessary in one frame"""
        self.despawn()
        self.animate()
