class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        return "{} eats {}".format(self.name, food)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # super() is used to call the parent class
        self.breed = breed


watson = Dog(
    "Watson", "Golden Retreiver"
)  # if we don't pass the name, it will throw an error
print(watson.eat("meat"))
print(watson.breed)
