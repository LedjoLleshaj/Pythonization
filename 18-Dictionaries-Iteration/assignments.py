# Declare a count_of_value function that accepts a dictionary and an integer.
# It should return a count of the number of times the integer appears 
# as a value among the dictionary’s values.
#
# EXAMPLE:
# my_dict = { "a" : 5, "b" : 3, "c" : 5 }
#
# count_of_value(my_dict, 5) => 2
# count_of_value(my_dict, 3) => 1

def count_of_value(dictionary,num):
    count = 0
    for key,value in dictionary.items():
        if value == num:
            count +=1
            
    return count

# Declare an invert function that accepts a dictionary object. 
# The function should return a new dictionary where the keys and values from the original dictionary are inverted. 
# Each key should now be a value, and each value should be a key. 
# Assume both the keys and values of the dictionary are immutable.
#
# EXAMPLE:
# my_dict = {
#   "A": "B", 
#   "C": "D",
#   "E": "F"
# }
#
# invert(my_dict) => {'B': 'A', 'D': 'C', 'F': 'E'}

def invert(dictionary):
    res = {}
    for key,value in dictionary.items():
        res[value]=key
    return res

# Declare a sum_of_values function that accepts a dictionary and a list of strings.
# The dictionary will have keys of strings and values of numbers.
#
# The function should return the sum of values for dictionary 
# keys that are also found in the list.
#
# NOTE: sum is a reserved keyword in Python. Don’t use it as a variable name.
#
# EXAMPLES:
# my_dict = { "a": 5, "b": 3, "c": 10 }
#
# sum_of_values(my_dict, ["a"])            => 5
# sum_of_values(my_dict, ["a", "c"])       => 15
# sum_of_values(my_dict, ["a", "c", "b"])  => 18
# sum_of_values(my_dict, ["z"])            => 0

def sum_of_values(dictionary,listt):
    total = 0
    for key,value in dictionary.items():
        if key in listt:
            total += value
            
    return total

# Declare a common_elements function that accepts a dictionary
# It should return a list with all of the elements that are found
# as both a key and a value in the dictionary
#
# HINT: Use the in operation to check for inclusion in a view or list object
#
# EXAMPLE:
# my_dict = {
#   "A": "K",
#   "B": "D",
#   "C": "A",
#   "D": "Z"
# }
#
# common_elements(my_dict) => ["A", "D"]

def common_elements(my_dict):
    # l = []
    # for key in my_dict.keys():
    #     if key in my_dict.values():
    #         l.append(key)
            
    # return l
    return [key for key in my_dict.keys() if key in my_dict.values()]

 # Declare a plenty_of_arguments function that accepts two parameters (a and b)
# and an additional **kwargs parameter.
#
# The function should return True if the sum of a, b, and the values of 
# **kwargs is greater than 100. It should return False otherwise.
#
# EXAMPLES:
# plenty_of_arguments(20, 30)                          => False
# plenty_of_arguments(a = 50, b = 75)                  => True
# plenty_of_arguments(a = 50, b = 25, c = 50)          => True
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 25)  => False
# plenty_of_arguments(a = 25, b = 25, c = 25, d = 26)  => True

def plenty_of_arguments(a,b,**kwargs):
    # total = 0
    # for val in kwargs.values():
    #     total += val
    
    # return (total + a + b) > 100
    return (sum(kwargs.values()) + a + b) > 100
    

# You are writing a Python program to model a remote control
# for a television set. Declare a stations_to_numbers
# function that accepts a dictionary. The keys will be
# channel numbers and the values will be the station names.
# For example...
# channels = {
#   2: "CBS",
#   4: "NBC",
#   5: "FOX",
#   7: "ABC"
# }
# The stations_to_numbers function should return an
# inverted dictionary where the keys are the station names
# and the values are the channel numbers
#
# stations_to_numbers(channels) => {'CBS': 2, 'NBC': 4, 'FOX': 5, 'ABC': 7}

def stations_to_numbers(channels):
    return {values:key for key,values in channels.items()}
    

# Declare a coaster_conversion function that accepts a dictionary
# The keys of the dictionary will be strings representing roller coasters
# The values will be the heights of each coaster in meters
#
# Return a new dictionary with the same keys.
# The values should be the heights converted from meters to feet,
# The final values (in feet) should also be rounded to the closest integer
# HINT: 1 meter is equal to 3.28084 feet
# HINT: The round function rounds a number to the nearest integer
#
# coasters = {
#   "Kingda Ka": 139,
#   "Top Thrill Dragster": 130,
#   "Superman: Escape From Krypton": 126
# }
#
# coaster_conversion(coasters) => {'Kingda Ka': 456, 'Top Thrill Dragster': 426, 'Superman: Escape From Krypton': 413}

def coaster_conversion(coasters):
    return { key:round((value*3.28084)) for key, value in coasters.items() }
    

