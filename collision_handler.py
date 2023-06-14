import pygame
from sprite_groups import SpriteGroups


class CollisionHandler():
    """Different ways entities can interact with each other"""

    def __init__(self, *sprite_groups):
        self.sprite_groups = sprite_groups

    def player_shoot_enemy(self):
        pygame.sprite.groupcollide(
            self.sprite_groups[SpriteGroups.ENEMIES.value], self.sprite_groups[SpriteGroups.PLAYER_BULLETS.value], True, True)

    def enemy_shoot_player(self):
        pygame.sprite.groupcollide(
            self.sprite_groups[SpriteGroups.PLAYERS.value], self.sprite_groups[SpriteGroups.ENEMY_BULLETS.value], True, True)
