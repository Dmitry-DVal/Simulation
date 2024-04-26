from Entities.creature import Creature


class Herbivore(Creature): # Травоядное. Задача найти траву.
    "Класс травоядное, стремится найти траву"

    def __init__(self, coordinate):
        super().__init__(coordinate)
        self.image = '🐇'

    def __str__(self):
        return 'The object Herbivore'

