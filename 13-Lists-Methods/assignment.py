# Define an encrypt_message function that accepts a string.
# The input string will consist of only alphabetic characters.
# The function should return a string where all characters have been moved
# "up" two spots in the alphabet. For example, "a" will become "c".
#
# EXAMPLES
# encrypt_message("abc") => "cde"
# encrypt_message("xyz") => "zab"
# encrypt_message("")    => ""

def encrypt_message(string):
    alphabet = "abcdefghijklmnopqrstuvwxyzab"
    res = ""
    
    for char in string:
        res += alphabet[alphabet.index(char) + 2]
        
    return res


def encrypt_message_improved(string):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    
    for char in string:
        res += alphabet[(alphabet.index(char) + 2) % 26]
        
    return res

# Define a word_lengths function that accepts a string. 
# It should return a list with the lengths of each word.
#
# EXAMPLES
# word_lengths("Mary Poppins was a nanny")  => [4, 7, 3, 1, 5]
# word_lengths("Somebody stole my donut")   => [8, 5, 2, 5]

def word_lengths(string):
    res = []
    for el in string.split(" "):
        res.append(len(el))
        
    return res

# Define a cleanup function that accepts a list of strings.
# The function should return the strings joined together by a space.
# There's one BIG problem -- some of the strings are empty or only consist of spaces!
# These should NOT be included in the final string
#
# cleanup(["cat", "er", "pillar"])           => "cat er pillar"
# cleanup(["cat", " ", "er", "", "pillar"])  => "cat er pillar"
# cleanup(["", "", " "])                     => ""

def cleanup(list):
    
    while " " in list:
        list.remove(" ")
        
    while "" in list:
        list.remove("")
        
    return " ".join(list)
    
def cleanup_improved(list):
    # return " ".join([el for el in list if el != " " and el != ""])

    clean = []
    for el in list:
        if el != " " and el != "":
            clean.append(el)

    return " ".join(clean)


# Define a fancy_concatenate function that accepts a list of lists of strings
# The function should return a concatenated string
# The strings in a list should only be concatenated if the length of the list is 3
#
# EXAMPLES
# fancy_concatenate([["A", "B", "C"]])                        => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F"]])       => "ABCDEF"
# fancy_concatenate([["A", "B", "C"], ["D", "E", "F", "G"]])  => "ABC"
# fancy_concatenate([["A", "B", "C"], ["D", "E"]])            => "ABC"
# fancy_concatenate([["A", "B"], ["C", "D"]])                 => ""

def fancy_concatenate(list):
    res = ""
    for lis in list:
        if len(lis) == 3:
            for string in lis:
                res += string
                
    return res

# Define a nested_sum function that accepts a list of lists of numbers
# The function should return the sum of the values
# The list may contain empty lists
#
# EXAMPLES
# nested_sum([[1, 2, 3], [4, 5]])            => 15
# nested_sum([[1, 2, 3], [], [], [4], [5]])  => 15
# nested_sum([[]])                           => 0
def nested_sum(list):
    total = 0
    for lis in list:
        for num in lis:
            total += num
            
    return total

# Uncomment the commented lines of code below and complete the list comprehension logic

# The floats variable should store the floating point values 
# for each string in the values list.
values = ["3.14", "9.99", "567.324", "5.678"]
floats = [float(el) for el in values]


# The letters variable should store a list of 5 strings. 
# Each of the strings should be a character from name concatenated together 3 times.
# i.e. ['BBB', 'ooo', 'rrr', 'iii', 'sss']
name = "Boris"
letters = [char * 3 for char in name]
# letters = [char+char+char for char in name]


# The 'lengths' list should store a list with the lengths
# of each string in the 'elements' list
elements = ["Hydrogen", "Helium", "Lithium", "Boron", "Carbon"]
lengths = [len(el) for el in elements]

# Declare a destroy_elements function that accepts two lists.
# It should return a list of all elements from the first list that are NOT contained in the second list.
# Use list comprehension in your solution.
#
# EXAMPLES
# destroy_elements([1, 2, 3], [1, 2])      => [3]
# destroy_elements([1, 2, 3], [1, 2, 3])   => []
# destroy_elements([1, 2, 3], [4, 5])      => [1, 2, 3]

def destroy_elements(list1,list2):
    return [el for el in list1 if el not in list2]
