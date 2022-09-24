print(type(5)) # <class 'int'>
print(type(5.0)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type("Hello")) # <class 'str'>

print(type([1, 2, 3])) # <class 'list'>
print(type((1, 2, 3))) # <class 'tuple'>
print(type({1, 2, 3})) # <class 'set'>
print(type({1: "one", 2: "two", 3: "three"})) # <class 'dict'>

print(type(1 == 1)) # <class 'bool'> 
print(type(5) == type(5.0)) # <class 'bool'> False
print(type(5) == type("5")) # <class 'bool'> False

print(type(5) == int) # <class 'bool'> True
print(type(5.0) == float) # <class 'bool'> True
print(type(True) == bool) # <class 'bool'> True
print(type("Hello") == str) # <class 'bool'> True

print(type([1, 2, 3]) == list) # <class 'bool'> True
print(type((1, 2, 3)) == tuple) # <class 'bool'> True
print(type({1, 2, 3}) == set) # <class 'bool'> True
print(type({1: "one", 2: "two", 3: "three"}) == dict) # <class 'bool'> True

