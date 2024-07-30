from Entities.entity import Entity


class Tree(Entity):
    '''Класс Дерево. Через него существа не могут ходить'''

    def __init__(self, coordinate: tuple[int, int], image: str = '🌲'):
        super().__init__(coordinate, image)

    def __str__(self):
        return 'Дерево'
