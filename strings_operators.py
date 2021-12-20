# # многострочный текст
# song = '''Jingle bells, jingle bells
# Jingle all the way
# Oh, what fun it is to ride
# In a one horse open sleigh'''

# print(song)


# # когда нам нужно в строку вставить длинный текст целиком, но так его будет неудобно читать в коде 
# # символ \ в конце первой и второй строк кода, он указывает интерпретатору игнорировать окончание строки и продолжить сразу со следующей.
# one_line_text = "Textual data in Python is handled with str objects, or strings. "\
#                 "Strings are immutable sequences of Unicode code points. "\
#                 "String literals are written in a variety of ways: single quotes, double quotes, triple quoted."
# print(one_line_text)


# ("spam " "eggs") == "spam eggs"  # True
# Выражение слева и выражение справа — это две равнозначные записи одного и того же текста 'spam eggs' и с точки зрения Python они неразличимы.


# #  ситуация, когда необходимо разбить строку на подстроки по некоторому символу,
# #  например, разбить текст на предложения по символу точки и пробела после точки, или предложение по словами.

# # Для такой задачи можно воспользоваться методом split,
# #  который принимает в качестве аргумента подстроку-маркер, которая будет границе по которой надо разбить строку на части.
# #  В результате вызова возвращается список строк.
# s = "I am learning strings in Python. Some new methods got now."
# sentences = s.split(". ")

# print(sentences[0]) # I am learning strings in Python
# print(sentences[1]) # Some new methods got now.

# # Вывод кодоировки каждого символа из последовательности цифр
# for i in range(16):
#     s = "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(i)
#     print(s)

width = 5
for num in range(12):
    print('{:^10} {:^10} {:^10}'.format(num, num**2, num**3))