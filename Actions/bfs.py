from Entities import grass, herbivore
class BFS():
    '''
    Класс для поиска в ширину
    '''
    def __init__(self, Simulation):
        self.Simulation = Simulation


    def get_neighbors(self, coordinates):
        '''
        Функция, для сосздания списка соседних клеток, на которые может наступить существо.
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

            for nx, ny in self.get_neighbors(creature.coordinate):
                if (nx, ny) in visited_peak: # Проверка посещалась ли уже вершина
                    continue
                if (nx, ny) in [pos for pos, _, _ in queue]:  # Проверка, есть уже данная вершина в очереди
                    continue
                # if level == creature.speed: # Добавление в возможные финальные координаты для существа
                #     if map[path[-1]] is None: # проверка, что клетка пустая
                #         #print(path[-1], "Могу быть тут")
                #         possible_final_coordinate.add(path[-1])
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
                            self.Simulation.Map.map[first_peak], self.Simulation.Map.map[(nx, ny)] = None, creature
                            creature.coordinate = (nx, ny)
                            print(f'Существо Перемещается на {closest_point}')
                            return path + [closest_point]
                        else:
                            return path
                else:
                    queue.append(((nx, ny), level + 1, path + [(nx, ny)]))
                    print(f'Добавлено в очередь: {((nx, ny), level + 1, path + [(nx, ny)])}') # Отладочное сообщение
        print(f'Существо не нашло цель и осталось на месте {first_peak}')  # Отладочное сообщение
        return []

def bfs_main():
# map1 = {(0, 0): None, (0, 1): <Entities.herbivore.Herbivore object at 0x0000022B0C01FE10>, (0, 2): None, (0, 3): None, (0, 4): None, (0, 5): None, (0, 6): None, (0, 7): <Entities.tree.Tree object at 0x0000022B0C01F490>, (1, 0): None, (1, 1): None, (1, 2): None, (1, 3): None, (1, 4): None, (1, 5): None, (1, 6): <Entities.tree.Tree object at 0x0000022B0C01F210>, (1, 7): <Entities.grass.Grass object at 0x0000022B0C01F010>, (2, 0): None, (2, 1): None, (2, 2): <Entities.rock.Rock object at 0x0000022B0C01F710>, (2, 3): None, (2, 4): None, (2, 5): <Entities.predator.Predator object at 0x0000022B0C01FC90>, (2, 6): None, (2, 7): <Entities.rock.Rock object at 0x0000022B0C01F690>, (3, 0): None, (3, 1): <Entities.rock.Rock object at 0x0000022B0C01FA90>, (3, 2): None, (3, 3): None, (3, 4): <Entities.grass.Grass object at 0x0000022B0C01EF90>, (3, 5): <Entities.tree.Tree object at 0x0000022B0C01F310>, (3, 6): None, (3, 7): None, (4, 0): None, (4, 1): None, (4, 2): None, (4, 3): None, (4, 4): None, (4, 5): None, (4, 6): None, (4, 7): <Entities.rock.Rock object at 0x0000022B0C01F910>, (5, 0): <Entities.tree.Tree object at 0x0000022B0C01F410>, (5, 1): None, (5, 2): <Entities.rock.Rock object at 0x0000022B0C01FC10>, (5, 3): None, (5, 4): None, (5, 5): None, (5, 6): <Entities.herbivore.Herbivore object at 0x0000022B0C01FF10>, (5, 7): None, (6, 0): None, (6, 1): None, (6, 2): None, (6, 3): None, (6, 4): None, (6, 5): None, (6, 6): None, (6, 7): None, (7, 0): None, (7, 1): None, (7, 2): None, (7, 3): <Entities.tree.Tree object at 0x0000022B0C01F290>, (7, 4): None, (7, 5): None, (7, 6): None, (7, 7): <Entities.tree.Tree object at 0x0000022B0C01F590>, (8, 0): None, (8, 1): None, (8, 2): None, (8, 3): <Entities.tree.Tree object at 0x0000022B0C01F390>, (8, 4): None, (8, 5): None, (8, 6): <Entities.rock.Rock object at 0x0000022B0C01F790>, (8, 7): <Entities.rock.Rock object at 0x0000022B0C01FB90>, (9, 0): None, (9, 1): None, (9, 2): None, (9, 3): None, (9, 4): None, (9, 5): None, (9, 6): None, (9, 7): None, (10, 0): None, (10, 1): None, (10, 2): None, (10, 3): None, (10, 4): None, (10, 5): None, (10, 6): None, (10, 7): None, (11, 0): None, (11, 1): None, (11, 2): None, (11, 3): None, (11, 4): <Entities.tree.Tree object at 0x0000022B0C01F510>, (11, 5): None, (11, 6): <Entities.rock.Rock object at 0x0000022B0C01F810>, (11, 7): <Entities.grass.Grass object at 0x0000022B0C01EF50>, (12, 0): <Entities.tree.Tree object at 0x0000022B0C01F610>, (12, 1): None, (12, 2): None, (12, 3): <Entities.tree.Tree object at 0x0000022B0C01F110>, (12, 4): None, (12, 5): None, (12, 6): None, (12, 7): None, (13, 0): <Entities.tree.Tree object at 0x0000022B0C01F190>, (13, 1): None, (13, 2): <Entities.tree.Tree object at 0x0000022B0C01F090>, (13, 3): None, (13, 4): <Entities.rock.Rock object at 0x0000022B0C01F890>, (13, 5): <Entities.rock.Rock object at 0x0000022B0C01FA10>, (13, 6): <Entities.predator.Predator object at 0x0000022B0C01FD50>, (13, 7): <Entities.rock.Rock object at 0x0000022B0C01FB10>, (14, 0): None, (14, 1): None, (14, 2): None, (14, 3): None, (14, 4): None, (14, 5): <Entities.rock.Rock object at 0x0000022B0C01F990>, (14, 6): None, (14, 7): None}
# map2 = {(0, 0): None, (0, 1): <Entities.herbivore.Herbivore object at 0x0000022B0C01FE10>, (0, 2): None, (0, 3): None, (0, 4): None, (0, 5): None, (0, 6): None, (0, 7): <Entities.tree.Tree object at 0x0000022B0C01F490>, (1, 0): None, (1, 1): None, (1, 2): None, (1, 3): None, (1, 4): None, (1, 5): None, (1, 6): <Entities.tree.Tree object at 0x0000022B0C01F210>, (1, 7): <Entities.grass.Grass object at 0x0000022B0C01F010>, (2, 0): None, (2, 1): None, (2, 2): <Entities.rock.Rock object at 0x0000022B0C01F710>, (2, 3): None, (2, 4): None, (2, 5): <Entities.predator.Predator object at 0x0000022B0C01FC90>, (2, 6): None, (2, 7): <Entities.rock.Rock object at 0x0000022B0C01F690>, (3, 0): None, (3, 1): <Entities.rock.Rock object at 0x0000022B0C01FA90>, (3, 2): None, (3, 3): None, (3, 4): <Entities.grass.Grass object at 0x0000022B0C01EF90>, (3, 5): <Entities.tree.Tree object at 0x0000022B0C01F310>, (3, 6): None, (3, 7): None, (4, 0): None, (4, 1): None, (4, 2): None, (4, 3): None, (4, 4): None, (4, 5): None, (4, 6): None, (4, 7): <Entities.rock.Rock object at 0x0000022B0C01F910>, (5, 0): <Entities.tree.Tree object at 0x0000022B0C01F410>, (5, 1): None, (5, 2): <Entities.rock.Rock object at 0x0000022B0C01FC10>, (5, 3): None, (5, 4): None, (5, 5): None, (5, 6): <Entities.herbivore.Herbivore object at 0x0000022B0C01FF10>, (5, 7): None, (6, 0): None, (6, 1): None, (6, 2): None, (6, 3): None, (6, 4): None, (6, 5): None, (6, 6): None, (6, 7): None, (7, 0): None, (7, 1): None, (7, 2): None, (7, 3): <Entities.tree.Tree object at 0x0000022B0C01F290>, (7, 4): None, (7, 5): None, (7, 6): None, (7, 7): <Entities.tree.Tree object at 0x0000022B0C01F590>, (8, 0): None, (8, 1): None, (8, 2): None, (8, 3): <Entities.tree.Tree object at 0x0000022B0C01F390>, (8, 4): None, (8, 5): None, (8, 6): <Entities.rock.Rock object at 0x0000022B0C01F790>, (8, 7): <Entities.rock.Rock object at 0x0000022B0C01FB90>, (9, 0): None, (9, 1): None, (9, 2): None, (9, 3): None, (9, 4): None, (9, 5): None, (9, 6): None, (9, 7): None, (10, 0): None, (10, 1): None, (10, 2): None, (10, 3): None, (10, 4): None, (10, 5): None, (10, 6): None, (10, 7): None, (11, 0): None, (11, 1): None, (11, 2): None, (11, 3): None, (11, 4): <Entities.tree.Tree object at 0x0000022B0C01F510>, (11, 5): None, (11, 6): <Entities.rock.Rock object at 0x0000022B0C01F810>, (11, 7): <Entities.grass.Grass object at 0x0000022B0C01EF50>, (12, 0): <Entities.tree.Tree object at 0x0000022B0C01F610>, (12, 1): None, (12, 2): None, (12, 3): <Entities.tree.Tree object at 0x0000022B0C01F110>, (12, 4): None, (12, 5): None, (12, 6): None, (12, 7): None, (13, 0): <Entities.tree.Tree object at 0x0000022B0C01F190>, (13, 1): None, (13, 2): <Entities.tree.Tree object at 0x0000022B0C01F090>, (13, 3): None, (13, 4): <Entities.rock.Rock object at 0x0000022B0C01F890>, (13, 5): <Entities.rock.Rock object at 0x0000022B0C01FA10>, (13, 6): <Entities.predator.Predator object at 0x0000022B0C01FD50>, (13, 7): <Entities.rock.Rock object at 0x0000022B0C01FB10>, (14, 0): None, (14, 1): None, (14, 2): None, (14, 3): None, (14, 4): None, (14, 5): <Entities.rock.Rock object at 0x0000022B0C01F990>, (14, 6): None, (14, 7): None}
    pass


if __name__ == '__main__':
    bfs_main()