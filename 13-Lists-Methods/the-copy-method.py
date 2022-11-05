# copy method return a shallow copy of the list
# shallow copy means that a new object is copied, but the elements inside the object are not copied
# so if the elements are mutable, they will be shared between the original and the copy
# if the elements are immutable, they will not be shared between the original and the copy
# the copy method is faster than the deepcopy method

units = ['meters', 'kilometers', 'feet', 'miles', 'yards', 'inches']
print(units)
print()

more_units = units.copy()
print(more_units)

units.remove('meters')
print(units)
print(more_units) #the copied list is not affected by the changes in the original list

even_more_units = units[:3].copy() # the copy method can be used to copy a slice of the list
print(even_more_units)

