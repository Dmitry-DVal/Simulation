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
            if self.Simulation.Map.map[random_key] == None:
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
        print('-' * 20)
        print(f'День {self.Simulation.day_counter}')
        self.add_grass()
        self.Simulation.show_map()
        for creature in living_creatures_copy:
            self.is_predator_hungry(creature)
        self.Simulation.day_counter += 1


    def is_predator_hungry(self, creature):
        if isinstance(creature, predator.Predator) and creature.hp == Config.predatorHp:
            print('Сытый волк - не охотник')
            creature.hp -= 2
        elif isinstance(creature, predator.Predator):
            self.damage_hp(creature)
            return self.make_move(creature)
        else:
            return self.make_move(creature)

    def damage_hp(self, creature, damage = 1):
        creature.hp -= damage
    def add_grass(self, count_grass = 2):
        while count_grass != 0:
            random_key = random.choice(list(self.Simulation.Map.map.keys()))
            if self.Simulation.Map.map[random_key] == None:
                self.Simulation.Map.map[random_key] = grass.Grass((random_key))
            count_grass -= 1
        print("Новый день, выросла новая Трава")



    def make_move(self, creature):
        print(f'Существо - {creature}, Здоровье - {creature.hp}/9, Скорость - {creature.speed}, Координаты - {creature.coordinate}')
        self.Simulation.bfs.make_move(creature)
        self.Simulation.show_map()
        print()



