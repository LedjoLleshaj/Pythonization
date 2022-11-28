class Student():
    def __init__(self,math,history,writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

################# Comparison #####################
    def __eq__(self,other):
        return self.grades == other.grades

    def __gt__(self,other):
        return self.grades > other.grades

    def __ge__(self,other):
        return self.grades >= other.grades

    def __lt__(self,other):
        return self.grades < other.grades

    def __le__(self,other): 
        return self.grades <= other.grades

    def __ne__(self,other):
        return self.grades != other.grades
################# Arithmetics ####################

    def __add__(self,other):
        return self.grades + other.grades

    def __sub__(self,other):
        return self.grades - other.grades

    def __mul__(self,other):
        return self.grades * other.grades

    def __truediv__(self,other):
        return self.grades / other.grades

    def __floordiv__(self,other):
        return self.grades // other.grades

    def __mod__(self,other):
        return self.grades % other.grades

    def __pow__(self,other):
        return self.grades ** other.grades

    

bob = Student(90,90,90)
jane = Student(100,90,80)
print(bob.grades)
print(bob == jane)
