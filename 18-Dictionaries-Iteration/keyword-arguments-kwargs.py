def length(word):
    return len(word)

print(length('hello'))

#print(length(word = 'hello' argument = 'hello'))# TypeError: length() got an unexpected keyword argument 'argument'

# what if we want python to accept any number of arguments?
# we can use **kwargs
# **kwargs is a dictionary
# now we can pass any number of arguments
def collect_keywords(**kwargs):
    print(kwargs) # this is a dictionary
    print(type(kwargs)) # this is a dictionary

collect_keywords(name = 'John', age =13, height = 5.5)

# we can also pass a dictionary
# we can use ** to unpack the dictionary


# *args vs **kwargs
# *args is used to pass a non-keyworded, variable-length argument list
# **kwargs is used to pass a keyworded, variable-length argument list
# *args creates a tuple of arguments while **kwargs creates a dictionary of arguments

def args_and_kwargs(*args, **kwargs):
    print(args)
    print(kwargs)

args_and_kwargs(1, 2, 3, name = 'John', age = 13, height = 5.5)
# args must come before kwargs
# python will throw an error if we do not follow this rule
