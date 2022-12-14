import unittest
from poker.card import Card
from poker.hand import Hand


class handTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [Card(rank="Ace", suit="Spades"), Card(rank="King", suit="Spades")]
        hand = Hand(cards=cards)
        self.assertEqual(hand.cards, cards)
