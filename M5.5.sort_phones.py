




def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone



def get_phone_numbers_for_countries(list_phones):
    phone_dict = {
        "UA":[],
        "JP":[],
        "TW":[],
        "SG":[]
        }
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        print(phone)
#     print(sanitize_phone_number)
        if "81" == phone[0:2]:
            phone_dict["JP"].append(phone)
        elif "65" in phone[0:2]:
            phone_dict["SG"].append(phone)
        elif "886" in phone[0:3]:
            phone_dict["TW"].append(phone)
        elif "380" == phone[0:3]:
            phone_dict["UA"].append(phone)
        else:
            phone_dict["UA"].append(phone)
    return phone_dict
    print(phone_dict)











get_phone_numbers_for_countries(["+38-093-98-64-156", "+38(093)9864178","+8193)9864178","+6593)9864178","+886"])










# def func1(i):
#     i = 5
#     return i 


# def main(data):
#     for i in data:
#         i = func1(i)
#         print(i)
    


# main([1,2,3,4,5])


    

