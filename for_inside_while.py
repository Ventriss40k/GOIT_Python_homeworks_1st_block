num = int(input("Введите целое число (0 для выхода): "))
sum = 0
while num > 0:
    for i in range(0,num+1):
        sum = sum + num
        num = num - 1
    print(sum)
    num = int(input("Введите целое число (0 для выхода): "))
    sum = 0
    