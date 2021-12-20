data = [1, 2, [3, 4, [5, 6]], 7]
# РАБОЧИЙ КОД, НО НЕ МОЙ
def flatten(data):
    if data == []:
        return data
    elif isinstance(data[0], list):
        first = flatten(data[0])
        second = flatten(data[1:])
        return first + second
    elif not isinstance(data[0], list):
        first = [data[0]]
        second = flatten(flatten(data[1:]))
        return first + second
# print(flatten([[[[[[[[[[1], 2], 3], 4], 5], 6], 7], 8], 9], 10]))
print(flatten([1, [2, 3], [4, [5, [6, 7]]], [[[8], 9], [10]]]))
flatten(data)
        

# МОЙ КОД, работает в реддакторе, но не принимаеться автопроверкой
data = [1, 2, [3, 4, [5, 6]], 7]
def reccursion(search_area,result):
    for i in search_area:
        
        if type(i) is not list:
            result.append(i)
        if type(i) is list:
            reccursion(search_area=i,result=result)
    return result
print(reccursion(data,[]))
        
    
        