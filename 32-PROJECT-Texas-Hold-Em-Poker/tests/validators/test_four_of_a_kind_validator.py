import unittest

from poker.card import Card
from poker.validators import FourOfAKindValidator


class FourOfAKindValidatorTest(unittest.TestCase):
    def setUp(self):

        self.six_of_spades = Card(rank="6", suit="Spades")
        self.six_of_hearts = Card(rank="6", suit="Hearts")
        self.six_of_diamonds = Card(rank="6", suit="Diamonds")
        self.six_of_clubs = Card(rank="6", suit="Clubs")

        self.cards = [
            self.six_of_clubs,
            self.six_of_diamonds,
            self.six_of_hearts,
            Card(rank="King", suit="Clubs"),
            self.six_of_spades,
            Card(rank="Ace", suit="Clubs"),
        ]

    def test_validates_that_cards_have_four_of_same_rank(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True,
        )

    def test_returns_a_list_of_cards_that_have_four_of_same_rank(self):
        validator = FourOfAKindValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.six_of_clubs,
                self.six_of_diamonds,
                self.six_of_hearts,
                self.six_of_spades,
            ],
        )
