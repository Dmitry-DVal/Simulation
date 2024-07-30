from Actions.actions import Actions
from Actions.bfs import BFS
from Entities.entity import Entity


class Simulation:
    """Должен включать в себя карту, счетчик ходов, рендер поля, actions"""

    def __init__(self, Config: 'Config', Map: 'Map') -> None:
        """Инициализирует игру, создает игровые ресурсы"""
        self.Config = Config() # Почему с большой буквы?
        self.Map = Map # Почему с большой буквы?
        self.actions = Actions(self)
        self.bfs = BFS(self)
        self.living_creatures = []
        self.day_counter = 1

    def show_map(self) -> None:
        "Выводит в консоль изображение карты."
        for y in range(self.Config.height):
            for x in range(self.Config.width):
                if self.Map.map[(x, y)] is None:
                    print("..", end="  ")  # Пустая клетка
                elif isinstance(self.Map.map[(x, y)], Entity):
                    print(self.Map.map[(x, y)].image, end="  ")
            print()  # Переход на новую строку