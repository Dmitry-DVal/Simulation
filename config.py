# Размер Поля
width = 15 # Y
height = 8 # X

# Количество животных
predadorNumbor = 5
herbivoreNumber = 5

# Диапозон скоростей. Атак. Здоровья
attackRange = []
hpRange = []
speedRange = []

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