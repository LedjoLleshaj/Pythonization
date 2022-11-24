# the attribute lookup order is: instance, class, superclass, metaclass

class Example():
    data = "Class Attribute"

e1 = Example()
e2 = Example()
print(e1.data)
print(e2.data)

e1.data = "Instance Attribute"
print(e1.data)
print(e2.data) # e2.data is still "Class Attribute"

del e1.data
print(e1.data) # e1.data is now "Class Attribute"
