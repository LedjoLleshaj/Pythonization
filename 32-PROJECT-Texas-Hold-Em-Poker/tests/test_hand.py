import unittest
from poker.card import Card
from poker.hand import Hand


class handTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        cards = [Card(rank="Ace", suit="Spades"), Card(rank="King", suit="Spades")]
        hand = Hand(cards=cards)
        self.assertEqual(hand.cards, cards)

    def test_figures_put_high_card_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="King", suit="Spades"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_out_pair_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="Ace", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Pair")
