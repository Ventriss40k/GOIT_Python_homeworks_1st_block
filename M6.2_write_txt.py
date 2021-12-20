# fh = open("text1.txt","w")
# employees = [['Robert Stivenson,28', 'Alex Denver,30'],['Drake Mikelsson,19']]
# for i in employees:
#     for b in i: 
#         fh.write(b)
#         fh.write("\n")
# fh.close()




def write_employees_to_file(employee_list, path):
    fh = open(path,"w")
    for i in employee_list:
        for b in i: 
            fh.write(b+"\n")
    fh.close()
write_employees_to_file([['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']],"text1.txt")
