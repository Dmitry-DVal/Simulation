from Entities.creature import Creature
from Entities.grass import Grass

class Herbivore(Creature):
    '''Класс травоядных. Задача найти траву'''

    def __init__(self, coordinate, speed, hp):
        super().__init__(coordinate, speed, hp)
        self.goal = Grass
        self.image = '🐇'

    def __str__(self):
        return 'Заяц'