from random import randrange,randint
min = 1
max = 2
quantity = 5

def get_numbers_ticket(min, max, quantity):
    result = []
    if quantity > max or min <0 or max >1000: return result
    while len(result) < quantity:
        i = randint(0, 9)
        if i not in result:
            result.append(i)
    result.sort()
    print(result)
    return result


print(get_numbers_ticket(min, max, quantity))
    
