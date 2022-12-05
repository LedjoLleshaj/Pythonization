def divide_five_by(number):
    try:
        return 5 / number
    except ZeroDivisionError:
        return "You Naughty Naughty...You tried to divide by zero"


print(divide_five_by(0))
print(divide_five_by(2))
