from Entities.entity import Entity
from abc import ABC, abstractmethod


class Creature(Entity, ABC):
    '''
    Класс для живых существ. У них появляется здоровье и скорость передвижения.
    '''

    def __init__(self, coordinate: tuple[int, int], speed: int, hp: int, image: str, goal=None):
        super().__init__(coordinate, image)
        self.speed = speed
        self.goal = goal
        self.__hp = hp

    @property
    def hp(self) -> int:
        return self.__hp

    @hp.setter
    def hp(self, value: int) -> None:
        if value < 0:
            self.__hp = 0
        else:
            self.__hp = value

    def __str__(self):
        pass

    @abstractmethod
    def make_move(self):
        pass

    def move_closer_to_goal(self, possible_final_coordinate: tuple, nx: int, ny: int, path: list[tuple, int, list],
                            first_peak: tuple[int, int],
                            creature, my_map: dict) -> list[tuple, int, list]:  # 2-й вариант, до цели еще далеко, существо не успевает дойти
        """Существо не успевает дойти до цели, оно перемещается по направлении к цели."""
        print(f'{(nx, ny)} - Конечные координаты цели, {creature} не успевает дойти.')
        # Поиск ближайшей точки
        min_abs = float('inf')
        closest_point = None
        for i in possible_final_coordinate:
            distance = abs((i[0] - nx) ** 2 + (i[1] - ny) ** 2)
            if distance < min_abs:
                min_abs = distance
                closest_point = i
        if closest_point:
            my_map[first_peak], my_map[closest_point] = None, creature
            creature.coordinate = closest_point
            print(f'{creature} перемещается на {closest_point}')
            return path + [closest_point]
        else:
            return path

