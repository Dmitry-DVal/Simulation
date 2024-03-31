from Entities.Entity import Entity

class Tree(Entity): # Дерево
    "Класс Дерево. Статический объект"
    def __init__(self,  coordinate, name):
        image = '🌲'
        super().__init__(coordinate, name, image)



