import pygame
import random
import constant.static
from setup import *
import constant.dynamic
from mechanics.events import Events
from mechanics.collisions import Collisions
from util import Util
from collection import Collection
import math

collection = Collection()
collision_handler = Collisions()
event_handler = Events()
util = Util()


collection.add_player()
pygame.time.set_timer(event_handler.ENEMY_SHOOT, random.randrange(int(constant.static.ENEMY_SHOOT_BASE_TIME * (
    1 - constant.static.ENEMY_SHOOT_TIME_VARIANCE)), math.ceil(constant.static.ENEMY_SHOOT_BASE_TIME * (1 + constant.static.ENEMY_SHOOT_TIME_VARIANCE))), 1)

while running:
    screen.fill(constant.static.BACKGROUND)
    event_handler.normal(pygame.event.get())
    collision_handler.everything()
    collection.update()
    collection.draw(screen)
    pygame.display.flip()
    clock.tick(constant.static.FPS)
pygame.quit
