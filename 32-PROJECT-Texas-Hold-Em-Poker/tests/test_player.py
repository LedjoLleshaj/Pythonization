import unittest
from unittest.mock import MagicMock

from poker.card import Card
from poker.hand import Hand
from poker.player import Player


class TestPlayer(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand()
        player = Player("Human", hand=hand)
        self.assertEqual(player.name, "Human")
        self.assertEqual(player.hand, hand)

    def test_figures_out_own_best_hand(self):
        mock_hand = MagicMock()
        mock_hand.best_rank.return_value = "Straight Flush"
        player = Player("Human", hand=mock_hand)

        player.best_hand()
        mock_hand.best_rank.assert_called()
        self.assertEqual(player.best_hand(), "Straight Flush")

    def test_passes_new_cards_to_hand(self):
        mock_hand = MagicMock()
        player = Player("Human", hand=mock_hand)

        cards = [Card(rank="Ace", suit="Spades"), Card(rank="King", suit="Spades")]

        player.add_cards(cards)
        mock_hand.add_cards.assert_called_once_with(cards)
