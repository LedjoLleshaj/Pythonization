# Define an invoke_thrice function.
# It should accept a single argument (which will be a function)
# In its body, the invoke_thrice function should invoke
# the function that's passed in exactly three times.

def invoke_thrice(func):
    func()
    func()
    func()

# Define an "outer" function that accepts no arguments
# Inside the body of "outer", define an "inner" function
# The "inner" function should return the value 5.
# From "outer", return the uninvoked "inner" function

def outer():
    def inner():
        return 5
        
    return inner

# Define a global "a" variable assigned to the value 1
a = 1

# Declare a "modify_a" function that accepts a single argument.
# It should overwrite the value of the a global variable with the argument
def modify_a(arg):
    global a 
    a = arg
    
