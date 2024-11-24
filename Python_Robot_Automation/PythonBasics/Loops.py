# While Loop
count = 0
while count < 5:
    print(f"Count is {count}")
    count += 1  # Increment to avoid infinite loop

# For Loop
colors = ["red", "blue", "green"]
for color in colors:
    print(color)

# Iterating over a string
for char in "Python":
    print(char)

# range(start, stop, step)
for i in range(1, 10, 2):  # Odd numbers from 1 to 9
    print(i)

# Hidden Concept: Reverse range
for i in range(10, 0, -1):  # Count down from 10
    print(i)

# break example
for i in range(5):
    if i == 3:
        break  # Exit the loop
    print(i)

# continue example
for i in range(5):
    if i == 3:
        continue  # Skip the rest of the code for this iteration
    print(i)

# Loop with Assertions
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    assert num > 0, "All numbers must be positive"
    print(num)
