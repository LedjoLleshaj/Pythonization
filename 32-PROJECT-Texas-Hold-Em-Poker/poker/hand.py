from poker.validators import (
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
            ("Four of a Kind", self._four_of_a_kind),
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

    def _ranks_with_count(self, count):
        return {
            rank
            for rank, rank_count in self._card_rank_counts.items()
            if rank_count == count
        }

    @property
    def _card_rank_counts(self):
        card_rank_counts = {}
        for card in self.cards:
            card_rank_counts.setdefault(card.rank, 0)
            card_rank_counts[card.rank] += 1
        return card_rank_counts

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

    def _four_of_a_kind(self):
        return len(self._ranks_with_count(4)) == 1
