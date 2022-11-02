the_simpsons = ['homer', 'marge', 'bart', 'lisa', 'maggie']

# Method 1
print(the_simpsons[::-1])
print()

# Method 2
for el in the_simpsons[::-1]:
    print(el)
print()

# Method 3
for el in reversed(the_simpsons): # reversed() returns a reversed iterator which is a generator object that can be iterated over and its a little more efficient than the slicing method
    print(el, type(reversed(the_simpsons))) # <class 'list_reverseiterator'> 




