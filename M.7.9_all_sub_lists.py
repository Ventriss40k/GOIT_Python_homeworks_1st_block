
    # print(data[0:1])
    # print(data[1:2])
    # print(data[2:3])

    # print(data[0:2])
    # print(data[1:3])
    # print(data)


    # # [4, 6, 1, 3]
    # #  [[], [4], [6], [1], [3], [4, 6], [6, 1], [1, 3], [4, 6, 1], [6, 1, 3], [4, 6, 1, 3]]

    # #  [[], - первый пустой список
    # #  [4], [6], [1], [3], - второй - каждый елемент
    # #  [4, 6], [6, 1], [1, 3], -третий - каждый елемент и следующий за ним (последний в одиночку не возвращаеться)
    # #  [4, 6, 1], [6, 1, 3], - четвертый - каждый елемент + 2 следующих (последний в одиночку не возвращаеться)
    # #  - n-й - каждый елемент +n последующих
    # #  [4, 6, 1, 3]] - последний - когда n знаков после первого достигло полного значения входного списка

    # # Как это работает:
    # data[0:0] - старт
    # data[0:1]; data[1:2];data[2:3];data[3:4] #-проход по 1 символу из data - прибавляем поочередно +1 к началу и концу слайса
    # # Цикл модернизируеться, когда конец слайса = len(data)+1
    # # Модернизация заключаеться в том, что сдвиг конца слайса увеличен на +1
    # # старт слайса сбрасываеться на 0, конец - изначальное значение сдвига
    # data[0:2]; data[1:3];data[2:4]
    # # цикл while долэен прекратиться когда сдвиг равен длинне data
def all_sub_lists(data):
    result =[]
    start =0
    finish = 0
    result.append(data[start:finish])
    while finish <len(data):
        finish=finish+1
        result.append(data[start:finish])
        start=start+1
    start =0
    finish = 1
    while finish <len(data):
        finish=finish+1
        result.append(data[start:finish])
        start=start+1
    start =0
    finish = 2
    while finish <len(data):
        finish=finish+1
        result.append(data[start:finish])
        start=start+1
    start =0
    finish = 3
    while finish <len(data):
        finish=finish+1
        result.append(data[start:finish])
        start=start+1

    print(result)

    return result
data =[4, 6, 1, 3]
all_sub_lists(data)

# def all_sub_lists(data):
#     result =[]
#     number_start = (-1)
#     element_start =(0)
#     for number in data:
#         number_start = number_start+1
#         for element in data:
#             element_start = element_start+1
#             result.append(data[number_start:element_start])
#         element_start=0