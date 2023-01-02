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
