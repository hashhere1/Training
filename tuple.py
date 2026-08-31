"""Tuple is similar to list but it is immutable, meaning-once created- you cannot change it."""
#Basic Syntax

coordinates = (36.781, 42.1234)
print(coordinates)

latitude, longitude = coordinates
print(latitude)
print(longitude)

# Tuple Slicing

print(coordinates[0:1])

# --------Tuple Methods--------

# - count()

testing_tuple = ("Hassaan", "Aleem", 10, 10, 20)
print(testing_tuple.count(10))

# - index()

print(testing_tuple.index(10))

"""---Exercise---
Bank Account Details...
-Take account holder's name
-Account number
-Account type
-Current Balance
"""

name = input("Enter your name: ")
account_number = int(input("Enter account number: "))
account_type = input("Enter Account type: ")
current_balance = int(input("Enter current balance: "))

new_tuple = (name, account_number, account_type, current_balance)

print("-----Bank Account Details-----")
print(f"The details are: {new_tuple}")
print(f"Account Holder: {new_tuple[0]}")
print(f"Account number: {new_tuple[1]}")
print(f"Current Balance: {new_tuple[-1]}")
print(f"The name and number are: {new_tuple[0:2]}")
acc_name, acc_number, acc_type, curr_balance = new_tuple
print(acc_name, acc_number, acc_type, curr_balance)