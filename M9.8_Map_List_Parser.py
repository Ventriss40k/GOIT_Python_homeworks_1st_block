# Есть список contacts элементы которого словари контактов следующего вида:

#     {
#         "name": "Allen Raymond",
#         "email": "nulla.ante@vestibul.co.uk",
#         "phone": "(992) 914-3792",
#         "favorite": False,
#     }
# Словарь содержит, имя пользователя, его email, телефонный номер и свойство избранный контакт или нет.
# Разработайте функцию get_emails, которая получает в параметре список list_contacts
#  и возвращает список который содержит электронные адреса всех контактов из списка list_contacts. Используйте при этом функцию map
list_contacts =  [{'name': 'Allen Raymond', 'email': 'nulla.ante@vestibul.co.uk', 'phone': '(992) 914-3792', 'favorite': False},
  {'name': 'Chaim Lewis', 'email': 'dui.in@egetlacus.ca', 'phone': '(294) 840-6685', 'favorite': False},
   {'name': 'Kennedy Lane', 'email': 'mattis.Cras@nonenimMauris.net', 'phone': '(542) 451-7038', 'favorite': False},
    {'name': 'Wylie Pope', 'email': 'est@utquamvel.net', 'phone': '(692) 802-2949', 'favorite': False},
     {'name': 'Cyrus Jackson', 'email': 'nibh@semsempererat.com', 'phone': '(501) 472-5218', 'favorite': False}]
def get_emails(list_contacts):
    result = []
    def get_email(current_dict):
        try:
            return current_dict["email"]
        except:
            pass
    for i in map(get_email,list_contacts):
        result.append(i)
    print(result)
    return result
get_emails(list_contacts)
