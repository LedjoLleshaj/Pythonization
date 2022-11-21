def be_nice(fn):
    def inner():
        print("I'm about to run the function you gave me!")
        fn()
        print("I just ran the function you gave me!")

    return inner

def complex_function():
    print("I'm a complex function!")

be_nice(complex_function)()
# or we can use the @ symbol to decorate a function:
@be_nice
def complex_function2():
    print("I'm a complex function!")


complex_function2()


# This is the decorator syntax
# so what is a decorator?
# A decorator is a function that takes another function as an argument
# and returns another function
# The function that is passed in as an argument is called the decorated function
# The function that is returned is called the wrapper function
