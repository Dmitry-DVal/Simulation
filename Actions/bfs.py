from Entities import grass, herbivore, predator


class BFS:
    '''
    Класс поиска в ширину.
    '''

    def __init__(self, Simulation: 'Simulation'):
        self.Simulation = Simulation

    def get_neighbors(self, coordinates: tuple[int, int]) -> list:
        '''
        Функция, для создания списка соседних клеток, на которые может наступить существо.
        :return: Список клеток, на которые можно сходить
        '''
        x, y = coordinates[0], coordinates[1]
        all_picks = [(x - 1, y - 1), (x - 1, y), (x - 1, y + 1),
                     (x, y - 1), (x, y), (x, y + 1),
                     (x + 1, y - 1), (x + 1, y), (x + 1, y + 1)]
        possible_peaks = []
        for peak in all_picks:
            if self.is_in_range(peak) and self.is_it_free_cell(peak):
                possible_peaks.append((peak[0], peak[1]))
        return possible_peaks

    def is_in_range(self, peaks: tuple[int, int]) -> bool:
        '''Проверяет входят ли точки в границы карты.'''
        return (peaks[0], peaks[1]) in self.Simulation.Map.map

    def is_it_free_cell(self, peaks: tuple[int, int]) -> bool:
        """Проверяет свободная ли клетка."""
        cell = self.Simulation.Map.map[(peaks[0], peaks[1])]
        return cell is None or isinstance(cell, (grass.Grass, herbivore.Herbivore))

    def make_move(self, creature: 'Creature'):
        """Ищет близжайщий маршрут до существа,
        обновляет его позицию,
        передвигает в сторону цели в случае если существо не успело дойти,
        проверяет хищник это или травоядное,
        бьет существо если хищник"""
        first_peak = creature.coordinate  # Начальные координаты
        visited_peak = set()  # Посещенные вершины
        queue = [(first_peak, 0, [])]  # Очередь, должна хранить координаты, глубину поиска и путь
        counter = 0
        possible_final_coordinate = set()

        while queue:
            item = queue.pop(0)
            (x, y), level, path = item
            counter += 1
            visited_peak.add((x, y))

            for nx, ny in self.get_neighbors((x, y)):
                if (nx, ny) in visited_peak or (nx, ny) in [pos for pos, _, _ in
                                                            queue]:  # Проверка посещалась ли уже вершина, есть ли она в очереди
                    continue
                if level == creature.speed:  # Добавление в возможные финальные координаты для существа
                    if self.Simulation.Map.map[path[-1]] is None:  # проверка, что клетка пустая
                        possible_final_coordinate.add(path[-1])
                if isinstance(self.Simulation.Map.map[(nx, ny)], creature.goal):  # Что если цель достигнута?
                    if level + 1 <= creature.speed:  # 1ый вариант, существо успевает дойти до цели. Травоядное
                        return creature.make_move(creature, first_peak, (nx, ny), level, counter,
                                                    path, self.Simulation.Map.map, self.Simulation.living_creatures, self.Simulation.Config.herbivoreHp, self.Simulation.Config.predatorHp)  # self.Simulation.actions.update_position(creature, first_peak, (nx, ny), level, counter, path)
                    else:  # 2ой вариант, до цели еще далеко, существо не успевает дойти
                        return creature.move_closer_to_goal(possible_final_coordinate, nx, ny, path, first_peak, creature, self.Simulation.Map.map)
                else:
                    queue.append(((nx, ny), level + 1, path + [(nx, ny)]))
        print(f'Существо не видит цель и остается на месте {first_peak}')  # Отладочное сообщение
        return []