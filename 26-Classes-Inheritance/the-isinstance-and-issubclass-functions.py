print(type({"a": 1}))

print(isinstance(1, int))

print(isinstance(1.2, (int, float)))  # can also pass a tuple of types

print(isinstance(1, object))  # every class in Python inherits from object


class Person:
    pass


class Student(Person):
    pass


ledjo = Student()
p = Person()

print(isinstance(ledjo, Student))  # True
print(isinstance(ledjo, Person))  # True
print(isinstance(p, Student))  # False
print(isinstance(p, Person))  # True

print(issubclass(Student, Person))  # True
print(issubclass(Person, Student))  # False
