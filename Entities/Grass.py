from Entities.entity import Entity

class Grass(Entity): # Трава
    "Класс Трава, может быть съеден травоядными"

    def __str__(self):
        return f'The object {self.name}'

    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.image = '🌿'
        self.name = 'Grass'
