def divide_five_by(number):
    try:
        return 5 / number
    except ZeroDivisionError:  # if we dont specifu any error then python will catche all the error and execute the same thing for any error
        return "You Naughty Naughty...You tried to divide by zero"
    except TypeError as e:
        return f"Mf you tried to divide by an {e}!"
    except (
        ValueError,
        NameError,
    ) as e:  # we can also catch multiple error in one except block
        return f"Error: {e}"


print(divide_five_by(0))
print(divide_five_by(2))
print(divide_five_by("a"))
