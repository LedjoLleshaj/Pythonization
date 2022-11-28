class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank} of {self.suit}"

    def __repr__(self):
        return f"Card({self.rank}, {self.suit})"

    # what is the difference between __str__ and __repr__?
    # __str__ is used for creating output for end users while __repr__ is mainly
    # used for debugging and development it is also used to
    # show the way to recreate an object

card = Card("Ace", "Spades")
print(card)
print(repr(card))