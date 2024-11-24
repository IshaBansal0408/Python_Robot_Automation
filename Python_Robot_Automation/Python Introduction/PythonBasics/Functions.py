# Function definition
def greet(name):
    return f"Hello, {name}!"


message = greet("Alice")
print(message)


# Function with parameters
def calculate_area(length, width):
    return length * width


area = calculate_area(5, 3)
print(f"Area: {area}")


# *args for positional arguments
def add_numbers(*args):
    return sum(args)


print(add_numbers(1, 2, 3, 4))


# **kwargs for keyword arguments
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25, city="Wonderland")

# Global scope
x = 10


def modify_variable():
    global x  # Modify global variable
    x += 5
    print(f"Inside function: {x}")


modify_variable()
print(f"Outside function: {x}")


# Local scope
def local_scope():
    y = 5  # Local variable
    print(f"Inside function: {y}")


local_scope()


# print(y)  # Error: y is not defined outside the function

def multiply(a, b):
    """
    Multiplies two numbers and returns the result.

    Parameters:
        a (int or float): First number
        b (int or float): Second number

    Returns:
        int or float: The product of a and b
    """
    return a * b


# Access documentation
print(multiply.__doc__)

# Lambda function
square = lambda x: x ** 2
print(square(5))

# map() with lambda
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(squared_numbers)


import ExternalFunction
print(ExternalFunction.add(5, 3))
print(ExternalFunction.subtract(10, 4))

import math
import random
from datetime import datetime
# Math module
print(math.sqrt(16))
# Random module
print(random.randint(1, 10))
# Datetime module
print(datetime.now())

