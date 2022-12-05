class NegativeNumberError(Exception):
    """One or more inputs are negative"""

    pass


def add_positive_numbers(x, y):
    try:
        if x <= 0 or y <= 0:
            raise NegativeNumberError("Negative input")
        return x + y
    except NegativeNumberError:
        return "Shame on you for doing this"


print(add_positive_numbers(-5, -2))
