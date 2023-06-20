import pygame


class Projectile(pygame.sprite.Sprite):
    """A projectile, in an abstract sense, is an entity spawned by either a player or an enemy,
    whose goal is to affect the other in some way.
    In a more concrete sense, it is what comes out of the business end of a weapon."""

    def __init__(self):
        super().__init__()

    def animate(self):
        """This method is called animate instead of move because while projectiles will definitely look cool,
        they do not necessary look cool by moving."""
        pass
