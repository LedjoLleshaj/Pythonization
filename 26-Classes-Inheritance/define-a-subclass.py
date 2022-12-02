class Store:
    def __init__(self):
        self.owner = "Ledjo"

    def exclaim(self):
        return "I'm the best store!"


# by passing the store as a parameter, we inherit all the methods and attributes from the store class
class CoffeeShop(Store):
    pass


starbucks = CoffeeShop()

print(starbucks.owner)
print(starbucks.exclaim())
