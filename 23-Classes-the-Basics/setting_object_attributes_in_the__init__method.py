class Guitar():
    # def __init__(self): # this way all the guitars will have the same qualities
        # self.wood = "Mahogany" 
        # self.strings = 6
        # self.year = 1990

    def __init__(self, wood, strings, year):
        self.wood = wood
        self.strings = strings
        self.year = year




acoustic = Guitar("Mahogany", 6, 1990)
electric = Guitar("Maple", 6, 2010)

print(acoustic.wood)
print(electric.wood)
print(acoustic.wood==electric.wood) # False. would print true if its the same even thought the objects are different


# baritone = Guitar() # this will give an error because we have not defined the attributes in the init method