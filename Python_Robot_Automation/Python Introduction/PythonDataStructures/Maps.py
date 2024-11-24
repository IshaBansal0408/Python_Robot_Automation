# Importing the array module
import array

# 1. Creating an array
# Syntax: array(typecode, [initial_values])
# Typecode: 'i' for integers, 'f' for floats, etc.
int_array = array.array('i', [1, 2, 3, 4, 5])  # Integer array
float_array = array.array('f', [1.1, 2.2, 3.3, 4.4])  # Float array

print("Integer Array:", int_array)  # Output: array('i', [1, 2, 3, 4, 5])
print("Float Array:", float_array)  # Output: array('f', [1.1, 2.2, 3.3, 4.4])

# 2. Accessing Array Elements
print("First element in int_array:", int_array[0])  # Output: 1
print("Last element in float_array:", float_array[-1])  # Output: 4.4

# 3. Array Methods
# Append elements to an array
int_array.append(6)
print("Array after appending 6:", int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Insert elements at a specific position
int_array.insert(2, 10)  # Inserts 10 at index 2
print("Array after inserting 10 at index 2:", int_array)  # Output: array('i', [1, 2, 10, 3, 4, 5, 6])

# Remove elements by value
int_array.remove(10)  # Removes the first occurrence of 10
print("Array after removing 10:", int_array)  # Output: array('i', [1, 2, 3, 4, 5, 6])

# Pop an element (remove and return the last element)
popped_element = int_array.pop()
print("Popped element:", popped_element)  # Output: 6
print("Array after popping an element:", int_array)  # Output: array('i', [1, 2, 3, 4, 5])

# 4. Array Length and Size
print("Length of int_array:", len(int_array))  # Output: 5

# 5. Array Slicing
# Getting a sub-array (slice) from index 1 to 3
sub_array = int_array[1:4]
print("Sliced array (1 to 3):", sub_array)  # Output: array('i', [2, 3, 4])

# 6. Array with Different Data Types
# You can create arrays of other types like 'f' (float), 'd' (double), etc.
char_array = array.array('u', ['a', 'b', 'c', 'd'])  # Array of characters
print("Character Array:", char_array)  # Output: array('u', ['a', 'b', 'c', 'd'])

# 7. Array Iteration
print("Iterating over the int_array:")
for num in int_array:
    print(num, end=" ")  # Output: 1 2 3 4 5

# 8. Array Conversion (from list)
list_data = [10, 20, 30, 40, 50]
converted_array = array.array('i', list_data)
print("\nConverted Array from List:", converted_array)  # Output: array('i', [10, 20, 30, 40, 50])

# 9. Array Conversion (to list)
array_to_list = int_array.tolist()
print("Array converted to List:", array_to_list)  # Output: [1, 2, 3, 4, 5]

# 10. Array Buffer
# Getting the memory address of an array
print("Memory address of int_array:", int_array.buffer_info())  # Output: (memory_address, size_in_bytes)

# 11. Array Extend
# Adding multiple elements to an array
int_array.extend([7, 8, 9])
print("Array after extend:", int_array)  # Output: array('i', [1, 2, 3, 4, 5, 7, 8, 9])

# 12. Array Reverse
# Reversing the array
int_array.reverse()
print("Reversed Array:", int_array)  # Output: array('i', [9, 8, 7, 5, 4, 3, 2, 1])

# 13. Array Indexing (Find position of an element)
index_of_element = int_array.index(5)
print("Index of 5 in int_array:", index_of_element)  # Output: 3

# 14. Array Equality
# Comparing arrays
array1 = array.array('i', [1, 2, 3])
array2 = array.array('i', [1, 2, 3])
print("Are array1 and array2 equal?", array1 == array2)  # Output: True
