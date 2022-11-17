candy_bars = {"Snickers", "Kit Kat", "Twix", "Milky Way", "Snickers"}
sweet_things = {"Soure Patch Kids", "Snickers", "Sour Skittles", "Milky Way"}

print(candy_bars.difference(sweet_things)) # {'Kit Kat', 'Twix'}
print(candy_bars - sweet_things) # {'Kit Kat', 'Twix'}
# # difference method returns a set that contains the difference between two sets