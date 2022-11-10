print(max([3, 2, 1, 4, 5]))
print(max([3, 2, 1, 4, -5], key=abs))

# the function max() will return the largest element in the list
# the function min() will return the smallest element in the list
print(min([3, 2, 1, 4, 5]))
print(min([3, 2, 1, 4, -5], key=abs))

# it also works with strings by returning the character with the highest/lowest ASCII value
print(max("abcde"))
print(min("abcde"))