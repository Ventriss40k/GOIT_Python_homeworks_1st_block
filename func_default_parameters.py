# В аргументе функци, 2 первых имеют только название, а третий название и значение по умолчанию.
# Это позволяет функции работать, если третий аргумент не указан
def get_fullname(first_name, last_name, middle_name=None):
    if middle_name == None:
        return first_name + " " + last_name
    elif middle_name:
        return first_name + " " + middle_name + " " + last_name


print(get_fullname("Anton", "Nazaruk", "Vladimirovich"))

