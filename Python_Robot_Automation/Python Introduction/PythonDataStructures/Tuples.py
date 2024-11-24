# Empty tuple
empty_tuple = ()
# Tuple with elements
tuple1 = (1, 2, 3)
# Tuple with mixed data types
mixed_tuple = (1, "Python", 3.14, True)
# Nested tuple
nested_tuple = ((1, 2), (3, 4), (5, 6))
print(tuple1)        # (1, 2, 3)
print(mixed_tuple)   # (1, 'Python', 3.14, True)
print(nested_tuple)  # ((1, 2), (3, 4), (5, 6))

tuple1 = (10, 20, 30, 40)
print(tuple1[0])   # 10 (First element)
print(tuple1[-1])  # 40 (Last element)
print(tuple1[1:3])  # (20, 30)
print(tuple1[:2])   # (10, 20)
print(tuple1[::2])  # (10, 30)

# Length of a tuple
tuple1 = (1, 2, 3)
print(len(tuple1))  # 3
# Concatenation
tuple2 = (4, 5)
print(tuple1 + tuple2)  # (1, 2, 3, 4, 5)
# Repetition
print(tuple1 * 3)  # (1, 2, 3, 1, 2, 3, 1, 2, 3)
# Membership
print(2 in tuple1)     # True
print(6 not in tuple1)  # True

tuple1 = (10, 20, 30)
# Modify by concatenating a new value
tuple1 = tuple1 + (40,)
print(tuple1)  # (10, 20, 30, 40)

tuple1 = (10, 20, 30, 40)
# Using a for loop
for item in tuple1:
    print(item)
# Using enumerate for index and value
for index, item in enumerate(tuple1):
    print(f"Index {index}: {item}")

tuple1 = (1, 2, 3, 1, 1)
# Count occurrences of an element
print(tuple1.count(1))  # 3
# Find the index of the first occurrence
print(tuple1.index(2))  # 1

nested_tuple = (1, (2, 3), (4, 5))
# Accessing nested tuple elements
print(nested_tuple[1])   # (2, 3)
print(nested_tuple[1][0])  # 2

tuple1 = (1, 2, 3)
# Unpacking the tuple
a, b, c = tuple1
print(a, b, c)  # 1 2 3

nested_tuple = (1, (2, 3), 4)
# Unpacking the nested tuple
x, (y, z), w = nested_tuple
print(x, y, z, w)  # 1 2 3 4
