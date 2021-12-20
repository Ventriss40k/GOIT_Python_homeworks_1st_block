# # написать функцию, которая будет принимать значение, которое будет искать в значениях словаря и возвращать списком ключи, имеющие это значение

# dictionary = {"A":1, "B":2,"C":3, "D":2, "E":1,"F":3}
# value = 2
# result = []
# for i,val in dictionary.items():
#     if value == val:
#         result.append(i)
# print (result)


# Рабочая функция для автопроверки
def lookup_key(data, value):
    result = []
    for i,val in data.items():
        if value == val:
            result.append(i)
    return result

