# Пусть есть строка с числами
# "The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."
# Необходимо реализовать функцию generator_numbers, которая будет парсить строку и находить все целые числа в ней,
#  и работая как генератор отдавать указанные числа при обращении к ней в цикле.
# Функция generator_numbers(string="") непосредственно распарсивает строку и при помощи yield возвращает текущее число.
# Функция sum_profit(string) суммирует числа, полученные от generator_numbers и возвращает общую сумму прибыли из строки.
import re
def generator_numbers(string=""):
    pool = re.findall('[0-9]+',string)
    for i in pool:
        yield i 

def sum_profit(string):
    result =0
    gen = generator_numbers(string)
    while True:
        try:result+= int(next(gen))
        except StopIteration: return result

    
print(sum_profit("The resulting profit was: from the southern possessions $ 100, from the northern colonies $500, and the king gave $1000."))  
    