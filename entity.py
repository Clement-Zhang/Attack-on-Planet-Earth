import pygame


class Entity(pygame.sprite.Sprite):
    """Everything on the screen is an entity"""
    def __init__(self):
        super().__init__()

    def update(self, control_args, sprite_group_args):
        pass
