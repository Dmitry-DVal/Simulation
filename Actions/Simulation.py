from config import *
from Entities import grass, tree, rock, predador, herbivore
import random
from Actions import map


class Simulation():  # Главный класс. Включает Счётчик ходов Рендерер поля Action
    "Главный класс приложения"

    def __init__(self, Map: 'Map', Config: 'Config'):
        self.Map = Map  # получает ЭК настроект или сам класс
        self.Config = Config  # получает карты  или сам класс

    def set_entity_to_map(self, entityNumber, Entity):
        while entityNumber != 0:
            random_key = random.choice(list(self.Map.map.keys()))
            if self.Map.map[random_key] == None:
                self.Map.map[random_key] = Entity
                entityNumber -= 1

    def set_entities_to_map(self):
        '''
        Принимает начения настроек (которые храняться в класса конифиг) и на основании этого расставляет по полю существ
        :return: Экземпляр класса Map с расставленными на карте сущностями
        '''
        for entity_number, Entity in zip([self.Config.grassNumber, self.Config.treeNumber,
                                          self.Config.rockNumber, self.Config.predatorNumber,
                                          self.Config.herbivoreNumber],
                                         [grass.Grass(), tree.Tree(), rock.Rock(),
                                          predador.Predator(), herbivore.Herbivore()]):
            self.set_entity_to_map(entity_number, Entity)
            # for Entity in [grass.Grass(), tree.Tree(), rock.Rock(), predador.Predator(), herbivore.Herbivore()]:
            #     self.set_entity_to_map(entity_number, Entity)
        # while self.Config.grassNumber != 0:
        #     random_key = random.choice(list(self.Map.map.keys()))
        #     if self.Map.map[random_key] == None:
        #         self.Map.map[random_key] = grass.Grass()
        #         self.Config.grassNumber -= 1
        # while self.Config.treeNumber != 0:
        #     random_key = random.choice(list(self.Map.map.keys()))
        #     if self.Map.map[random_key] == None:
        #         self.Map.map[random_key] = tree.Tree()
        #         self.Config.treeNumber -= 1
        # while self.Config.rockNumber != 0:
        #     random_key = random.choice(list(self.Map.map.keys()))
        #     if self.Map.map[random_key] == None:
        #         self.Map.map[random_key] = rock.Rock()
        #         self.Config.rockNumber -= 1
        # while self.Config.predatorNumber != 0:
        #     random_key = random.choice(list(self.Map.map.keys()))
        #     if self.Map.map[random_key] == None:
        #         self.Map.map[random_key] = predador.Predator()
        #         self.Config.predatorNumber -= 1
        # while self.Config.herbivoreNumber != 0:
        #     random_key = random.choice(list(self.Map.map.keys()))
        #     if self.Map.map[random_key] == None:
        #         self.Map.map[random_key] = herbivore.Herbivore()
        #         self.Config.herbivoreNumber -= 1

    def __str__(self):
        return f'The object Simulations. The main class of the game'

    def show_map(self):
        # покажет карту со всеми существами
        pass

    def field_renderer(self):  # рендер поля
        pass

    def next_turn(self):  # просимулировать один ход
        pass

    def start_simulation(self):  # запустить бесконечный цикл симуляции и рендеринга
        pass

    def pause_simulation(self):  # приостановить бесконечный цикл симуляции и рендеринга
        pass
