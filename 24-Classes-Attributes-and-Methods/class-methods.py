#classmethods are used to create a method that is bound to the class rather than
#the object of the class. They have the access to the state of the class as it
#takes a class parameter that points to the class and not the object instance.
#They can modify a class state that would apply across all the instances of the

class SushiPlatter():
    def __init__(self,salmon,tuna,shrimp,squid):
        self.salmon = salmon
        self.tuna = tuna
        self.shrimp = shrimp
        self.squid = squid

    @classmethod
    def lunch_special_A(cls): # class method that returns a SushiPlatter object
        return cls(salmon=5,tuna=5,shrimp=5,squid=5)

    @classmethod
    def tuna_lover(cls):
        return cls(salmon=0,tuna=10,shrimp=0,squid=0)

    

ledjo = SushiPlatter(salmon=8,tuna=6,shrimp=10,squid=4)
print(ledjo.salmon)

lunch_eater = SushiPlatter.lunch_special_A()
print(lunch_eater.salmon)
tuna_lover = SushiPlatter.tuna_lover()
print(tuna_lover.tuna)

