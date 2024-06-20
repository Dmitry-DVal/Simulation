from Entities.entity import Entity


class Tree(Entity):
    '''Класс Дерево. Через него существа не могут ходить'''

    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.goal = None
        self.image = '🌲'
