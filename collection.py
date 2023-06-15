from enums.sprite_group import SpriteGroup
from enums.player import Player
import data.constant
import data.var


class Collection():
    """Manage sprite groups"""

    def add_enemy(enemy):
        Collection.get_enemies().add(enemy)
        Collection.get_all().add(enemy)

    def add_player(player):
        Collection.get_players().add(player)
        Collection.get_all().add(player)

    def add_enemy_bullet(enemy_bullet):
        Collection.get_enemy_bullets().add(enemy_bullet)
        Collection.get_all().add(enemy_bullet)

    def add_player_bullet(player_bullet):
        Collection.get_player_bullets().add(player_bullet)
        Collection.get_all().add(player_bullet)

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
