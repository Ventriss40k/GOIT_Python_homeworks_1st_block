name = input("What is your name: ")
age = int(input("What is your age: "))
licence = int(input("Do you have driving licence? (1 for 'Yes' 0 for 'No'): "))
if name and age >= 18 and licence == 1:
    print("You can rent a car")
else:
    no_name = ""
    under_18 = ""
    no_licence = ""
    if not name:
        no_name = "name not entered, "
    if age <= 17:
        under_18 = "youre under 18 years old, "
    if  licence !=1:
        no_licence = "you dont have driving licence, "
    print(f"You cant rent a car, because: {no_name}{under_18}{no_licence}come back later.")