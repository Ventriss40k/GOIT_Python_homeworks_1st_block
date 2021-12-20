DEFAULT_DISCOUNT = 0.05


def get_discount_price_customer(price, customer):
    if "discount" in customer.keys():
        return price - (price * customer["discount"])
    else:
        return price - (price * DEFAULT_DISCOUNT)

price = 10
customer = {'name': 'Dima'}
print(get_discount_price_customer(price, customer))