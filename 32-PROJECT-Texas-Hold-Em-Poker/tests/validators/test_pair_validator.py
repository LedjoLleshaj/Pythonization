import unittest

from poker.card import Card
from poker.hand import Hand
from poker.validators import PairValidator


class PairValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_exaclty_one_pair(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="Ace", suit="Hearts"),
        ]
        validator = PairValidator(cards=cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_a_pair_from_card_collection(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        ace_of_hearts = Card(rank="Ace", suit="Hearts")
        cards = [
            Card(rank="2", suit="Spades"),
            Card(rank="3", suit="Hearts"),
            ace_of_spades,
            ace_of_hearts,
            Card(rank="5", suit="Spades"),
        ]
        validator = PairValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [ace_of_spades, ace_of_hearts],
        )
