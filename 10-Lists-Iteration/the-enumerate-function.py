errands = ["Buy milk", "Pick up dry cleaning", "Call mom"]

print(enumerate(errands)) # <enumerate object at 0x7f9b1c2b8b40> it's an object that can be iterated over with a for loop 

# enumerate() returns a tuple of the index and the value at that index
# first parameter in a for loop is the index, second is the value
for index, errand in enumerate(errands):
    print(f"{index + 1}: {errand}")

