students = ["Harry", "Ron", "Hermione"]
print(students)
athletes = students
nerds = ["Harry", "Ron", "Hermione"]
print(athletes)
print(nerds)    
print(students == athletes) # True because they are the same list
print(students == nerds) # True because the values are the same
print(students is athletes) # True because they are the same object in memory
print(students is nerds) # this is False because they are not the same object in memory
b = 3
a = 3
print("3 is 3", a is b) # True because they are the same object in memory
print("3 == 3", a == b) # True because they are the same value


a = 3.14
b = 3.14
print("3.14 and 3.14",a == b) # True because the values are the same
print("3.14 and 3.14", a is b) # True

a = "hello"
b = "hello"
print("hello",a == b) # True because the values are the same
print("hello",a is b) # True because they are the same object in memory

# python doesnt bother to create a new object for the same value
# it just points to the same object in memory
# this is called interning
# since these object are immutable in python
# and the risk of changing the value is low
