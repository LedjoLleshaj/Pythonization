name = "Ledjo"
sirname = "Lleshaj"
print(len(name)) # 5
print(len(sirname)) # 8
print(len(name + sirname)) # 13
print(name + sirname) # LedjoLleshaj
print(name + " " + sirname) # Ledjo Lleshaj
print(name + " " + sirname + "!") # Ledjo Lleshaj!

# name[0] = "l" # TypeError: 'str' object does not support item assignment Immutable
print(name[0]) # L

def long_word(str):
    return len(str)> 7

def first_longer_than_second(str1,str2):
    return len(str1)>len(str2)

print(long_word(name)) # False
print(long_word(sirname)) # True