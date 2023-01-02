import unittest

from poker.card import Card
from poker.validators import FullHouseValidator


class FullHouseValidatorTest(unittest.TestCase):
    def setUp(self):

        self.six_of_spades = Card(rank="6", suit="Spades")
        self.six_of_hearts = Card(rank="6", suit="Hearts")
        self.six_of_diamonds = Card(rank="6", suit="Diamonds")
        self.jack_of_spades = Card(rank="Jack", suit="Spades")
        self.jack_of_hearts = Card(rank="Jack", suit="Hearts")

        self.cards = [
            self.six_of_diamonds,
            self.six_of_hearts,
            self.six_of_spades,
            Card(rank="King", suit="Clubs"),
            self.jack_of_hearts,
            self.jack_of_spades,
            Card(rank="Ace", suit="Clubs"),
        ]

    def test_validates_that_cards_have_two_of_same_rank_and_three_of_another_rank(self):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.is_valid(),
            True,
        )

    def test_returns_a_list_of_cards_that_have_two_of_same_rank_and_three_of_another_rank(
        self,
    ):
        validator = FullHouseValidator(cards=self.cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                self.six_of_diamonds,
                self.six_of_hearts,
                self.six_of_spades,
                self.jack_of_hearts,
                self.jack_of_spades,
            ],
        )
