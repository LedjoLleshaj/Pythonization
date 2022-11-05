print(["abcdefghijklmnopqrstuvwxyz".index(char) for char in "donut"])

print([number/2 for number in range(21)])

# filtering using list comprehension
# we can use the if statement to filter the list

donuts = ["jelly donut", "chocolate donut", "glazed donut"]
print([donut for donut in donuts if donut != "glazed donut"])
# it will print only if the condition is true
print([donut for donut in donuts if len(donut) <12])

# list comprehensions are a great way to filter lists when you want to
# create a new list from an existing list and you want to filter out
# some of the elements in the list and you want to apply some expression
# to each element in the list and you want to do all of this in one line
# but it has limitations, it is not always the best way to filter a list
# and it is not always the best way to create a new list from an existing list
# when you want to filter a list, you can use the filter function

