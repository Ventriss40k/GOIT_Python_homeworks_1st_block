def calc(a, symbol, b):
    result = 0
    try:
        if symbol == "+":
            result = a + b
        if symbol == "-":
            result = a - b
        if symbol == "*":
            result = a * b
        if symbol == "/":
            result = a/b
    except:
        print("eror")
    return result  
     


