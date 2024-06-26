from config import *
from Entities import grass, tree, rock, predador, herbivore
from Actions import actions
import random
from Actions import map


class Simulation(actions.Actions):  # Главный класс. Включает Счётчик ходов Рендерер поля Action
    "Главный класс приложения"

    def __init__(self, Map: 'Map', Config: 'Config'):
        self.Map = Map  # получает ЭК настроект или сам класс
        self.Config = Config  # получает класс c настройками

    def set_entity_to_map(self, entityNumber, Entity):
        while entityNumber != 0:
            random_key = random.choice(list(self.Map.map.keys()))
            if self.Map.map[random_key] == None:
                if issubclass(Entity, predador.Predator):
                    self.Map.map[random_key] = Entity([random_key], Config.predatorSpeed, Config.predatorHp, Config.predatorDamage)
                elif issubclass(Entity, herbivore.Herbivore):
                    self.Map.map[random_key] = Entity([random_key], Config.herbivoreSpeed, Config.herbivoreHp)
                else:
                    self.Map.map[random_key] = Entity([random_key])
                entityNumber -= 1

    def set_entities_to_map(self):
        '''
        Принимает начения настроек (которые храняться в класса конифиг) и на основании этого расставляет по полю существ
        :return: Экземпляр класса Map с расставленными на карте сущностями
        '''
        for entity_number, Entity in zip([self.Config.grassNumber, self.Config.treeNumber,
                                          self.Config.rockNumber, self.Config.predatorNumber,
                                          self.Config.herbivoreNumber],
                                         [grass.Grass, tree.Tree, rock.Rock,
                                          predador.Predator, herbivore.Herbivore]):
            self.set_entity_to_map(entity_number, Entity)


    def __str__(self):
        return f'The object Simulations. The main class of the game'


    def next_turn(self, new_coardinate : list):  # просимулировать один ход
        # Пока просто проверяем как существо переместиться с клетки на клетку
        self.Map.map[(0, 0)], self.Map.map[new_coardinate] = self.Map.map[new_coardinate], self.Map.map[(0, 0)]

    def field_renderer(self):  # рендер поля
        pass



    def start_simulation(self):  # запустить бесконечный цикл симуляции и рендеринга
        pass

    def pause_simulation(self):  # приостановить бесконечный цикл симуляции и рендеринга
        pass
