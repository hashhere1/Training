"""Sets are
-unorderd
-no duplicates(one item appears only one time)
-mutable(Only add or remove an item)
-unchangeable(Can change the values in the set)
-Can store different data types
"""
# Syntax
numbers = {10, 20, 30, 10}
print(numbers)

# IMP(Creating empty set)
empty_set = set() # Correct way
empty_set = {}  #Creates an empty dictionary

# Set Functions

skills = {"Python", "Django", "FastAPI", }

# - add()
skills.add("python")
print(skills)

# - remove()
skills.remove("python")
print(skills) # remove() raises an error if the item doesn't exist

# - discard()
skills.discard("Python")
print(skills)   # discard() doesn't raise an error when the item isn't present

# - pop()
skills.pop()
print(skills) # remove an arbitary item

# - clear()
skills.clear()
print(skills) # clears the set and returns an empty set


# -------------SET OPERATIONS------------

python_students = {"Hassaan", "Usama", "Hannan"}
django_students = {"Hassaan", "Inam", "Haroon", "Azam"}

# UNION
print(python_students | django_students) # combines both sets and write down all the values

# INTERSECTION
print(python_students & django_students)

# DIFFERENCE
print(python_students - django_students)

# SYMETRIC DIFFERENCE
print(python_students ^ django_students) # Students who are in one set but not in other


"""Exercise regarding sets
You're building a system for a software company.
Ask the user to enter 5 different skills they know, one at a time.
Store them in a set.

Then:

Print the complete set.
Print how many unique skills they entered.
Ask the user for another skill and add it using add().
Ask the user for a skill to remove and use discard().
Create another set containing these required company skills:
required_skills = {"python", "git", "sql"}
Find which required skills the employee already has using intersection.
Find which required skills the employee is missing using difference.
Check whether "python" is in the employee's skills.
"""

print('Software Company System')
print("Enter five different skills: ")
skill_1 = input("Enter first skill: ").lower()
skill_2 = input("Enter second skill: ").lower()
skill_3 = input("Enter third skill: ").lower()
skill_4 = input("Enter fourth skill: ").lower()
skill_5 = input("Enter fifth skill: ").lower()

skill_set = {skill_1, skill_2, skill_3, skill_4, skill_5}

print(f"The complete skill set is: {skill_set}")
print(f"Unique skills that you entered: {len(skill_set)}")

additional_skill = input("Add another skill: ").lower()
skill_set.add(additional_skill)
print(f"{additional_skill} added")

removing_skill = input("Enter a skill you want to remove: ").lower()
skill_set.discard(removing_skill)
print(f"{removing_skill} removed")

required_skills = {"python", "git", "sql"}

print(f"The skills you already have are: {required_skills & skill_set}")
print(f"The skills that you are missing are: {required_skills - skill_set}")
print(f"Is python in your skills: {'python' in skill_set}")

