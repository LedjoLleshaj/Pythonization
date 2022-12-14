# Part A: Instantiation

# Define a BusTrip class that is initialized with a destination, 
# a bus company, and a price for the trip. 
# Preserve the arguments as attributes on the object.
# The choice of whether to use protected attributes is up to you.
class BusTrip():
    def __init__(self,destination,company,price):
        self.destination = destination
        self.company = company
        self.price = price
        
# Part B: String Representation

# The string representation of a BusTrip object must be a string in the form of:
#    "You paid 24.99 to Greyhound to go to Boston.""
# In this example, “Boston” is the destination, “Greyhound” is the bus company, and 24.99 is the price.
# These are all fed in as arguments when a BusTrip object is initialized.

    def __str__(self):
        return f"You paid {self.price} to {self.company} to go to {self.destination}."
# Part C: Equality

# Implement equality logic between two different BusTrip objects.
# Two BusTrips object are considered equal if:
#   -- they have the same destination
#   -- their price is within 3 dollars of each other
# HINT: Use Python’s abs function to calculate the absolute value of a number.
    def __eq__(self,other):
        return self.destination == other.destination and abs(self.price - other.price) < 3
        
# Sample Execution
boston1 = BusTrip(destination = "Boston", company = "Greyhound", price = 24.99)
boston2 = BusTrip(destination = "Boston", company = "Megabus", price = 22.99)
boston3 = BusTrip(destination = "Boston", company = "Megabus", price = 49.99)
philly  = BusTrip(destination = "Philadelphia", company = "Peter Pan", price = 12.99)

print(boston1)            # You paid 24.99 to Greyhound to go to Boston.
print(boston1 == philly)  # False - different destinations
print(boston1 == boston2) # True - same destination and insignificant price difference
print(boston1 == boston3) # False - large price difference

# Define a CollegeStudent class that accepts and assigns a university attribute.
class CollegeStudent():
    """Blueprint for a student at an institution of higher learning"""
    def __init__(self,university):
        self.university = university
# Add a docstring for the class equal to "Blueprint for a student at an institution of higher learning"
    def sleep():
        """Sleep through class"""
        pass
    def eat():
        """Go to the cafeteria"""
        pass
    def party():
        """Hit the books hard"""
        pass
# Define three instance methods — sleep, eat, and party. 
# The actual content of the methods is irrelevant (feel free to use the pass keyword)

# The sleep method should have the docstring "Sleep through class".
# The eat method should have the docstring "Go to the cafeteria".
# The party method should have the docstring "Hit the books hard".

# To simplify the test evaluation, submit ALL docstrings without any line breaks.
# Example: """Sample docstring"""
# You're welcome to use single quotes, double quotes, or triple quotes.

# See sample execution below

print(CollegeStudent.__doc__) # Blueprint for a student at an institution of higher learning

marty = CollegeStudent("Python Community College") 
print(marty.sleep.__doc__) # Sleep through class
print(marty.eat.__doc__)   # Go to the cafeteria
print(marty.party.__doc__) # Hit the books hard

import collections
# Use the namedtuple function to create a GymExercise class whose instances
# will have three attributes: name, weight, and reps.
GymExercise = collections.namedtuple("GymExercise",["name","weight","reps"])
# Assign a squat variable to a GymExercise tuple object with 
# a name of “squat”, a weight of 265, and a rep count of 3.
squat = GymExercise(name="squat",weight=265,reps=3)

# Assign a bench variable to a GymExercise tuple object with 
# a name of “benchpress”, a weight of 185, and a rep count of 5.
bench = GymExercise(name="benchpress",weight=185,reps=5)
# Assign a deadlift variable to a GymExercise tuple object with
# a name of “deadlift”, a weight of 225, and a rep count of 6.
deadlift = GymExercise(name = "deadlift",weight=225,reps=6)

# Assign a press variable to a GymExercise tuple object with 
# a name of “press”, a weight of 120, and a rep count of 8.
press = GymExercise(name="press",weight=120,reps=8)

# Define a Car class that accepts a maker (string), model (string),
# and year (number) parameters and assigns them to respective
# attributes
class Car():
    def __init__(self,maker,model,year):
        self.maker = maker
        self.model = model
        self.year = year
    
        
# Define a Dealership class. Each Dealership object should instantiate
# with a "cars" attribute set to an empty list.

class Dealership():
    def __init__(self):
        self.cars = []

# A Dealership object should have a accept_delivery instance method
# that accepts a Car object and adds it to the Dealership's internal
# "cars" list
    def accept_delivery(self,car):
        self.cars.append(car)

# Indexing into a Dealership with a number should access a specific
# Car object in the Dealership.
    def __getitem__(self,index):
        return self.cars[index]

# An index position in a Dealership should also be overwriteable
# with a new Car object (see examples below)
    def __setitem__(self,index,car):
        self.cars[index]= car


f150 = Car(maker = "Ford", model = "F-150", year = 2019)
camry = Car(maker = "Toyota", model = "Camry", year = 2020)
porsche = Car (maker = "Porsche", model = "911 Carrera", year = 2021)

dealership = Dealership()

dealership.accept_delivery(f150)
dealership.accept_delivery(camry)

print(dealership[0].year) # 2019 -- the F150's year

dealership[0] = porsche

for car in dealership:
  print(car.maker) # Porsche, Toyota
# Declare a Newspaper class. 
class Newspaper():
    def __init__(self,pages,sections):
        self.pages = pages
        self.sections = sections
# Each Newspaper will have a 'pages' attribute set to an integer 
# and a 'sections' attribute set to a dictionary.
# The keys in 'sections' will be strings representing a section (i.e. "Politics") 
# and the values will be the starting page for that section (i.e. "A5").

# The length of a newspaper should be equal to the number of pages it holds.
    def __len__(self):
        return self.pages
# Indexing the newspaper by a section should return the starting pasge for that section.
    def __getitem__(self,index):
        return self.sections[index]

# Make it so two newspapers are considered equal if they have the 
# same number of pages AND the same number of sections
    def __eq__(self,other):
        return len(self.sections) == len(other.sections) and self.pages == other.pages

# EXAMPLE:
monday_sections = {
  "Politics": "A5",
  "Sports": "B2",
  "Entertainment": "C3"
}

tuesday_sections = {
  "Travel": "A5",
  "Cooking": "B2",
}

wednesday_sections = {
  "Classifieds": "A5",
  "Weddings": "B2",
  "Weather": "C3"
}

np1 = Newspaper(pages = 80, sections = monday_sections)
np2 = Newspaper(pages = 60, sections = tuesday_sections)
np3 = Newspaper(pages = 80, sections = wednesday_sections)

print(len(np1))        # 80
print(len(np2))        # 60
print(np1 == np2)      # False -- np1 has 3 sections while np2 has 2 sections
print(np1 == np3)      # True -- both have 80 pages and 3 sections
print(np1["Politics"]) # "A5"
print(np2["Cooking"])  # "B2"


