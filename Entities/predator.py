from Entities.creature import Creature
from Entities.herbivore import Herbivore


class Predator(Creature):
    '''
    Класс хищников. Появляется сила атака. Задача поймать травоядного
    '''

    def __init__(self, coordinate: tuple, speed: int, hp: int, damage: int, image: str = '🐺'):
        super().__init__(coordinate, speed, hp, image, goal=Herbivore)
        self.damage = damage
        # self.goal = Herbivore

    def __str__(self):
        return 'Волк'

    def test_move(self):
        pass
