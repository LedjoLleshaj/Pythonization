# legb rules is a way to determine the scope of a variable
# the order of precedence is:
# local scope which is the scope of the function
# enclosing functions which is the scope of the enclosing function
# global scope which is the scope of the module
# built-in scope which is the scope of the built-in functions

# x = 15 # global scope
def outer():
    #x = 1 # enclosing scope
    def inner():
        # x = 2  # local scope
        return len # len is a built-in function

    return inner()

print(outer()("hello"))

