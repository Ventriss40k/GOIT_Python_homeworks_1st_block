def token_parser(s):
    result =[]
    to_write = None
    operands = "+-+*/()"
    numbers ="0123456789"
    for symbol in s:
        if symbol in numbers:
            if to_write == None: to_write = str(symbol)
            elif to_write: to_write = to_write+str(symbol)
        elif symbol in operands:
            if to_write:result.append(to_write)
            to_write = None
            result.append(symbol)
    if to_write:result.append(to_write)

        


    return result
            
    
s = "2+ 34 -5 * 3"
# ['2', '+', '34', '-', '5', '*', '3']
print(token_parser(s))
