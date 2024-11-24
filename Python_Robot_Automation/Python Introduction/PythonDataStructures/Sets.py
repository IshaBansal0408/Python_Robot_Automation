# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Original Set:", my_set)  # Output: {1, 2, 3, 4, 5}

# Creating a set from a list (duplicates will be removed)
my_set_from_list = set([1, 2, 2, 3, 3, 4])
print("Set from List:", my_set_from_list)  # Output: {1, 2, 3, 4}

# Empty set (note that {} creates an empty dictionary, not a set)
empty_set = set()
print("Empty Set:", empty_set)  # Output: set()

# Accessing elements by iteration (sets are unordered)
for item in my_set:
    print("Iterating through set:", item)

# Set Operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

# Union: Combines two sets (removes duplicates)
union_set = set1 | set2  # or set1.union(set2)
print("Union of Set1 and Set2:", union_set)  # Output: {1, 2, 3, 4, 5}

# Intersection: Common elements between two sets
intersection_set = set1 & set2  # or set1.intersection(set2)
print("Intersection of Set1 and Set2:", intersection_set)  # Output: {3}

# Difference: Elements in Set1 but not in Set2
difference_set = set1 - set2  # or set1.difference(set2)
print("Difference of Set1 and Set2:", difference_set)  # Output: {1, 2}

# Symmetric Difference: Elements in either of the sets but not in both
symmetric_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference between Set1 and Set2:", symmetric_diff_set)  # Output: {1, 2, 4, 5}

# Adding elements to a set (sets do not allow duplicates)
set1.add(6)
print("Set1 after adding an element:", set1)  # Output: {1, 2, 3, 6}

# Removing elements from a set
set1.remove(6)  # Removes element 6 (raises error if element not found)
print("Set1 after removing 6:", set1)  # Output: {1, 2, 3}

# Discarding an element (does not raise an error if element is not found)
set1.discard(5)  # No error even if 5 is not in the set
print("Set1 after discarding 5:", set1)  # Output: {1, 2, 3}

# Popping an arbitrary element from a set
popped_item = set1.pop()
print(f"Popped item: {popped_item}")
print("Set1 after popping an item:", set1)

# Checking if an element is in the set
print("Is 3 in Set1?", 3 in set1)  # Output: True
print("Is 5 in Set1?", 5 in set1)  # Output: False

# Set Comprehension: Creating a new set
squares_set = {x**2 for x in range(5)}
print("Set of squares from 0 to 4:", squares_set)  # Output: {0, 1, 4, 9, 16}

# Copying a set
set_copy = set1.copy()
print("Copy of Set1:", set_copy)  # Output: {1, 2, 3}

# Clearing all elements from a set
set1.clear()
print("Set1 after clearing:", set1)  # Output: set()

# Checking if a set is a subset or superset
set2 = {3, 4, 5}
print("Is Set2 a subset of Set1?", set2.issubset({1, 2, 3, 4, 5}))  # Output: True
print("Is Set2 a superset of {3, 4}?", set2.issuperset({3, 4}))  # Output: True

# Frozen Set: Immutable version of a set
frozen_set = frozenset([1, 2, 3])
print("Frozen Set:", frozen_set)  # Output: frozenset({1, 2, 3})

# Trying to add an element to a frozen set (raises error)
# frozen_set.add(4)  # Uncommenting this will raise AttributeError: 'frozenset' object has no attribute 'add'

# Performance: Checking if an element exists in a set
my_set = {1, 2, 3, 4, 5}
print("Is 3 in my_set?", 3 in my_set)  # Output: True
