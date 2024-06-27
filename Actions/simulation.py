from Actions.actions import Actions
from Actions.bfs import BFS
from Entities.entity import Entity

class Simulation:
    def __init__(self, Config, Map):
        self.Config = Config
        self.Map = Map.map
        self.Map = Map
        self.living_creatures = []  # перечисление всех живых существ
        self.actions = Actions(self)
        self.bfs = BFS(self)

    def show_map(self):
        "Рендер поля"
        for y in range(self.Config.height):
            for x in range(self.Config.width):
                if self.Map.map[(x, y)] is None:
                    print("..", end="  ")  # Пустая клетка
                elif isinstance(self.Map.map[(x, y)], Entity):
                    print(self.Map.map[(x, y)].image, end="  ")  # Клетка с изображением сущности
            print()  # Переход на новую строку
