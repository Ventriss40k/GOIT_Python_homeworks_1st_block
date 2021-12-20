s= 1
while s is 1:
    age = int(input("How old are you: "))
    if age >= 1 and age <= 5:
        print("your a toddler") 
    elif age >=6 and age <= 12:
        print("youre a child") 
    elif age >=13 and age <= 20:
        print("youre a teen")  
    elif age >=21 and age <= 26:
        print("youre a young man")      
    elif age >=27 and age <= 60:
        print("youre a man")     
    else :
        print("youre a grandpa")
    s=int(input("Enter '1' to restart: "))
    if s == 1:
        print("Lets try again:)")
    else:
        print("Fine, bye")
        

      
