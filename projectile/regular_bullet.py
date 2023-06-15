from projectile.projectile import Projectile
import os
import pygame
import constant.static
import constant.dynamic


class RegBullet(Projectile):
    """Projectile fired by the default gun"""

    def __init__(self, start_speed, start_location):
        super().__init__()
        bullet_folder = os.path.join(
            constant.dynamic.PROJECTILE_FOLDER, "regular bullet")
        if start_speed > 0:
            img = pygame.image.load(os.path.join(
                bullet_folder, "bullet down.png")).convert()
        elif start_speed < 0:
            img = pygame.image.load(os.path.join(
                bullet_folder, "bullet up.png")).convert()
        self.image = pygame.transform.scale(
            img, constant.static.REGULAR_BULLET_SIZE)
        self.rect = self.image.get_rect()
        self.speed = start_speed
        self.rect.center = start_location

    def animate(self):
        """Move the bullet at a constant speed"""
        self.rect.centery += self.speed

    def despawn(self):
        """Despawn the bullet if it's in a useless location"""
        if self.rect.bottom < constant.static.ENEMY_SPAWN_Y_MAX or self.rect.top > constant.static.HEIGHT:
            self.kill()

    def update(self):
        """Perform all the actions necessary in one frame"""
        self.despawn()
        self.animate()
