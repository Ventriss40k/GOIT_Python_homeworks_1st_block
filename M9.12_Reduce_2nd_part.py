# Вернемся к нашей первой задаче с четвертого модуля и перепишем ее с помощью функции reduce.
# payment = [1, -3, 4]

# def amount_payment(payment):
#     sum = 0
#     for value in payment:
#         if value > 0:
#             sum = sum + value
#     return sum
# Напомним условие. У нас есть список показаний задолженностей по коммунальным услугам в конце месяца — список payment. 
# Задолженности могут быть отрицательными — у нас переплата или положительными, если необходимо оплатить по счетам. 
# С помощью reduce, просуммируйте положительные значения и сумму платежа в конце месяца верните из функции amount_payment.
payment = [1, -3, 4]
from functools import reduce

def amount_payment(payment):
    positive_values = []
    for i in filter(lambda x: x>0,payment):
        positive_values.append(i)
    result = reduce(lambda x,y: x+y, positive_values)
    return result
print(amount_payment(payment))