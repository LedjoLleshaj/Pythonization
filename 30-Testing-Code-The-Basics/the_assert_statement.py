def add(x, y):
    assert isinstance(x, int) and isinstance(y, int), "x and y must be integers"
    return x + y


print(add(3, 5))
print(add(3, "5"))  # AssertionError: x and y must be integers
