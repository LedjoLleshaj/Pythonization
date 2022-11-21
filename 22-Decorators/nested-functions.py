# nested functions allow us to split the code into smaller pieces
# and use them in a more modular way
# nested functions are not visible outside the function they are defined in

#define a function that converts gallons to cups

def gallons_to_cups(gallons):
    def gallons_to_quarts(gallons):
        print(f'{gallons} gallons is {gallons * 4} quarts')
        return gallons * 4

    def quarts_to_pints(quarts):
        print(f'{quarts} quarts is {quarts * 2} pints')
        return quarts * 2

    def pints_to_cups(pints):
        print(f'{pints} pints is {pints * 2} cups')
        return pints * 2

    # quarts = gallons_to_quarts(gallons)
    # pints = quarts_to_pints(quarts)
    # cups = pints_to_cups(pints)
    # return cups
    return pints_to_cups(quarts_to_pints(gallons_to_quarts(gallons)))

print(gallons_to_cups(1))
