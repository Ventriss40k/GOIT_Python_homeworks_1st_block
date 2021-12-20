from datetime import datetime
# Разработайте функцию get_days_from_today(date), которая будет возвращать количество дней от текущей даты, 
# где параметр date - это строка формата '2020-10-09' (год-месяц-день).
date ="2021-10-09"
def get_days_from_today(date):
    today_date = datetime.now()
    date = date.split("-"); new_date =datetime(year=int(date[0]), month=int(date[1]), day=int(date[2]), hour=0) # ['2021', '10', '09']xasdsaDSAds
    difference = today_date - new_date
    return difference.days
get_days_from_today(date)


