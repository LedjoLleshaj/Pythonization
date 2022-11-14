print ("erm" in "watermelon") # True

print(10 in [1, 2, 3, 4, 5]) # False
print(10 in [1, 2, 3, 4, 5, 10]) # True

#for dictionaries, we can check if a key is in the dictionary 
pokemon = {"pikachu": "electric", "squirtle": "water", "charmander": "fire"}
print("pikachu" in pokemon) # True 
print("Pikachu" in pokemon) # False (case sensitive)
print("electric" in pokemon) # False (only checks keys)

print(pokemon.keys()) # dict_keys(['pikachu', 'squirtle', 'charmander'])
print(type(pokemon.keys())) # <class 'dict_keys'>
# print(pokemon.keys()[0]) # TypeError: 'dict_keys' object does not support indexing