from Actions.simulation import Simulation
from Actions.map import Map
from config import Config


def main():
    s = Simulation(Config, Map(Config()))
    s.show_map()




if __name__ == '__main__':
    main()