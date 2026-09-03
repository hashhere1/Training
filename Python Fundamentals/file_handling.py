file = open("Python Fundamentals/data.txt", "r")
content = file.read()
print(content)
file.close()

#Three ways of reading a file:
with open("Python Fundamentals/data.txt", "r") as file:
    content = file.read()
    print(content)

with open("Python Fundamentals/data.txt", "r") as file:
    content = file.readline()
    print(content)

with open("Python Fundamentals/data.txt", "r") as file:
    for line in file:
        print(line)

try:
    with open("Python Fundamentals/notes.txt", "w") as file:
        file.write(input("Write what you want to write "))

    with open("Python Fundamentals/notes.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File not found")



numbers = int(input("Enter how many files you want to create: "))

for number in range(numbers):
    with open(f"{number + 1}.txt", "w") as file:
        file.write(str(number + 1))
        print(number)

