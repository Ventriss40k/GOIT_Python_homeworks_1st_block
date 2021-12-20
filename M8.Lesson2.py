# import random
# d = {
#     "q1?": [["a", "b", "c", "d"], "a"],
#     "q2?": [["a", "b", "c", "d"], "b"],
#     "q3?": [["a", "b", "c", "d"], "c"],
#     "q4?": [["a", "b", "c", "d"], "d"],
# }
# lq = random.sample(d.keys(), 3)
# for i in lq:
#     random.shuffle(d[i][0])
#     print(f"{i} answers:\n{d[i][0]}")

# from collections import namedtuple
# # person = tuple([1,2])
# # print(person)
# Person = namedtuple("Person",["name","age"])
# person = Person("Vasya",21)
# print(person.age)
# print(person[0])

# from collections import Counter
# data = [1,1,2,3,4,1,2,3,5]
# d = dict(Counter(data))
# print(d)


# data = [1,1,2,3,4,1,2,3,5]
# d = {}
# for i in data:
#     if not i in d.keys():
#         d[i] = 0
#     if i in d.keys():
#         d[i] +=1
# print(d)

# from collections import OrderedDict
#  позволяет при переводде другого вида данных в словарь, сохранить последоватьельность
#  Нужен для пайтон тарше 3.6 в более новых все словари - orderdict

# from collections import deque

# d = deque()
# d.append('last')
# d.appendleft('first')
# d.insert(1, "midle")
# print(d)

from collections import deque
from itertools import count

def is_same_from_both_sides():
    d = deque("1234554321")
    for i in range(len(d)):
        if d.pop != d.popleft:
            print("n")
            # return False
        else:
            print("y")
    # return True
print(is_same_from_both_sides())
        





