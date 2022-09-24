print(int(3.9)) # 3 removes the decimal
print(int("3")) # 3 converts the string to an integer
print(int("3.9")) # ValueError: invalid literal for int() with base 10: '3.9'
print(int(True)) # 1 converts the boolean to an integer
print(int(False)) # 0 converts the boolean to an integer
print(int("Hello")) # ValueError: invalid literal for int() with base 10: 'Hello'

print(float(3)) # 3.0 converts the integer to a float
print(float("3")) # 3.0 converts the string to a float
print(float("3.9")) # 3.9 converts the string to a float
print(float(True)) # 1.0 converts the boolean to a float
print(float(False)) # 0.0 converts the boolean to a float
print(float("Hello")) # ValueError: could not convert string to float: 'Hello'

print(str(3)) # '3' converts the integer to a string
print(str(3.9)) # '3.9' converts the float to a string
print(str(True)) # 'True' converts the boolean to a string
print(str(False)) # 'False' converts the boolean to a string

print(bool(3)) # True converts the integer to a boolean
print(bool(3.9)) # True converts the float to a boolean
print(bool(0)) # False converts the integer to a boolean
print(bool(0.0)) # False converts the float to a boolean
print(bool("Hello")) # True converts the string to a boolean
print(bool("")) # False converts the string to a boolean

print(str(6) + "9" ) # '69' 
print(int("6") + 9) # 15
print(float("6") + 9) # 15.0  (float + int = float)
print (4 + 2.9) # 6.9 (float + int = float) automatic conversion
