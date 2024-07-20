from Actions.simulation import Simulation
from Actions.map import Map
from config import Config



def main():
    s = Simulation(Config, Map(Config()))
    print('Установим существ на поле в случайном порядке')
    s.actions.set_entities_to_map()
    s.show_map()
    while len(s.living_creatures) > 2:
        s.actions.make_move_all_creatures()
    print(f'Игра окончена, колчество полных дней - {s.day_counter}')





if __name__ == '__main__':
    main()