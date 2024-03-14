from config import *

Map = {(x, y): None for x in range(width) for y in range(height)}  # Создание пустой карты.
# Скорее всего я сделаю Map, где ключ будет коллецией ( координаты х, у), а значение - экземпляр класса Entity(), либо None