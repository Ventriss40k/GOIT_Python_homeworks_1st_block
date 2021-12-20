# Для списка numbers подсчитать сумму элементов с помощью функции reduce.

# numbers = [3, 4, 6, 9, 34, 12]
# Создайте функцию sum_numbers(numbers) результатом выполнения которой будет сумма чисел всех элементов списка numbers.
from functools import reduce


def sum_numbers(numbers):
    return reduce(lambda x,y: x+y, numbers)
print(sum_numbers([3, 4, 6, 9, 34, 12]))
