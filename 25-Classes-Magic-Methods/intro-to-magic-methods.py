# magic methods are special methods that allow us to use built-in functions
# and operators with our own classes

# hooks are a procedure that intercepts a function call and allows us to
# modify the arguments or the return value

# __init__ is a constructor method that is called when an object is created
# from a class and it allows the class to initialize the attributes of a class

# __str__ is a method that is called when we try to print an object
# it returns a string representation of the object

# __len__ is a method that is called when we try to get the length of an object
# it returns the length of the object

# __add__ is a method that is called when we try to add two objects
# it returns the sum of the two objects

# __eq__ is a method that is called when we try to compare two objects
# it returns True if the objects are equal, False otherwise

print(3.3+40)
print(3.3.__add__(40))

print("h" in "hello")
print("hello".__contains__("h"))

# operator overloading is the ability of a class to define the behavior of
# operators
