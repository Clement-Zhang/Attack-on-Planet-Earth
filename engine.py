import pygame
import random
import data.constant
from setup import *
import data.var
from mechanics.events import Events
from mechanics.collisions import Collisions
from util import Util
from collection import Collection
import math


Collection.add_player()
pygame.time.set_timer(data.var.enemy_shoot, random.randrange(int(data.constant.ENEMY_SHOOT_BASE_TIME * (
    1 - data.constant.ENEMY_SHOOT_TIME_VARIANCE)), math.ceil(data.constant.ENEMY_SHOOT_BASE_TIME * (1 + data.constant.ENEMY_SHOOT_TIME_VARIANCE))), 1)

while running:
    screen.fill(data.constant.BACKGROUND)
    Events.normal(pygame.event.get())
    Collisions.everything()
    Collection.update()
    Collection.draw(screen)
    pygame.display.flip()
    clock.tick(data.constant.FPS)
pygame.quit
