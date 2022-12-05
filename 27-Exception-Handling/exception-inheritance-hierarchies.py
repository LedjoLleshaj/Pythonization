class Mistake(Exception):
    pass


class StupidMistake(Mistake):
    pass


class SillyMistake(Mistake):
    pass


try:
    raise StupidMistake("This is a stupid mistake")
except StupidMistake as e:
    print(f"Caught stupid mistake {e}")

try:
    raise StupidMistake("Extra stupid mistake")
except Mistake as e:
    # This will not be executed since
    # we hae a different mistake subclass which are different
    # we can fix by excepting Mistake instead of StupidMistake
    print(f"Caught mistake {e}")

# sibiling classes will not catch each others exceptions
