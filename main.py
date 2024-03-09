# https://zhukovsd.github.io/python-backend-learning-course/Projects/Simulation/#herbivore

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


# Map = [[None for _ in range(width)] for _ in range(height)] # Сначало думал о списке в списке, самый простой вариант. Но в ТЗ совет его не использовать.


width = 15 # Y
height = 5 # X

Map = {(x, y): None for x in range(width) for y in range(height)}

Map[(0, 4)] = 'Заяц'
Map[(8, 3)] = 'Волк'


# Рисуем поле. Добавить потом проверку на сущность 
for y in range(height):
    for x in range(width):
        if Map[(x, y)] is None:
            print(".", end=" ")  # Пустая клетка
        else:
            print("X", end=" ")  # Клетка с объектом
    print()  # Переход на новую строку


width = 15  # x
height = 5  # y

map_data = {(x, y): None for x in range(width) for y in range(height)}

map_data[(0, 5)] = 55
