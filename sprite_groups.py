from enum import Enum


class SpriteGroups(Enum):
    """Used to index into sprite_group_args"""
    ALL = 0
    PLAYERS = 1
    ENEMIES = 2
    BULLETS = 3
