# Создайте класс Cat родительским классом которого является класс Animal. 
# В классе Cat выполните переопределение метода say, чтобы он возвращал строку "Meow" для экземпляров класса Cat.
# Создайте также переменную cat, которая будет являться экземпляром класса Cat.
#  При создании переменной cat имя кота должно быть "Simon", а вес в 10 единиц.
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass

    def change_weight(self, weight):
        self.weight = weight

class Cat(Animal):
    def say(self):
        return "Meow"

cat =Cat("Simon", 10)
    
        

