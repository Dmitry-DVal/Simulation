from config import Config

class Map:
    def __init__(self, Config):
        '''Принимает размер карты, создает пустую карту исходя из полученных размеров'''
        self.height = Config.height
        self.width = Config.width
        self.map = {(x, y): None for x in range(self.width) for y in range(self.height)} #

