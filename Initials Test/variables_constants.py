#Casting of Variables
#If you want to assign a specific data-type to a variable it is called casting

x = str("123")
y = int(91283)
print(x, y)

"""Variable names should not begin with
- numbers(0-9)
- should not have special characters(!@#$%)
- or should not have space in between
"""

# @variable = 123
# my variable = 123
# 1variable = 123

"""Write a simple program which takes employees detail"""
"""Employee Details"""
print("Enter Your Details: \n")
emp_name = str(input("Enter your name: "))
emp_age = int(input("Enter your age: "))
emp_profession = str(input("Enter job tilte: "))
emp_salary = int(input("Enter your salary: "))
emp_status = bool(input("Currently active? "))

print("-----Employee Profile-----")
print("Comapny: Linked Matrix\n")
print(f"Name: {emp_name}")
print(f"Age: {emp_age}")
print(f"Job Title: {emp_profession}")
print(f"Salary: {emp_salary}")
print(f"Currently Working: {emp_status}")


"""Build a simple ATM machine draft which takes
-Emp name
-Acc number
-Acc balance
-Withdrawl amount
-Is acc active or not
"""

BANK_NAME = "Habib Bank Limited"

print("-----Enter Account Detail-----")
acc_name = str(input("Enter Your Name: "))
acc_number = int(input("Enter Account Number: "))
acc_balance = int(input("Enter Account Balance: "))
amount_withdrawn = int(input("Enter the amount you have withdrawn: "))
acc_status = bool(int(input("Is your account active(0/1): ")))

print("-----Account Information-----")
print(f"Bank Name: {BANK_NAME}\n \
      Account Name: {acc_name} \
      Account Number: {acc_number}\
      Account Balance: {acc_balance}\
      Amount Withdrawn: {amount_withdrawn}\
      Account Status: {acc_status}")

