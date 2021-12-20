import re
def read_employees_from_file(path):
    fh = open(path,"r")
    result =[]
    line =[]
    while True:
        line = fh.readline()
        if not line:
            break
        result.append((re.findall("[^\n]+",line))[0])
        print(result)
        
    fh.close()
    return result

read_employees_from_file("text1.txt")