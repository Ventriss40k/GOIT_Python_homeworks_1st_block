# Функция принимает цену price и скидку discount это дробное число от 0 до 1.
# И на этот размер мы понижаем итоговую цена товара.
# Логику функции необходимо прописать во внутренней функции apply_discount используя объявление переменой price как nolocal

# оглашаем, что у нас есть главная функция, которая принимает значения цены и скидки 
def discount_price(price, discount):
    # оглашаем функцию, которая будет применять скидку к цене, указанной в главной функции
    def apply_discount():
        # говорим, что значение price, которое есть во внутренне функции, будет передано в главную функцию
        nonlocal price
        price = price - price*discount
    # огласив внутреннюю функцию, тут же, внутри главной функции, вызываем ее и говорим,
    #  что она должна возвращать значение price (Без этого функция возвратит None)
    apply_discount()
    return price
   
        

# указываем, что здесь может произойти ошибка 
try:
    # вызываем принт основной функции, с вводом аргументов. 
    # Функция возвратит price, т.к его возвращает внутренняя фунция, а главная функция ниччего не возвращает
    print(discount_price(float(input("Input price: ")), float(input("Input discount: "))))
    # Заготавливаем обрабтку исключения
except:
    print("incorect input")  
