from Actions.simulation import Simulation
from Actions.map import Map
from config import Config
from Actions.actions import Actions


def main():
    s = Simulation(Config, Map(Config()))
    print('Установим существ на поле, в случайном порядке')
    s.actions.set_entities_to_map()
    s.show_map()
    while len(s.living_creatures) > 2:
        s.actions.make_move_all_creatures()





if __name__ == '__main__':
    main()