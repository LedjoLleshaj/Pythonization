# intersection method returns a set that contains the similarity between two sets
candy_bars = {"Snickers", "Kit Kat", "Twix", "Milky Way", "Snickers"}
sweet_things = {"Soure Patch Kids", "Snickers", "Sour Skittles", "Milky Way"}
print(candy_bars.intersection(sweet_things)) # {'Snickers', 'Milky Way'}
# we can also use the & operator
print(candy_bars & sweet_things) # {'Snickers', 'Milky Way'}
values = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
more_values = {4,5,6,7,8,9,10,11,12,13}

print(values.intersection(more_values)) # {4, 5, 6, 7, 8, 9, 10}
print(values & more_values) # {4, 5, 6, 7, 8, 9, 10}