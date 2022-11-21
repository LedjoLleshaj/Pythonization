#  a higher order function is a function that takes a function as an argument
#  or returns a function as a result
#  a decorator is a higher order function that takes a function as an argument
#  and returns a function as a result

def one():
    return 1

print(type(one)) # <class 'function'> a higher order example

def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def math(a,b,func):
    return func(a,b)

print(math(2,2,add)) # 4
print(math(2,2,sub)) # 0