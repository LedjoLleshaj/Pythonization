import unittest
from unittest.mock import MagicMock, patch

from poker.card import Card
from poker.deck import Deck


class DeckTest(unittest.TestCase):
    def test_stores_no_cards_at_start(self):
        deck = Deck()
        self.assertEqual(deck.cards, [])

    def test_adds_cards_to_deck(self):
        card = Card("Ace", "Spades")
        deck = Deck()
        deck.add_cards([card])
        self.assertEqual(deck.cards, [card])

    @patch("random.shuffle")
    def test_shuffles_cards_in_random_order(self, mock_shuffle):
        cards = [Card("Ace", "Spades"), Card("King", "Spades")]

        deck = Deck()
        deck.add_cards(cards)
        deck.shuffle()
        mock_shuffle.assert_called_once_with(cards)

    def test_removes_specified_number_of_cards_from_deck(self):
        ace = Card("Ace", "Spades")
        king = Card("King", "Spades")

        deck = Deck()
        deck.add_cards([ace, king])

        self.assertEqual(deck.remove_cards(1), [ace])
        self.assertEqual(deck.cards, [king])
