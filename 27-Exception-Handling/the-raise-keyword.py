def add_positive_numbers(x, y):
    try:
        if x <= 0 or y <= 0:
            raise ValueError("Both numbers must be positive!")
        return x + y
    except ValueError as e:
        return f"I caught ya bitch {e}"


print(add_positive_numbers(-2, 3))
print(add_positive_numbers(2, 3))
