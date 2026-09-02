#For loop
cart = ["Mouse", "Keyboard", "CPU", "LCD", "Motherboard"]

for product in cart:
    print(f"Product: {product}")

sales = [1500, 1200, 500, 600, 700]
total = 0

for sale in sales:
    total = total + sale

print(f"The total sale is: {total}")

for i in range(6):
    print(f"Number: {i}")

# """Simple exercise"""

prices = [1000, 2500, 5000, 7500]

for price in prices:
    discounted_price = price * 0.1
    print(f"The price after 10% dicount is: {price - discounted_price}")

#While loop with break statement

correct_pin = '1234'
pin = True
tries = 0

while pin:
    entered_pin = input("Enter your pin: ")
    if entered_pin == correct_pin:
        print("Access granted!")
        pin = False
    else:
        tries += 1
        print("Incorrect pin. Try again!")

        if tries == 3:
            print("Account locked!")
            break


# For loop with continue statement:

numbers = [10, 20, -5, 30, -10, 40]

for number in numbers:
    if number >= 0:
        print(number)
    else:
        continue
    

simple_numbers = [1, 2, 3, 4, 5]

for number in simple_numbers:
    if number < 3:
        print("Processing")
    elif number == 3:
        pass
    else:
        print("Completed")


authentic_pin = "1234"
balance = 50000
transactions = [5000, -2000, 10000, -1500, 3000]
attempts = 0

outer_loop = True

while outer_loop:
    check_pin = input("Enter your pin: ")
    if check_pin == authentic_pin:
        print("Access granted!")
        outer_loop = False

        while True:
            print("====ATM Menu====\n" 
            "1.Check Balance\n" 
            "2.Deposit\n" 
            "3.Withdraw\n" 
            "4.Transaction History\n" 
            "5.Exit")
            ask_user = int(input("Enter the number you want to perform: "))

            if ask_user == 1:
                print(f"Your current balance is: {balance}")

            elif ask_user == 2:
                deposit_amount = int(input("Enter deposit amount: "))
                if deposit_amount <=0:
                    print("Invalid amount!")
                    continue
                else:
                    balance += deposit_amount
                    print(f"New balance: {balance}")

            elif ask_user == 3:
                withdraw_amount = int(input("Enter the amount you want to withdraw: "))
                if withdraw_amount <= 0:
                    print("Invalid amount!")
                elif withdraw_amount > balance:
                    print("Insufficient balance!")
                else:
                    balance -= withdraw_amount
                    print(f"Remaining Balance: {balance}")

            elif ask_user == 4:
                for transaction in transactions:
                    if transaction > 0:
                        print(f"Transaction: +{transaction}")
                    else:
                        print(f"Transaction: {transaction}")

            elif ask_user == 5:
                print("Thank you for using our transaction service!")
                break

            else:
                pass
            

    else:
        attempts += 1
        print("Incorrect pin. Try again.")
        if attempts == 3:
            print("Account Locked!")
            break