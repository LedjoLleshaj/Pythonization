# Diamond Shaped Inheritance
class FilmMaker:
    def give_interview(self):
        print("I am a film maker")


class ScreenWriter(FilmMaker):
    pass


class Director(FilmMaker):
    def give_interview(self):
        print("I am a director")


# This is a diamond shaped inheritance
# JackOfAllTrades inherits from both Director and ScreenWriter
# which both inherit from FilmMaker
# Python will remove the earlier occurrence
# of any duplicate superclasses in the hierarchy


class JackOfAllTrades(ScreenWriter, Director):
    pass


stallone = JackOfAllTrades()
stallone.give_interview()
print(JackOfAllTrades.mro())
