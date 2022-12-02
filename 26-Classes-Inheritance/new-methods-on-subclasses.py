# the beauty of inheritance is that you can extend a class
# without modifying the original class by adding new methods
# this is called polymorphism


class Employee:
    def do_work(self):
        print("I'm working!")


class Manager(Employee):
    def waste_time(self):
        print("I'm wasting time!")


e = Employee()
m = Manager()

e.do_work()
m.do_work()
m.waste_time()


class Director(Manager):
    def fire_employee(self):
        print("You're fired!")


d = Director()
d.fire_employee()
