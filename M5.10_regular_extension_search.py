# Задача:
# Написать функцию find_word, принимающую аргументы: text и word. 
# Функция ищет слово word в тексте text  спомощью функции search  и возвращает словарь
# {
#     'result': True, # результат поиска True или False
#     'first_index': 34, # начальная позиция совпадения
#     'last_index': 40, # конечная позиция совпадения
#     'search_string': 'Python', #часть строки, в которой было совпадение
#     'string': 'Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.'
# } string - строка переданная в функцию

import re

def find_word(text,word):
    result = {
    'result': False, # результат поиска True или False
    'first_index': None, # начальная позиция совпадения
    'last_index': None, # конечная позиция совпадения
    'search_string': word,
    'string': text
    } 

    seek = re.search(word,text)
    if seek:
        result["result"] = True
    try:
        result["first_index"] = seek.span()[0]
    except:
        pass
    try:   
        result["last_index"] = seek.span()[1]
    except:
        pass
    return result
    
print(find_word("Guido van Rossum began working on Python in the late 1980s, as a successor to the ABC programming language, and first released it in 1991 as Python 0.9.0.", "Python"))