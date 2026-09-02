"""Conditional statements allow user to make decisions based on given data
-Types:
--if
--elif
--else
"""

#Understanding by solving a basic problem

print("---University Admission Criteria---")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
if age >= 18:
    matric_marks = int(input("Enter your Matric marks/1100: "))
    if matric_marks > 1100 or matric_marks < 0:
        print("Enter the correct data!!")
    intermediate_marks = int(input("Enter your intermediate marks/1100: "))
    if intermediate_marks > 1100 or intermediate_marks < 0:
        print("Enter the correct data!!")
    entrytest_marks = int(input("Enter your entry test marks/100: "))
    if entrytest_marks > 100 or entrytest_marks < 0:
        print("Enter the correct data!!")

    total_intermediate_marks = 1100
    intermediate_percentage = (intermediate_marks/total_intermediate_marks * 100)

    print(f"Your matric marks are: {matric_marks}")
    print(f"Your intermediate marks are: {intermediate_marks}")
    print(f"Entry test marks: {entrytest_marks}")
    print(f"Intermediate percentage: {intermediate_percentage:.2f}")

    if (intermediate_percentage and entrytest_marks) < 50:
        print("You are not eligible")
    elif (intermediate_percentage and entrytest_marks) < 60:
        print("C grade")
    elif (intermediate_percentage and entrytest_marks) < 70:
        print("B grade")
    elif (intermediate_percentage and entrytest_marks) < 80:
        print("A grade")
    else:
        print("A+ grade")

else:
    print("you are not eligible")



