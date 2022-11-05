car_lot = ["Ford", "BMW", "Toyota", "ford"]

print(car_lot.count("Ford"))
print(car_lot.count("BMW"))

# The count method returns the number of times an item appears in a list.ù
# The count method is case sensitive.
# To overcome this, we can use the lower method to convert all the items in the list to lowercase.
# We can then use the count method to count the number of times a lowercase item appears in the list.

car_lot.lower()
print(car_lot.count("ford"))