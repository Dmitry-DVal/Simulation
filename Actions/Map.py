from config import height, width
from Entities.Entity import Entity
from Entities.Grass import Grass
from Entities.Rock import Rock

# Скорее всего я сделаю Map, где ключ будет коллецией ( координаты х, у), а значение - экземпляр класса Entity(), либо None
class Map:
    "Класс карты симуляции"

    def __str__(self):
        return 'The object Map'
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map = {(x, y): None for x in range(self.width) for y in range(self.height)} # Создание пустой карты.

    def show_map(self):
        "Функция рисует в консоли карту"
        for y in range(self.height):
            for x in range(self.width):
                if self.map[(x, y)] is None:
                    print("..", end="  ")  # Пустая клетка
                ### !!! Код ниже везде повторяется. Можно в классе сущности просивоить кажому свое изображение и выводить его
                elif isinstance(self.map[(x, y)], Entity):
                    print(self.map[(x, y)].image, end="  ")  # Клетка с травой
            print()  # Переход на новую строку

# m = Map(height, width)
# m.show_map()
# print(len(m.map))
# print(m.map)
# print()
#
# m.map[1,2] = Grass([1,2], 'mamr')
# m.map[2,3] = Rock([1,2], 'mamr')
#
# m.show_map()
# print(m.map)

