from entity import Entity


class Mob(Entity):
    """A mob is a moving entity"""

    def __init__(self, *sprite_groups):
        super().__init__(*sprite_groups)

    def move(self):
        pass
