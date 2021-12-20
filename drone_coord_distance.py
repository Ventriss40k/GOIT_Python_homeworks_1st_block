# ЗАДАЧА: Написать функцияю, которая будет принимать на вход список координат четырехугольника
# Нужно посчитаь общее пройденное расстояние которое дрон пролетит между точками


points = {
    (0, 1): 2,
    (0, 2): 3.8,
    (0, 3): 2.7,
    (1, 2): 2.5,
    (1, 3): 4.1,
    (2, 3): 3.9,
# Здесь ключ - это первая и вторая точка полета, значение - расстояние между ними
}
# # #ЗАДАЧА: Нужно выделять по 2 елемента из списка и искать их как ключ в словаре points
# list_coordinates = [0, 1, 3, 2, 0, 2]
# previous = None
# total_distance = 0 # - расстояние которое пролетел дрон в сумме 17.6
# for i in list_coordinates:
#     key_coordinates = []
#     if previous != None:
#         if i > previous: # Устанавливаем порядок для key_koordinates, что бы первое число всегда было меньшим
#             key_coordinates.append(previous)
#             key_coordinates.append(i)
#         else:
#             key_coordinates.append(i)
#             key_coordinates.append(previous)

#     previous = i
#     if key_coordinates: # Что бы не пустой список в первый раз
#         key_coordinates = tuple(key_coordinates)
#         print(key_coordinates)
#         # ЗАДАЧА: Искать в словаре значения по ключу, добавлять значения к total_distance
           
#         for i in points.keys():
#             if i == key_coordinates:
#                 total_distance = total_distance + points.get(i)
#                 print(total_distance)

            


def calculate_distance(coordinates):
    global points
    points
    previous = None
    total_distance = 0 # - расстояние которое пролетел дрон в сумме 17.6
    for i in coordinates:
        key_coordinates = []
        if previous != None:
            if i > previous: # Устанавливаем порядок для key_koordinates, что бы первое число всегда было меньшим
                key_coordinates.append(previous)
                key_coordinates.append(i)
            else:
                key_coordinates.append(i)
                key_coordinates.append(previous)

        previous = i
        if key_coordinates: # Что бы не пустой список в первый раз
            key_coordinates = tuple(key_coordinates)
            print(key_coordinates)
            # ЗАДАЧА: Искать в словаре значения по ключу, добавлять значения к total_distance
            
            for i in points.keys():
                if i == key_coordinates:
                    total_distance = total_distance + points.get(i)
                    print(total_distance)
    return total_distance 

