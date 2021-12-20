import re
def total_salary(path):
    fh = open(path,"r")
    result = 0
    while True:
        line = fh.readline()
        sallary = re.findall('([0-9]+)',line)
        if sallary:   
            result += float(sallary[0])
            # Нужно сделать суммацию и вывод резульата

        if not line:
            break
    fh.close()
    return result
    