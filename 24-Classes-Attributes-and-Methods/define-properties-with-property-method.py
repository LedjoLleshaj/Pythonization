# we are going to use the dot syntax to access the property value but 
# internally the property method will call the getter and setter methods
# to get and set the value of the property

class Height():
    def __init__(self,feet):
        self._inches = feet * 12

    def _get_feet(self):
        return self._inches / 12

    def _set_feet(self,feet):
        if feet >=0:
            self._inches = feet * 12

    feet = property(_get_feet,_set_feet) # this is the property method which takes 3 arguments: getter, setter and deleter

h = Height(5)
print(h.feet) # this will call the getter method since there is no feet attribute in Height
# it has the name of the property so if we changed feet in line 16 to height then we would have to call h.height

h.feet = 6 # this will call the setter method since we are trying to set the value of the property
print(h.feet)

h.feet = -1 # this will not change the value of the property since the setter method will not allow it

# We ave to be careful to have different names for the property and the attribute or it can cause problems like recursion
# we can also use the property method to create a read only property
