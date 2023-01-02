from poker.validators import StraightFlushValidator


class RoyalFlushValidator:
    def __init__(self, cards):
        self.cards = cards

    def is_valid(self):
        if not StraightFlushValidator(self.cards).is_valid():
            return False

        return self.cards[-1].rank == "Ace"

    def valid_cards(self):
        return StraightFlushValidator(self.cards).valid_cards()
