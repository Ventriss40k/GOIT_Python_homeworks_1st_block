# ЗАДАНИЕ
# 1. функициия formatted_grades принимает на вход словарь вида: students = {"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"}
# 2. Возвращает список отформатированных строк вида:
#    1|Nick      |  A  |  5
#    2|Olga      |  B  |  5
#    3|Mike      | FX  |  2
#    4|Anna      |  C  |  4
# Параметры таблицы:
# первый столбец ширина 4 символа, выравнивание по правому краю
# второй столбец ширина 10 символов, выравнивание по левому краю
# четвертый и пятый столбец ширина 5 символов и выравнивание по центру
# вертикальный символ | не входит в ширину столбца

grade = {"A": 5, "B": 5, "C": 4, "D": 3, "E": 3, "FX": 2, "F": 1}
def formatted_grades(students):
    global grade
    count = 1
    result = []
    for k,v in zip(dict(students).keys(),dict(students).values()):
        string = '{:>4}|{:<10}|{:^5}|{:^5}'.format(count, k,v,grade[v])
        count+=1
        result.append(string)
    # for i in result:
    #     print(i)
    return result
    

formatted_grades({"Nick": "A", "Olga": "B", "Mike": "FX", "Anna": "C"})

