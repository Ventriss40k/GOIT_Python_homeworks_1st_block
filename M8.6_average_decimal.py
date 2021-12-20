from decimal import Decimal, getcontext


def decimal_average(number_list, signs_count):
    result = Decimal(0)
    getcontext().prec = signs_count
    for i in number_list:
        result +=Decimal(i)
    result = result/len(number_list)
    print(result)
    return result
    




decimal_average([3, 5, 77, 23, 0.57], 6)