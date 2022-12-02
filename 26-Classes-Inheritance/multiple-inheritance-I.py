# What happens when the same method is defined in both parent classes?
# Python uses the method resolution order (MRO) to determine which method to call.
# The MRO is the order in which Python looks for a method in a hierarchy of classes.
# So practically the first class argument that was passed first
class FrozenFood:
    def thaw(self, minute):
        print("Thawing the food for {} minutes".format(minute))

    def store(self):
        print("Storing the food in the freezer")


class Desert:
    def add_weight(self, weight):
        print("Adding {} grams of weight".format(weight))

    def store(self):
        print("Storing the Desert in the fridge")


class IceCream(FrozenFood, Desert):
    pass


ice_cream = IceCream()
ice_cream.thaw(10)
ice_cream.add_weight(100)
ice_cream.store()

print(IceCream.mro())
