# d = {}
# d['Hello'] = "world"
# print(d)
# d[1] = 2
# print(d)
# d['qwerty'] = 1234
# print(d)
# d[(1,3)] =3

# # вывести данные из n  ячейки
# print(d[1])
# # достать значение данных с ключом ... или выдать ...
# print(d.get(5, "Error"))

# # вывести ключи
# for i in d.keys():
#     print(i)
# # Вывести значения
# for i in d.keys():
#     print(i)


# print("\n<----items------>")
# for key, value in d.items():
#     print(key, ":", value)


import collections # -  импорт модуля колекции
# from collections import  Counter - # более компактная формулировка, которая достает только нужный метод из модуля


d = {"math": 4, "english": 4, "biology": 3, "russian": 3}
summ = 0
average = 0
count = 0
for i in d.values():
    count += 1
    summ = summ + i
average = summ/count
print(average)
    

