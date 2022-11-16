print(set([1,2,3,4,5,5,3,2,1])) # set function accepts a list
print(set((1,2,3,4,5,5,3,2,1))) # set function accepts a tuple
print(set({1,2,3,4,5,5,3,2,1})) # set function accepts a set DUH
print(set({1:2, 3:4, 5:6})) # set function accepts a dictionary, but it will only use the keys
print(set("Hello World")) # set function accepts a string, but it will only use the unique characters
