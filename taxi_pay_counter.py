# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def trip_price(path):
#     global base_rate, price_per_km, total_trip
#     total_trip += 1
#     return int(path) * price_per_km + base_rate
# path = input("Enter kilometrage: ")    
# print(trip_price(path))
# print(f"total_trip: {total_trip}")
# # path = input("Enter kilometrage: ")
# # try:
# #     print(trip_price(path))
# # except:
# #     print("You entered invalid number of kilometers. Try again.")


# base_rate = 40
# price_per_km = 10
# total_trip = 0


# def trip_price(path):
#     global base_rate, price_per_km, total_trip
#     total_trip += 1
#     return path * price_per_km + base_rate

#     trip_price(path)

# print(trip_price(float(input("Enter kilometrage: "))))
# print
# print(f"total_trip: {total_trip}")

base_rate = 40
price_per_km = 10
total_trip = 0


def trip_price(path):
    global base_rate, price_per_km, total_trip
    total_trip += 1
    return path * price_per_km + base_rate

while True:
    try:
        path = float(input("Enter kilometrage: "))
    except:
        print("You entered not correct data.")
    else:
        print(f"Your trip costs {trip_price(path)}")
        print(f"Its your {total_trip} trip!")
        break

# автопровекрка  приняла после того, как был убран while и  break