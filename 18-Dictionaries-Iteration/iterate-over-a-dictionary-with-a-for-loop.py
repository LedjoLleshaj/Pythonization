chinese_food = {
    "Sesame Chicken": 4.99,
    "Sweet and Sour Pork": 5.99,
    "Egg Rolls": 2.99,
}
for food in chinese_food:
    print(food) # prints only the keys

for food in chinese_food:
    print(f"{food}: ${chinese_food[food]}") # prints the keys and values

# Even though the dictionary is unordered, the for loop will always iterate over the keys in the same order.
# Best practise is to consider dictionaries as unordered and to use lists if we need to keep track of the order of the items.
 

pounds_to_kg = {
    5: 2.26796,
    10: 4.53592,
    25: 11.3398
}

# 5 pounds is 2.26796 kilograms

for pounds in pounds_to_kg:
    print(f"{pounds} pounds is {pounds_to_kg[pounds]} kilograms")

