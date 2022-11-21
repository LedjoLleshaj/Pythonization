def be_nice(fn):
    def inner(*args, **kwargs):
        print("I'm about to run the function you gave me!")
        print(fn(*args,**kwargs))
        print("I just ran the function you gave me!")

    return inner

@be_nice
def complex_function_sum(num1,num2):
    return num1+num2

complex_function_sum(num1=10,num2=20)



