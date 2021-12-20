# 1.Приложение принимает один операнд или один оператор за один цикл запрос-ответ.
# 2. Все операции приложение выполняет по мере поступления одну за одной.
# 3. Приложение выводит результат вычислений когда получает от пользователя =.
# 4. Приложение заканчивает свою работу после того, как выведет результат вычисления.
# 5. Пользователь по очереди вводит числа и операторы.
# 6. Если пользователь вводит оператор два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# 7. Если пользователь вводит число два раза подряд, то он получает сообщение об ошибке и может ввести повторно.
# 8. Приложение корректно обрабатывает ситуацию некорректного ввода (exception).
from time import process_time
result = None
operand = None
operator = None
wait_for_number = True
list_of_operators = ("+", "-", "*", "/", "=")
# Ввод первого числа. Проверка на то что это число. Просьба переввести если не число. Переключение на ожидание оператора.
while wait_for_number == True:
        try:
            operand = float(input("Введите число 1: "))  
            wait_for_number = False
        except:
            print("Вы ввели не число")
        print(f"Вы ввели число {operand}")
        result = operand
while True:
# Ввод знака с проверкой на 1 символ из заданного списка, выдача результата, если знак - равно
    while wait_for_number == False:
        operator = str(input("Введите символ +, -, *, /, = : "))
        if operator in list_of_operators:
            print(f"Вы ввели символ {operator}")
            wait_for_number = True
        else:
            print(f"{operator} - не коректный символ")
        if operator == "=":
            print(f"Ответ: {result}")  
            print (process_time())
            break
            
    
# Ввод последующих чисел,Выполнение математического действия
    while wait_for_number == True:
        try:
            operand = float(input("Введите число 2: "))  
            wait_for_number = False
        except:
            print("Вы ввели не число")
    print(f"Вы ввели число {operand}")
    if operator == "+":
        result = float(result + operand)
    elif operator == "-":
        result = float(result - operand)
    elif operator == "*":
        result = float(result * operand)
    elif operator == "/":
        result = float(result / operand)
    












    
            

       