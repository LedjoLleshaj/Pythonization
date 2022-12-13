import unittest
from poker.card import Card


class CardTest(unittest.TestCase):
    def test_has_rank(self):
        card = Card(rank="Queen", suit="Hearts")
        self.assertEqual(card.rank, "Queen")

    def test_has_suit(self):
        card = Card(rank="Ace", suit="Spade")
        self.assertEqual(card.suit, "Spade")
