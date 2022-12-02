class Teacher:
    def teach_class(self):
        print("I am teaching a class")

    def grab_lunch(self):
        print("I am grabbing lunch")

    def grade_homework(self):
        print("I am grading homework")


class CollegeProfessor(Teacher):
    def publish_research(self):
        print("I am publishing research")

    # what if we redefine a method from the parent class?
    def teach_class(self):
        print("I am teaching a college class")


teacher = Teacher()
teacher.teach_class()
teacher.grab_lunch()
teacher.grade_homework()
professor = CollegeProfessor()
print("\n")
professor.teach_class()  # this is the new method from the subclass different from parent class
professor.grab_lunch()
professor.grade_homework()
professor.publish_research()
