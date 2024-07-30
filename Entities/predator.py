from Entities.creature import Creature
from Entities.herbivore import Herbivore


class Predator(Creature):
    '''
    Класс хищников. Появляется сила атака. Задача поймать травоядного
    '''

    def __init__(self, coordinate: tuple[int, int], speed: int, hp: int, damage: int, image: str = '🐺'):
        super().__init__(coordinate, speed, hp, image, goal=Herbivore)
        self.__damage = damage

    @property
    def damage(self) -> int:
        return self.__damage

    @damage.setter
    def damage(self, value: int) -> None:
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value
    def __str__(self):
        return 'Волк'

    def make_move(self, creature: 'Creature', first_peak: tuple[int, int], finish_peak: tuple[int, int],
                  level: int, counter, path: list[tuple, int, list], my_map: dict, living_creatures: list,
                  herbivoreHp: int,
                  predatorHp: int) -> list[tuple, int, list]:
        """Существо перемещается до цели."""
        print(f'{creature} нашел Зайца, Глубина = {level + 1}')
        if creature.damage > my_map[finish_peak].hp:  # Урон больше чем здоровье зайца
            print(f'{creature} убивает Зайца и перемещается на {finish_peak}')
            living_creatures.remove(my_map[finish_peak])  # Удалить из списка живых существ
            my_map[first_peak], my_map[finish_peak] = None, creature
            creature.coordinate = finish_peak
            creature.hp = predatorHp
            return path + [finish_peak]
        else:
            print(f'Волк бьет Зайца, но Заяц слишком живучий')
            my_map[finish_peak].hp -= creature.damage
            if len(path) > 0:
                my_map[first_peak], my_map[path[-1]] = None, creature
                creature.coordinate = path[-1]
            return path
