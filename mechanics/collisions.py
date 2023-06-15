import pygame
from collection import Collection
from util import Util
from mechanics.events import Events


class Collisions():
    """Different ways entities can interact with each other"""

    def __init__(self):
        self.collection = Collection()
        self.util = Util()
        self.events = Events()

    def player_shoot_enemy(self):
        pygame.sprite.groupcollide(
            self.collection.get_enemies(), self.collection.get_player_bullets(), True, True)
        if len(self.collection.get_enemies()) == 0:
            self.util.new_wave()

    def enemy_shoot_player(self):
        if pygame.sprite.groupcollide(
                self.collection.get_players(), self.collection.get_enemy_bullets(), True, True):
            self.util.flash()
        if len(self.collection.get_players()) == 0:
            pygame.event.post(pygame.event.Event(pygame.QUIT))

    def everything(self):
        self.player_shoot_enemy()
        self.enemy_shoot_player()
