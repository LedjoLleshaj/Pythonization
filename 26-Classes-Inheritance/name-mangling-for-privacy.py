# to remove the possibility of name clashes between attributes in the base class and those in the derived class.
# The Python interpreter mangles the name of the attribute with a prefix _classname, where classname is the name of the class.
class Nonsense:
    def __init__(self):
        self.__some_attribute = "This is a private attribute"

    def __some_method(self):
        print("This is a private method")


class SpecialNonsense(Nonsense):
    pass


n = Nonsense()
# print(n.__some_attribute)
# n.__some_method()
sn = SpecialNonsense()
# print(sn.__some_attribute)
# sn.__some_method()

print(n._Nonsense__some_attribute)
n._Nonsense__some_method()
print(sn._Nonsense__some_attribute)
sn._Nonsense__some_method()

# this way we can access the private attributes and methods of the base class from the derived class.
# But this is not recommended as it is not a good practice to access private attributes and methods of a class from outside the class.
# So python makes it difficult to access private attributes and methods of a class from outside the class.
