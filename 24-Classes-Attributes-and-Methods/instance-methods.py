#an instance method is a method that is defined inside a class and can only be called from an instance of that class.
#Instance methods can access and modify data that belongs to the class.
#Instance methods take a special first parameter that points to the instance object. By convention, this parameter is named self.
#The self parameter is not a Python keyword; you can name it whatever you like, but it has to be the first parameter of any instance method.

class Pokemon():
    def __init__(self,name,specialty,health=100):
        self.name=name
        self.specialty=specialty
        self.health=health
    
    def roar(self):# all instance HAVE to have a self parameter
        print("Roar!!!")

    def description(self):
        print(f"I am a pokemon named {self.name} and my specialty is {self.specialty}.")

    def take_damage(self,damage):
        self.health-=damage
        print(f"{self.name} took {damage} damage and now has {self.health} health.")

squirtle = Pokemon("Squirtle","Water")
charmender = Pokemon("Charmender","Fire",110)
charmender.roar()
charmender.description()
charmender.roar()
squirtle.take_damage(10)
