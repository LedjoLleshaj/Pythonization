class Emotion():
    def __init__(self,positivity,negativity):
        self.positivity = positivity
        self.negativity = negativity

    def __bool__(self):
        return self.positivity > self.negativity

my_state = Emotion(positivity=50,negativity=75)

if my_state:
    print("I'm feeling good!")
else:
    print("I'm feeling bad!")

my_state.positivity = 100

if my_state:
    print("I'm feeling good!")
else:
    print("I'm feeling bad!")