from datetime import datetime,timedelta
import random,decimal

# s= datetime.now()
# print(s)
# print(s.month)
# print(s.day)
# print(s.second)
# print(s.date())

# s = datetime(year = 2100, month=1, day = 2, hour = 12)
# print(s)
# s = s.replace(month=12)
# print(s)


# today = datetime.now()
# product_expire = {"кефир":datetime(year=2021, month=7,day=30), "молоко":datetime(year=2021, month=7,day=10), "салат":datetime(year=2021, month=7,day=14)}
# for product in product_expire.items():
#     if product[1] < today:
#         print(f"{product[0]} OK")
#     else:
#         print(f"{product[0]} Bad")

# data1 = datetime.now()
# data2 = datetime(year=1996,month=12,day=20)
# my_age = data1 - data2
# print(my_age)

# count =0
# d1 = datetime.now()
# while datetime.now() - d1 <= timedelta(seconds=5):
#     count +=1
# print(count)

# d1 = datetime.now()
# print(d1.strftime("%A %B %Y"))
# print(d1.strftime("%a %b %y"))
# d1 = d1.strftime("%a %b %y")
# print(d1)


# list1 = [1,2,3,4,5,6,7,8,9]
# random.shuffle(list1)
# print(list1)

# list1 = [1,2,3,4,5,6,7,8,9]
# random.choice(list1)
# print(list1)
    
d = {"a":1,
"b":2,
"c":3,
}
print(d)