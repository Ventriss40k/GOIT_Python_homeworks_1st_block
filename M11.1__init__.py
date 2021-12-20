# Создайте класс Point, который будет отвечать за отображение геометрической точки на плоскости.
# Реализуйте через конструктор __init__ инициализацию двух атрибутов: координаты x и координаты y.
# Пример:

# point = Point(5, 10)
# print(point.x)  # 5
# print(point.y)  # 10
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y=y



        
point = Point(5,10)
print(point.x)
print(point.y)
