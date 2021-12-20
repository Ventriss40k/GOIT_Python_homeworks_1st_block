# Слайсы (срезы)
string = "Hello world!"
print(string)
hello1 = string[0:5] # Первое число в скобке - с какого символа начинать срез, второе - на каком заканчивать
# ВАЖНО: здесь, как и везде в Пайтое первый символ имеет индекс 0 а не 1 
# ВАЖНО: в результат включаються символы ДО второго аргумента, тоесть в данном случае символ с индексом 5 в результат НЕ ВХОДИТ
print(hello1)
hello2 = string[5:] # Если не указать второе число, то это значит от определенного начала, и до самого конца
print(hello2)
hello3 = string[::2] # так же можно указать третье число - это шаг с которым будет вестись выборка 
# (в данном случае - каждое второе число, НАЧИНАЯ С ПЕРВОГО попадет в результат)
print(hello3)
hello4 = string[::-1] # а таким способом можно воспользоваться, что бы полчить строку в обратном порядке
print(hello4)