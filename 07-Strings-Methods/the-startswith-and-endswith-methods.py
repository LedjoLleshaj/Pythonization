salutation = "Hello, how are you?"
print(salutation.startswith("Hello"))
print(salutation.startswith("hello"))
print(salutation.startswith("H"))
print(salutation.startswith("H", 1)) # start at index 1

print(salutation.endswith("?"))
print(salutation.endswith("you?"))
print(salutation.endswith("you", 0, 17)) # start at index 0, end at index 17
print(salutation.endswith("you", 0, 18)) # start at index 0, end at index 18
