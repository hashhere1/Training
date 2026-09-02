""" map, filter, zip, enumerate """

#map() applies function to every item in an iterable

prices = [1000, 2000, 3000, 4000, 5000]
discounted_price = map(lambda price: price * 0.9, prices)
print(list(discounted_price))

# filter() applies to those that satisfy a certain condition

price = [500, 600, 700, 1000, 1500, 2000]
final_price = filter(lambda number: number > 1000, price)
print(list(final_price))

check_prices = filter(lambda number: number >= 1500, price)
print(list(check_prices))

# zip() combine items from two or more lists position by position

name = ["Laptop", "Mobile", "Mouse"]
product_prices = [100000, 50000, 5000]
category = ["Electronics", "Daily Use", "IT"]
result = zip(name, product_prices, category)
dict_result = zip(name, product_prices)
print(list(result))
print(dict(dict_result))


# enumerate() lets us loop through the sequence while getting both the index and the value
for index, product in enumerate(name, start=1):
    print(f"-{index} {product}")

enumerated_prices = [1000, 2000, 3000, 4000, 5000]
for index, product_price in enumerate(enumerated_prices, start=1):
    if product_price > 1000:
        print(f"-{index} {product_price}")

