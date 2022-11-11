birthday = (29, 8, 2000)
print(birthday)
print(type(birthday))
print(birthday[0])
print(birthday[1])
print(birthday[2])
print(dir(birthday))
# birthday[0] = 30 # TypeError: 'tuple' object does not support item assignment


# tuples are immutable however a tuple can contain other mutable data types
# such as lists and dictionaries which can be changed.
adresses = (
    ['Street 1', 'Street 2'],
    ['City 1', 'City 2'],
)
print(adresses)
adresses[1][0] = 'City 3'  # this is possible because the list is mutable
print(adresses)
adresses[1].append('City 4')  # this is possible because the list is mutable
print(adresses)
print(type(adresses[0]))
