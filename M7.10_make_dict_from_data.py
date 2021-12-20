keys =['name', 'age', 'email']
values = ['Nick', '23', 'nick@test.com']

def make_request(keys, values):
    result = {}
    count = 0
    if len(keys)==len(values):
        for i in keys:
            result[str(keys[count])]=str(values[count])
            count+=1
    return result
    print(result)
make_request(keys,values)
