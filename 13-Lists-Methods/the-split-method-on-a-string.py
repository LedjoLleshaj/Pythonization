users = "Bob, Carol, Ted, Alice"
print(users.split(", ")) # ['Bob', 'Carol', 'Ted', 'Alice']
users_list = users.split(", ")
print(users_list)

#split method on a string
#the split method on a string returns a list of substrings that were separated by the given delimiter
#the delimiter is the string that is used to separate the substrings
#the delimiter is not included in the returned list
#the delimiter can be a single character or a string of characters
#the delimiter can be a space, a comma, a period, a dash, a slash, etc.
#it returns a list of substrings that were separated by the given delimiter
# the second argument is the maximum number of splits that will be performed
# if the second argument is not provided, all the splits will be performed

                                                #one element
print(users.split(", ", 2)) # ['Bob', 'Carol', 'Ted, Alice']
