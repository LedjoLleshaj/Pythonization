a = 3
b = a

print(a, b)
print(id(a), id(b))
a = 4
print(a, b)
# in this case since they are both pointing to a number object
# and numbers are immutable in Python 
# the value of a is changed but the value of b is not

# b is not changed because it is a copy of a
# a and b are pointing to different objects in memory
# a and b are not aliases of each other
# a and b are not references to the same object in memory

a = [1,2,3]
b = a
print(a, b)
print(id(a), id(b))
a.append(4)
print(a, b)
# in this case since they are both pointing to a list object
# and lists are mutable in Python
# the value of a is changed and the value of b is also changed
