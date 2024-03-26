class Entity(): # Сущность. Класс для всех существ и объектов. У всех есть координаты и картинки
    def __init__(self, coordinate, name, image):
        self.coordinate = coordinate
        self.name = name
        self.image = image

    # def show_image(self): # Будет показывать изображение
    #     return image #