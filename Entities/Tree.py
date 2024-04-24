from Entities.entity import Entity

class Tree(Entity): # Дерево
    "Класс Дерево. Статический объект"

    def __str__(self):
        return 'The object Tree'
    def __init__(self):
        self.image = '🌲'
    #     super().__init__(coordinate, name)




