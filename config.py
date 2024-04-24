import random


class Config:
    # Размер Поля
    width = 15  # Y
    height = 8  # X
    # Всего ячеек - 120
    # Количество животных, сущностей
    entity_count = {'predator': 5,
                    'herbivore': 5,
                    'tree': 5,
                    'grass': 10,
                    'rock': 7
                    }
    predatorNumber = 5
    herbivoreNumber = 5
    treeNumber = 7
    grassNumber = 10
    rockNumber = 7

    # Диапозон скоростей. Атак. Здоровья
    attackRange = []
    hpRange = []
    speedRange = []
