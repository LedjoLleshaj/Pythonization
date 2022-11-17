# modules in python are just python files
# we can import them and use the functions defined in them
# we can import the whole module


creator = "Ledjo Lleshaj"
PI = 3.141592653589793
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def area_of_circle(r):
    return PI * r * r

if __name__ == "__main__":
    print("I am a module")
    print("I am not supposed to be executed directly")
