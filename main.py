from Actions.simulation import Simulation
from Actions.map import Map
from config import Config
from Actions.actions import Actions


def main():
    s = Simulation(Config, Map(Config()))
    print("Проверяем, что создается пустое поле")
    s.show_map()
    print('Установим сущест на поле, в случайном порядке')
    s.actions.set_entities_to_map()
    s.show_map()
    print('Список живых существ')
    print(s.living_creatures)
    s.actions.make_move_all_creatures()





if __name__ == '__main__':
    main()