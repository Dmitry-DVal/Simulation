from Entities import grass, herbivore

# Текущие проблемы
# Существа не перемещаются - решено
# Существо не исчезает когда его сожрали
# Существо не движется в сторону цели, если оно не успевает дойти - решено
# Хищник не наносит урон, а сразу жрет существо
# Сделать возможность ходить перыми зайцам - сделано

class BFS:
    '''
    Класс для поиска в ширину
    '''
    def __init__(self, Simulation):
        self.Simulation = Simulation


    def get_neighbors(self, coordinates):
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
            if (peak[0], peak[1]) not in self.Simulation.Map.map: # Проверки, находится ли клетка в пределах карты.
                continue
            if self.Simulation.Map.map[(peak[0], peak[1])] is None or isinstance(self.Simulation.Map.map[peak], (
                grass.Grass, herbivore.Herbivore)): # Проверка, что клетка свободна
                possible_peaks.append((peak[0], peak[1]))
        return possible_peaks


    def make_move(self, creature):
        first_peak = creature.coordinate # Начальные координаты
        goal = creature.goal # На самом деле можно и не делать отдельную переменную
        visited_peak = set()  # Посещенные вершины
        queue = [(first_peak, 0, [])]  # Очередь, должна хранить координаты, глубину поиска и путь
        counter = 0
        possible_final_coordinate = set()


        while queue:
            item = queue.pop(0)
            (x, y), level, path = item
            counter += 1
            visited_peak.add((x, y))

            for nx, ny in self.get_neighbors((x, y)): # Ошибка была такая self.get_neighbors(creature.coordinate)
                if (nx, ny) in visited_peak: # Проверка посещалась ли уже вершина
                    continue
                if (nx, ny) in [pos for pos, _, _ in queue]:  # Проверка, есть уже данная вершина в очереди
                    continue
                if level == creature.speed: # Добавление в возможные финальные координаты для существа
                    if self.Simulation.Map.map[path[-1]] is None: # проверка, что клетка пустая
                        possible_final_coordinate.add(path[-1])
                if isinstance(self.Simulation.Map.map[(nx, ny)], goal): # Что если цель достигнута?
                    if level + 1 <= creature.speed: # 1ый вариант, существо успевает дойти до цели
                        print(f'Вы выиграли, вы нашли {goal}, количество ходов = {counter}, Глубина = {level + 1}')
                        print(f'ЭТО КОНЕЧНЫЕ КООРДИНАТЫ {(nx, ny)}')
                        self.Simulation.Map.map[first_peak], self.Simulation.Map.map[(nx, ny)] = None, creature
                        creature.coordinate = (nx, ny)
                        return path + [(nx, ny)]
                    else: # 2ой вариант, до цели еще далеко, существо не успевает дойти
                        print(f'Вы не успели дойти до цели')
                        print(f'А СЮДА МОЖЕТ ПОПАТЬ СУЩЕСТВО {possible_final_coordinate}')
                        print(f'ЭТО КОНЕЧНЫЕ КООРДИНАТЫ ЦЕЛИ {(nx, ny)}')
                        # Поиск ближайшей точки
                        min_abs = float('inf')
                        closest_point = None
                        for i in possible_final_coordinate:
                            distance = abs((i[0] - nx) ** 2 + (i[1] - ny) ** 2)
                            if distance < min_abs:
                                min_abs = distance
                                closest_point = i
                        if closest_point:
                            self.Simulation.Map.map[first_peak], self.Simulation.Map.map[closest_point] = None, creature
                            creature.coordinate = closest_point
                            print(f'Существо Перемещается на {closest_point}')
                            return path + [closest_point]
                        else:
                            return path
                else:
                    queue.append(((nx, ny), level + 1, path + [(nx, ny)]))
                    # print(f'Добавлено в очередь: {((nx, ny), level + 1, path + [(nx, ny)])}') # Отладочное сообщение
        print(f'Существо не нашло цель и осталось на месте {first_peak}')  # Отладочное сообщение
        return []

