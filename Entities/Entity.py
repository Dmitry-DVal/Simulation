class Entity(): # Сущность. Класс для всех существ и объектов. У всех есть координаты и картинки
    "Класс для всех существ и объектов, существующих в симуляции"

    def __str__(self):
        return 'The object Entity'
    def __init__(self, coordinate: list):
        self.coordinate = coordinate
    #     self.name = name
    #     self.image = image

    # def show_image(self): # Будет показывать изображение
    #     return image #