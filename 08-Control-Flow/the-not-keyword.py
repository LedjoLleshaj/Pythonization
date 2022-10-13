print(not True) # False
print(not False) # True
print(not 5 > 8) # True
print(not 5 < 8) # False
print(not 5 == 5) # False
print(not 5 == 8) # True
print(not 5 != 5) # True
print(not 5 != 8) # False
print(not "cat" == "cat") # False
print(not "cat" == "dog") # True
print(not "cat" != "cat") # True
print(not "cat" != "dog") # False
print(not 5 > 8 and 3 > 2) # True
print(not 5 > 8 and 3 < 2) # False
print(not 5 < 8 and 3 > 2) # False
print(not 5 < 8 and 3 < 2) # False
print(not 5 > 8 or 3 > 2) # True
print(not 5 > 8 or 3 < 2) # True
print(not 5 < 8 or 3 > 2) # True
print(not 5 < 8 or 3 < 2) # False
print(not "cat" == "cat" and "dog" == "dawg") # False
print(not "cat" == "cat" and "dog" == "dog") # False
