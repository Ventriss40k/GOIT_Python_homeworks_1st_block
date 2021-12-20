num = int(input("Введите число: "))

if num > 0:
    if  num % 2:
        result = "Положительное нечетное число"
    else:
        result = "Положительное четное число"
elif num <0:
    result = "Отрицательное число"
else:
    result = "Это ноль"
print(result)
