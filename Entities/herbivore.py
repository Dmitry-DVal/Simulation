from Entities.creature import Creature
from Entities.grass import Grass


class Herbivore(Creature):
    '''Класс травоядных. Задача найти траву'''

    def __init__(self, coordinate: tuple, speed: int, hp: int, image: str = '🐇'):
        super().__init__(coordinate, speed, hp, image, goal=Grass)

    def __str__(self):
        return 'Заяц'

    def test_move(self):
        pass
