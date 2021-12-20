def data_preparation(list_data):
    result =[]
    for outer_list in list_data:
        outer_list.sort()
        if len(outer_list) <=2: 
            for element in outer_list: result.append(element)
        else: 
            outer_list =(outer_list[1:len(outer_list)-1])
            for element in outer_list: result.append(element)
                # if len(element)==2: result.append(outer_list)
                # if len(element)==1: result.append
    result.sort(key=None, reverse=True)
    return result
        







list_data =[[1,2,3],[3,4], [5,6]]
print(data_preparation(list_data))