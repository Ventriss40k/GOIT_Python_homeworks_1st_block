from datetime import date, datetime
# Напишите функцию для определения количества дней в конкретном месяце.
#  Ваша функция должна принимать два параметра: номер месяца в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех цифр.
#  Убедитесь, что функция корректно обрабатывает февраль високосного года.
month =9
year = 2021
def get_days_in_month(month, year):
    date1 = datetime(year=year, month=month, day = 1)
    if month <12:
        date2 = datetime(year=year, month=month+1, day = 1)
    if month ==12 :
        date2 = datetime(year=year+1, month=1, day = 1)
    month_lenght = date2-date1
    print(month_lenght.days)
    return month_lenght.days
    print(date1,date2)



get_days_in_month(month, year)
    