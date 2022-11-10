print(all([True]))
print(all([True, True, True]))
print(all([True, True, False]))
print(all([False, False, False]))
print(all([]))
print(all([0, 1, 2, 3]))
print(all([0, 1, 2, 3, 0]))

print(any([True]))
print(any([True, True, True]))
print(any([True, True, False]))
print(any([False, False, False]))
print(any([]))
print(any([0, 1, 2, 3]))
print(any([0, 1, 2, 3, 0]))

# the function all() will return True if all elements in the list are True
# the function any() will return True if any element in the list is True