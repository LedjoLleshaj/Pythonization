employee = ("John Smith", 22, "IT", "London")

name = employee[0]
age = employee[1]
department = employee[2]
location = employee[3]
print(name, age, department, location)
# or we can unpack the tuple into variables
name, age, department, location = employee
print(name, age, department, location)

# we can also unpack the tuple into variables using the * operator
# this is useful when we don't know how many items are in the tuple
# and instead of getting a ValueError we can use the * operator
# or we don't want to unpack all the items in the tuple
name, *other = employee
print(name, other)
name, *other, location = employee
print(name, other, location)

#if we want to swap the values of two variables
a = 10
b = 20
a, b = b, a # this is called tuple unpacking

# we can also use unpacking for lists
str = ["Python", "is", "awesome"]
first, second, third = str

