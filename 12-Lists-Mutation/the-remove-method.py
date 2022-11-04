nintendo_games = ['Super Mario Bros.', 'The Legend of Zelda', 'Metroid', 'Donkey Kong']
print(nintendo_games)

# The remove method removes the first item from a list that matches the input.
nintendo_games.remove('Metroid')
print(nintendo_games)

# The remove method only removes the first matching item.
# If there are duplicate items in a list, only the first item will be removed.
# If the item isn't in the list, a ValueError will be thrown.
# nintendo_games.remove('Contra') # ValueError: list.remove(x): x not in list