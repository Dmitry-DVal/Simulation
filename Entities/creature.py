from entity import Entity


class Creature(Entity):
    '''
    Класс для живых существ. У них появляется здоровье и скорость передвижения.
    №№№! Переделать в абстрактный класс
    '''

    def __init__(self, coordinate, speed, hp):
        super.__init__(coordinate)
        self.speed = speed
        self.hp = hp


def main():
    'описываются все действия, которые необходимо сделать'
    print('Colled from creature.py')

if __name__ == '__main__':
    main()



