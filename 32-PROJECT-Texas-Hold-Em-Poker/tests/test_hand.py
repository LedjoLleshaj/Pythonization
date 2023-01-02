import unittest
from poker.card import Card
from poker.hand import Hand


class handTest(unittest.TestCase):
    def test_starts_with_no_cards(self):
        hand = Hand()
        self.assertEqual(hand.cards, [])

    def test_shows_all_its_cards_in_technical_representation(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        hand = Hand()
        hand.add_cards([ace_of_spades, king_of_spades])
        self.assertEqual(
            repr(hand),
            "King of Spades, Ace of Spades",
        )

    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        cards = [ace_of_spades, king_of_spades]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.cards, [king_of_spades, ace_of_spades])

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Spades"),
            Card(rank="6", suit="Hearts"),
            Card(rank="6", suit="Diamonds"),
            Card(rank="6", suit="Clubs"),
            Card(rank="Jack", suit="Hearts"),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Four of a Kind")

    def test_figures_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Clubs"),
            Card(rank="2", suit="Clubs"),
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Straight Flush")

    def test_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Clubs"),
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
        ]
        hand = Hand()
        hand.add_cards(cards)
        self.assertEqual(hand.best_rank(), "Royal Flush")
