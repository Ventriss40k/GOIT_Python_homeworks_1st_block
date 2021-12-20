terra = [[1, 2, 5, 10], [2, 10, 2], [1, 3, 1]]
power = 1
for i in terra:
    skip = False
    print(f"i = {i}")
    for e in i:
        print(f"e = {e}, power = {power}")
        if skip == False:
            if power >= e:
                power += e
                print(f"new power = {power}")
            else:
                skip = True
                print(f"e is more then power")  
print(f"final power = {power}")





# def game(terra, power):
#     for i in terra:
#         skip = False
#         print(f"i = {i}")
#         for e in i:
#             print(f"e = {e}, power = {power}")
#             if skip == False:
#                 if power >= e:
#                     power += e
#                     print(f"new power = {power}")
#                 else:
#                     skip = True
#                     print(f"e is more then power")  
#     print(f"final power = {power}")
#     return power
