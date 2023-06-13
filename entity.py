import pygame


class Entity(pygame.sprite.Sprite):
    """Everything on the screen is an entity"""

    def __init__(self, *sprite_groups):
        super().__init__()
        # entities are associated with certain groups
        for sprite_group in sprite_groups:
            sprite_group.add(self)

    def update(self, control_args, sprite_group_args):
        pass
