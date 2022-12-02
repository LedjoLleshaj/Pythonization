# If one class is too big, you can split it into smaller classes
# and use them as attributes of the main class
# This is called composition


class Paper:
    def __init__(self, text, case):
        self.text = text
        self.case = case


class BriefCase:
    def __init__(self, price):
        self.price = price
        self.paper = []

    def add_paper(self, paper):
        self.paper.append(paper)

    def view_notes(self):
        return [paper.text for paper in self.paper]


# this way we can use the BriefCase class as an attribute of the Lawyer class
# and separate the logic of the BriefCase class from the Lawyer class
class Lawyer:
    def __init__(self, name, briefcase):
        self.name = name
        self.briefcase = briefcase

    def add_paper(self, paper):
        self.briefcase.add_paper(paper)

    def write_notes(self, text, case):
        paper = Paper(text, case)
        self.briefcase.add_paper(paper)

    def view_notes(self):
        return self.briefcase.view_notes()


cheap_brifcase = BriefCase(10)
lawyer = Lawyer("John", cheap_brifcase)
lawyer.write_notes("I need to win this case", "Case 1")
lawyer.write_notes("I need to win this case", "Case 2")
lawyer.write_notes("I need to win this case", "Case 3")
print(lawyer.view_notes())
