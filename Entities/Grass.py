from Entities.entity import Entity

class Grass(Entity): # Трава
    "Класс Трава, может быть съеден травоядными"

    def __str__(self):
        return 'The object Grass'

    def __init__(self):
        # super().__init__(coordinate, name)
        self.image = '🌿'
