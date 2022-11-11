# we can shallow copy a list using the list() function or the slice operator [:] or the copy() method
# shallow copy creates a new list object in memory

a = [1, 2, 3]

b = list(a)
c = a[:]
d = a.copy()
print("a == b", a == b) # True
print("a == c", a == c) # True
print("a == d", a == d) # True
print("a is b", a is b) # False
print("a is c", a is c) # False
print("a is d", a is d) # False

numbers = [1, 2, 3]
a = [0, numbers, 4]
b = list(a)
c = a[:]
d = a.copy()
print(a)
print("a == b", a == b) # True
print("a == c", a == c) # True
print("a == d", a == d) # True
print("a is b", a is b) # False
print("a is c", a is c) # False
print("a is d", a is d) # False
print("a[1] is b[1]", a[1] is b[1]) # True 
print("a[1] is c[1]", a[1] is c[1]) # True
print("a[1] is d[1]", a[1] is d[1]) # True

numbers.append(4)
print(a)
print(b)
print("a == b", a == b) # True
print("a == c", a == c) # True
print("a == d", a == d) # True
print("a is b", a is b) # False
print("a is c", a is c) # False
print("a is d", a is d) # False
print("a[1] is b[1]", a[1] is b[1]) # True
print("a[1] is c[1]", a[1] is c[1]) # True
print("a[1] is d[1]", a[1] is d[1]) # True


# we can deep copy a list using the copy.deepcopy() function
# deep copy creates a new list object in memory and copies all the elements in the list
# deep copy is useful when we want to copy a list but dont want to change the original list
# when we change the elements in the new list, the original list is not affected

import copy
numbers_deep = copy.deepcopy(numbers)
print("numbers_deep == numbers", numbers_deep == numbers) # True
print("numbers_deep is numbers", numbers_deep is numbers) # False
print("numbers_deep[1] is numbers[1]", numbers_deep[1] is numbers[1]) # True
numbers_deep.append(5)
print(numbers_deep)
print(numbers)


