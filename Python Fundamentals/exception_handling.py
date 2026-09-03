"""Try, except, finally, raise"""

try:
    number = int(input("Enter number: "))
    print(f"The answer is: {100/number}")

except ZeroDivisionError:
    print("The number cannot be divided by zero")

except ValueError:
    print("Please enter correct value!")

finally:
    print("Calculation process completed.")


print("====ATM Withdrawl System====")

try:
    balance = int(input("Enter Account Balance: "))
    withdraw = int(input("Enter Withdrawl amount: "))

    if withdraw == 0:
            raise ValueError ("Withdrawl amount cannot be zero")
    elif withdraw > balance:
        raise ValueError ("Insufficient Balance")

    remaining = balance - withdraw
    print(f"Remaining Balance is: {remaining}")


except ValueError as error:
    print(error)

finally:
    print("Transaction process completed")



