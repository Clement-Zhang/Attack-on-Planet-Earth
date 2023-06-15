import pygame
import random
import constant.static
from collection import Collection


class Events():
    """Different events are important in different situations"""
    # singleton because don't call custom type more than once per custom event
    instance = None

    def __new__(cls):
        if not Events.instance:
            Events.instance = Events.__Events()
        return Events.instance

    class __Events():

        def __init__(self):
            self.ENEMY_SHOOT = pygame.event.custom_type()
            self.collection = Collection()

        def normal(self, event_queue):
            for event in event_queue:
                if event.type == pygame.QUIT:
                    quit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.collection.get_player1().shoot(self.collection)
                elif event.type == self.ENEMY_SHOOT:
                    if len(self.collection.get_enemies()) > 0:
                        random.choice(self.collection.get_enemies().sprites()).shoot(
                            self.collection)
                    pygame.time.set_timer(self.ENEMY_SHOOT, random.randrange(constant.static.ENEMY_SHOOT_BASE_TIME * (
                        1 - constant.static.ENEMY_SHOOT_TIME_VARIANCE), constant.static.ENEMY_SHOOT_BASE_TIME * (1 + constant.static.ENEMY_SHOOT_TIME_VARIANCE)), 1)

        def alternating(self, event_queue):
            for event in event_queue:
                if event.type == pygame.QUIT:
                    quit()
