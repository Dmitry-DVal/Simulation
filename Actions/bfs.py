from Entities import grass, herbivore, predator

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
            if self.is_in_range(peak) and self.is_it_free_cell(peak):
                possible_peaks.append((peak[0], peak[1]))
        return possible_peaks

    def is_in_range(self, peaks):
        return (peaks[0], peaks[1]) in self.Simulation.Map.map

    def is_it_free_cell(self, peaks):
        cell = self.Simulation.Map.map[(peaks[0], peaks[1])]
        return cell is None or isinstance(cell,(grass.Grass, herbivore.Herbivore))

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
                    if level + 1 <= creature.speed and isinstance(creature, herbivore.Herbivore): # 1ый вариант, существо успевает дойти до цели. Травоядное
                        print(f'Вы выиграли, вы нашли {goal}, количество ходов = {counter}, Глубина = {level + 1}')
                        print(f'ЭТО КОНЕЧНЫЕ КООРДИНАТЫ {(nx, ny)}, вы у нас {creature}')
                        creature.hp = self.Simulation.Config.herbivoreHp
                        self.Simulation.Map.map[first_peak], self.Simulation.Map.map[(nx, ny)] = None, creature
                        creature.coordinate = (nx, ny)
                        return path + [(nx, ny)]
                    elif level + 1 <= creature.speed and isinstance(creature, predator.Predator): # 1.5 вариант, существо успевает дойти до цели. Хищник
                        print(f'Вы вы нашли {goal}, количество ходов = {counter}, Глубина = {level + 1}')
                        if creature.damage > self.Simulation.Map.map[(nx, ny)].hp: # Урон больше чем здоровье зайца
                            print(f'ЭТО КОНЕЧНЫЕ КООРДИНАТЫ {(nx, ny)}, вы у нас {creature}')
                            # Удалить из списка живых существ
                            self.Simulation.living_creatures.remove(self.Simulation.Map.map[(nx, ny)])
                            self.Simulation.Map.map[first_peak], self.Simulation.Map.map[(nx, ny)] = None, creature
                            creature.coordinate = (nx, ny)
                            return path + [(nx, ny)]
                        else:
                            print(f'Заяц слишком живучий')
                            self.Simulation.Map.map[(nx, ny)].hp -= creature.damage
                            if len(path) > 0:
                                self.Simulation.Map.map[first_peak], self.Simulation.Map.map[path[-1]] = None, creature
                                creature.coordinate = path[-1]
                            return path
                    else:  # 2ой вариант, до цели еще далеко, существо не успевает дойти
                        return self.move_closer_to_goal(possible_final_coordinate, nx, ny, path, first_peak, creature)
                else:
                    queue.append(((nx, ny), level + 1, path + [(nx, ny)]))
                    # print(f'Добавлено в очередь: {((nx, ny), level + 1, path + [(nx, ny)])}') # Отладочное сообщение
        print(f'Существо не нашло цель и осталось на месте {first_peak}')  # Отладочное сообщение
        return []

    def move_closer_to_goal(self, possible_final_coordinate, nx, ny, path, first_peak, creature):  # 2-й вариант, до цели еще далеко, существо не успевает дойти
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
