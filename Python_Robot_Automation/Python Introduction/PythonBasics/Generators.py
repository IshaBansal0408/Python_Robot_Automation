def my_generator():
    yield 1
    yield 2
    yield 3


gen = my_generator()
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3


# print(next(gen))  # StopIteration error

squares = (x**2 for x in range(5))
print(next(squares))  # 0
print(next(squares))  # 1

