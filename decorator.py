# import functools
# import time

# def greet():
#     return "Hello!"

# say_hi = greet
# print(say_hi())

# def run_t(func):
#     func()
#     func()

# print(run_t(greet))

# def make_greeter(name):
#     def greet():
#         return f"Hello, {name}!"
#     return greet

# hello_john = make_greeter("John")
# print(hello_john())

from functools import wraps

# def shout(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         print(">>> stop the action")
#         result = func(*args, **kwargs)
#         print(">>> stop the action")
#     return wrapper



# @shout
# def greet(name):
#     print("Hello, {name}")


# greet("Alice")

import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f"{func.__name__} took {end - start:.4f}s")
        return result
    return wrapper



@timer
def process_data(n):
    return sum(range(n))

process_data(1_000_000)