powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    res = []
    for num in numbers:
        res.append(num**2)
    return res

print(powerball_numbers)
print(squares(powerball_numbers))

def convert_to_floats(numbers):
    res = []
    for num in numbers:
        res.append(float(num))
    return res

print(convert_to_floats(powerball_numbers))