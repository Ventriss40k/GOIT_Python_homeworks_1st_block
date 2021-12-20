import collections
from typing import Collection


Cat = collections.namedtuple("Cat", ["nickname", "age", "owner"])
# -----------
# cats = [Cat("Mick", 5, "Sara"), Cat("Barsik", 7, "Olga"), Cat("Simon", 3, "Yura")]
# -----------
cats = [
    {"nickname": "Mick", "age": 5, "owner": "Sara"},
    {"nickname": "Barsik", "age": 7, "owner": "Olga"},
    {"nickname": "Simon", "age": 3, "owner": "Yura"},
]
# -----------
def convert_list(cats):
    result = []
    if type(cats[0]) == dict: 
        print("dict")
        for i in cats:
            result.append(Cat(i["nickname"],i["age"],i["owner"]))
        print(result)
    elif isinstance(cats,list):
        print("list")
        for i in cats:
            result.append({"nickname": i.nickname, "age": i.age, "owner": i.owner})
            print(i)
            print(type(i))
        print(result)
    return result
convert_list(cats)
    