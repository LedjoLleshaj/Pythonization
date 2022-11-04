mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']
print(mountains)

mountains.extend(["Lhotse", "Makalu"])
print(mountains)

# The extend() method adds all the elements of an iterable (list, tuple, string etc.) to the end of the list.
# The extend() method doesn't have to return any value

mountains.extend([])
print(mountains)

lakes = ['Tanganyika', 'Victoria', 'Baikal']
print(lakes)

world = mountains + lakes # using the + operator to concatenate two lists together is the same as using the extend() method
print(world)
