from entity import Entity


class Mob(Entity):
    """A mob is a moving entity"""
    def __init__(self):
        super().__init__()

    def move(self):
        pass
