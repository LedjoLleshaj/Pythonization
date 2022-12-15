import unittest
from poker.card import Card
from poker.hand import Hand


class handTest(unittest.TestCase):
    def test_receives_and_stores_cards(self):
        ace_of_spades = Card(rank="Ace", suit="Spades")
        king_of_spades = Card(rank="King", suit="Spades")
        cards = [ace_of_spades, king_of_spades]
        hand = Hand(cards=cards)
        self.assertEqual(hand.cards, [king_of_spades, ace_of_spades])

    def test_figures_put_high_card_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="3", suit="Clubs"),
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

    def test_figures_out_two_pair_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="Ace", suit="Hearts"),
            Card(rank="5", suit="Spades"),
            Card(rank="King", suit="Spades"),
            Card(rank="King", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Two Pair")

    def test_figures_out_three_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Spades"),
            Card(rank="Ace", suit="Hearts"),
            Card(rank="Ace", suit="Diamonds"),
            Card(rank="7", suit="Spades"),
            Card(rank="King", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Three of a Kind")

    def test_figures_out_straight_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Spades"),
            Card(rank="2", suit="Hearts"),
            Card(rank="3", suit="Diamonds"),
            Card(rank="4", suit="Spades"),
            Card(rank="5", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Straight")

    def test_does_not_consider_two_consecutive_cards_as_straight(self):
        cards = [
            Card(rank="6", suit="Spades"),
            Card(rank="7", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "High Card")

    def test_figures_out_flush_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Spades"),
            Card(rank="8", suit="Spades"),
            Card(rank="3", suit="Spades"),
            Card(rank="Jack", suit="Spades"),
            Card(rank="5", suit="Spades"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Flush")

    def test_figures_out_full_house_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Spades"),
            Card(rank="6", suit="Hearts"),
            Card(rank="6", suit="Diamonds"),
            Card(rank="Jack", suit="Spades"),
            Card(rank="Jack", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Full House")

    def test_figures_out_four_of_a_kind_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Spades"),
            Card(rank="6", suit="Hearts"),
            Card(rank="6", suit="Diamonds"),
            Card(rank="6", suit="Clubs"),
            Card(rank="Jack", suit="Hearts"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Four of a Kind")

    def test_figures_out_straight_flush_is_best_rank(self):
        cards = [
            Card(rank="6", suit="Clubs"),
            Card(rank="2", suit="Clubs"),
            Card(rank="3", suit="Clubs"),
            Card(rank="4", suit="Clubs"),
            Card(rank="5", suit="Clubs"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Straight Flush")

    def test_figures_out_royal_flush_is_best_rank(self):
        cards = [
            Card(rank="Ace", suit="Clubs"),
            Card(rank="10", suit="Clubs"),
            Card(rank="Jack", suit="Clubs"),
            Card(rank="Queen", suit="Clubs"),
            Card(rank="King", suit="Clubs"),
        ]
        hand = Hand(cards=cards)
        self.assertEqual(hand.best_rank(), "Royal Flush")
