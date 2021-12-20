# Для кода из задания, вам необходимо реализовать класс CatDog не используя наследование от класса Animal, 
# но, чтобы экземпляр класса CatDog вел себя так же, как экземпляр класса Cat, т.е. он должен притвориться, что он класс Cat

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


class CatDog():
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight
    def change_weight(self, weight):
        self.weight = weight
    def say(self):
        return "Meow"
  

    
        
        

    
        

    
        