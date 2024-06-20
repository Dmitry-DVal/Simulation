
class BFS():
    '''
    Класс для поиска в глубину
    '''
    def __init__(self, Simulation):
        self.Simulation = Simulation


    def get_neighbors(self, x, y):
        '''
        Функция, для сосздания списка соседних клеток, на которые может наступить существо.
        СЕЙЧАС ТУТ НЕ ПРОВЕРЯЕТСЯ Заняты ли клетки
        :return: Список клеток, на которые можно сходить
        '''
        all_picks = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                (x, y - 1), (x, y), (x, y + 1),
                (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        possible_peaks = []
        for peak in all_picks:
            if (peak[0], peak[1]) not in self.Simulation.Map.map: # Проверки, находится ли клетка в пределах карты.
                # print("Вершина в границах карты, проверим, что она свободна")
                continue
            if self.Simulation.Map.map[(peak[0], peak[1])] is None: # Проверка, что клетка свободна
                # print("Вершина не занята объектом, добавим ее в очередь")
                possible_peaks.append((peak[0], peak[1]))
        return possible_peaks
