from os import path
import re
path = "cat_list.txt"
def get_cats_info(path):
    dict_data ={}
    result = []
    
    with open(path, 'r') as fh:
        while True:
            line = fh.readline()
            if not line:
                return result
            line = line.split(",")
            print(line)
            print(dict_data)
            result.append({"id":line[0],"name":line[1],"age":line[2].removesuffix("\n")})

print(get_cats_info(path))
# Код еще не закончен! 