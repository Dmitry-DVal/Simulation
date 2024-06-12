from Entities.creature import Creature

class Herbivore(Creature):
    '''Класс травоядных. Задача найти траву'''

    def __init__(self, coordinate, speed, hp):
        super().__init__(coordinate, speed, hp)
        self.image = '🐇'

