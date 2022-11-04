soups = ["French Onion", "Clam Chowder", "Chicken Noodle", "Tomato"]

del soups[1] #deletes the item at index 1
print(soups) # ['French Onion', 'Chicken Noodle', 'Tomato'] 

# The del keyword can also be used to delete a slice of items from a list.
del soups[1:3] #deletes the items at index 1 and 2
print(soups) # ['French Onion']

