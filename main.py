from Actions.simulation import Simulation
from Actions.map import Map
from config import Config
from Actions.actions import Actions


def main():

    s = Simulation(Config, Map(Config()))
    # print("Проверяем, что создается пустое поле")
    # s.show_map()
    print('Установим существ на поле, в случайном порядке')
    s.actions.set_entities_to_map()
    s.show_map()
    print(s.Map.map)
    print('Список живых существ', s.living_creatures, sep='\n')
    s.actions.make_move_all_creatures()
    print(s.Map.map)
    print(f'Оставшиеся живые существа {s.living_creatures}')





if __name__ == '__main__':
    main()