first = int(input("Введите первое целое число: "))
second = int(input("Введите второе целое число: "))
if first > second:
    nod = second 
else:
    nod = first
    #выбираем наименьшее из 2х чисел, как первый делитель
while first % nod != 0 or second % nod != 0:
    nod = nod - 1
    # Проверяем, деляться ли без отатка оба числа на выбранный делитель, если нет - уменьшаем делитель на 1 и проверяем снова
print(nod)
    

