# x = 10

try:
    print(x + 5)
except NameError:
    print("x is not defined")
else:
    print("This will run if there is no error in the try")
finally:
    print("this will run no matter what after the execution of the try block")
