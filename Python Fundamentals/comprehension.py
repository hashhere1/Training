"""Comprehensions are used as a smaller and shorter version.
-Make the code clean.
"""
#List comprehension
prices = [1000, 2000, 1000, 3000, 4000, 3000, 5000]

discounted_price = [(price - (price * 0.1)) for price in prices]

print(discounted_price)

req_prices = [price for price in prices if price > 2000]
print(req_prices)

wallet_prices = [500, 1200, 2500, 800, 3000, 1500]
exp_prices = [(price* 0.9) for price in wallet_prices if price > 1000]
print(exp_prices)

#Dictionary Comprehension
products = {"Laptop": 100000,
            "Phone": 50000,
            "Mouse": 3000
            }

expensive_products = {key:value for key,value in products.items() if value > 10000}
print(expensive_products)

unique_discounted_prices = {(price * 0.9) for price in prices }
print(unique_discounted_prices)