from Entities.entity import Entity
from abc import ABC, abstractmethod


class Creature(Entity, ABC):
    '''
    Класс для живых существ. У них появляется здоровье и скорость передвижения.
    '''

    def __init__(self, coordinate: tuple, speed: int, hp: int, image: str, goal=None):
        super().__init__(coordinate, image)
        self.speed = speed
        self.hp = hp
        self.goal = goal

    def __str__(self):
        pass

    @abstractmethod
    def test_move(self):
        pass
