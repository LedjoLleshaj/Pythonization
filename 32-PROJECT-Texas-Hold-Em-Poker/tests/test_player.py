import unittest
from unittest.mock import MagicMock

from poker.hand import Hand
from poker.player import Player


class TestPlayer(unittest.TestCase):
    def test_stores_name_and_hand(self):
        hand = Hand(cards=[])
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
