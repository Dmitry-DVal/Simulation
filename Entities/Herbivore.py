from Entities.creature import Creature


class Herbivore(Creature): # Травоядное. Задача найти траву.
    "Класс травоядное, стремится найти траву"

    def __init__(self, coordinate, speed, hp):
        super().__init__(coordinate, speed, hp)
        self.image = '🐇'

    def __str__(self):
        return 'The object Herbivore'

