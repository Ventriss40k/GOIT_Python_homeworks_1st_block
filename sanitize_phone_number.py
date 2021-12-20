# ВЫРАЖЕНИЕ НА РЕГУЛЯРКАХ. работает, но не принимаеться автопроверкой
import re
def sanitize_phone_number(phone):
    phone = phone.strip() # убрали пробелы справа и слева
    result = re.sub(r'\D', "" ,phone)
    return result
    print(result)
    print(len(result))
print(sanitize_phone_number("     0503451234",))


