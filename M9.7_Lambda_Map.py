# Есть список name с именами пользователей, но все начинаются со строчной буквы.
# name = ["dan", "jane", "steve", "mike"]
# Разработайте функцию normal_name, которая принимает список имен и возвращает тоже список имен, но уже с правильными именами с заглавной буквы.
# ['Dan', 'Jane', 'Steve', 'Mike']
# Необходимо использовать функцию map. Не забудьте, что необходимо выполнить преобразование типов для map

def normal_name(list_name):
    result = []
    for i in map(lambda x:x.capitalize(),list_name):
        result.append(i)
    return result

