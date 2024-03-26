from Entities.Entity import Entity

class Tree(Entity): # Дерево

    def __init__(self,  coordinate, name):
        image = '🌲'
        super().__init__(coordinate, name, image)



