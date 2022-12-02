class Restaurant:
    def make_reservation(self, party_size):
        print("Making a reservation for " + str(party_size) + " people.")


class Steakhouse(Restaurant):
    pass


class Bar:
    def make_reservation(self, party_size):
        print(f"Booked a lounge for {party_size}")


class BarAndGrill(Restaurant, Bar):
    pass


bag = BarAndGrill()
bag.make_reservation(10)

# Python uses a depth-first, left-to-right search when resolving methods.
# So in this case Restaurant.make_reservation() will be called.
print(BarAndGrill.mro())
