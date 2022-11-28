class Student():
    def __init__(self,math,history,writing):
        self.math = math
        self.history = history
        self.writing = writing

    @property
    def grades(self):
        return self.math + self.history + self.writing

    def __eq__(self,other):
        return self.grades == other.grades

bob = Student(90,90,90)
jane = Student(100,90,80)
print(bob.grades)
print(bob == jane)
