import unittest

from poker.card import Card

from poker.validators import HighCardValidator

class HighCardValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_a_high_card(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="3", suit="Clubs"),
        ]
        validator = HighCardValidator(cards = cards)
        
        self.assertEqual(validator.is_valid(), True)

    def test_returns_high_card_from_card_collection(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="3", suit="Clubs"),
            Card(rank="5", suit="Diamonds"),
            Card(rank="7", suit="Hearts"),
            ace_of_spades,
        ]
        validator = HighCardValidator(cards = cards)
        
        self.assertEqual(
            validator.valid_cards(),
            [ace_of_spades],
        )