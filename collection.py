import pygame
from enums.sprite_group import SpriteGroup
from enums.player import Player
from entity.mob.enemy import Enemy
from entity.mob.player1 import Player1
from projectile.regular_bullet import RegBullet
import constant.static


class Collection():
    """Everything to do with managing CRU of sprites.
    Deletion is done by the sprites themselves to make things easier."""
    # singleton
    instance = None
    def __new__(cls):
        if not Collection.instance:
            Collection.instance = Collection.__Collection()
        return Collection.instance

    class __Collection():
        # create
        def __init__(self):
            self.sprite_groups = [pygame.sprite.Group()
                                  for _ in range(len(SpriteGroup))]

        def add_enemy(self, spot):
            e = Enemy(spot)
            self.get_enemies().add(e)
            self.get_all().add(e)

        def add_player(self):
            p = Player1()
            self.get_players().add(p)
            self.get_all().add(p)

        def add_enemy_bullet(self, spot):
            b = RegBullet(constant.static.REGULAR_BULLET_SPEED, spot)
            self.get_enemy_bullets().add(b)
            self.get_all().add(b)

        def add_player_bullet(self, spot):
            b = RegBullet(-constant.static.REGULAR_BULLET_SPEED, spot)
            self.get_player_bullets().add(b)
            self.get_all().add(b)

        # read

        def get_collections(self):
            return self.sprite_groups

        def get_all(self):
            return self.sprite_groups[SpriteGroup.ALL.value]

        def get_players(self):
            return self.sprite_groups[SpriteGroup.PLAYERS.value]

        def get_enemies(self):
            return self.sprite_groups[SpriteGroup.ENEMIES.value]

        def get_enemies_length(self):
            return len(self.get_enemies())

        def get_player_bullets(self):
            return self.sprite_groups[SpriteGroup.PLAYER_BULLETS.value]

        def get_enemy_bullets(self):
            return self.sprite_groups[SpriteGroup.ENEMY_BULLETS.value]

        def get_player1(self):
            return self.get_players().sprites()[Player.ONE.value]
        # update

        def update(self):
            self.get_all().update()

        def draw(self, screen):
            self.get_all().draw(screen)
