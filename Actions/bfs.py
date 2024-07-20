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
                if (nx, ny) in visited_peak or (nx, ny) in [pos for pos, _, _ in queue]: # Проверка посещалась ли уже вершина, есть ли она в очереди
                    continue
                if level == creature.speed: # Добавление в возможные финальные координаты для существа
                    if self.Simulation.Map.map[path[-1]] is None: # проверка, что клетка пустая
                        possible_final_coordinate.add(path[-1])
                if isinstance(self.Simulation.Map.map[(nx, ny)], creature.goal): # Что если цель достигнута?
                    if level + 1 <= creature.speed: # 1ый вариант, существо успевает дойти до цели. Травоядное
                       return self.update_position(creature, first_peak, (nx, ny), level, counter, path)
                    else:  # 2ой вариант, до цели еще далеко, существо не успевает дойти
                        return self.move_closer_to_goal(possible_final_coordinate, nx, ny, path, first_peak, creature)
                else:
                    queue.append(((nx, ny), level + 1, path + [(nx, ny)]))
        print(f'Существо не нашло цель и осталось на месте {first_peak}')  # Отладочное сообщение
        return []

    def update_position(self, creature, first_peak, finish_peak, level, counter, path):
        if level + 1 <= creature.speed and isinstance(creature, herbivore.Herbivore):  # 1ый вариант, существо успевает дойти до цели. Травоядное
            print(f'{creature} нашел {creature.goal}, количество ходов = {counter}, Глубина = {level + 1}')
            print(f'{creature}, ваши конечные координаты {finish_peak}')
            creature.hp = self.Simulation.Config.herbivoreHp
            self.Simulation.Map.map[first_peak], self.Simulation.Map.map[finish_peak] = None, creature
            creature.coordinate = finish_peak
            return path + [finish_peak]
        elif level + 1 <= creature.speed and isinstance(creature, predator.Predator):  # 1.5 вариант, существо успевает дойти до цели. Хищник
            print(f'{creature} нашел {creature.goal}, количество ходов = {counter}, Глубина = {level + 1}')
            if creature.damage > self.Simulation.Map.map[finish_peak].hp:  # Урон больше чем здоровье зайца
                print(f'ЭТО КОНЕЧНЫЕ КООРДИНАТЫ {finish_peak}, вы у нас {creature}')
                self.Simulation.living_creatures.remove(self.Simulation.Map.map[finish_peak]) # Удалить из списка живых существ
                self.Simulation.Map.map[first_peak], self.Simulation.Map.map[finish_peak] = None, creature
                creature.coordinate = finish_peak
                return path + [finish_peak]
            else:
                print(f'Волк бьет зайца, но Заяц слишком живучий')
                self.Simulation.Map.map[finish_peak].hp -= creature.damage
                if len(path) > 0:
                    self.Simulation.Map.map[first_peak], self.Simulation.Map.map[path[-1]] = None, creature
                    creature.coordinate = path[-1]
                return path
    def move_closer_to_goal(self, possible_final_coordinate, nx, ny, path, first_peak, creature):  # 2-й вариант, до цели еще далеко, существо не успевает дойти
        print(f'{(nx, ny)} - Конечные координаты цели, {creature} не успевает дойти.')
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
            print(f'{creature} перемещается на {closest_point}')
            return path + [closest_point]
        else:
            return path