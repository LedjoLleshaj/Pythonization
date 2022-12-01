import time
class Garbage:
    def __del__(self):
        print("Garbage collected")

g = Garbage()
g = None # now python will collect the garbage
time.sleep(5) # wait for 5 seconds

print("End of program")
