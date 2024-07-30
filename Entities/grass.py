from Entities.entity import Entity


class Grass(Entity):
    '''
    Класс Трава. Может быть съедена травоядным, это восполнит здоровье существа
    '''

    def __init__(self, coordinate: tuple[int, int], image: str = '🌿'):
        super().__init__(coordinate, image)

    def __str__(self):
        return 'Травка'
