#from config import *
import random
# from Actions.simulation import Simulation
from config import Config
# from Actions.simulation import Simulation
from Entities import entity, creature, grass, herbivore, predator, rock, tree


class Actions:
    '''
    Класс, управляющий действиями совершаемыми над игровым миром
    '''

    def __init__(self, Simulation):
        self.Simulation = Simulation

    def set_entity_to_map(self, entityNumber, Entity):
        while entityNumber != 0:
            random_key = random.choice(list(self.Simulation.Map.map.keys()))
            if self.Simulation.Map.map[random_key] == None: # Попробуй просто через мап, ане через симуляцию
                if issubclass(Entity, predator.Predator):
                    self.Simulation.Map.map[random_key] = Entity((random_key), Config.predatorSpeed, Config.predatorHp, Config.predatorDamage)
                    self.Simulation.living_creatures += (Entity((random_key), Config.predatorSpeed, Config.predatorHp, Config.predatorDamage),)
                elif issubclass(Entity, herbivore.Herbivore):
                    self.Simulation.Map.map[random_key] = Entity((random_key), Config.herbivoreSpeed, Config.herbivoreHp)
                    self.Simulation.living_creatures += (Entity((random_key), Config.herbivoreSpeed, Config.herbivoreHp),)
                else:
                    self.Simulation.Map.map[random_key] = Entity((random_key))
                entityNumber -= 1

    def set_entities_to_map(self):
        for entity_number, Entity in zip([Config.grassNumber, Config.treeNumber,
                                          Config.rockNumber, Config.predatorNumber,
                                          Config.herbivoreNumber],
                                         [grass.Grass, tree.Tree, rock.Rock,
                                             predator.Predator, herbivore.Herbivore]):
            self.set_entity_to_map(entity_number, Entity)

