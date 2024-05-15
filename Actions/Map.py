from Entities.entity import Entity

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
                elif isinstance(self.map[(x, y)], Entity):
                    print(self.map[(x, y)].image, end="  ")  # Клетка изображением сущности
            print()  # Переход на новую строку

