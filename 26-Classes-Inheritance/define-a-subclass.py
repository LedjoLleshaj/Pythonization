class Store:
    def __init__(self):
        self.owner = "Boris"

    def exclaim(self):
        return "I'm defined in the superclass!"


class HardwareStore(Store):
    pass


home_depot = HardwareStore()
print(home_depot.owner)
print(home_depot.exclaim())
