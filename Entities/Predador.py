from Entities.Creature import Creature

class Predator(Creature): # Хищник. Должен иметь силу атаки. Задача сожрать травоядного.
    "Класс хищник, стремится сожрать травоядного"

    def __str__(self):
        return 'The object Pretador'
    def __init__(self, coordinate, name):
        super().__init__(coordinate, name)
        self.image = '🐺'


P = Predator(22, 'colw')
print(P.image)