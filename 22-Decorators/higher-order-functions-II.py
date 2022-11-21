def calculator(operation):
    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    if operation == "add":
        return add
    else:
        return subtract

print(calculator("add")(1, 2))
print(calculator("subtract")(1, 2))


def square(x):
    return x * x

def cube(x):
    return x * x * x

def times_10(x):
    return x * 10

operations = [square, cube, times_10] # lists can contain functions since functions are objects

for func in operations:
    print(func(2))