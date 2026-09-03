"""Genrator is a function that can pause and resume it's execution.
-When a generator function is called it returns a generator object which is iterator.
-The code inside the function isn't executed. It's just compiled. It's executed when you iterate over it.
--To print generator function we use:
---next()
---for loop
"""

def kuch_karo_gen():
    print("Shuru")
    yield "pehla"
    print("Darmiyan")
    yield "doosra"
    print("Khatam")
    yield "teesra"

for i in kuch_karo_gen():
    print(i)


def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(100):
    print(num)


even_gen = (i for i in range(100) if i % 2 == 0)

for numbers in even_gen:
    print(numbers)