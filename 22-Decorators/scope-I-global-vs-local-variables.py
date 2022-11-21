# a scope is a region of a program where a namespace is directly accessible
# for example, all variables that are assigned in a function belong to the local scope of that function
# and are inaccessible from the outside

age = 20 # global variable

def height():
    h =  12 # local variable
    print(h)
    print(age)

height()
# a lower scope can access variables from a higher scope, but not vice versa
# for example, the local scope of the function height() can access the global variable age

# shadow variables are local variables that have the same name as a global variable
# when a shadow variable is assigned a value, the global variable is not affected
# its not a good idea to use shadow variables

#constants are variables that are not supposed to change
#constants are usually written in all capital letters
#constants are not enforced by Python, but by convention
#constants are not supposed to be changed by the program

TAX_RATE = 0.2
def calculate_tax(price):
    return round(price * TAX_RATE,2)

def calculate_tip(price):
    return round(price * 0.1,2)

print("Tax is",calculate_tax(100))
print("Tip is",calculate_tip(100))