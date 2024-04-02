from Entities.Entity import Entity

class Creature(Entity): # Существо. Класс для всех живых. Здоровье. Скорость.
    "Класс для живых существ"
    def __init__(self, speed, hp):
        self.speed = speed
        self.hp = hp
    def make_move(self): #
        '''
        :return:
        '''
        pass
