# 1. Print Statement
print("First print line.")  # Single Element Print
print("First element", "Second Element", True, "45", "5.3")  #Multiple Elements Print
print("Python", "is", "amazing", sep=" - ")  # Separators in Print
print("Coding is", end=" - ")  # End Parameter in Print
print("fun")
print("Her name is \"Jennie\"")  # Escape Characters

# 2. Comments in Python
# Single line comment
"""
Multi
Line
Comment
"""

# 3. Simple Input & Output
name = input("Enter your name: ")  # Input from User
print("Hello, ", name)  # Output to User

#4. Typecasting
num = int(input("Enter a number: "))  # Input from User
print("The number is:", num + 5)  # Typecasting

# 5. Different Output Formats
print(f"My name is {name} and I am {num} years old.")
print("My name is {} and I am {} years old.".format(name, num))
print("My name is %s and I am %d years old." % (name, num))
pi = 3.14159265359
print(f"Pi is approximately {pi:.2f}")
print(f"|{'centered':^10}|")
print(f"|{'left':<10}|")
print(f"|{'right':>10}|")

# 6. Operators in Python
x, y = 5, 2
print(x + y, x - y, x * y, x / y, x // y, x % y, x ** y)
print(x > y, x < y, x == y, x != y)
print(x > 0 and y > 0)
print(x > 0 or y < 0)
print(x & y, x | y, x ^ y, ~x, x << 2, x >> 2)
# print(x > 0 and y / 0)  # Short-circuiting
