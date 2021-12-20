# Есть список contacts элементы которого словари контактов следующего вида:
contacts=  [{
        "name": "Allen Raymond",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": False,
    },
    {
        "name": "Allen Garrison",
        "email": "nulla.ante@vestibul.co.uk",
        "phone": "(992) 914-3792",
        "favorite": True,
    }]
# Словарь содержит, имя пользователя, его email, телефонный номер и свойство избранный контакт или нет.
# Создайте функцию get_favorites(contacts), которая будет возвращать список содержащий только избранные контакты. 
# Используйте при этом функцию filter, чтобы отфильтровать по полю favorite только избранные контакты
def get_favorites(contacts):
    result = []
    for i in filter(lambda current_dict: current_dict["favorite"]==True,contacts):
        result.append(i)
    return result
print(get_favorites(contacts))

    