from os import path


path= "text1.txt"
record = "Drake Mikelsson, 19"
def add_employee_to_file(record, path):
    fh = open(path,"a")
    fh.write(record+"\n")
    fh.close()
add_employee_to_file(record,path)
