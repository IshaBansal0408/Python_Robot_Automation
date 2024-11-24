# Empty list
empty_list = []
# List with elements
numbers = [1, 2, 3, 4, 5]
# Mixed data types
mixed = [1, "Python", 3.14, True]
# Nested lists
nested = [[1, 2], [3, 4], [5, 6]]
print(numbers)  # [1, 2, 3, 4, 5]
print(mixed)    # [1, "Python", 3.14, True]
print(nested)   # [[1, 2], [3, 4], [5, 6]]

numbers = [10, 20, 30, 40, 50]
print(numbers[0])   # First element: 10
print(numbers[-1])  # Last element: 50

numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[::2])   # [10, 30, 50]

# Length of a list
numbers = [1, 2, 3, 4]
print(len(numbers))  # 4
# Concatenation
list1 = [1, 2]
list2 = [3, 4]
print(list1 + list2)  # [1, 2, 3, 4]
# Repetition
print(list1 * 3)  # [1, 2, 1, 2, 1, 2]
# Membership
print(2 in list1)    # True
print(5 not in list1)  # True

numbers = [1, 2, 3, 4]
# Append: Adds an element to the end
print(numbers)  # [1, 2, 3, 4]
# Extend: Adds multiple elements
numbers.extend([5, 6])
print(numbers)  # [1, 2, 3, 4, 5, 6]
# Insert: Adds at a specific index
numbers.insert(2, 99)
print(numbers)  # [1, 2, 99, 3, 4, 5, 6]

numbers = [1, 2, 3, 4, 5]
# Remove by value
numbers.remove(3)
print(numbers)  # [1, 2, 4, 5]
# Pop by index
last_item = numbers.pop()  # Removes and returns the last item
print(last_item)  # 5
print(numbers)    # [1, 2, 4]
# Clear the list
numbers.clear()
print(numbers)  # []

numbers = [10, 20, 30, 40]
# Using a for loop
for num in numbers:
    print(num)
# Using enumerate for index and value
for index, num in enumerate(numbers):
    print(f"Index {index}: {num}")

# Generate a list of squares
squares = [x**2 for x in range(5)]
print(squares)  # [0, 1, 4, 9, 16]
# Filter even numbers
evens = [x for x in range(10) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8]

numbers = [5, 2, 9, 1, 5, 6]
# Sort in ascending order
numbers.sort()
print(numbers)  # [1, 2, 5, 5, 6, 9]
# Sort in descending order
numbers.sort(reverse=True)
print(numbers)  # [9, 6, 5, 5, 2, 1]
# Reverse the list
numbers.reverse()
print(numbers)  # [1, 2, 5, 5, 6, 9]

numbers = [1, 2, 3, 4, 2]
# Count occurrences
print(numbers.count(2))  # 2
# Find index
print(numbers.index(3))  # 2
# Copy a list
copy_numbers = numbers.copy()
print(copy_numbers)  # [1, 2, 3, 4, 2]

# Flatten a 2D list
matrix = [[1, 2], [3, 4], [5, 6]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6]

# Stack (LIFO)
stack = [10, 20]
print(stack.pop())  # 20
# Queue (FIFO)
from collections import deque
queue = deque([1, 2, 3])
queue.append(4)
print(queue.popleft())  # 1

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
zipped = list(zip(list1, list2))
print(zipped)  # [(1, 'a'), (2, 'b'), (3, 'c')]