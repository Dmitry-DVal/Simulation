from Entities.Creature import Creature

class Predador(Creature): # Хищник. Должен иметь силу атаки. Задача сожрать травоядного.
    "Класс хищник, стремится сожрать травоядного"
    def __init__(self, coordinate, name):
        image = '🐺'
        super().__init__(coordinate, name, image)


P = Predador(22, 'colw')