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
        if type(x) == int or type(x) == float:
            self.__x = x
        else:
            self.__x = None

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if type(y) == int or type(y) == float:
            self.__y = y
        else:
            self.__y = None
# ---------------------------
point = Point(5,10)  
print(point.x); print(point.y)
print("-----------")
point.x = "11"; print(point.x)
print("-----------")
point_new = Point("a","b")
print(point_new.x);print(point_new.x)
