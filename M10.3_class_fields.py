class Animal:
    nickname = "Barsik"
    weight = 100
    def say():
        pass
# --------------------------
class Animal:
    def __init__(self, nickname, weight):
        self.nickname = nickname
        self.weight = weight

    def say(self):
        pass


animal = Animal("Boris", 34)
