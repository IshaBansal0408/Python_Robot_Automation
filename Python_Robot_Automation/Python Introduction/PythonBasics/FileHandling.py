# Reading a file line by line
try:
    with open("example.txt", "r") as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("File not found.")


# Writing to a file
with open("example.txt", "w") as file:
    file.write("This is the first line.\n")
    file.write("This is the second line.\n")

with open("example.txt", "r") as file:
    content = file.read()
    print("Full content:", content)
    file.seek(0)  # Move the pointer to the start of the file
    print("First line:", file.readline().strip())
    file.seek(0)
    print("All lines:", file.readlines())

# Appending to a file
with open("example.txt", "a") as file:
    file.write("This is an appended line.\n")

try:
    with open("nonexistent.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("The file does not exist.")
except PermissionError:
    print("You don't have permission to access this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

with open("example.txt", "w") as file:
    file.write("The with statement handles closing the file.")
# File is automatically closed here
