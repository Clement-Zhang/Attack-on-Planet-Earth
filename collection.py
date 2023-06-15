import pygame
from enums.sprite_group import SpriteGroup
from enums.player import Player
from entity.mob.enemy import Enemy
from entity.mob.player1 import Player1
from projectile.regular_bullet import RegBullet
import data.constant
import data.var


class Collection():
    """Everything to do with managing CRU of sprites.
    Deletion is done by the sprites themselves to make things easier."""

    def add_enemy(spot):
        e = Enemy(spot)
        Collection.get_enemies().add(e)
        Collection.get_all().add(e)

    def add_player():
        p = Player1()
        Collection.get_players().add(p)
        Collection.get_all().add(p)

    def add_enemy_bullet(spot):
        b = RegBullet(data.constant.REGULAR_BULLET_SPEED, spot)
        Collection.get_enemy_bullets().add(b)
        Collection.get_all().add(b)

    def add_player_bullet(spot):
        b = RegBullet(-data.constant.REGULAR_BULLET_SPEED, spot)
        Collection.get_player_bullets().add(b)
        Collection.get_all().add(b)

    # read

    def get_all():
        return data.var.sprite_groups[SpriteGroup.ALL.value]

    def get_players():
        return data.var.sprite_groups[SpriteGroup.PLAYERS.value]

    def get_enemies():
        return data.var.sprite_groups[SpriteGroup.ENEMIES.value]

    def get_enemies_length():
        return len(Collection.get_enemies())

    def get_player_bullets():
        return data.var.sprite_groups[SpriteGroup.PLAYER_BULLETS.value]

    def get_enemy_bullets():
        return data.var.sprite_groups[SpriteGroup.ENEMY_BULLETS.value]

    def get_player1():
        return Collection.get_players().sprites()[Player.ONE.value]
    # update

    def update():
        Collection.get_all().update()

    def draw(screen):
        Collection.get_all().draw(screen)
