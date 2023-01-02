from poker.validators import (
    FourOfAKindValidator,
    FullHouseValidator,
    FlushValidator,
    StraightValidator,
    ThreeOfAKindValidator,
    TwoPairValidator,
    PairValidator,
    HighCardValidator,
    NoCardsValidator,
)


class Hand:
    def __init__(self):
        self.cards = []

    def add_cards(self, cards):
        copy = self.cards[:]
        copy.extend(cards)
        copy.sort()
        self.cards = copy

    def __repr__(self):
        return (", ").join([str(card) for card in self.cards])

    @property
    def _rank_validations_from_best_to_worst(self):
        return (
            ("Royal Flush", self._royal_flush),
            ("Straight Flush", self._straight_flush),
            ("Four of a Kind", FourOfAKindValidator(self.cards).is_valid),
            ("Full House", FullHouseValidator(self.cards).is_valid),
            ("Flush", FlushValidator(self.cards).is_valid),
            ("Straight", StraightValidator(self.cards).is_valid),
            ("Three of a Kind", ThreeOfAKindValidator(self.cards).is_valid),
            ("Two Pair", TwoPairValidator(self.cards).is_valid),
            ("Pair", PairValidator(self.cards).is_valid),
            ("High Card", HighCardValidator(self.cards).is_valid),
            ("No Cards", NoCardsValidator(self.cards).is_valid),
        )

    def best_rank(self):

        for rank in self._rank_validations_from_best_to_worst:
            name, validator_function = rank
            if validator_function():
                return name

    # Validation methods
    def _royal_flush(self):
        if not self._straight_flush():
            return False

        return self.cards[0].rank == "10" and self.cards[-1].rank == "Ace"

    def _straight_flush(self):
        return (
            StraightValidator(self.cards).is_valid()
            and FlushValidator(self.cards).is_valid()
        )
