print("Hello".islower()) # false
print("hello".islower()) # true
print("hello123".islower()) # true
print("hello 123".islower()) # true
print("hello123!".islower()) # true
print("HELLO".islower()) # false
print("123".islower()) # false
print("".islower()) # false

# isupper() method
print("Hello".isupper()) # false
print("HELLO".isupper()) # true
print("HELLO123".isupper()) # true
print("HELLO 123".isupper()) # true
print("HELLO123!".isupper()) # true
print("hello".isupper()) # false
print("123".isupper()) # false
print("".isupper()) # false

# isalpha() method
print("Hello".isalpha()) # true
print("HELLO".isalpha()) # true
print("hello123".isalpha()) # false
print("hello 123".isalpha()) # false
print("hello123!".isalpha()) # false
print("".isalpha()) # false

# isalnum() method
print("Hello".isalnum()) # true
print("HELLO".isalnum()) # true
print("hello123".isalnum()) # true
print("hello 123".isalnum()) # false
print("hello123!".isalnum()) # false

# isdecimal() method
print("123".isdecimal()) # true
print("123.0".isdecimal()) # false

# isspace() method
print(" ".isspace()) # true
print("Hello".isspace()) # false
print(" ".isspace()) # true

# istitle() method
print("This Is A Title Case String".istitle()) # true
print("This Is A Title Case String!".istitle()) # true
print("This Is A Title Case String 123".istitle()) # true
print("This Is A Title Case String 123!".istitle()) # true
print("This Is NOT A Title Case String".istitle()) # false
print("This Is NOT A Title Case String!".istitle()) # false

