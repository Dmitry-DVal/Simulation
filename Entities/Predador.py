from Entities.creature import Creature

class Predator(Creature): # Хищник. Должен иметь силу атаки. Задача сожрать травоядного.
    "Класс хищник, стремится сожрать травоядного"

    def __str__(self):
        return 'The object Pretador'
    def __init__(self, coordinate, speed, hp, damage):
        super().__init__(coordinate, speed, hp)
        self.damage = damage
        self.image = '🐺'


