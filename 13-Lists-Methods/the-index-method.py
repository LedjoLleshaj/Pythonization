pizzas = [ 'pepperoni','Cheese', 'cheese', 'sausage', 'mushroom', 'pineapple' ]

print(pizzas.index('Cheese')) # 1
print(pizzas.index('sausage')) # 2

# The index method returns the index of the first occurrence of an item in a list.
# The index method is case sensitive.
# To overcome this, we can use the lower method to convert all the items in the list to lowercase.
# We can then use the index method to find the index of the first occurrence of a lowercase item in the list.
# Returns an error if the item is not in the list.
# So, we can use the in operator to check if the item is in the list before using the index method.


pizzas.lower()
print(pizzas.index('cheese')) # 1