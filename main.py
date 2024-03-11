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

    def __init__(self, speed, hp):
        self.speed = speed
        self.hp = hp
    def make_move(self): #
        '''
        :return:
        '''
        pass

class Herbivore(Creature): # Травоядное. Задача найти траву.
    pass

class Predador(Creature): # Хищник. Должен иметь силу атаки. Задача сожрать травоядного.
    pass



class Simulation(): #  Главный класс. Включает Счётчик ходов Рендерер поля Action
    pass

class Actions(): # действие, совершаемое над миром
    pass

Map = {(x, y): None for x in range(width) for y in range(height)}  # Создание пустой карты.
# Скорее всего я сделаю Map, где ключ будет коллецией ( координаты х, у), а значение - экземпляр класса Entity(), либо None

class Simulation(): #  Главный класс. Включает Счётчик ходов Рендерер поля Action
    def __init__(self, Map):
        self.Map = Map # получение начальной карты
        self.count_move = 0 # счетчик ходов

    def show_map(self):
        # покажет карту со всеми существами
        pass

    def field_renderer(self): # рендер поля
        pass

    def next_turn(self): # просимулировать один ход
        pass

    def start_simulation(self): # запустить бесконечный цикл симуляции и рендеринга
        pass

    def pause_simulation(self): # приостановить бесконечный цикл симуляции и рендеринга
        pass