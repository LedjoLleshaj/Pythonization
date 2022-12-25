import unittest

from poker.card import Card
from poker.validators import NoCardsValidator


class NoCardsValidatorTest(unittest.TestCase):
    def test_validates_that_cards_have_no_cards(self):
        cards = []
        validator = NoCardsValidator(cards=cards)

        self.assertEqual(validator.is_valid(), True)

    def test_returns_no_valid_cards_from_card_collection(self):
        cards = []
        validator = NoCardsValidator(cards=cards)

        self.assertEqual(
            validator.valid_cards(),
            [],
        )
