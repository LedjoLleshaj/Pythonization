import unittest

from poker.card import Card
from poker.validators import FlushValidator


class FlushValidatorTest(unittest.TestCase):
    def setUp(self):

        self.six_of_spades = Card(rank="6", suit="Spades")
        self.two_of_spades = Card(rank="2", suit="Spades")
        self.jack_of_spades = Card(rank="Jack", suit="Spades")
        self.nine_of_spades = Card(rank="9", suit="Spades")
        self.ace_of_spades = Card(rank="Ace", suit="Spades")
        self.five_of_spades = Card(rank="5", suit="Spades")

        self.cards = [
            self.two_of_spades,
            self.five_of_spades,
            self.six_of_spades,
            self.nine_of_spades,
            self.jack_of_spades,
            Card(rank="King", suit="Clubs"),
            self.ace_of_spades,
        ]

    def test_validates_tha_five_cards_of_same_suits_exists_in_collection(self):

        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True,
        )

    def test_returns_five_highest_cards_of_same_suit(self):

        validator = FlushValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                Card(rank="5", suit="Spades"),
                Card(rank="6", suit="Spades"),
                Card(rank="9", suit="Spades"),
                Card(rank="Jack", suit="Spades"),
                Card(rank="Ace", suit="Spades"),
            ],
        )
