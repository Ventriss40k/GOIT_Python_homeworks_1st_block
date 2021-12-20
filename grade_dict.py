# ПРОСТОЙ ВАРИАНТ
def get_grade(key):
    grade = {"F":1, "FX":2, "E":3,"D":3, "C":4, "B":5, "A":5}
    return grade.get(key)
    
def get_description(key):
    description = {"F":"неудовлетворительно", "FX":"неудовлетворительно", "E":"достаточно","D":"удовлетворительно", "C":"хорошо", "B":"очень хорошо", "A":"отлично"}
    return description.get(key)

print(get_grade("A"))
print(get_description("B"))

# СЛОЖНЫЙ ВАРИАНТ
# grade_dict = {"F":[1, "неудовлетворительно"], 
# "FX":[2, "неудовлетворительно" ], "E":[3,"достаточно"], "D":[3,"удовлетворительно"], "C": [4,"хорошо"], "B":[5, "очень хорошо"], "A":[5, "отлично"]}
# def get_grade(key):
#     global grade_dict
#     # 2. Написать функцию, которая будет принимать ключ ECTS и возвращать пятибальную оценку
#     try:
#         result = grade_dict.get(key)[0]
#     except TypeError:
#         result = None
#     print(result)
# def get_description(key):
#     # 3. Написать функцию, которая будет принимать ключ ECTS и возвращать обьяснение
#     try:
#         result = grade_dict.get(key)[1]
#     except TypeError:
#         result = None   
#     print(result)
# get_grade("A")
# get_description("A")