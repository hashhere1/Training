"""This involves everything i have learned so far."""

print("----Ecommerce Order and Customer Support System------")

STORE_NAME = "TechMart"

name = input("Enter your full name: ").title()
age = int(input("Enter your age: "))
email = input("Enter your Email: ").lower()
city = input("Enter the city in which you live: ")
product_name = input("Enter product name: ").upper()
product_price = float(input("Enter product price: "))
quantity = int(input("Enter the quantity of product: "))
premium_customer = input("Are you a premium customer? ")

print("------Enter your skills-----")
skill_1 = input("Enter first skill/interest: ").strip().lower()
skill_2 = input("Enter second skill/interest: ").strip().lower()
skill_3 = input("Enter third skill/interest: ").strip().lower()

print("-------String indexing/slicing----")
print(f"First character of customer's name is: {name[0]}")
print(f"Last character of customer's name is: {name[-1]}")
print(f"First three characters of city are: {city[0:3]}")
print(f"Last four characters of email are: {email[-4:]}")
print(f"Reversed customer name is: {name[::-1]}")

#Creating a list
print("---List---")
cart = [product_name]
cart.append("Mouse")
cart.insert(1, "USB Cable")
cart.remove("Mouse")
print(f"The total number of items in cart are: {len(cart)}")
print(f"Does the orignal product exists in the cart? {product_name in cart}")

#Creating a tuple
print("---Tuple---")
country = "Pakistan"
postal_code = 60000
customer_location = (city, country, postal_code)
print(f"The city is: {customer_location[0]}")
print(f"The last value is: {customer_location[-1]}")
cit, con, post = customer_location
print(f"The city is: {cit}")
print(f"The country is: {con}")
print(f"The postal_code is: {post}")

#Creating a set
skills = {skill_1, skill_2, skill_3}
recommended = {"python", "git", "sql"}
print(f"The unique skills are: {skills ^ recommended}")
print(f"Common interests are: {skills & recommended}")
print(f"Recommended interests that you don't have: {recommended - skills}")
print(f"Checking if python exists in your interests/skills: {'python' in skills}")

#Creating a dictionary
order = {
    "customer": name,
    "age": age,
    "email": email,
    "product": product_name,
    "price": product_price,
    "quantity": quantity,
    "premium": premium_customer,
    "cart": cart
}

print("---Dictionary items---")
order["city"] = city
updated_price = int(input("Enter the updated product price: "))
order["price"] = updated_price
total = updated_price * quantity
order["total"] = total
print(f"All the key are: {order.keys()}")
print(f"All the values are: {order.values()}")
print(f"All the key-value pairs are: {order.items()}")
print(f"Checking if email exists: {'email' in order}")
print(f"The phone number of customer is: {order.get('phone', 'Not provided')}")

print("----Order Summary----")
print(f'Store: {STORE_NAME}')
print(f"Customer: {name}")
print(f'Age: {age}')
print(f"Email: {email}")
print(f"City: {city}")
print(f"Product: {product_name}")
print(f"Price: {updated_price}")
print(f"Quantity: {quantity}")
print(f"Total: {total}")
print(f"Premium Customer: {premium_customer}")
print(f"Cart: {cart}")
print(f"Location: {customer_location}")
print(f"Interests/skills: {skills}")