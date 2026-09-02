"""Dictionaries are important when doing Backend Development.
They store value as key-value pair.
- The keys must be unique
- Dictionaries are mutable.
- The items are ordered.
"""

# Syntax

demo_dict = {
    "name": "Hassaan",
    "age": 21,
    "role": "Intern"
}

print(demo_dict["name"])
print(demo_dict["age"])
print(demo_dict["role"])

# -------Dictionary Functions and Operations---------------

# Assigning a new key-value
demo_dict["qualification"] = "BS"
demo_dict["city"] = "multan"
print(demo_dict)

# Updating a value
demo_dict["qualification"] = "BS-Software Engineering"
print(demo_dict)

# Removing Data  ---- pop()
demo_dict.pop("city")
# del demo_dict["city"]
print(demo_dict)

# Retrive all the keys ---- keys()
print(demo_dict.keys())

# Retrive all the values ----- values()
print(demo_dict.values())

# Retrive key-value pairs ------ items()
print(demo_dict.items())

# Retrive the value using key ----- get()
print(demo_dict.get("qualification", "Qualification not provided"))
# if the value is not present instead of giving an error it returns None(or you can also assign whatever you want instead of none)

# Nested Dictionaries
user_profile = {
    "Name": "Hassaan",
    "age": 21,
    "job": {
        "role": "intern",
        "salary": 00,
        "department": "Backend-dev"
    }
}

print(user_profile["job"]["salary"])


"""---------Employee Management System-------"""
employee = {
    "Employee ID": "101",
    "Name": "Hassaan",
    "Age": 24,
    "Job Title": "Backend Intern",
    "Salary": 00,
    "Department": "Software Engineering",
    "Active": True
}

print(employee)
print(f"Name of employee is: {employee['Name']}")
print(f"The salary of employee is: {employee['Salary']}")
experience = input("How many number of experience do you have? ")
employee["experience"] = experience
employee["Salary"] = 1
email = input("Enter email address: ")
employee["Email"] = email

employee.pop("Active")

print(f"All the dictionary keys are: {employee.keys()}")
print(f"All the Values are: {employee.values()}")

print(f"All the key value pairs are: {employee.items()}")
print(f"Does the email exists? {"Email" in employee}")
print(f"The phone number is: {employee.get("Phone", "Phone number not provided")}")





