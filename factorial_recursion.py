# Вычисляем факториал числа n с помощью рекурсии
# @param n – число для которого надо рассчитать факториал
# @return факториал числа n
def factorial(n):
    if n < 2:
        return 1  # Базовый случай
    else:
        return n * factorial(n - 1)  # Рекурсивный случай


num = int(input("Введите положительное целое число: "))
result = factorial(num)
print(f"Факторила числа {num} равен {result}")
    