from Entities.entity import Entity

class Creature(Entity): # Существо. Класс для всех живых. Здоровье. Скорость.
    "Класс для живых существ"

    def __str__(self):
        return 'The object Creature'

    def __init__(self, coordinate, speed): # speed/ hp
        super().__init__(coordinate)
        self.speed = speed
        # self.hp = hp
    def make_move(self): #
        '''
        :return:
        '''
        pass
