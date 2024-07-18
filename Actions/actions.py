import random
from config import Config
from Entities import grass, herbivore, predator, rock, tree


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
                                          Config.rockNumber, Config.herbivoreNumber, Config.predatorNumber,
                                          ],
                                         [grass.Grass, tree.Tree, rock.Rock, herbivore.Herbivore,
                                             predator.Predator]):
            self.set_entity_to_map(entity_number, Entity)

    def make_move_all_creatures(self):
        living_creatures_copy = self. Simulation.living_creatures.copy()
        for creature in living_creatures_copy:
            self.make_move(creature)



    def make_move(self, creature):
        print(f'Существо - {creature}, Здоровье - {creature.hp}, Скорость - {creature.speed}')
        #print(f'Характеристики', creature.__dict__)
        print('Координаты =', creature.coordinate)
        init_coordinates = creature.coordinate
        # goal = grass.Grass if isinstance(creature, herbivore.Herbivore) else herbivore.Herbivore # Цель существа
        # print(f'Цель существа - {goal}')
        # print(f"Возможные ходы - {self.Simulation.bfs.get_neighbors(creature.coordinate)}")
        self.Simulation.bfs.make_move(creature)
        self.Simulation.show_map()
        print()



