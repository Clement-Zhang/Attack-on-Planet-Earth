import pygame
import random
import data.var
import data.constant
from collection import Collection


class Events():
    """Different events are important in different situations"""

    def normal(event_queue):
        for event in event_queue:
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Collection.add_player_bullet(Collection.get_player1().shoot())
            elif event.type == data.var.enemy_shoot:
                if len(Collection.get_enemies()) > 0:
                    Collection.add_enemy_bullet(random.choice(
                        Collection.get_enemies().sprites()).shoot())
                pygame.time.set_timer(data.var.enemy_shoot, random.randrange(data.constant.ENEMY_SHOOT_BASE_TIME * (
                    1 - data.constant.ENEMY_SHOOT_TIME_VARIANCE), data.constant.ENEMY_SHOOT_BASE_TIME * (1 + data.constant.ENEMY_SHOOT_TIME_VARIANCE)), 1)

    def alternating(event_queue):
        for event in event_queue:
            if event.type == pygame.QUIT:
                quit()
