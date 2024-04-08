from Entities.Entity import Entity

class Grass(Entity): # Трава
    "Класс Трава, может быть съеден травоядными"

    def __str__(self):
        return 'The object Grass'
    def __init__(self, coordinate, name):
        image = '🌿'
        super().__init__(coordinate, name, image)
