# 1. 'if' statements
x = 10
if x > 5:
    print("x is greater than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 5")

# Inline if-else (ternary)
result = "Positive" if x > 0 else "Non-positive"
print(result)

# Assert example
assert x > 0, "x should be positive"
print("Assertion passed")
