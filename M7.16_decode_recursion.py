data =["X", 3, "Z", 2, "X", 2, "Y", 3, "Z", 2]
def decode(data):
    result =[]
    def reccursion(data,result):
        if data:
            symbol = data.pop(0)
            count = data.pop(0)
            while count>0:
                result.append(symbol)
                count-=1
            reccursion(data,result)
        return result
    return reccursion(data,result)
print(decode(data))