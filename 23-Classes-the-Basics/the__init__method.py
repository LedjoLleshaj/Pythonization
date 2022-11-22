class Guitar():
    def __init__(self): # we can use any name but it is a convention to use self
        print(f"A new guitar is being created {self}")

acoustic = Guitar()
print(acoustic) # it shows the memory address of the object wich is the same as 'self'

