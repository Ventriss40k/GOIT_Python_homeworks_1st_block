num = int(input("Введите число для деления: "))
for variable in range(num):
    if variable % 2 == 1:
        continue
    # continue пропускает текущюю итерацию и начинает следующую.
    # Таким образом, если число было 3, то оно пропускаеться и подставляеться число 4, которое уже не подходит под условие if и его печатает
    print(variable)
