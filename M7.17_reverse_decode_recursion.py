
# 1. привести data к виду списка, что бы можно было использовать data.pop()
# ________________
# 2. если last_symbol == None - записать data.pop(0) в переменную last_symbol
# 2.1 увеличить symbol_count на 1
# 3. если data.pop(0) == last_symbol - увеличить count на 1
# ________________
# 4.если data.pop(0)!= last_sumbol, то:
# 4.1 result.append(last_symbol)
# 4.2 result.append(count)
# В рекурсию передать data, result

data =["X", "X", "X", "Z", "Z", "X", "X", "Y", "Y", "Y", "Z", "Z"]
data = "XXXZZXXYYYZZ"
data=[]
data=""
def encode(data):
    result =[]
    count = 0
    last_pop_symbol = None
    # проверка на пустые входные данные
    if data =="": return []
    if data == []: return []
    # Приведение data к списку, если это строка
    if isinstance(data,str):
        new_data =[]
        for i in data: new_data.append(i)
        data = new_data
    def symbol_check(data,result,count,last_pop_symbol):
        if not data: result.append(last_pop_symbol); result.append(count); return result  
        if last_pop_symbol == None: last_pop_symbol = data.pop(0); count+=1 
        elif last_pop_symbol == data[0]: last_pop_symbol= data.pop(0); count +=1
        elif last_pop_symbol != data[0]: result.append(last_pop_symbol); result.append(count); count = 0; last_pop_symbol = None
        return symbol_check(data,result,count,last_pop_symbol)
    return symbol_check(data,result,count,last_pop_symbol)
print(encode(data))
    




        

    
    
        

    

    
