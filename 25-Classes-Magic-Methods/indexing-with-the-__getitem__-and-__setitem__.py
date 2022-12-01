pillows = {
    "soft": 79.99,
    "medium": 89.99,
    "hard": 99.99
}

print(pillows["soft"])
print(pillows.__getitem__("soft"))# this is what pythons does in background

class CrayonBox():
    def __init__(self):
        self.crayons = []

    def add(self, crayon):
        return self.crayons.append(crayon)

    def __getitem__(self, index):
        return self.crayons[index]

    def __setitem__(self, index, value):
        self.crayons[index] = value

cb = CrayonBox()
cb.add("red")
cb.add("blue")

print(cb.crayons)
print(cb[0]) # this wont work unless we define the __getitem__ method

cb[0] = "green" # this wont work unless we define the __setitem__ method
print(cb[0])

# we can also use the for loop to iterate over the class now that we have defined the __getitem__ method
for crayon in cb:
    print(crayon)
