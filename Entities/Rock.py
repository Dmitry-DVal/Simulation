from Entities.Entity import Entity


class Rock(Entity): # Камень
    def __init__(self,  coordinate, name ):
        image = '🪨'
        super().__init__(coordinate, name, image)

