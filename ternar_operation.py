# is_nice = True
# state = "nice" if is_nice else "not nice"

##--------------------------------
# number = input("input: ")
# state = "yes" if number else "no"
# #if и else  можно писать в 1 строке при таком варианте использования
# print(state)
##--------------------------------

data = None
msg = data or "Не было возвращено данных"
# таким образом можно проверить, содержит ли переменная данные, если нет - вывести сообщение без использования if, else
print(msg)
