path = "text.txt"
profession = "courier"
def get_employees_by_profession(path, profession):
    result =[]
    with open(path,"r") as fh:
        lines = fh.readlines()
        # print(lines)
        for i in lines:
           if i.find(profession)!=(-1): result.append(i)
    # print(result)
    return_str ="".join(result)
    # return_str = return_str.replace(" ","")
    return_str = return_str.replace("\n","")
    return_str = return_str.replace(profession,"")
    return return_str.rstrip()
    print(return_str)
print(get_employees_by_profession(path, profession))
