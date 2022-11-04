temperatures=[10,-20,-289,100]
temperatures.sort()
print(temperatures)
#reverse order
temperatures.sort(reverse=True)
# or 
temperatures.sort()
temperatures.reverse()

# The sort() method sorts the list in place, meaning that it changes the list itself.
# The sort() method does not return a value. Instead, it changes the original list.
# Sort() method sorts the list in ascending order by default.
# You can also make it sort in descending order by passing the keyword argument reverse=True to the sort() method.
# It works for both numbers and strings.
# The sort() method is case sensitive, meaning that capital letters come before lower case letters:

