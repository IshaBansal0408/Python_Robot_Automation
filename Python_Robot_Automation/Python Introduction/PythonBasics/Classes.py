class NewStyleClass:
    pass


print(isinstance(NewStyleClass(), object))  # True


class Person:
    def __init__(self, name, age):
        self.name = name  # Instance variable
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."


person1 = Person("Alice", 25)
print(person1.greet())


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def circumference(self):
        return 2 * 3.14 * self.radius


# Using instance methods
circle = Circle(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())


class Animal:
    def speak(self):
        return "I make a sound."


class Dog(Animal):
    def speak(self):
        return "Woof!"


# Using inherited and overridden methods
animal = Animal()
dog = Dog()
print(animal.speak())  # "I make a sound."
print(dog.speak())  # "Woof!"


class Bird:
    def speak(self):
        return "Tweet!"


class Cat:
    def speak(self):
        return "Meow!"


# Polymorphism in action
animals = [Bird(), Cat()]
for animal in animals:
    print(animal.speak())


class NegativeValueError(Exception):
    """Custom exception for negative values."""

    def __init__(self, value):
        super().__init__(f"Negative value not allowed: {value}")
        self.value = value


# Using the custom exception
def factorial(n):
    if n < 0:
        raise NegativeValueError(n)
    if n == 0:
        return 1
    return n * factorial(n - 1)


try:
    print(factorial(-5))
except NegativeValueError as e:
    print(e)


class ApplicationError(Exception):
    """Base class for custom exceptions."""
    pass


class DatabaseError(ApplicationError):
    """Raised for database-related errors."""
    pass


class NetworkError(ApplicationError):
    """Raised for network-related errors."""
    pass


try:
    raise NetworkError("Unable to connect to the server.")
except ApplicationError as e:
    print(f"Application error occurred: {e}")
