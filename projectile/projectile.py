from entity.entity import Entity


class Projectile(Entity):
    """A projectile, in an abstract sense, is an entity spawned by either a player or an enemy,
    whose goal is to affect the other in some way.
    In a more concrete sense, it is what comes out of the business end of a weapon."""

    def animate(self):
        """This method is called animate instead of move because while projectiles will definitely look cool,
        they do not necessary look cool by moving."""
        pass
