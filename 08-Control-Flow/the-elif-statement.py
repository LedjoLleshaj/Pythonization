def positive_or_negative(number):
    if number > 0:
        print("Positive")
    elif number < 0:
        print("Negative")
    else:
        print("Zero")

positive_or_negative(1)
positive_or_negative(-1)
positive_or_negative(0)
positive_or_negative(-0.5)
positive_or_negative(0.5)