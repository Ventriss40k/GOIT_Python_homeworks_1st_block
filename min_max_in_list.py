# ЗАДАЧА: найти среднее зачение списка. 
# Разделить список на 2 списка: меньше и равно среднему и строго выше
# функция возвращает кортеж этих двух списков

# Подход №1 - среднее значение между максимальным и минимальным
# поик мин и макс значения
# LIST = [5, 21, 55, 1, 3 ,5, 29]
# maximum = LIST[0]
# minimum = LIST[0]
# for i in LIST:
#     if i > maximum:
#         maximum = i
#     elif i <minimum:
#         minimum = i
# avgerage = (maximum + minimum)/2
# print(avgerage)


# Подход № 2 - среднее арифметическое
LIST = [5, 21, 55, 1, 3 ,5, 29]
average = 0
summ = 0
for i in LIST:
    summ += i
try:
    average = summ/len(LIST)
    print(average)
except:
    pass
# Разбивка на 2 списка - больше среднего и меньше - равно среднему значению
lower_list = []
upper_list = []
for i in LIST:
    if i > average:
        upper_list.append(i)
    else:
        lower_list.append(i)
print(upper_list)
print(lower_list)

#  Создание кортежа из 2х списков
result = (upper_list,lower_list)
print(result)


def split_list(grade):
    average = 0
    summ = 0
    for i in grade:
        summ += i
    try:
        average = summ/len(grade)
        print(average)
    except:
        pass
    # Разбивка на 2 списка - больше среднего и меньше - равно среднему значению
    lower_list = []
    upper_list = []
    for i in grade:
        if i > average:
            upper_list.append(i)
        else:
            lower_list.append(i)
    print(upper_list)
    print(lower_list)

    #  Создание кортежа из 2х списков
    result = (lower_list,upper_list)
    print(result)
    return(result)

