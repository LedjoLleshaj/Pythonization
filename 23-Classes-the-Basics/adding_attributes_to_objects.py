class Guitar():
    def __init__(self): # we can use any name but it is a convention to use self
        print(f"A new guitar is being created {self}")

acoustic = Guitar()
electric = Guitar()

# acoustic.wood = "Mahogany" # works but not a good practice
# acoustic.strings = 6      # this defies the purpose of a class and the init method
# acoustic.year = 1990      # so we will transfer this to the init method

# electric.nickname = "Slayer"

# print(acoustic.wood)
