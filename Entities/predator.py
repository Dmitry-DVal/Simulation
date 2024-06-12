from Entities.creature import Creature

class Predator(Creature):
    '''
    Класс хищников. Появляется сила атака. Задача поймать травоядного
    '''

    def __init__(self, coordinate, speed, hp, damage):
        super().__init__(coordinate, speed, hp)
        self.damage = damage
        self.image = '🐺'
