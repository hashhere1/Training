def show_store_info():
    print('====TechMart====\n' \
    'Welcome to TechMart\n' \
    'Your Trusted online store')

show_store_info()

def calculate_discount(price, discount):
    print(f"Orignal Price: {price}")
    print(f"Discount: {discount}%")
    discount_amount = (price * discount)/100
    print(f"Dicount amount: {discount_amount}")
    print(f"Final price: {price-discount_amount}")

calculate_discount(5000, 10)

# Function which returns a value
def calculate_total(price, quantity):
    print(f"Price of the product is: {price}")
    print(f"Quantity of the product is: {quantity}")

    total = price * quantity
    return total

amount = calculate_total(1500, 4)
print(f"The total amount is: {amount}")

#Fucntion with default arguments
def create_product(name, price, category='General'):
    print(f"Name of product is: {name}")
    print(f"Price of product is: {price}")
    print(f"Category of product is: {category}")

create_product("Laptop", 100000, "Electronics")
create_product("Notebook", 500)


# *args is used when we don't know how many input values we will receive from the user
# It stores the values in the form of tuple

def calculate_total(*args):
    total = 0
    for number in args:
        total += number
    print(f"Total amount is: {total}")

calculate_total(10, 20, 30, 40)

# **kwargs are used when we have arbitary named arguments
# it stores value in the form of dictionary

def employee_information(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

employee_information( name="Hassaan",role="Backend Developer",experience="Fresh",salary=80000)

print("====Ecommerce Order Calculator====")
def create_order(customer_name, discount=0, *prices, **kwargs):

    for key, value in kwargs.items():
                print(f"{key}: {value}")

    total = 0
    for price in prices:
        total += price

    if discount > 0:
        discounted_price = (total * discount)/ 100
        print(f"The discount price is: {discounted_price}")
        return total - discounted_price     

    return total   

    


price = create_order('Hassaan', 10, 1500, 2000, 3000, email="aleemhassaan70@gmail.com", 
             city="Multan")

print(f"Total price: {price}")

#Lamda functions
discount_calculate = lambda price, discount: price - (price * discount)/100

total = discount_calculate(5000, 10)
print(total)

#Ternary operator
current_price = 1500
result = "Expensive" if current_price > 1000 else "Affordable"
print(result)

#Lamda and ternary operators together
check_price = lambda price: "Expensive" if price >= 1000 else "Affordable"
print(check_price(1000))

