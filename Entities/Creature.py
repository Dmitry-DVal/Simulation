from .Entity import Entity

class Creature(Entity): # Существо. Класс для всех живых. Здоровье. Скорость.

    def __init__(self, speed, hp):
        self.speed = speed
        self.hp = hp
    def make_move(self): #
        '''
        :return:
        '''
        pass
