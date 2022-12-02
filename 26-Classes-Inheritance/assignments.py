# Declare a HardwareStore subclass that inherits from the Store superclass.
# Do not define any attributes and methods on the subclass.
# Use the pass keyword to avoid a class body in HardwareStore.
# Instantiate a new instance of the HardwareStore class and assign it to a home_depot variable.
# Access the value of the "owner" attribute on your HardwareStore instance.
# Invoke the exclaim instance method on your HardwareStore instance.


class Store:
    def __init__(self):
        self.owner = "Ledjo"

    def exclaim(self):
        return "I'm defined in the superclass!"


class HardwareStore(Store):
    pass


home_depot = HardwareStore()
print(home_depot.owner)
print(home_depot.exclaim())

# Define a Clothing superclass with wear and sell instance methods.
# The wear method should return the string “I'm wearing this fashionable piece of clothing!”
# The sell method should return the string “Buy my piece of clothing!”

# Define a Socks subclass that inherits from the Clothing superclass.
# It should define a lose_one instance method that
# returns the string “Where did my other one go?”
# It should override the wear method to
# return the string “Take a look at my socks! They're gorgeous!”
# It should override the sell method to
# return the string “Buy my socks!”
class Clothing:
    def wear(self):
        return "I'm wearing this fashionable piece of clothing!"

    def sell(self):
        return "Buy my piece of clothing!"


class Socks(Clothing):
    def lose_one(self):
        return "Where did my other one go?"

    def wear(self):
        return "Take a look at my socks! They're gorgeous!"

    def sell(self):
        return "Buy my socks!"


# Declare a Musician class that accepts a name argument in its initialization.
# The initialization should assign a name argument to a name attribute.
# In addition, each Musician object should have an "albums" attribute
# that begins as an empty list.
# Define a release_album instance method on a Musician that accepts a title (string).
# It should append the string to the end of the list held by the
# albums attribute (see examples below).
class Musician:
    def __init__(self, name):
        self.name = name
        self.albums = []

    def release_album(self, title):
        self.albums.append(title)


# Declare a Drummer subclass than inherits from the Musician superclass.
# In addition to a name, a drummer should also have a stamina attribute
# represented by an integer.
# The subclass should invoke the Musician superclass’s initialization procedure
# and pass it the drummer’s name.
# It should also set the stamina attribute in its own initialization process.
class Drummer(Musician):
    def __init__(self, name, stamina):
        super().__init__(name)
        self.stamina = stamina


# EXAMPLE:
lars = Drummer(name="Lars", stamina=2)
print(lars.name)  # "Lars"
print(lars.stamina)  # 2
print(lars.albums)  # []
lars.release_album("Ride the Lightning")
print(lars.albums)  # ["Ride the Lightning"]

lars.release_album("Master of Puppets")
print(lars.albums)  # ["Ride the Lightning", 'Master of Puppets']

# In this exercise, we'll be modelling a routine for proper dental health,
# which includes brushing our teeth, flossing, and using mouthwash.
# The order of these three varies from person to person.

# Declare a DentalHealthItem class. Its initialization should set a "price"
# attribute.
class DentalHealthItem:
    def __init_(self):
        self.price = 100


# Declare a Toothbrush subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Brushing the teeth"
class Toothbrush(DentalHealthItem):
    def use(self):
        return "Brushing the teeth"


# Declare a Floss subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Flossing the teeth"
class Floss(DentalHealthItem):
    def use(self):
        return "Flossing the teeth"


# Declare a Mouthwash subclass that inherits from DentalHealthItem.
# On it, define a "use" instance method that returns "Washing the teeth"
class Mouthwash(DentalHealthItem):
    def use(self):
        return "Washing the teeth"


# Instantiate an instance of a Toothbrush and assign it a "toothbrush" variable.
toothbrush = Toothbrush()
# Instantiate an instance of a Floss and assign it a "floss" variable.
floss = Floss()
# Instantiate an instance of a Mouthwash and assign it a "mouthwash" variable.
mouthwash = Mouthwash()
# Declare a "dental_health_kit" variable. It should be a list that stores the three objects.
dental_health_kit = [toothbrush, floss, mouthwash]
# Import the "random" module (see last lesson for reference).
# Invoke the "shuffle" function from the module, passing in the dental_health_kit list.
# This will mutate the list, randomizing the order of its elements.
import random

random.shuffle(dental_health_kit)
# Use list comprehension to invoke the "use" method on all three objects in "dental_health_kit".
# Assign the resulting list of strings to an "actions" variable.
actions = [action.use() for action in dental_health_kit]
