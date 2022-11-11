# tuples are immutable lists (cannot be changed)
# tuples are faster than lists
# tuples are used to store related pieces of information
# tuples are created using parentheses
# tuples are accessed using square brackets
# tuples are indexed starting at 0
# tuples can hold any data type (int, float, string, list, tuple, dictionary)
# tuples can be nested inside other tuples
# you cannot add items to a tuple or remove items from a tuple 
# you cannot sort a tuple
# you cannot change the values in a tuple
# you cannot remove a tuple
# you can find the length of a tuple
# you can use the in operator to see if an item is in a tuple
# you can use the count method to count the number of times an item appears in a tuple

foods = "pizza", "hamburger", "hotdog", "fries", "soda", "chips", "ice cream"
print(type(foods))
foods = ("pizza", "hamburger", "hot dog", "fries", "ice cream")
print(type(foods))
print(foods[0])
# tuples are created by using commas and not parentheses which serve as a visual aid
print(tuple(["pizza", "hamburger", "hot dog", "fries", "ice cream"]))
print(type((1,2)))