candy_bars = {"Snickers", "Kit Kat", "Twix", "Milky Way", "Snickers"}
sweet_things = {"Soure Patch Kids", "Snickers", "Sour Skittles", "Milky Way"}

print(candy_bars.symmetric_difference(sweet_things)) # {'Kit Kat', 'Twix', 'Soure Patch Kids', 'Sour Skittles'}
print(candy_bars ^ sweet_things) # {'Kit Kat', 'Twix', 'Soure Patch Kids', 'Sour Skittles'}
# symemetric difference is the opposite of intersection, 
# it returns a set that contains a mix of items in both sets, 
# but not the items that are present in both sets
