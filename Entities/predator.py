from Entities.creature import Creature
from Entities.herbivore import Herbivore

class Predator(Creature):
    '''
    Класс хищников. Появляется сила атака. Задача поймать травоядного
    '''

    def __init__(self, coordinate, speed, hp, damage):
        super().__init__(coordinate, speed, hp)
        self.damage = damage
        self.goal = Herbivore
        self.image = '🐺'
