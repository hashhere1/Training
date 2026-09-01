"""All about lists"""

# Lists are the datatypes that are used to store multiple values in a single variable.
# - These are mutable
# - Ordered
# - Can contain multiple data types
# - Allow duplicates

#Creating a list

example_list = ["Banana", "Cherry", "Apple"]
example_alphanumberic_list = ["Hassaan", 21, 3.41, "GCUF"]

print(example_alphanumberic_list[0]) #Accessing the elements in list
print(example_alphanumberic_list[0:2]) #List slicing
print(example_alphanumberic_list[::-1]) #Reversing a list
print(example_list[-1:])
example_list[2] = "Mango"
print(example_list)

# ---------List Operations----------
# append()
list_appending = ["Wire", "Mouse", "Computer"]
list_appending.append("LCD") # Adds an item on the last of list
print(list_appending) 

# insert()
list_inserting = ["Hassaan", "Hannan", "Inam"]
list_inserting.insert(1, "Mannan") # Insert value at any index inside a list
print(list_inserting)

# remove()
list_removing = ['Hassaan', 'Mannan', 'Hannan', 'Inam']
list_removing.remove("Mannan") # Remove an item by it's value
print(list_removing)

# pop()
list_pop = ['Hassaan', 'Mannan', 'Hannan', 'Inam']
list_pop.pop(1) # Removes items using index. If we don't write anything inside pop() it automatically removes last item from the list.
print(list_pop)

# sort()
list_sorting = [1500, 200, 500, 700]
list_sorting.sort() # sorts list in assending order
print(list_sorting)

list_sorting.sort(reverse=True) # sorts list in decending order
print(list_sorting)

# reverse()
list_reversing = ["Hassaan", "Hannan", "Inam"]
list_reversing.reverse() # Reverses the list
print(list_reversing)

# count()
list_counting = ["apple", "banana", "apple", "apple", "mango"]
print(list_counting.count("apple")) # counts the occurance of an item

# index()
list_index = ["mango", "apple"]
print(list_index.index("mango")) # returns the index of item

# extend()
list_extend = ["Hello", 'Morning', "Night"]
list_extend.extend(["Noon", "After-noon"]) # adds multiple items to different index on list(different then append)
print(list_extend)

"""Take input from a user and store it in list"""

carts = []
product_1 = str(input('Enter first product: ')).lower()
carts.append(product_1)
product_2 = str(input("Enter second product: ")).lower()
carts.append(product_2)
product_3 = str(input("Enter third product: ")).lower()
carts.append(product_3)
product_4 = str(input("Enter fourth product: ")).lower()
carts.append(product_4)
product_5 = str(input("Enter fifth product: ")).lower()
carts.append(product_5)
print(f"The products in the cart are: {carts}")
print(f"Number of products in the cart are: {len(carts)}")
remove_product = (input("Type the product you want to remove: ")).lower()
carts.remove(remove_product)

product_6 = (input("Enter one more product: ")).lower()
carts.append(product_6)
print(carts)

checking_item = ("laptop" in carts)
print(f"Does the cart include Laptop? {checking_item}")