powerball_numbers = [4, 8, 15, 16, 23, 42]

def squares(numbers):
    res = []
    for num in numbers:
        res.append(num**2)
    return res

print(powerball_numbers) # [4, 8, 15, 16, 23, 42]
print(squares(powerball_numbers)) # [16, 64, 225, 256, 529, 1764]

def convert_to_floats(numbers):
    res = []
    for num in numbers:
        res.append(float(num))
    return res

print(convert_to_floats(powerball_numbers)) # [4.0, 8.0, 15.0, 16.0, 23.0, 42.0]