breakfast = ["eggs", "bacon", "sausage", "toast"]
lunch = ["pizza", "pasta", "salad", "nachos"]
dinner = ["steak", "chicken", "pork", "fish"]

# zip() combines two lists into a list of tuples
print(zip(breakfast, lunch)) # <zip object at 0x7f9b8c0b5c48>

# zip objects are iterable and can be converted to a list
print(list(zip(breakfast, lunch))) # [('eggs', 'pizza'), ('bacon', 'pasta'), ('sausage', 'salad'), ('toast', 'nachos')]
print(list(zip(breakfast, lunch, dinner))) # [('eggs', 'pizza', 'steak'), ('bacon', 'pasta', 'chicken'), ('sausage', 'salad', 'pork'), ('toast', 'nachos', 'fish')]

for meal in zip(breakfast, lunch, dinner):
    print(meal) # prints each tuple on a new line

print()

# zip() can also be used to iterate over multiple lists at the same time
for breakfast_item, lunch_item, dinner_item in zip(breakfast, lunch, dinner):
    print(f"I ate {breakfast_item} for breakfast, {lunch_item} for lunch, and {dinner_item} for dinner.")



