# Single quotes
single_quote = 'Hello'
# Double quotes
double_quote = "World"
# Triple quotes (multi-line strings)
multi_line = '''This
is
a multi-line string.'''
print(single_quote)  # Hello
print(double_quote)  # World
print(multi_line)

string = "Python"
print(string[0])   # P
print(string[-1])  # n (last character)
print(string[0:3])   # Pyt
print(string[:4])    # Pyth
print(string[::2])   # Pto (every second character)

string = "hello World"
print(string.upper())    # HELLO WORLD
print(string.lower())    # hello world
print(string.capitalize())  # Hello world
print(string.title())       # Hello World
print(string.swapcase())    # HELLO wORLD

string = "banana"
print(string.count('a'))      # 3
print(string.find('na'))      # 2
print(string.replace('na', 'ma'))  # bamama

string = "Python3"
print(string.isalpha())   # False (contains numbers)
print("Hello".isalpha())  # True
print("123".isdigit())    # True
print("hello123".isalnum())  # True
print(" ".isspace())      # True

# Concatenation
string1 = "Hello"
string2 = "World"
print(string1 + " " + string2)  # Hello World
# Repetition
print("Python! " * 3)  # Python! Python! Python!

string = "Python"
for char in string:
    print(char)

sentence = "Python is awesome"
words = sentence.split()  # Split by whitespace
print(words)  # ['Python', 'is', 'awesome']
csv_data = "apple,banana,cherry"
fruits = csv_data.split(",")  # Split by comma
print(fruits)  # ['apple', 'banana', 'cherry']

words = ['Python', 'is', 'awesome']
sentence = " ".join(words)
print(sentence)  # Python is awesome

string = "   Hello, World!   "
print(string.strip())    # "Hello, World!" (remove spaces from both ends)
print(string.lstrip())   # "Hello, World!   " (remove leading spaces)
print(string.rstrip())   # "   Hello, World!" (remove trailing spaces)

print("Hello\nWorld")  # New line
print("Tab\tSpace")    # Tab space
print("He said, \"Python is great!\"")  # Double quotes

string = "Python"
reversed_string = string[::-1]
print(reversed_string)  # "nohtyP"

string = "madam"
is_palindrome = string == string[::-1]
print(is_palindrome)  # True

print(ord('A'))  # 65
print(chr(65))   # 'A'

