x = 10

def change_stuff():
    global x # This is the global keyword that tells Python to use the global variable x
    x = 20

print(x)
change_stuff()
print(x)