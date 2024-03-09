
width = 15 # Y
height = 5 # X

Map = {(x, y): None for x in range(width) for y in range(height)}

Map[(0, 4)] = 'Заяц'
Map[(8, 3)] = 'Волк'

number

# Рисуем поле. Добавить потом проверку на сущность
for y in range(height):
    for x in range(width):
        if Map[(x, y)] is None:
            print(".", end=" ")  # Пустая клетка
        else:
            print("X", end=" ")  # Клетка с объектом
    print()  # Переход на новую строку





