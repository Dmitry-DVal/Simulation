class Config:
    '''
    Класс с настройками симуляции
    '''

    def __init__(self, width=15, height=8, predatorNumber=2, herbivoreNumber=3,
                 treeNumber=12, grassNumber=3, rockNumber=12,
                 predatorSpeed=5, herbivoreSpeed=3,
                 predatorHp=9, herbivoreHp=9, predatorDamage=5):
        """Инициализирует настройки игры"""

        # Размер Поля
        self.width = width  # Y
        self.height = height  # X

        # Кол-во существ
        self.predatorNumber = predatorNumber  # 5
        self.herbivoreNumber = herbivoreNumber  # 6
        self.treeNumber = treeNumber  # 7
        self.grassNumber = grassNumber  # 10
        self.rockNumber = rockNumber  # 7

        # Скорость существ
        self.predatorSpeed = predatorSpeed
        self.herbivoreSpeed = herbivoreSpeed

        # Здоровье существ
        self.predatorHp = predatorHp
        self.herbivoreHp = herbivoreHp

        # Урон хищника
        self.predatorDamage = predatorDamage
