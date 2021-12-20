# | decimal  |   hex    |  binary  |
# |0         |    0     |         0|
# |1         |    1     |         1|
# |2         |    2     |        10|
# |3         |    3     |        11|
def formatted_numbers():
    num_list = []
    num_list.append(('|{:^10}|{:^10}|{:^10}|').format("decimal","hex","binary"))
    string = ""
    for i in range(0,16):
        string = ('|{:<10d}|{:^10x}|{:>10b}|').format(i,i,i)
        num_list.append(string)
    for i in num_list:
        print(i)
    return num_list
formatted_numbers()