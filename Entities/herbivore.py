from Entities.creature import Creature
from Entities.grass import Grass


class Herbivore(Creature):
    '''Класс травоядных. Задача найти траву'''

    def __init__(self, coordinate: tuple[int, int], speed: int, hp: int, image: str = '🐇'):
        super().__init__(coordinate, speed, hp, image, goal=Grass)

    def __str__(self):
        return 'Заяц'

    def make_move(self, creature: 'Creature', first_peak: tuple[int, int], finish_peak: tuple[int, int],
                  level: int, counter, path: list[tuple, int, list], my_map, living_creatures, herbivoreHp,
                  predatorHp) -> list[
        tuple, int, list]:
        """"""
        print(f'{creature} нашел Траву, Глубина = {level + 1}')
        print(f'{creature}, ваши конечные координаты {finish_peak}')
        creature.hp = herbivoreHp
        my_map[first_peak], my_map[finish_peak] = None, creature
        creature.coordinate = finish_peak
        return path + [finish_peak]
