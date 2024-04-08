from Entities.Entity import Entity


class Rock(Entity): # Камень
    "Класс Камень. Статический объект"

    def __str__(self):
        return 'The object Rock'

    def __init__(self,  coordinate, name ):
        image = '🪨'
        super().__init__(coordinate, name, image)

