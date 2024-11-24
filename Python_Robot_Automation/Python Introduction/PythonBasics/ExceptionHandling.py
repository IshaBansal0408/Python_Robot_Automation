try:
    # Code that might cause an exception
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")

try:
    value = int("abc")  # Raises ValueError
except ZeroDivisionError:
    print("Division by zero is not allowed.")
except ValueError:
    print("Invalid conversion to integer.")

try:
    value = int("abc")  # ValueError
    result = 10 / 0  # ZeroDivisionError
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")


# Custom Exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value not allowed: {value}")


# Function that raises the exception
def square_root(value):
    if value < 0:
        raise NegativeNumberError(value)
    return value ** 0.5


# Testing the function
try:
    result = square_root(-4)
    print(result)
except NegativeNumberError as e:
    print(e)

try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("The file was not found.")
finally:
    # Ensure resources are closed
    if 'file' in locals() and not file.closed:
        file.close()
        print("File closed.")
