from main import *



width = 15 # Y
height = 5 # X

Map = {(x, y): None for x in range(width) for y in range(height)}

Map[(0, 4)] = Herbivore(3,4)
Map[(8, 3)] = Predador(2, 7)
Map[(0, 3)] = Grass()
Map[(1,0)] = Rock()
Map[(6,4)] = Tree()

# Рисуем поле.
# Позже сделать вывод через джоин (возможно)
for y in range(height):
    for x in range(width):
        if Map[(x, y)] is None:
            print("..", end="  ")  # Пустая клетка
        ### !!! Код ниже везде повторяется. Можно в классе сущности просивоить кажому свое изображение и выводить его
        elif isinstance(Map[(x, y)], Grass):
            print("🌿", end="  ")  # Клетка с травой
        elif isinstance(Map[(x,y)], Rock):
            print("🪨", end="  ")  # Клетка с камнем
        elif isinstance(Map[(x,y)], Tree):
            print("🌲", end="  ")  # Клетка с деревом
        elif isinstance(Map[(x,y)], Predador):
            print("🐺", end="  ")  # Клетка с деревом
        elif isinstance(Map[(x,y)], Herbivore):
            print("🐇", end="  ")  # Клетка с деревом
    print()  # Переход на новую строку


