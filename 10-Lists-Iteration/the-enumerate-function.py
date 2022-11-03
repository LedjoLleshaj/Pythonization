errands = ["Buy milk", "Pick up dry cleaning", "Call mom"]

print(enumerate(errands)) # <enumerate object at 0x7f9b1c2b8b40> it's an object that can be iterated over with a for loop 

# enumerate() returns a tuple of the index and the value at that index
# first parameter in a for loop is the index, second is the value
for index, errand in enumerate(errands):
    print(f"{index + 1}: {errand}")

# Define an in_list function that accepts a list of strings and a separate string.
# Return the index where the string exists in the list.
# If the string does not exist, return -1.
# Do NOT use the find or index methods.
#
# EXAMPLES
# strings = ["enchanted", "sparks fly", "long live"]
# in_list(strings, "enchanted")  ==> 0
# in_list(strings, "sparks fly") ==> 1
# in_list(strings, "fifteen")    ==> -1
# in_list(strings, "love story") ==> -1

def in_list(list,sep):
    
    for i,el in enumerate(list):
        if el == sep:
            return i
            
    return -1
        
# Define a sum_of_values_and_indices function that accepts a list of numbers. 
# It should return the sum of all of the elements along with their index values.
#
# EXAMPLES
# sum_of_values_and_indices([1, 2, 3])    => (1 + 0) + (2 + 1) + (3 + 2) => 9
# sum_of_values_and_indices([0, 0, 0, 0]) => 6
# sum_of_values_and_indices([])           => 0

def sum_of_values_and_indices(list):
    total = 0
    for index,el in enumerate(list):
        total = total + index + el
        
    return total