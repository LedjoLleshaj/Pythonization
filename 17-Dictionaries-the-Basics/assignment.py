# Create an empty dictionary and assign it to the variable empty.
empty = {}
# Create a dictionary with three key-value pairs. 
# The keys should be strings and the values should be integer values. 
# Assign the dictionary to a my_dict variable.
my_dict = {"one":1,"two":2,"three":3}
# A dictionary’s keys can be any immutable data structure. 
# Create a dictionary with two key-value pairs and assign it to
# a winning_lottery_numbers variable. 
# Both of the keys should be tuples. 
# One of the values should be True, the other value should be False.
winning_lottery_numbers = {(1,2,3,4):True,(1,2):False}


# Define a to_dictionary function that accepts a list of strings. 
# The function should return a dictionary where the keys are the strings 
# and the values are their original index positions in the list.
#
# EXAMPLE:
# detectives = ["Sherlock Holmes", "Hercule Poirot", "Nancy Drew"]
# to_dictionary(detectives) => {'Sherlock Holmes': 0, 'Hercule Poirot': 1, 'Nancy Drew': 2}
def to_dictionary(list1):
    rdict = {}
    for index,el in enumerate(list1):
        rdict[el] = index
        
    return rdict

# Define a length_counts function that accepts a list of strings. 
# The function should return a dictionary where the keys represent
# length and the values represent how many strings have that length.
#
# EXAMPLE:
# sa_countries = ["Brazil", "Venezuela", "Argentina", "Ecuador", "Bolivia", "Peru"]
# length_counts(sa_countries) => # {6: 1, 9: 2, 7: 2, 4: 1}
# There is 1 string with 6 letters, 2 strings with 9 letters, 
# 2 strings with 7 letters, and 1 string with 4 letters.

def length_counts(list1):
    count = {}
    for el in list1:
        if len(el) in count:
            count[len(el)] += 1
        else:
            count[len(el)] = 1
    return count

# Declare a delete_keys function that accepts two arguments:
# a dictionary and a list of strings. 
# For each string in the list, if the string exists as a dictionary key, 
# delete the key-value pair from the dictionary. 
#
# If the string does not exist as a dictionary key, avoid an error. 
# The return value should be the modified dictionary object.
#
# EXAMPLE:
# my_dict = {
#   "A": 1,
#   "B": 2,
#   "C": 3
# }
#
# strings = ["A", "C"]
# delete_keys(my_dict, strings) => {'B': 2}

def delete_keys(dic,list1):
    for el in list1:
        if el in dic:
            del dic[el]
    
    return dic
    
