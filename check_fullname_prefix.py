# Задача: проверить, являеться ли first_name префиксом full_name
def is_check_name(fullname, first_name):
    return fullname.startswith(first_name) # функция .startswith определяет, начинаеться ли искомая строка данный на фрагмент или нет, выводит True|False
    # есть еще функция endswith, она проверяет конец
print(is_check_name)