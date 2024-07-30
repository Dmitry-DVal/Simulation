class Map:
    """Содержит в себе коллекцию для хранения существ и их расположения."""

    def __init__(self, Config: 'Config') -> None:
        '''Принимает размер карты, создает пустую карту исходя из полученных размеров'''
        self.height = Config.height
        self.width = Config.width
        self.map = {(x, y): None for x in range(self.width) for y in range(self.height)}  #
