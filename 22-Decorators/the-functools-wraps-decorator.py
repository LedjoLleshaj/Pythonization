import functools

def be_nice(fn):
    @functools.wraps(fn) # to make sure the function name and docstring are not changed
    def inner(*args, **kwargs):
        print("I'm about to run the function you gave me!")
        result = fn(*args,**kwargs)
        print("I just ran the function you gave me!")
        return result
    return inner

@be_nice
def complex_function_sum(num1,num2):
    "Adds two numbers together" 
    return num1+num2

#print(complex_function_sum(num1=10,num2=20))



help(complex_function_sum)