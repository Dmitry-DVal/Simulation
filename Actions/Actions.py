class Actions(): # действие, совершаемое над миром
    "Класс управляющий действиями, соверщенными над миром."

    firsy_peak = (3, 6)  # Первая вершина от которой ищем
    visited_peak = set()  # Посещенные вершины
    queue = [(firsy_peak, 0)]  # Очередь, должна хранить координаты и глубину поиска
    counter = 0
    my_map = {(0, 0): None, (0, 1): None, (0, 2): '🐺', (0, 3): None, (0, 4): None, (0, 5): None, (0, 6): '🐺',
              (0, 7): None,
              (1, 0): None, (1, 1): '🌿', (1, 2): None, (1, 3): None, (1, 4): None, (1, 5): None, (1, 6): None,
              (1, 7): None,
              (2, 0): None, (2, 1): None, (2, 2): None, (2, 3): '🪨', (2, 4): '🐇', (2, 5): '🌲', (2, 6): None,
              (2, 7): None,
              (3, 0): None, (3, 1): None, (3, 2): None, (3, 3): None, (3, 4): None, (3, 5): None, (3, 6): '🐇',
              (3, 7): None,
              (4, 0): None, (4, 1): '🪨', (4, 2): None, (4, 3): None, (4, 4): '🐺', (4, 5): None, (4, 6): None,
              (4, 7): '🌲'
              }

    def __str__(self):
        return 'The object Actions'

    @staticmethod
    def get_neighbors(x, y):
        return [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                (x, y - 1), (x, y), (x, y + 1),
                (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]


    def add_queue(self, queue, x, y, counter):  # добавить в очередь
        """
        Функция добавления в очередь возможные варианты
        :param queue: текущая очередь
        :param x: координата x
        :param y: координата y
        :return: обновленная очередь
        """
        while queue:
            (x, y), level = queue.pop(0)
            counter += 1
            self.visited_peak.add((x, y))
            print(f'Ход номер ={counter}, Глубина = {level}')
            for nx, ny in self.get_neighbors(x, y):
                if (nx, ny) not in self.my_map:
                    # print('нет диапозона', (nx, ny))
                    continue
                if (nx, ny) in self.visited_peak:
                    # print('Вершина уже посещалась', (nx, ny))
                    continue
                if (nx, ny) in queue:
                    # print('уже есть в очереди', (nx, ny))
                    continue
                if self.my_map[(nx, ny)] == '🌿':
                    print(f'Вы выиграли, вы нашли траву, количество ходов = {counter}, Глубина = {level + 1}')
                    self.my_map[self.firsy_peak], self.my_map[(nx, ny)] = None, self.my_map[self.firsy_peak]
                    return
                elif self.my_map[(nx, ny)] in ['🐺', '🪨', '🐇', '🌲']:
                    # print(f'{(nx, ny)} сюда не иди, тут поле занято')
                    self.visited_peak.add((nx, ny))
                    continue
                else:
                    # print(f'поле {(nx, ny)} сводно, добавим его в очередь')
                    queue.append(((nx, ny), level + 1))
        print('Текущая очередь', queue)
        print('Посещенные верщины', self.visited_peak)



my_map = {(0, 0): None, (0, 1): None, (0, 2): '🐺', (0, 3): None, (0, 4): None, (0, 5): None, (0, 6): '🐺', (0, 7): None,
          (1, 0): None, (1, 1): '🌿', (1, 2): None, (1, 3): None, (1, 4): None, (1, 5): None, (1, 6): None, (1, 7): None,
          (2, 0): None, (2, 1): None, (2, 2): None, (2, 3): '🪨', (2, 4): '🐇', (2, 5): '🌲', (2, 6): None, (2, 7): None,
          (3, 0): None, (3, 1): None, (3, 2): None, (3, 3): None, (3, 4): None, (3, 5): None, (3, 6): '🐇', (3, 7): None,
          (4, 0): None, (4, 1): '🪨', (4, 2): None, (4, 3): None, (4, 4): '🐺', (4, 5): None, (4, 6): None, (4, 7): '🌲'
          }


# Функция вывода начального поля
def show_map(my_map):
    "Функция рисует в консоли карту"
    for y in range(5):
        for x in range(8):
            if my_map[(y, x)] is None:
                print("..", end="  ")  # Пустая клетка
            else:
                print(my_map[(y, x)], end="  ")  # Клетка изображением сущности
        print()  # Переход на новую строку


a = Actions()
show_map(a.my_map)
a.add_queue(a.queue, 3, 6, a.counter) # Проверка что поля нет в очереди
show_map(a.my_map)