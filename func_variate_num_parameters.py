# здесь мы указываем вторым аргументом кортеж
def first(size, *pos ):
    return size + len(pos)
    
print(first(1,3,4))
# здесь мы указываем вторым аргументом словарь
def second(size, **pos ):
    return size + len(pos)

print(second(1,a=1,b=2,c=3,d=4))
    