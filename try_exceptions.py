data = input("type smth: ")
try:
    #  Говорю, что сейчас может быть ошибка
    data = int(data)
    #Пытаюсь перевести data в тип  "целое число"
except ValueError:
    print(f"{data} is not a number")
    #Называю название ошибки(ValueError) и говорю что делать в случае если она случилась
else:
    print(f"{data} + 1 = {data+1}")
    # else: Говорю что делать если не случилось оговоренной выше ошибки
finally:
    print("Operation ended")
    # finally: то что будет выполнено в любом случае, случилась ли ошибка или нет