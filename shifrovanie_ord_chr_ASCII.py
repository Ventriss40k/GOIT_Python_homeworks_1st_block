# message = input("Введите сообщение: ")
# message = ord(c)(message)
# print(message)
# # Вводим символ (не слово) и получаем его код


# message = int(input("Введите сообщение: "))
# message = chr(message)
# print(message)
# # Вводим код (обяхательно int) и получаем символ, который под ним зашифрован в таблице ASCII
        
        
#Задача: Перевести каждый символ из ввода в код, добавить сдвиг. Нужно сделать так, что бы шифровались только буквы, поетому нужно установить  вернуть обратно в форму символа,
#  из символов составить закодированное "предложение"
        
    # -Первести каждый символ в код - for i in message
    #  i = ord(i)
    # добавить сдвиг i = i + offset
    # i = chr(i)
        
# # 1. Код, который выводит перевод сообщения в набор кодов для каждого символа
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#   ch = ord(ch)
#   encoded_message = encoded_message + str(ch) + " "
# print(encoded_message)
        
# # 2. Код, который добавляет смещение в код каждого символа, и потом образует текстовую строку
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#   ch = ord(ch) + offset
#   ch = chr(ch)
#   encoded_message = encoded_message + str(ch)
# print(encoded_message)

# 3. Код который устанавливает "границы" в которых введенные символы будут изменяться (большие и малые англ буквы)
# message = input("Введите сообщение: ")
# offset = int(input("Введите сдвиг: "))
# encoded_message = ""
# for ch in message:
#   if ord(ch) in range(97, 122) or ord(ch) in range(65,90):
#     ch = ord(ch) + offset
#     ch = chr(ch)
#   else:
#     ch = ord(ch)
#     ch = chr(ch)
#   encoded_message = encoded_message + str(ch)
# print(encoded_message)

# # Код, который при сдвиге, выходящем за алфавит, начинает счет сначала
# 1. определить, символ относиться к верх/нижн регистру
# 2. расчитать смещение в рамках большого или малого англ алфавита не выходя за его рамки
# 3. интегрировать в прошлый код проверку на превышение сдвига

# 1.
# if ord(ch) in range(97, 122):

# if ord(ch) in range(65,90):

# # 2.
# if ord(ch) in range(97, 122):
#   pos = ord(ch) - ord("a")
#   pos = (pos + offset)%26 

# elif ord(ch) in range(65,90):
#   pos = ord(ch) - ord("A")
#   pos = (pos + offset)%26 



# 3.Рабочая модель, ура!!
message = input("Введите сообщение: ")
offset = int(input("Введите сдвиг: "))
encoded_message = ""
for ch in message:
  if ord(ch) in range(97, 122): # Для малых букв англ алфавита
    pos = ord(ch) - ord("a") # определяем разницу в позиции символа относительно первого символа в алфавите
    pos = (pos + offset)%26 # в англ алфавите 26 букв. Получаем остаток от деления смещения
    new_char = chr(pos + ord("a")) # Опеределяем новое смещение (которое не выходит за алфавит)
    encoded_message = encoded_message + str(new_char) # добавляем к разкодированному сообщению новую букву
  elif ord(ch) in range(65,90):# Для больших букв англ алфавита
    pos = ord(ch) - ord("A")
    pos = (pos + offset)%26
    new_char = chr(pos + ord("A"))
    encoded_message = encoded_message + str(new_char)
  else: # если символ не являеться большой или малой буквой англ алфавита
    ch = ord(ch)
    ch = chr(ch)
    encoded_message = encoded_message + str(ch)
print(encoded_message)