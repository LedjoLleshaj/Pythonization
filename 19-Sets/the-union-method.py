candy_bars = {"Snickers", "Kit Kat", "Twix", "Milky Way", "Snickers"}
sweet_things = {"Soure Patch Kids", "Snickers", "Sour Skittles", "Milky Way"}
# union method returns a set that contains all items from both sets, duplicates are excluded obviously
print(candy_bars.union(sweet_things)) # {'Snickers', 'Kit Kat', 'Twix', 'Milky Way', 'Soure Patch Kids', 'Sour Skittles'}
# we can also use the | operator
print(candy_bars | sweet_things) # {'Snickers', 'Kit Kat', 'Twix', 'Milky Way', 'Soure Patch Kids', 'Sour Skittles'}