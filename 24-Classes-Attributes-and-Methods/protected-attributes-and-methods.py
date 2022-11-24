# protected attributes and methods are accessible from within the class and its subclasses
# but not from outside the class 

# Encapsulation is the process of hiding the implementation details of a class from the outside world
# and only showing the functionality to the outside world.

# Plymorhism is the ability of an object to take on many forms
# The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

# Inheritance is the ability to define a new class with little
# or no modification to an existing class.

class SmartPhone():
    def __init__(self):
        self._company = "Apple"
        self._firmware = 11

    def getFirmware(self):
        return self._firmware

    def update_firmware(self):
        self._firmware += 1


#by using the _ before the attribute name, we are making it a protected attribute
# in fact we are not changing anything accroding to the python interpreter but 
# it is a very important convention to follow in python and not use that atribute wihtout
# using some kind of api or method defined in the class and available to the public

iphone = SmartPhone()
print(iphone._company)
print(iphone._firmware)
print(iphone.getFirmware())
iphone.update_firmware()
print(iphone.getFirmware())


# this way we can access the attributes of the class and change them
# iphone._company = "Samsung"
# iphone._firmware = "Android 9.0"
# print(iphone._company)
# print(iphone._firmware)





