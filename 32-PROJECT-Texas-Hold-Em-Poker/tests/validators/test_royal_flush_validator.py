import unittest

from poker.card import Card
from poker.validators import RoyalFlushValidator


class RoyalFlushValidatorTest(unittest.TestCase):
    def test_figures_out_royal_flush_exists_in_collection(self):
        cards = [
            Card(rank="2", suit="Clubs"),
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
            Card(rank="Ace", suit="Clubs"),
            Card(rank="Ace", suit="Diamonds"),
        ]
        validator = RoyalFlushValidator(cards=cards)
        self.assertEqual(validator.is_valid(), True)

    def test_figures_out_royal_flush_does_not_exist_in_collection(self):
        cards = [
            Card(rank="2", suit="Clubs"),
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Diamonds"),
            Card(rank="Ace", suit="Clubs"),
            Card(rank="Ace", suit="Diamonds"),
        ]
        # we have a bug where if we have two Rank with different suits, it will return True but it should be False
        validator = RoyalFlushValidator(cards=cards)
        self.assertEqual(validator.is_valid(), False)

    def test_returns_cards_that_make_up_the_royal_flush(self):

        ten = Card(rank="10", suit="Clubs")
        jack = Card(rank="Jack", suit="Clubs")
        queen = Card(rank="Queen", suit="Clubs")
        king = Card(rank="King", suit="Clubs")
        ace = Card(rank="Ace", suit="Clubs")

        cards = [
            Card(rank="2", suit="Clubs"),
            ten,
            jack,
            queen,
            king,
            ace,
            Card(rank="Ace", suit="Diamonds"),
        ]
        validator = RoyalFlushValidator(cards=cards)
        self.assertEqual(validator.valid_cards(), [ten, jack, queen, king, ace])
