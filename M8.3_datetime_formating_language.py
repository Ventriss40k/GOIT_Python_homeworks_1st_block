from datetime import datetime
# Разработайте функцию get_str_date(date), которая будет преобразовывать дату из базы данных в формате ISO "2021-05-27 17:08:34.149Z"
#  в строковое представление "Thursday 27 May 2021" — день недели, число, месяц и год. Преобразованное значение функция должна вернуть при вызове.
date = "2021-05-27 17:08:34.149Z"
def get_str_date(date):
    new_date = datetime(year=int(date[0:4]), month=int(date[5:7]), day =int(date[8:10]))
    # print
    result = datetime.strftime(new_date, '%A %d %B %Y')
    print(result)
    return result
    
get_str_date(date)