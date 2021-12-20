message = "Never argue with stupid people, they will drag you down to their level and then beat you with experience."
search = "r"
result = 0
for i in message:
    # i - это переменная в котору. будет записываться каждая новая итерация цикла  for 
    # (в данном случае - это перебор букв из message, по 1й букве за раз)
    if i == search:
        # здесь проверяем, равна ли текущая буква тому что мы ищем (r)
      result = result + 1
      # если да, то увеличиваем счетчик на +1
print(result)
        