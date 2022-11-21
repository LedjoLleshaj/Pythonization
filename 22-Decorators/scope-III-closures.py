# scope closure is a function that remembers the variables from the scope in which it was created
# even if the scope is no longer present

def outer_func():
    message = 'Hi'
    def inner_func():
        return message
    return inner_func

the_func = outer_func() # the_func is a closure function
print(the_func()) # even though the outer_func() is no longer present, the_func remembers the message variable

