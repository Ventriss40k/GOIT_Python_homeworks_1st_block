# ЗАДАЧА
# -------------
# Написать функцию, которая будет принимать аргументом список паролей, и возвращать True или False в зависимости от того, все ли значения соответствуют критериям, или нет
# КРИТЕРИИ
# 1. Нет дубликатов
# 2. Все значения в виде строк
# 3. Длиннна ровно 4 символа
# 4. Содержат только цифры
# ----------------
# ГИПОТЕЗА
# 1. Нет дубликатов 
# -Проверка множеством
# 2. Все значения в виде строк
# - поискать метод проверки 
# - type(o) is str
# 3. Длиннна ровно 4 символа
# - фор и лен
# 4. Содержат только цифры
# -Метод проверки ис диджит

def is_valid_pin_codes(pin_codes):
    result = True

    # Проверка на непустой список
    if len(pin_codes) == 0:
        result = False
        print("List is empty")

    # Проверка на дубликаты
    test_double = set(pin_codes)
    if not len(list(test_double)) == len(pin_codes):
        print("there are duplicates")
        result = False
    else:
        print("there are no dublicates")

    # Все значения в виде строк?
    for i in pin_codes:
        if type(i) is str:
            print(f"{i} is str")
        else:
            print(f"{i} is not str")
            result = False

    # 3. Длинна = 4 символа
    for i in pin_codes:
        if len(i) != 4:
            print(f"{i} is not 4 symbol long")
            result = False
            
    # 4. Содержат только цифры
    NUMBERS = ["0","1","2","3","4","5","6","7","8","9"]
    for i in pin_codes:
        for e in i:
            if e not in NUMBERS:
                print(f"{i} is not number")
                result = False    
    print(f"List of passwords correct: {result}")
    return result
    
is_valid_pin_codes(['1101', '9034', '0010'])
    

