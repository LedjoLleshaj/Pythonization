# print(dir([]))
# # the function dir() will return a list of all attributes of the object
# # in this case, the list
print(len("pasta"))
print("pasta".__len__()) # this is the same as the above

print("st" in "pasta")
print("pasta".__contains__("st")) # this is the same as the above

print("pasta"+"sauce")
print("pasta".__add__("sauce")) # this is the same as the above

print("pasta".upper())
print("pasta".__str__().upper()) # this is the same as the above


