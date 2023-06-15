import pygame
from collection import Collection
from util import Util


class Collisions():
    """Different ways entities can interact with each other"""

    def player_shoot_enemy():
        pygame.sprite.groupcollide(
            Collection.get_enemies(), Collection.get_player_bullets(), True, True)
        if len(Collection.get_enemies()) == 0:
            Util.new_wave()

    def enemy_shoot_player():
        if pygame.sprite.groupcollide(
                Collection.get_players(), Collection.get_enemy_bullets(), True, True):
            Util.flash()
        if len(Collection.get_players()) == 0:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def everything():
        Collisions.player_shoot_enemy()
        Collisions.enemy_shoot_player()
