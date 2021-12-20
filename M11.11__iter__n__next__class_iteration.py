# Необходимо реализовать класс RandomVectors, который сможет создавать итерируемый объект и позволять итерироваться по случайным векторам.

# Формат класса:

# RandomVectors(max_vectors: int, max_points: int) -> Iterable(max_vectors,  max_points)
# где:

# max_vectors - определяет максимальное количество элементов (экземпляров класса Vector) в итерируемой последовательности
# max_points - определяет максимальное значение для координат x и y (в диапазоне 0...max_points)
# Чтобы экземпляры класса RandomVectors были итерируемыми объектами, в классе должен быть реализован метод __iter__, который возвращает итератор. Итератор - это любой объект, который на каждом шаге итерации (шаг итерации - это вызов метода next() для этого итератора) - возвращает следующее значение - и так до исчерпания количества итераций (определяется параметром max_vectors).

# В нашем случае итератором будет класс Iterable в котором необходимо реализовать метод __next__. Он в конструкторе получает те же параметры max_vectors и max_points, что и класс RandomVectors.

# Метод __next__ должен выдавать каждое последующее значение из списка self.vectors. Создайте в конструкторе набор случайных векторов self.vectors длиной max_vectors с помощью randrange. Атрибут current_index - указатель-индекс на текущий вектор из списка vectors, необходим для итерирования

# Пример работы класса `RandomVectors:

# vectors = RandomVectors(5, 10)

# for vector in vectors:
#     print(vector)
# Вывод должен быть похожим на этот:

# Vector(7,7)
# Vector(0,0)
# Vector(8,9)
# Vector(1,9)
# Vector(6,6)
# Детализируем нашу задачу:

# Класс RandomVectors должен иметь метод __iter__, который должен вернуть объект итератора (класс Iterable)
# Объект итератора (экземпляр класса Iterable) должен иметь метод __next__
# Метод __next__ следит за количеством возможных шагов итерации, они определяются параметром max_vectors
# Если мы исчерпали возможные шаги — то метод __next__ генерирует исключение StopIteration
# В противном случае метод __next__ — возвращает вектор со случайными координатами (экземпляр класса Vector), размер  координат вектора определяется параметром max_points.
from random import randrange


class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y

    def __str__(self):
        return f"Point({self.x},{self.y})"


class Vector:
    def __init__(self, coordinates: Point):
        self.coordinates = coordinates

    def __setitem__(self, index, value):
        if index == 0:
            self.coordinates.x = value
        if index == 1:
            self.coordinates.y = value

    def __getitem__(self, index):
        if index == 0:
            return self.coordinates.x
        if index == 1:
            return self.coordinates.y

    def __call__(self, value=None):
        if value:
            self.coordinates.x = self.coordinates.x * value
            self.coordinates.y = self.coordinates.y * value
        return self.coordinates.x, self.coordinates.y

    def __add__(self, vector):
        x = self.coordinates.x + vector.coordinates.x
        y = self.coordinates.y + vector.coordinates.y
        return Vector(Point(x, y))

    def __sub__(self, vector):
        x = self.coordinates.x - vector.coordinates.x
        y = self.coordinates.y - vector.coordinates.y
        return Vector(Point(x, y))

    def __mul__(self, vector):
        return (
                self.coordinates.x * vector.coordinates.x
                + self.coordinates.y * vector.coordinates.y
        )

    def len(self):
        return (self.coordinates.x ** 2 + self.coordinates.y ** 2) ** 0.5

    def __str__(self):
        return f"Vector({self.coordinates.x},{self.coordinates.y})"

    def __eq__(self, vector):
        return self.len() == vector.len()

    def __ne__(self, vector):
        return self.len() != vector.len()

    def __lt__(self, vector):
        return self.len() < vector.len()

    def __gt__(self, vector):
        return self.len() > vector.len()

    def __le__(self, vector):
        return self.len() <= vector.len()

    def __ge__(self, vector):
        return self.len() >= vector.len()

# -----------------------------------------------------------------------
class Iterable:
    def __init__(self, max_vectors, max_points):
        self.current_index = 0
        self.vectors = []
        self.max_vectors = max_vectors
        self.max_points = max_points

        
            

    def __next__(self):
        if self.current_index<self.max_vectors:
            self.current_index+=1
            return Vector(Point(randrange(0,self.max_points),randrange(0,self.max_points)))
        else: 
            raise StopIteration
        
        
            
            
class RandomVectors:
    def __init__(self, max_vectors=10, max_points=50):
        self.max_vectors = max_vectors
        self.max_points = max_points
        
        
        
        

    def __iter__(self):
        return Iterable(self.max_vectors, self.max_points)
        


vectors = RandomVectors(5,30)