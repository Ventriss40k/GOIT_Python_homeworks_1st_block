# Онлайн-магазин "У Бобра" предоставляет услугу экспресс-доставки для своих 
# товаров по цене 5¤ за первый товар в заказе и 2¤ – за все последующие товары. 
# Необходимо реализовать функцию, принимающую в качестве первого параметра количество товаров в заказе quantity,
#  так же должен присутствовать параметр, передаваемый только по ключу discount.
#  Параметр discount по умолчанию имеет значение 0 - скидки нет. Принимает значения от 0 до 1.
#  Функция cost_delivery возвращает общую сумму доставки.


def cost_delivery(quantity, *_ , discount=0 ):
    return (5 + ((quantity - 1)*2))*(1-discount)

print(cost_delivery(10,21,34,56,78,90, discount=0.5))
