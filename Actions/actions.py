import random

from Entities import grass, herbivore, predator, rock, tree


class Actions:
    '''
    Класс, управляющий действиями совершаемыми над игровым миром
    '''

    def __init__(self, simulation: 'Simulation') -> None:
        self.Simulation = simulation

    def set_entities_to_map(self) -> None:
        """Устанавливает существ на поле в случайном месте."""
        for entity_number, Entity in zip([self.Simulation.Config.grassNumber, self.Simulation.Config.treeNumber,
                                          self.Simulation.Config.rockNumber, self.Simulation.Config.herbivoreNumber,
                                          self.Simulation.Config.predatorNumber,
                                          ],
                                         [grass.Grass, tree.Tree, rock.Rock, herbivore.Herbivore,
                                          predator.Predator]):
            self.set_entity_to_map(entity_number, Entity)

    def set_entity_to_map(self, entityNumber: int, Entity: 'Entity') -> None:
        """Устанавливает существо на поле в случайном месте."""
        while entityNumber != 0:
            random_key = random.choice(list(self.Simulation.Map.map.keys()))
            if self.Simulation.Map.map[random_key] == None:  # Можно добавить несколько функций для каждого блока
                if issubclass(Entity, predator.Predator):
                    self.set_predator_to_map(random_key, Entity)
                elif issubclass(Entity, herbivore.Herbivore):
                    self.set_herbivore_to_map(random_key, Entity)
                else:
                    self.Simulation.Map.map[random_key] = Entity((random_key))
                entityNumber -= 1

    def set_predator_to_map(self, random_key: list[int, int], Entity: 'Entity') -> None:
        """Устанавливает Хищника на поле в случайном месте."""
        self.Simulation.Map.map[random_key] = Entity((random_key), self.Simulation.Config.predatorSpeed,
                                                     self.Simulation.Config.predatorHp,
                                                     self.Simulation.Config.predatorDamage)
        self.Simulation.living_creatures += (
            Entity((random_key), self.Simulation.Config.predatorSpeed, self.Simulation.Config.predatorHp,
                   self.Simulation.Config.predatorDamage),)

    def set_herbivore_to_map(self, random_key: list[int, int], Entity: 'Entity') -> None:
        """Устанавливает Травоядное на поле в случайном месте."""
        self.Simulation.Map.map[random_key] = Entity((random_key), self.Simulation.Config.herbivoreSpeed,
                                                     self.Simulation.Config.herbivoreHp)
        self.Simulation.living_creatures += (
            Entity((random_key), self.Simulation.Config.herbivoreSpeed,
                   self.Simulation.Config.herbivoreHp),)

    def make_move_all_creatures(self):
        """Все живые существа делают ход по очереди."""
        living_creatures_copy = self.Simulation.living_creatures.copy()
        print('-' * 20)
        print(f'День {self.Simulation.day_counter}')
        self.add_grass()
        self.Simulation.show_map()
        for creature in living_creatures_copy:
            self.is_predator_hungry(creature)
        self.Simulation.day_counter += 1

    def is_predator_hungry(self, creature: 'Creature') -> None:  # Так же каждый блок если - отдельная функция
        """Проверяет голоден ли хищник."""
        if isinstance(creature, predator.Predator) and creature.hp == self.Simulation.Config.predatorHp:
            print('Сытый волк - не охотник')
            creature.hp -= 2
        elif isinstance(creature, predator.Predator):
            self.damage_hp(creature)
            return self.make_move_one_creature(creature)
        else:
            return self.make_move_one_creature(creature)

    def damage_hp(self, creature: 'Creature', damage: int = 1) -> None:
        """Наносит урон существу, уменьшая его здоровье."""
        creature.hp -= damage

    def add_grass(self, count_grass: int = 2) -> None:
        """Добавляет траву на поле."""
        while count_grass != 0:
            random_key = random.choice(list(self.Simulation.Map.map.keys()))
            if self.Simulation.Map.map[random_key] == None:
                self.Simulation.Map.map[random_key] = grass.Grass((random_key))
            count_grass -= 1
        print("Новый день, выросла новая Трава")

    def make_move_one_creature(self, creature: 'Creature') -> None:
        """Cущество делает один ход."""
        print(
            f'Существо - {creature}, Здоровье - {creature.hp}/9, Скорость - {creature.speed}, Координаты - {creature.coordinate}')
        self.Simulation.bfs.bfs(creature)
        self.Simulation.show_map()
        print()
