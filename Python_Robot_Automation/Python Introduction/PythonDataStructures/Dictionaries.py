# Creating a dictionary
my_dict = {
    "name": "John",        # Key-value pair (key = "name", value = "John")
    "age": 25,             # Key-value pair (key = "age", value = 25)
    "is_student": True,    # Key-value pair (key = "is_student", value = True)
    "courses": ["Math", "Science"]  # Key-value pair (key = "courses", value = list)
}

# Accessing dictionary values by key
print(my_dict["name"])  # Output: John
print(my_dict["age"])   # Output: 25

# Using get() method (avoids KeyError if key does not exist)
print(my_dict.get("is_student"))  # Output: True
print(my_dict.get("gender", "Not Found"))  # Output: Not Found (default value)

# Modifying values in a dictionary
my_dict["age"] = 26  # Changing the value of the "age" key
print(my_dict["age"])  # Output: 26

# Adding new key-value pairs
my_dict["gender"] = "Male"  # Adding a new key "gender" with value "Male"
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'is_student': True, 'courses': ['Math', 'Science'], 'gender': 'Male'}

# Removing key-value pairs
del my_dict["is_student"]  # Removing the "is_student" key
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'courses': ['Math', 'Science'], 'gender': 'Male'}

# Using pop() to remove a key-value pair and return the value
course = my_dict.pop("courses")
print(course)  # Output: ['Math', 'Science']
print(my_dict)  # Output: {'name': 'John', 'age': 26, 'gender': 'Male'}

# Using popitem() to remove and return the last inserted key-value pair (order is maintained in Python 3.7+)
last_item = my_dict.popitem()
print(last_item)  # Output: ('gender', 'Male')
print(my_dict)  # Output: {'name': 'John', 'age': 26}

# Iterating through a dictionary (keys, values, or both)
# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through both keys and values
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Checking if a key exists in the dictionary
print("name" in my_dict)  # Output: True
print("address" in my_dict)  # Output: False

# Dictionary comprehension (creating a new dictionary)
squared_numbers = {x: x**2 for x in range(5)}
print(squared_numbers)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Merging two dictionaries (Python 3.5+)
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {**dict1, **dict2}
print(dict3)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Nested dictionaries
nested_dict = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}
print(nested_dict["student1"]["name"])  # Output: Alice
