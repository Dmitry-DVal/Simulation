# https://zhukovsd.github.io/python-backend-learning-course/Projects/Simulation/#herbivore

from config import *
class Entity(): # Сущность. Класс для всех существ и объектов
    pass

class Grass(Entity): # Трава
    pass

class Rock(Entity): # Камень
    pass

class Tree(Entity): # Дерево
    pass

class Creature(Entity): # Существо. Класс для всех живых. Здоровье. Скорость.
    pass

class Herbivore(Creature): # Травоядное. Задача найти траву.
    pass

class Predador(Creature): # Хищник. Должен иметь силу атаки. Задача сожрать травоядного.
    pass



class Simulation(): #  Главный класс. Включает Счётчик ходов Рендерер поля Action
    pass

class Actions(): # действие, совершаемое над миром
    pass

Map = {(x, y): None for x in range(width) for y in range(height)}  # Создание пустой карты  


