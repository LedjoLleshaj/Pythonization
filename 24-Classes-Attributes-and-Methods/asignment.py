# Declare a Musician class that accepts age and income parameters. 
class Musician():
    def __init__(self,age,income):
        self.age=age
        self.income=income
# In the instantiation process for an object, assign the two parameters
# to two attributes with the same name.

# Declare an enter_club instance method. 
# If the musician is less than 21 years old, the method should 
# return the string "Access denied!”. 
# If the musician is 21 or older, the method should
# return the string "Access granted!".
    def enter_club(self):
        if self.age <21:
            return "Access denied!"
        return "Access granted!"

# Declare a play_show instance method. The method should
# increment the musician’s income by 5.
    def play_show(self):
        self.income+=5

# EXAMPLES
#
cliff = Musician(age = 27, income = 0)
print(cliff.age)    # 27
print(cliff.enter_club())  # "Access granted!"
print(cliff.income) # 0
cliff.play_show()
print(cliff.income) # 5
cliff.play_show()
print(cliff.income) # 10

# book.py

# Let’s say we want to model a Book as a Python object. 
# A Book has an author and a publisher, which are characteristics that cannot change. 
# A Book also has a page_count, which could be altered if you rip some pages from the book.
class Book():
    def __init__(self,author,publisher,page_count):
        self._author = author
        self._publisher = publisher
        self.page_count = page_count
        
# Declare a Book class that accepts author, publisher, and page_count parameters. 
# Each of the parameters should be assigned to an attribute. 
# The author and publisher attributes should be designated as protected (use an underscore). 
# The page_count attribute should be designated public.

    def copyright(self):
        return "Copyright "+ self._author + ", " + self._publisher

# Define a copyright instance method that returns a string with information about the copyright. 
# It should look the string below, where “Grant Cardone” is the value of the protected
# author attribute and “10X Enterprises” is the value of the protected publisher attribute.

# => Copyright Grant Cardone, 10X Enterprises

# The public page_count attribute can always be manually modified. 
# However, we can still define an instance method that modifies it. 
    def rip_in_half(self):
        if self.page_count >1:
            self.page_count = self.page_count /2
        else:
            self.page_count = 0
# Declare a rip_in_half instance method. 
# If the book has more than 1 page, it should halve the page_count. 
# If the book has 1 page or less, it should set the page_count to 0.

# See sample execution below

book = Book(author = "Grant Cardone", publisher = "10X Enterprises", page_count = 10)

print(book.copyright()) # Copyright Grant Cardone, 10X Enterprises

print(book.page_count) # 10
book.rip_in_half()
print(book.page_count) # 5.0
book.rip_in_half()
print(book.page_count) # 2.5
book.rip_in_half()
print(book.page_count) # 1.25
book.rip_in_half()
print(book.page_count) # 0.625
book.rip_in_half()
print(book.page_count) # 0
book.rip_in_half()
print(book.page_count) # 0

# Declare a PizzaPie class that accepts a total_slices parameter. 
# In the instantiation process for an object, assign the parameter to an 
# attribute with the same name. 
class PizzaPie():
    def __init__(self,total_slices):
        self.total_slices = total_slices
        self._slices_eaten = 0
# A PizzaPie object should also be initialized with a _slices_eaten 
# protected attribute set to 0.
# Define a slices_eaten property. 
# The getter method should retrieve the value of the _slices_eaten attribute. 
# The setter method should set a new value for the _slices_eaten attribute
# but only if the argument is less than total_slices.

# Define a percentage property that calculates how much of the pie has been eaten 
# (the number of slices eaten divided by the total slices available). 
# The percentage property should be read-only.

# See sample execution below
#
# cheese = PizzaPie(8)
# cheese.slices_eaten = 2
# print(cheese.percentage) # 0.25
#
# cheese.slices_eaten = 4
# print(cheese.percentage) # 0.5
#
# cheese.slices_eaten = 10 # _slices_eaten should not change because there's only 8 slices in pie
# print(cheese.percentage) # 0.5
#
# ERROR - AttributeError: can't set attribute
# cheese.percentage = 0.50
    @property
    def slices_eaten(self):
        return self._slices_eaten
    
    @slices_eaten.setter
    def slices_eaten(self,slices_eaten):
        if slices_eaten < self.total_slices:
            self._slices_eaten +=slices_eaten
            
    @property
    def percentage(self):
        return self._slices_eaten / self.total_slices
    
# Define a Chocolate class that accepts and assigns a cacao_content attribute.
class Chocolate():
    def __init__(self,cacao_content):
        self.cacao_content=cacao_content
        
    
# Define a "sweet" class method that returns a 
# Chocolate object with a cacao_content value of 30.
    @classmethod
    def sweet(cls):
        return cls(cacao_content=30)
# Define a "semisweet" class method that returns a 
# Chocolate object with a cacao_content value of 50.
    @classmethod
    def semisweet(cls):
        return cls(cacao_content=50)
# Define a "bittersweet" class method that returns a 
# Chocolate object with a cacao_content value of 70.
    @classmethod
    def bittersweet(cls):
        return cls(cacao_content=70)
# Define a "bitter" class method that returns a 
# Chocolate object with a cacao_content value of 99.
    @classmethod
    def bitter(cls):
        return cls(cacao_content=99)



