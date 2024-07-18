from Entities.entity import Entity


class Grass(Entity):
    '''
    Класс Трава. Может быть съедена травоядным, это восполнит здоровье существа
    '''

    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.goal = None
        self.image = '🌿'

    def __str__(self):
        return 'Травка'