"""Decorators are used to modify or enhance the function by wrapping it with another function"""
import time

def time_decorator(func):
    def wrapper():
        print(time.time())
        func()
        print(time.time())
    return wrapper

@time_decorator
def simple_function():
    total = 0
    for i in range(100000):
        total += i
    return total


simple_function()




def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"Function ({func.__name__}) is called with args: {args}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@log_decorator
def jama(a, b):
    return a + b

@log_decorator
def salam(name):
    return(f"Assalam o Alaikum: {name}")

jama(5, 6)
salam("Hassaan")
