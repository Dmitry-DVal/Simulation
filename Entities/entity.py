from abc import ABC, abstractmethod


class Entity(ABC):
    '''
    Класс для всех существ и объект, существующих в симуляции, все объекты получают координаты расположения на карте.
    '''

    def __init__(self, coordinate: tuple, image: str):
        self.coordinate = coordinate
        self.image = image

    @abstractmethod
    def __str__(self):
        pass
