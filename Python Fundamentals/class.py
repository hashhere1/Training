class Car:
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year

c1 = Car("Toyota", 2022)
c2 = Car("Honda", 2023)

print(c1.brand, c1.year)
print(c2.brand, c2.year)


class Student:
    #class variable
    school_name = "GCUF"

    def __init__(self, name, roll_number):
        #instance variable
        self.name = name
        self.roll_number = roll_number

s1 = Student("Hassaan", 221983)
s2 = Student("Hannan", 222222)
print(s1.school_name, s1.name, s1.roll_number)
print(s2.school_name, s2.name, s2.roll_number)


"""There are three type of methods in class.
-instance method -(uses self) -(Works on object data)
-class method (uses cls)    -(Works on class data)
-static method (no parameter)   -(Simple utility or function)
"""

class BankAccount:
    bank_name = "HBL"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def show_balance(self):
        return(f"The balance is: {self.balance}")

    @classmethod
    def change_bank(cls,new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        return (amount > 0)

BankAccount.change_bank("UBL")
print(BankAccount.bank_name)

o1 = BankAccount("Hassaan", 1000)
print(o1.bank_name, o1.balance, o1.owner, o1.is_valid_amount(600), o1.show_balance())



#Inheritance

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def show_details(self):
        return (f"Name: {self.name}, Salary: {self.salary}")

class Manager(Employee):
    def team_meeting(self):
        return (f"{self.name} is conducting a team meeting")

m1 = Manager("Ahmad", 80000)
print(m1.show_details()
      , m1.team_meeting())


#Multilevel inheritance

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        return f"My name is {self.name} "

class Student(Person):
    def study(self):
        return (f"{self.name} is studying")

class GraduateStudent(Student):
    def research(self):
        return (f"{self.name} is doing research")

g1 = GraduateStudent("Hassaan")
print(g1.introduce())
print(g1.study())
print(g1.research())

# Super()

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"{name} animal formed")

class Dog(Animal):
    def __init__(self, name, bread):
        super().__init__(name)
        self.bread = bread

d = Dog("Tommy", "Pitbull")
print(d.name)
print(d.bread)

