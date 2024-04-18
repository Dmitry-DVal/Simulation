class Simulation():  # Главный класс. Включает Счётчик ходов Рендерер поля Action
    "Главный класс приложения"

    def __str__(self):
        return f'The object Simulations. The main class of the game'

    def __init__(self, Map):
        self.Map = Map  # получение начальной карты
        self.count_move = 0  # счетчик ходов

    def show_map(self):
        # покажет карту со всеми существами
        pass

    def field_renderer(self):  # рендер поля
        pass

    def next_turn(self):  # просимулировать один ход
        pass

    def start_simulation(self):  # запустить бесконечный цикл симуляции и рендеринга
        pass

    def pause_simulation(self):  # приостановить бесконечный цикл симуляции и рендеринга
        pass

