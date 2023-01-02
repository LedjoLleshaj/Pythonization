import unittest

from poker.card import Card
from poker.validators import StraightFlushValidator


class StraightFlushValidatorTest(unittest.TestCase):
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

    def test_figures_out_that_there_are_not_five_cards_in_a_row_of_the_same_suit(self):
        cards = [
            Card(rank="2", suit="Clubs"),
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Diamonds"),
            Card(rank="6", suit="Clubs"),
            Card(rank="Ace", suit="Clubs"),
            Card(rank="King", suit="Diamonds"),
        ]
        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            False,
        )

    def test_figures_out_that_there_are_five_consecutive_cards_of_the_same_suit(self):
        cards = [
            Card(rank="2", suit="Clubs"),
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
            Card(rank="6", suit="Clubs"),
            Card(rank="Ace", suit="Clubs"),
            Card(rank="King", suit="Diamonds"),
        ]
        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.is_valid(),
            True,
        )

    def test_figures_out_that_there_are_five_consecutive_cards_of_the_same_suit(self):

        two = Card(rank="2", suit="Clubs")
        three = Card(rank="3", suit="Clubs")
        four = Card(rank="4", suit="Clubs")
        five = Card(rank="5", suit="Clubs")
        six = Card(rank="6", suit="Clubs")

        cards = [
            two,
            three,
            four,
            five,
            six,
            Card(rank="Ace", suit="Clubs"),
            Card(rank="King", suit="Diamonds"),
        ]
        validator = StraightFlushValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [
                two,
                three,
                four,
                five,
                six,
            ],
        )
