# ЗАДАЧА: 
# Создать генератор паролей, состоящий из заданных символов, 8 символов в длинну, используяметод  randint, таблицу ASCII и методы ord и chr
# ()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~
# В таблице ASCII это символы с 40 по 126


from random import randint


def get_random_password():
    password = "12345678"
    new_password =[]
    for i in password:
        new_password.append(chr(randint(40,126)))
        result = ''.join(new_password)
    print(result)
    return result
get_random_password()



